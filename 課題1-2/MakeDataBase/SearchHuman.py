# -*- coding: utf-8 -*-
import MySQLdb


connection = MySQLdb.connect(host = "" ,db = "", user = "" , passwd = "")
cursor = connection.cursor()

def SearchHumanIDs():

    cursor.execute("select * from categorylinks where cl_to='存命人物'")
    result = cursor.fetchall()

    searchHumanIDs = []
    for raw in result:
        #cl_fromを入手pageに対応
        searchHumanIDs.append(raw[0])
        print raw[0]

    cursor.close()
    connection.close()

    return searchHumanIDs
