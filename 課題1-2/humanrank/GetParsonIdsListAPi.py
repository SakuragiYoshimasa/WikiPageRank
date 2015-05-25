# -*- coding: utf-8 -*-
import MySQLdb

connection = MySQLdb.connect(host = "" ,db = "", user = "" , passwd = "")
cursor = connection.cursor()

def GetParsonList():
    cursor.execute("select * from humanranking")
    result = cursor.fetchall()

    ids = []
    for raw in result:
        #存命人物のidlist
        ids.append(raw[0])

    return ids
