# -*- coding: utf-8 -*-
import GetTitleFromIdApi
import LinkTargetAmountApi
import LinkedPagesListApi

class page():

    page_id = 0
    page_title = ""
    number_of_target_links = 0.0
    link_page_ids = []

    def __init__(self,page_id):

        self.page_id = page_id
        self.link_page_ids = LinkTargetAmountApi.GetLinkTargets(self.page_id)
        self.number_of_target_links = len(self.link_page_ids)
        self.page_title = GetTitleFromIdApi.GetTitle(page_id)

    def getLinkPageIds(self):

        return self.link_page_ids

    def getLinkedPageIds(self):

        return LinkedPagesListApi.GetLinkedPages(self.page_title)

    def makeRow(self,AllPageIds):

        row = []

        for i in range(0,len(AllPageIds)):

            if(AllPageIds[i] in self.link_page_ids):

                row.append(1.0/ float(self.number_of_target_links) )

            else:
                row.append(0)

        #print len(row)
        return row
