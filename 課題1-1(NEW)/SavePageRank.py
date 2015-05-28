# -*- coding: utf-8 -*-
import MySQLdb

def save(*pageRankVector):
    
    offset = 0

    #DB接続
    connection = MySQLdb.connect(host = "" ,db = "", user = "" , passwd = "")
    cursor = connection.cursor()


    ranks =  list(pageRankVector)
    rank = ranks[0]
    #print pageRankVector
    print rank


    for i in range(0,len(rank)):
        try:
            #print rank[i]
            cursor.execute("insert into humanrank set page_id="+ str(i + offset) + ", pagerank="+ str(rank[i]))
        except:
            pass

    connection.commit()
    cursor.close()
    connection.close()

    print "Finish!"
