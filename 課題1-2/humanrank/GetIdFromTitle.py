# -*- coding: utf-8 -*-
import MySQLdb



def GetId(targetTitle):

    
    connection = MySQLdb.connect(host = "mysql496.db.sakura.ne.jp" ,db = "ysrhsp_nextvanguard", user = "ysrhsp" , passwd = "nextvanguard0")
    cursor = connection.cursor()

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
