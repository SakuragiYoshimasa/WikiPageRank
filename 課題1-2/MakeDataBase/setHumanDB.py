# -*- coding: utf-8 -*-
import MySQLdb
import SearchHuman



def SetHumanDB():

    connection = MySQLdb.connect(host = "mysql496.db.sakura.ne.jp" ,db = "ysrhsp_nextvanguard", user = "ysrhsp" , passwd = "nextvanguard0")
    cursor = connection.cursor()

    searchHumanIDs = SearchHuman.SearchHumanIDs()

    for i in range(0,len(searchHumanIDs)):

        cursor.execute("insert into humanranking set page_id="+ str(searchHumanIDs[i]))
    connection.commit()
    cursor.close()
    connection.close
    print "Finish!!"
