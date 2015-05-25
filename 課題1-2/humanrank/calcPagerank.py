# -*- coding: utf-8 -*-
import MySQLdb
import GetTitleFromIdApi
import LinkTargetAmountApi
import LinkedPagesListApi
import page
import PageManager
import GetIdFromTitle
import numpy as np
import time
import InertHumanPageRankApi

def calc(depth):



    #n次正方行列の生成(depth >= 0,targetID)
    #pageManager = PageManager.PageManager(int(depth),targetPage.page_id)
    #pageManager.makePagesCollction()
    matrix = PageManager.make(int(depth))

    #行列の転置
    transposedMatrix = Transpose(matrix)
    print transposedMatrix

    #初期ベクトルの生成
    pageRankVector = np.array([1 for col in range(transposedMatrix.shape[0])])

    #行列計算のループ
    pageRankVector = operationMatrixMultiple(transposedMatrix,pageRankVector)

    print pageRankVector
    #入力に対するPageRank
    print pageRankVector[0]

    InsertHumanPageRankApi.InsertPageRank(pageRankVector)

#転置
def Transpose(matrix):
    """transposed =  [[0 for col in range(len(matrix))] for row in range(len(matrix))]

    for i in range(0,len(matrix)):
        for j in range(0,len(matrix)):
            transposed[i][j] = matrix[j][i]
    return transposed
    """
    return np.transpose(matrix)

#行列演算
def operationMatrixMultiple(transposedMatrix,pageRankVector):
    t = time.time()
    for i in range(0,10):

        #newPageRank = [0 for j in range(len(transposedMatrix))]
        newPageRank = transposedMatrix.dot(pageRankVector)
        newPageRank = 0.15 + newPageRank * 0.85
        """
        for n in range(0,len(transposedMatrix)):

            for k in range(0,len(transposedMatrix)):

                newPageRank[n] += pageRankVector[n]*transposedMatrix[n][k]

            newPageRank[n] = 0.15 + 0.85 * newPageRank[n]
        """
        pageRankVector = newPageRank
    print time.time() - t

    return pageRankVector
