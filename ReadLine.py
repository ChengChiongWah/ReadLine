#-*- coding:utf-8 -*-
#对某文件夹里面文本进行逐行抽取，并把抽取信息insert到数据库中。
import os, zipfile, time, shutil, cx_Oracle
from time import strftime
os.chdir(r'C:\Users\Cheng\Desktop\readline')                   #切换程序运行时的目录
ZipName = strftime("%Y_%m_%d_%H_%M", time.localtime())+ '.zip' #设定压缩文件名格式
Path_Root = (r'C:\Users\Cheng\Desktop\readline')#需要处理的文本文件所在文件夹
os.putenv('ORACLE_HOME', r'C:\app\Cheng\product\11.2.0\client_1')  #执行oracle时设定的参数1
os.putenv('LD_LIBRARY_PATH', r'C:\app\Cheng\product\11.2.0\client_1\LIB')#执行oracle时设定的参数2
sql = "insert into ** values(:c1, :c2, :c3, :c4, :c5, :c6, :c7, :c8, :c9, :c10, :c11, :c12, :c13)"  
conn = cx_Oracle.connect('**/**@**/**')  #数据库连接 *号需要对应改成实际的信息
cursor = conn.cursor()

for FileName in os.listdir(Path_Root):
    Path_File = os.path.join(Path_Root,FileName)
    f = open(Path_File)
    for eachline in f:                          #遍历文本每一行
        #print eachline, FileName
        Record_Inf = eachline.split('\t')
        Record_Inf[-1] = Record_Inf[-1].strip()    #最后一个元素有一个换行符，去掉之

        #每一条数据插入到数据库
        cursor.execute(sql, c1=Record_Inf[0], c2=Record_Inf[1], c3=Record_Inf[2], c4=Record_Inf[3], c5=Record_Inf[5], c6=Record_Inf[5], c7=Record_Inf[6],
                           c8=Record_Inf[7], c9=Record_Inf[8], c10=Record_Inf[9], c11=Record_Inf[10], c12=Record_Inf[11],  c13= FileName)
        del Record_Inf[:]
        
    f.close()

#    zip_file =  zipfile.ZipFile(ZipName, 'a', zipfile.ZIP_DEFLATED)#压缩文件
#    zip_file.write(Path_File)
#    zip_file.close()

    Dest_File = os.path.join(r'C:\Users\Cheng\Desktop\readline2', FileName)#处理过后的文件存放目录
    shutil.move(Path_File, Dest_File)

cursor.close()
conn.commit()
conn.close()

