# -*- coding: utf-8 -*-
import MySQLdb

def save(pageRankVector):

    #DB接続
    connection = MySQLdb.connect(host = "" ,db = "", user = "" , passwd = "")
    cursor = connection.cursor()

    for i in range(0,len(pageRankVector)):
        try:
            cursor.execute("insert into humanrank set page_id="+ str(i) + ",pagerank="+ str(pageRankVector[i]))
        except:
            pass

    connection.commit()
    cursor.close()
    connection.close()

    print "Finish!"
