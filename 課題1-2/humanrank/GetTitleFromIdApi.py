# -*- coding: utf-8 -*-
import MySQLdb



def GetTitle(Id):


    connection = MySQLdb.connect(host = "" ,db = "", user = "" , passwd = "")
    cursor = connection.cursor()

    cursor.execute("select * from page where page_id=" + str(Id) + " and page_namespace=0")
    result = cursor.fetchall()

    #titleを返す
    if(len(result) > 0):
        return result[0][2]

    return ''
