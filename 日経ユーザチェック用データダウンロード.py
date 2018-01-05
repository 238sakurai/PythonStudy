import subprocess
from subprocess import Popen, PIPE
import datetime
from datetime import timedelta

print('日経ユーザーデータファイルをダウンロードします。')


# 日付のリストを作成する YYYY-MM-DD
def make_day_list(start_day , end_day):
    start_date = datetime.datetime(int(start_day[0:4]),int(start_day[5:7]),int(start_day[8:10]))
    result = []
    while True:
        #print(start_date)
        result.append(start_date.strftime("%Y-%m-%d"))
        if start_date.strftime("%Y-%m-%d") == end_day:
            break
        start_date += timedelta(1)
    return result

# lsコマンド実行
def aws_ls(ls_command):
    p = Popen(ls_command.split(' '), stdout=PIPE, stderr=PIPE)
    out, err = p.communicate()
    #print(out)
    return out

# lsコマンドの結果からファイル名リストを作成
def aws_file_list_make(out):
    aws_file_list = []

    #for i in str(out).split('\\r\\n'):
    for i in out.decode().split('\r\n'):
        #tmp_list = i.replace('   ', ' ').replace('\r','').replace('\r','').split(' ')
        tmp_list = [x for x in i.split(' ') if x]
        #print (i)
        #print(tmp_list)
        if len(tmp_list)>2:
            if '.gz' in tmp_list[3]:
                aws_file_list.append(tmp_list[3])

    #print(aws_file_list)
    return aws_file_list

# cpコマンドを実行する
def aws_cp(aws_file_list , cp_command_pre , output_file_path):
    # ファイルリストから取得を行う cp command
    for file_name in aws_file_list:
        cp_command = cp_command_pre + file_name + output_file_path + file_name
        p = Popen(cp_command.split(' '), stdout=PIPE, stderr=PIPE)
        out, err = p.communicate()
        #print(out)


def aws_firstfile_download(target_day):
    ls_command = 'aws s3 ls s3://krux-partners/client-cci/nikkei/' + target_day + '/'
    p = Popen(ls_command.split(' '), stdout=PIPE, stderr=PIPE)
    out, err = p.communicate()
    aws_file_list = []
    first_file = ''
    for i in str(out).split('\n'):
        #tmp_list = i.replace('   ', ' ').replace('\r','').split(' ')
        tmp_list = [x for x in i.split(' ') if x]
        #print(tmp_list)
        for tmp in tmp_list:
            if 'first_party_segments' in tmp:
                print(tmp)
                first_file = tmp.replace('\\r','').replace('\\n','').replace('\r','').replace('\n','').replace("'",'')
                break

    first_output_file_path = ' nikkei/' + target_day + '/' + 'ca.csv.gz'
    cp_command = 'aws s3 cp s3://krux-partners/client-cci/nikkei/' + target_day + '/' + first_file + first_output_file_path
    p = Popen(cp_command.split(' '), stdout=PIPE, stderr=PIPE)
    out, err = p.communicate()

# ダウンロード設定

### Proxy設定
set_command = 'set HTTPS_PROXY=https://proxy.cci.co.jp:3128'
###


### 開始日と終了日の設定
start_day = input('集計対象日をYYYY-MM-DD形式で入力してください---> ')
end_day   = start_day
### 1日の場合は開始日と終了日を同日にする

# ユーザーデータダウンロード
for target_day in day_list:
    user_cp_command_pre   = 'aws s3 cp s3://krux-partners/client-cci/nikkei/' + target_day + '/user_audience_segment_map/'
    user_output_file_path = ' nikkei/' + target_day + '/user_audience_segment_map/'
    user_cp_command = user_cp_command_pre + " " + user_output_file_path + " --recursive"
    print(user_cp_command)
    p = Popen(user_cp_command, stdout=PIPE, stderr=PIPE)
    out, err = p.communicate()
    print(err)

print('ユーザーデータダウンロード完了!!')


# サイトデータダウンロード
for target_day in day_list:
    attr_cp_command_pre   = 'aws s3 cp s3://krux-partners/client-cci/nikkei/datalayer/site-user-data/' + target_day + '/'
    attr_output_file_path = ' nikkei/' + target_day + '/site-user-data/'
    attr_cp_command = attr_cp_command_pre + " " + attr_output_file_path + " --recursive"
    print(attr_cp_command)
    p = Popen(attr_cp_command, stdout=PIPE, stderr=PIPE)
    out, err = p.communicate()
    print(err)

print('サイトデータダウンロード完了!!')


# 実行日付のリスト作成
day_list = make_day_list(start_day , end_day)
print(start_day + 'のデータをダウンロード開始します。')

# マスターデータダウンロード
for target_day in day_list:
    aws_firstfile_download(target_day)

print('マスターデータダウンロード完了!!')
