# -*- coding: utf-8 -*-
import MySQLdb
import multiprocessing as mp
import time
#import SavePageRank
proc = 4
loop = 1000
pageRankVector = []
cost = []
#allIds = []
d = 0.85
reD = 0.15
size = 3216300
linkedPages = []

def calcPageRank():

    global cost
    #global allIds
    global pageRankVector
    global size
    global linkedPages

    cost = [0 for n in range(0,size)]
    linkedPages = [[] for j in range(0,size)]

    #DB接続 #processごとに分ける
    connection = MySQLdb.connect(host = "" ,db = "", user = "" , passwd = "")
    cursor = connection.cursor()

    cursor.execute("select * from linkcost;")
    result = cursor.fetchall()

    for i in range(0,len(result)):
        #allIds.append(result[i][0])
        cost[result[i][0]] = result[i][1]
        #print i




    cursor.close()
    connection.close()


    #初期ベクトルの初期化
    pageRankVector = [1 for page_id in range(0,size)]

    t = time.time()
    print "start"

    #被リンクの配列作成
    pool = mp.Pool(proc)
    process_result = pool.map(makingDataMultiprocessing,range(0,proc))
    linkedPages = process_result[0] + process_result[1] + process_result[2] + process_result[3]

    print time.time() - t
    t = time.time()
    print "linkedPagesConstructed"

    #計算
    for l in range(0,loop):
        pool = mp.Pool(proc)
        process_result = pool.map(calcPageRankMultiprocessing,range(0,proc))
        pageRankVector = process_result[0] + process_result[1] + process_result[2] + process_result[3]

    print pageRankVector

    print "finish"
    print time.time() - t

    SavePageRank.save(pageRankVector)


#
def calcPageRankMultiprocessing(process_number):

    global pageRankVector
    global size
    global cost
    global allIds
    global linkedPages

    start = size * process_number / proc
    end = size * (process_number + 1) /proc

    newPageRanks = []

    for i in range(start,end):

        newPageRank = 0
        for link_from in linkedPages[i]:

            newPageRank += pageRankVector[link_from] / cost[link_from]

        newPageRanks.append(reD + d * newPageRank)

    return newPageRanks





#about 1000s
def makingDataMultiprocessing(process_number):

    global pageRankVector
    global size
    global cost
    global allIds
    #global linkedPages

    start = size * process_number / proc
    end = size * (process_number + 1) /proc

    linkedPage = [[] for j in range(0,end - start)]

    #DB接続 #processごとに分ける
    connection = MySQLdb.connect(host = "" ,db = "", user = "" , passwd = "")
    cursor = connection.cursor()

    for i in range(start,end):

        #if(process_number == 0):
        #    print i

        #DBに存在しない時 linkedPage[i]はからのまま
        if(cost[i] == 0):continue

        #try:

        #t = time.time()
            #costに入ってるので存在する
        cursor.execute("select * from suggested where page_id="+str(i)+";")
        result = cursor.fetchall()

        linked = []

        #print time.time() - t
        #t = time.time()

        #newPageRank = 0

        for raw in result:

            if(raw[0] is None):continue

            linked.append(raw[0])

        linkedPage[i - start] = linked

            #newPageRank += pageRankVector[raw[0]] / cost[raw[0]]

        #newPageRanks.append(reD + d * newPageRank)

        #except:
            #print "Error"
            #newPageRanks.append(reD)

    cursor.close()
    connection.close()

    return linkedPage
