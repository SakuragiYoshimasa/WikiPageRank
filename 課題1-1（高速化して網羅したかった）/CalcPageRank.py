# -*- coding: utf-8 -*-
import MySQLdb
import time
import numpy as np
import multiprocessing as mp
import GetTitleFromIDApi
from numpy import linalg as la

#4並列
proc = 4
size = 3216300
#idの最大の大きさ3216299
#matrix = np.zeros([size,size])

#allIDs = []
#t = 0
#loop = 0
#count = "count:"

#makeMatrixを並列処理2758799のデータを８並列で

def calc():
    #global allIDs
    #global matrix
    #allIDs = FetchAllPageIds()
    #print allIDs
    #print time.time() - t

    pool = mp.Pool(proc)
    pool.map(writeMatrix, range(0,proc))
    #writeMatrix()

    #各行を単位ベクトルにしてから転置
    for i in range(0,size):
        outAllow = matrix[i].sum()
        matrix[i] = matrix[i] / float(outAllow)
        matrix = la.transpote(matrix)

    print "Finish"
    #print matrix

def writeMatrix(process_number):
    
    filename = "Matrix"+str(process_number)
    file = open(filename,'a+')

    start = size * process_number / proc
    end   = size * (process_number + 1) / proc

    loop = 0

    if(process_number == proc - 1):
        end = size - 1

    connection = MySQLdb.connect(db = "wiki", user = "root")
    cursor = connection.cursor()

    for i in range(int(start),int(end)):
        #時間計測
        t = time.time()

        #文字列で行を表現
        raw_list = list("0" * size)

        targetTitle = GetTitleFromIDApi.GetTitle(i)
        targetTitle = targetTitle.replace('\\','\\\\')
        targetTitle = targetTitle.replace("'","\\'")

        if(targetTitle != ''):
                #page_id i のpageがリンクされているpage_idの集合
                cursor.execute("select * from pagelinks where pl_title='" + str(targetTitle) + "' and pl_namespace=0")
                result = cursor.fetchall()

                for pageID in result:
                    #リンクされていたら１
                    raw_list[pageID[0]] = "1"
        #一行ごとに書き込み
        rawtext = "".join(list(raw_list))
        file.write(rawtext)
        file.write("\n")
        #一行の書き込み時間

        print filename +" : "+ str(loop / 800000) + "%"
        loop = loop + 1

    file.close()








#From id , get title and put it pl_title and get linked ids list use for colum of the matrix
#リンクを表現する行列の列を生成しノルムで格行を調整後転置
def MakeMatrix(process_number):


    global matrix
    global result
    global t
    global loop

    start = size * process_number / proc
    end   = size * (process_number + 1) / proc
    if(process_number == proc - 1):
        end = size - 1

    connection = MySQLdb.connect(db = "wiki", user = "root")
    cursor = connection.cursor()
    result = []
    targetTitle = ""
    row =

    for i in range(int(start),int(end)):
        t = time.time()
        #日本語のバイト文字のバックスラッシュ対策

        targetTitle = GetTitleFromIDApi.GetTitle(i)
        targetTitle = targetTitle.replace('\\','\\\\')
        targetTitle = targetTitle.replace("'","\\'")
        if(targetTitle == ''):
            continue

        cursor.execute("select * from pagelinks where pl_title='" + str(targetTitle) + "' and pl_namespace=0")
        result = cursor.fetchall()

        for raw in result:

            #matrix[リンク元][リンク先]
            matrix[raw[0]][i] = 1
            #print matrix[raw[0]][i]

        #print count + str(i)
        #print list(matrix)
        print time.time() - t
        print count + str(loop)
        loop = loop + 1

    cursor.close()
    connection.close()



#Fetch All ids spend about 23 second
def FetchAllPageIds():
    global allIDs
    connection = MySQLdb.connect(db = "wiki", user = "root")
    cursor = connection.cursor()
    cursor.execute("select * from page")
    result = cursor.fetchall()
    allIDs = []
    for raw in result:
        allIDs.append(raw[0])
    cursor.close()
    connection.close()

    return allIDs

