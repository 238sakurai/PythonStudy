# coding: utf-8
# nc_idcheck をチェックしてセグメント保有者のローカルストレージ情報とローデータの所持セグメントが同じかどうか出力する
# nc_idcheck に出力される値はセグメントIDで集計IDではないので要注意

# 実行対象日の設定
target_day = input("YYYY-MM-DD形式で日付を入力---> ")
print('実行対象日を'+ target_day +'で作業開始します。しばらくお待ちください。')

# In[5]:

# KruxのAWSから指定日の日経ユーザーデータファイルをダウンロードする
# 前提：AWSコマンドが使える状態であること
import subprocess
from subprocess import Popen, PIPE

set_command = 'set HTTPS_PROXY=https://proxy.cci.co.jp:3128'

user_ls_command       = 'aws s3 ls s3://krux-partners/client-cci/nikkei/' + target_day + '/user_audience_segment_map/'
user_cp_command_pre   = 'aws s3 cp s3://krux-partners/client-cci/nikkei/' + target_day + '/user_audience_segment_map/'
user_output_file_path = ' nikkei/' + target_day + '/user_audience_segment_map/'

attr_ls_command       = 'aws s3 ls s3://krux-partners/client-cci/nikkei/datalayer/site-user-data/' + target_day + '/'
attr_cp_command_pre   = 'aws s3 cp s3://krux-partners/client-cci/nikkei/datalayer/site-user-data/' + target_day + '/'
attr_output_file_path = ' nikkei/' + target_day + '/site-user-data/'

first_output_file_path = ' nikkei/' + target_day + '/' + 'ca.csv.gz'


# lsコマンド実行
def aws_ls(ls_command):
    p = Popen(ls_command.split(' '), stdout=PIPE, stderr=PIPE)
    out, err = p.communicate()
    out = out.decode()
    return out

# lsコマンドの結果からファイル名リストを作成
def aws_file_list_make(out):
    aws_file_list = []
    for i in out.split('\n'):
        tmp_list = i.replace('   ', ' ').replace('\r','').split(' ')
        if len(tmp_list)>2:
            #print (tmp_list[3])
            if '.gz' in tmp_list[3]:
                aws_file_list.append(tmp_list[3])

    return aws_file_list

# cpコマンドを実行する
def aws_cp(aws_file_list , cp_command_pre , output_file_path):
    # ファイルリストから取得を行う cp command
    for file_name in aws_file_list:
        cp_command = cp_command_pre + file_name + output_file_path + file_name
        p = Popen(cp_command.split(' '), stdout=PIPE, stderr=PIPE)
        out, err = p.communicate()
        print(out)
        out = out.decode()

def aws_firstfile_download():
    ls_command = 'aws s3 ls s3://krux-partners/client-cci/nikkei/' + target_day + '/'
    p = Popen(ls_command.split(' '), stdout=PIPE, stderr=PIPE)
    out, err = p.communicate()
    out = out.decode()
    aws_file_list = []
    first_file = ''
    for i in out.split('\n'):
        tmp_list = i.replace('   ', ' ').replace('\r','').split(' ')
        for tmp in tmp_list:
            if 'first_party_segments' in tmp:
                first_file = tmp
                break

    cp_command = 'aws s3 cp s3://krux-partners/client-cci/nikkei/' + target_day + '/' + first_file + first_output_file_path
    p = Popen(cp_command.split(' '), stdout=PIPE, stderr=PIPE)
    out, err = p.communicate()
    out = out.decode()

# In[8]:

# サイトデータから対象ユーザーを抽出する
import os
import gzip

check_word = 'nc_idcheck'

def site_data_user_extract(file_path):

    max_count = 500000000
    result_dict = {}
    all_count = 0

    for p in os.listdir(file_path):
        file_name = file_path + p
        _f = gzip.open(file_name, 'rb')
        _line = _f.readline()

        count = 0
        err_count = 0
        while _line:
            if all_count >= max_count:
                break
            _text = _line.decode('utf-8')
            segm = _text.split('^')

            if len(segm) > 9:
                kuid = segm[2].replace('\"','')
                attrs = segm[8].replace('"','').replace('\n','').split('&')

                for atr in attrs:
                    if check_word in atr:
                        if 'noid' not in atr:
                            try:
                                if ':' in atr:
                                    val = atr.split('=')[1].split(':')[1]
                                    if len(val) > 0:
                                        result_dict[kuid] = val
                            except:
                                err_count += 1
                                continue

            _line = _f.readline()
            count+=1
            all_count+=1
        _f.close()
        #print (file_name + ' : ' + str(count) + ' : ' + str(len(result_dict)))
        print ('{} : {} : {}   err={}'.format(file_name, count,len(result_dict), err_count))

    return result_dict


# In[9]:

# サイトデータから対象ユーザーの抽出
nikkei_rowdata_file_path = 'C:\\Users\\gm3910\\nikkei\\' + target_day + '\\site-user-data\\'

kuid_dict = site_data_user_extract(nikkei_rowdata_file_path)


# In[10]:

len(kuid_dict)


# In[ ]:

# ユーザーデータからユーザー抽出する
import os
import gzip
import time
from datetime import datetime

# NIKKEIIDユーザーを抽出
def nikkei_krux_user_extract(file_path , kuid_dict):
    print('集計開始 '  + 'segment , filepath : ' + file_path)
    start_time = time.time()
    allcount = 0
    duplicount = 0
    result_dict = {}
    for p in os.listdir(file_path):
        file_name = file_path + p
        _f = gzip.open(file_name, 'rb')
        _line = _f.readline()
        mid_time = time.time()
        count = 0
        while _line:
            if allcount > 500000000:
                break
            _text = _line.decode('utf-8')
            segm = _text.split('^')

            # kuid_dictに該当するユーザーのみ抽出
            if segm[0] in kuid_dict:
                result_dict[segm[0]] = segm[2].replace('\n','')

            count+=1
            allcount+=1
            _line = _f.readline()

        _f.close()
        elapsed_time = time.time() - mid_time
        print(file_name + ' ,　行数 : ' + str(count) + ' , 集計時間 : {0:.3f}'.format(elapsed_time) + '秒')

    print (str(allcount))
    print (str(duplicount))
    end_time = time.time() - start_time
    print('集計終了 , 実行時間 : {0:.3f}'.format(end_time) + '秒')
    return result_dict


# In[ ]:

# ユーザーデータからユーザーセグメントの抽出
nikkei_user_rowdata_file_path = 'C:\\Users\\gm3910\\nikkei\\' + target_day + '\\user_audience_segment_map\\'

user_result_dict = nikkei_krux_user_extract(nikkei_user_rowdata_file_path , kuid_dict)


# In[ ]:

len(user_result_dict)


# In[ ]:

# マスター読み込み
import codecs, csv

target_day

master_file_path = 'C:\\Users\\gm3910\\nikkei\\' + target_day + '\\ca.csv\\'

file_name = master_file_path + 'ca.csv'
master_dict={}
# 文字コード指定でファイルを読み込み
csv_reader = csv.reader(codecs.open(file_name, encoding="utf-8"), delimiter = ',')
# ヘッダー読み飛ばし
next(csv_reader)
cou=0
for row in csv_reader:
    if len(row)>5:
        master_dict[row[5]] = row[4]
    cou+=1
print(file_name + ' : ' + str(cou) + 'row read')


# In[ ]:




# In[ ]:

# ユーザーセグメントのチェック
def check_id(segment , segs , m_dict):
    if seg in m_dict:
        if m_dict[segment] in segs:
            return '0'

    return '1'

result_file_path = 'C:\\Users\\gm3910\\nikkei\\nikkei_user_id_check' + '\\'
result_file_name = result_file_path + 'nikkei_user_id_check_' + target_day + '.csv'
result_file = open(result_file_name, 'w')
result_file.write('kuid,segmentid,result,count\n')

for k,v in user_result_dict.items():
    if k in kuid_dict:
        local_segments = kuid_dict.get(k)
        user_segments = v
        for seg in local_segments.split(','):
            result_file.write(k + ',' + seg + ',' + check_id(str(seg) , user_segments , master_dict) + ',' + str('1')  + '\n')

result_file.close()
