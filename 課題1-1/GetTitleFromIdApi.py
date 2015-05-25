# -*- coding: utf-8 -*-
import MySQLdb



def GetTitle(Id):

    #ローカルMySQLを使用
    connection = MySQLdb.connect(db = "wiki", user = "root")
    cursor = connection.cursor()

    cursor.execute("select * from page where page_id=" + str(Id) + " and page_namespace=0")
    result = cursor.fetchall()

    #titleを返す
    if(len(result) > 0):
        return result[0][2]

    return ''
