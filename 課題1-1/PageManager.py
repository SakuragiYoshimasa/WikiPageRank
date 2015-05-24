# -*- coding: utf-8 -*-
import page

class PageManager():

    depth = 0
    targetPageID = 0
    AllPageIds = []
    matrix = []
    pages = []

    def __init__(self,depth,targetPageID):
        self.depth = depth

        self.AllPageIds.append(targetPageID)

    def makePagesCollction(self):

        loopStart = 0
        loopEnd = len(self.AllPageIds)

        for i in range(0,self.depth + 1):

            for page_id_index in range(loopStart,loopEnd):

                self.pages.append(page.page(self.AllPageIds[page_id_index]))

                #必要ない場合スルー
                if(i < self.depth ):
                    self.AllPageIds = self.AllPageIds + self.pages[page_id_index].getLinkPageIds() + self.pages[page_id_index].getLinkedPageIds()

                    self.AllPageIds = list(set(self.AllPageIds))

            loopStart = loopEnd

            loopEnd = len(self.AllPageIds)



    def MakeMatrix(self):
        for i in range(0,len(self.pages)):
            self.matrix.append(self.pages[i].makeRow(self.AllPageIds))
        return self.matrix
