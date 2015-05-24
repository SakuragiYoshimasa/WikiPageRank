# -*- coding: utf-8 -*-
import MySQLdb
import GetTitleFromIdApi
import LinkTargetAmountApi
import LinkedPagesListApi
import page
import PageManager
import GetIdFromTitle

def calc(word,depth):

    targetPage = page.page(GetIdFromTitle.GetId(word))

    #n次正方行列の生成(depth >= 0,targetID)
    pageManager = PageManager.PageManager(int(depth),targetPage.page_id)
    pageManager.makePagesCollction()
    matrix = pageManager.MakeMatrix()

    #行列の転置
    transposedMatrix = Transpose(matrix)

    #初期ベクトルの生成
    pageRankVector = [1 for col in range(len(matrix))]

    #行列計算のループ
    pageRankVector = operationMatrixMultiple(transposedMatrix,pageRankVector)

    print pageRankVector
    #入力に対するPageRank
    print pageRankVector[0]

#転置
def Transpose(matrix):
    transposed =  [[0 for col in range(len(matrix))] for row in range(len(matrix))]

    for i in range(0,len(matrix)):
        for j in range(0,len(matrix)):
            transposed[i][j] = matrix[j][i]
    return transposed

#行列演算
def operationMatrixMultiple(transposedMatrix,pageRankVector):
    for i in range(0,3):

        newPageRank = [0 for j in range(len(transposedMatrix))]

        for n in range(0,len(transposedMatrix)):

            for k in range(0,len(transposedMatrix)):

                newPageRank[n] += pageRankVector[n]*transposedMatrix[n][k]

            newPageRank[n] = 0.15 + 0.85 * newPageRank[n]

        pageRankVector = newPageRank

    return pageRankVector
