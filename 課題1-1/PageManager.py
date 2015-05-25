# -*- coding: utf-8 -*-
import page
import numpy as np
import multiprocessing as mp
import time



depth = 0
targetPageID = 0
AllPageIds = []
pages = []
#4並列
proc = 4
loopStart = 0
loopEnd = 0
nowDepth = 0
process_result = []
flag = 1


def make(input_depth,targetPageID):
    global depth
    global AllPageIds

    depth = input_depth
    AllPageIds.append(targetPageID)

    makePagesCollction()

    return MakeMatrix()

def makePagesCollction():

    global depth
    global AllPageIds
    global pages
    global proc
    global loopStart
    global loopEnd
    global nowDepth
    global process_result

    loopStart = 0
    loopEnd = len(AllPageIds)

    for i in range(0,depth + 1):

        #for page_id_index in range(loopStart,loopEnd):
        #一回目以降は並列に
        #二回目からほぼ並列処理
        if loopEnd - loopStart > proc - 1:
            nowDepth = i
            pool = mp.Pool(proc)
            process_result = pool.map(makePagesCollectionMultiProcessing, range(0,proc))

            arrangementResultMultiProcessing(process_result)

        else:
            for page_id_index in range(loopStart,loopEnd):
                pages.append(page.page(AllPageIds[page_id_index]))

                #必要ない場合スルー
                if(i < depth ):
                    AllPageIds = AllPageIds + pages[page_id_index].getLinkPageIds() + pages[page_id_index].getLinkedPageIds()

                    AllPageIds = list(set(AllPageIds))

        loopStart = loopEnd

        loopEnd = len(AllPageIds)

def makePagesCollectionMultiProcessing(process_number):

    global depth
    global AllPageIds
    global pages
    global proc
    global loopStart
    global loopEnd
    global nowDepth

    newPages = []
    newIDs  = []

    start = loopStart + (loopEnd - loopStart) * process_number / proc
    end =   loopStart + (loopEnd - loopStart) * (process_number + 1) / proc
    if(process_number == proc -1):
        end = loopEnd

    for page_id_index in range(start,end):

        print "process_number:" + str(process_number) + ": loop :" + str(page_id_index)
        newPages.append(page.page(AllPageIds[page_id_index]))

        #必要ない場合スルー
        if(nowDepth < depth ):
            
            newIDs = newIDs + newPages[page_id_index - start].getLinkPageIds() + newPages[page_id_index - start].getLinkedPageIds()

            newIDs = list(set(newIDs))


    return newPages,newIDs
    #,newIDs

def arrangementResultMultiProcessing(result):
        global AllPageIds
        global pages

        for i in range(0,proc):
            pages = pages + result[i][0]
            AllPageIds = AllPageIds + result[i][1]
        AllPageIds = list(set(AllPageIds))


def MakeMatrix():

    global pages
    global AllPageIds
    print AllPageIds
    #for i in range(0,len(self.pages)):
    #self.matrix.append(self.pages[i].makeRow(self.AllPageIds))
    matrix = np.array([pages[i].makeRow(AllPageIds) for i in range(len(pages)) ])
    print len(pages)
    #print matrix
    return matrix
