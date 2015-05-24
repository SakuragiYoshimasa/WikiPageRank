# -*- coding: utf-8 -*-
import MySQLdb

#ローカルMySQLを使用
connection = MySQLdb.connect(db = "wiki", user = "root")
cursor = connection.cursor()

def GetId(targetTitle):


    #日本語のバイト文字のバックスラッシュと'対策
    targetTitle = targetTitle.replace('\\','\\\\')
    targetTitle = targetTitle.replace("'","\\'")
    cursor.execute("select * from page where page_title='" + str(targetTitle) + "' and page_namespace=0")
    result = cursor.fetchall()

    #idを返す
    if(len(result) > 0):

        return result[0][0]
    #idがなければ空文字を返して無視
    return ''
