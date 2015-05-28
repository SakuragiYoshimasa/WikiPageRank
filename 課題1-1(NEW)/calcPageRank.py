# -*- coding: utf-8 -*-
import MySQLdb
import multiprocessing as mp
import time
import SavePageRank
proc = 4
loop = 10
pageRankVector = []
cost = []

d = 0.85
reD = 0.15
#size  = 1000000 #debug sizeとオフセットで範囲指定できる　基本的にsize = 3216300 offset = 0
size = 3216300
offset = 0
linkedPages = []

def calcPageRank():

    global cost
    global pageRankVector
    global size
    global linkedPages

    cost = [0 for n in range(0 ,size)]
    linkedPages = [[] for j in range(0 ,size )]

    #DB接続 
    connection = MySQLdb.connect(host = "" ,db = "", user = "" , passwd = "")
    cursor = connection.cursor()

    cursor.execute("select * from linkcost;")
    result = cursor.fetchall()

    for i in range(0 + offset,len(result)):
        #debug
        if(result[i][0] < size + offset and result[i][0] > offset):
            cost[result[i][0] - offset] = result[i][1]


    cursor.close()
    connection.close()

    print "linkCostFetched"


    #初期ベクトルの初期化
    pageRankVector = [1.0 for page_id in range(0,size)]

    #被リンクの配列作成
    pool = mp.Pool(proc)
    process_result = pool.map(makingDataMultiprocessing,range(0,proc))
    linkedPages = process_result[0] + process_result[1] + process_result[2] + process_result[3]

    print "linkedFetched"

    #計算
    for l in range(0,loop):
        calc_process_result = pool.map(wrapper,[(i,linkedPages) for i in range(0,proc)])
        print "EndCalc"
        pageRankVector = calc_process_result[0]
        print "0Plus"
        pageRankVector += calc_process_result[1]
        print "1Plus"
        pageRankVector += calc_process_result[2]
        print "2Plus"
        pageRankVector += calc_process_result[3]
        print "3Plus"
        print "EndConts"
        #if(l % 100 == 99):
        #print pageRankVector
        f = open('loop'+ str(l)+'rank.txt', 'w')
        f.write(str(pageRankVector))
        f.close()
    print "EndLoop"

    resultPageRank = pageRankVector

    print "EndPut"

    SavePageRank.save(resultPageRank)


def wrapper(args):
    return calcPageRankMultiprocessing(*args)


def calcPageRankMultiprocessing(process_number,linkedpages):

    global pageRankVector
    global size
    global cost
    global offset


    start = size * process_number / proc
    end = size * (process_number + 1) /proc

    newPageRanks = []

    for i in range(start,end):
        if(process_number == 0):
            if(i % 100 == 0):
                print i

        newPageRank = 0

        for link_from in linkedpages[i]:
            #debug
            if(link_from < size + offset and link_from >= offset):

                newPageRank += pageRankVector[link_from - offset] / float(cost[link_from - offset])

        newPageRanks.append(reD + d * newPageRank)

    return newPageRanks



def makingDataMultiprocessing(process_number):

    global pageRankVector
    global size
    global cost
    global offset

    start = size * process_number / proc
    end = size * (process_number + 1) /proc

    linkedPage = [[] for j in range(0,end - start)]

    #DB接続 #processごとに分ける
    connection = MySQLdb.connect(host = "" ,db = "", user = "" , passwd = "")
    cursor = connection.cursor()

    for i in range(start,end):


        #DBに存在しない時 linkedPage[i]はからのまま
        if(cost[i] == 0):
            continue

        if(process_number == 0):
            if(i % 100 == 0):
                print i
            #print i
        #try:

        #t = time.time()
            #costに入ってるので存在する
        cursor.execute("select * from suggested where page_id="+str(i + offset)+";")
        result = cursor.fetchall()

        linked = []

        #print time.time() - t
        #t = time.time()

        #newPageRank = 0

        for raw in result:

            if(raw[0] is None):continue
            #debug?
            if(raw[0] < size + offset and raw[0] < offset):

                linked.append(raw[0] - offset)

        linkedPage[i - start] = linked

            #newPageRank += pageRankVector[raw[0]] / cost[raw[0]]

        #newPageRanks.append(reD + d * newPageRank)

        #except:
            #print "Error"
            #newPageRanks.append(reD)

    cursor.close()
    connection.close()

    return linkedPage
