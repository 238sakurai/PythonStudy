
# coding: utf-8

# In[ ]:

import os
import gzip
import codecs, csv

#環境設定、リスト作成
A_ID = []
B_ID = []
IP = []

MASTER_AB_DICT = {}
DAILY_AIP_DICT = {}


#処理１.MASTER_DATA.tsv.gzを読み込む
MASTER_DATA = gzip.open('MASTER_DATA.tsv.gz','rt')
for line in MASTER_DATA:
    line = line.split('^')
    A_ID = line[0]
    B_IDALL = line[1].split('=')
    B_ID = B_IDALL[1]
    MASTER_AB_DICT[A_ID] = B_ID
MASTER_DATA.close()

#処理2.DAILY_DATA.tsv.gzを読み込む
DAILY_DATA = gzip.open('DAILY_DATA.tsv.gz','rt',encoding="UTF-8")
for line1 in DAILY_DATA:
    line2 = line1.split('^')
    A_IDq = line2[2]
    A_ID = A_IDq.replace('"','') 
    IPq = line2[3]
    IP = IPq.replace('"','')
    DAILY_AIP_DICT[A_ID] = IP
    
DAILY_DATA.close()


# In[ ]:

#処理１.デバック用
#MASTER_AB_DICT


# In[ ]:

#処理2.デバック用
#DAILY_AIP_DICT


# In[ ]:

#処理3. それぞれのリストをfor文で回して要素を取り出し比較する

AID_BID_IP_LIST = []
AID_BID_IP = []

A_ID = []
B_ID= []
IP = []

#DAILY_AIP_DICTのA_IDを１つ取得しDAILY_Aに代入
for k in DAILY_AIP_DICT:
    DAILY_A = k    
    #MASTER_AB_DICTのA_IDを１つ取得しMASTER_Aに代入
    if k in MASTER_AB_DICT:
        A_ID = k
        #一致したUASM_KUS_LISTのB_IDを取得
        B_ID = MASTER_AB_DICT[A_ID]
        #一致したSUD_KUIP_LISTのIPを取得
        IP = DAILY_AIP_DICT[A_ID]
        
        #A_ID,B_ID,IPを1つのレコード(AID_BID_IP)に格納する
        AID_BID_IP = (A_ID,B_ID,IP)
        
        #格納したレコードを(AID_BID_IP_LIST)リストにする
        AID_BID_IP_LIST.append(AID_BID_IP)    


# In[ ]:

#処理3.デバック用
#AID_BID_IP_LIST

#処理3デバック用　ファイル出力
#test = open('AID_BID_IP_LIST.csv', 'wt')
#for line in AID_BID_IP_LIST:
#    A_ID = line[0]
#    B_ID = line[1]
#    IP = line[2]
#    test.write(A_ID + '\t' + B_ID + '\t' + IP + '\n')
#test.close()


# In[ ]:

#処理4.管理資料エクセルファイルを参照する
#(手作業)IP列だけを(テキストファイル)IP.txtに書き込む。
IP_LIST = []

IPtxt = open('IP.txt','rt')
for line in IPtxt:
    IP = line.strip()
    IP_LIST.append(IP)
IPtxt.close()


# In[ ]:

#処理4.デバック用
#IP_LIST


# In[ ]:

#処理5．IPLISTの1列目をAID_BID_IP_LISTのIPと完全一致検索する

IP_LIST_SET = set(IP_LIST)
AID_BID_IP_LIST_SET = set([x[2] for x in AID_BID_IP_LIST])
SHARE_IP = IP_LIST_SET & AID_BID_IP_LIST_SET


# In[ ]:

#処理6.処理5にて作成したリストをファイル出力する
test = open('DATA.csv', 'wt')
for line in SHARE_IP:
    test.write(line + '\n')
test.close()


# In[ ]:




# In[ ]:



