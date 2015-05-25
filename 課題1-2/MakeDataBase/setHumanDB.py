# -*- coding: utf-8 -*-
import MySQLdb
import SearchHuman



def SetHumanDB():

    connection = MySQLdb.connect(host = "" ,db = "", user = "" , passwd = "")
    cursor = connection.cursor()

    searchHumanIDs = SearchHuman.SearchHumanIDs()

    for i in range(0,len(searchHumanIDs)):

        cursor.execute("insert into humanranking set page_id="+ str(searchHumanIDs[i]))
    connection.commit()
    cursor.close()
    connection.close
    print "Finish!!"
