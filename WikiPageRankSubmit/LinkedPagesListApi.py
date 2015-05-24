# -*- coding: utf-8 -*-
import MySQLdb

#ローカルMySQLを使用
connection = MySQLdb.connect(db = "wiki", user = "root")
cursor = connection.cursor()

def GetLinkedPages(targetTitle):

    if(targetTitle == ''):
        return []

    #日本語のバイト文字のバックスラッシュ対策
    targetTitle = targetTitle.replace('\\','\\\\')
    targetTitle = targetTitle.replace("'","\\'")

    #print "select * from pagelinks where pl_title='" + str(targetTitle) + "' and pl_namespace=0"
    cursor.execute("select * from pagelinks where pl_title='" + str(targetTitle) + "' and pl_namespace=0")
    result = cursor.fetchall()

    linked_page_ids = []

    for row in result:

        linked_page_ids.append(row[0])

    return linked_page_ids
