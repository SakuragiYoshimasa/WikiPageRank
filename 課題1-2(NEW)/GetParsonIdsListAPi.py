# -*- coding: utf-8 -*-
import MySQLdb




def GetParsonList():

    connection = MySQLdb.connect(host = "" ,db = "", user = "" , passwd = "")
    cursor = connection.cursor()
    cursor.execute("select * from humanranking")
    result = cursor.fetchall()
    print "fetched"

    ids = []
    for raw in result:
        #存命人物のidlist
        ids.append(raw[0])

    cursor.close()
    connection.close()

    return ids




