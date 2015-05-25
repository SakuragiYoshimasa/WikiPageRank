# -*- coding: utf-8 -*-
import MySQLdb



def GetLinkedPages(targetTitle):

    
    connection = MySQLdb.connect(host = "mysql496.db.sakura.ne.jp" ,db = "ysrhsp_nextvanguard", user = "ysrhsp" , passwd = "nextvanguard0")
    cursor = connection.cursor()

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
