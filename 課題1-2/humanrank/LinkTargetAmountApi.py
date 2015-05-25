# -*- coding: utf-8 -*-
import MySQLdb
import GetIdFromTitle


def GetLinkTargetAmount(id):



    connection = MySQLdb.connect(host = "" ,db = "", user = "" , passwd = "")
    cursor = connection.cursor()

    cursor.execute("select * from pagelinks where pl_from=" + str(id) + " and pl_namespace=0")
    result = cursor.fetchall()

    return len(result)

def GetLinkTargets(id):



    connection = MySQLdb.connect(host = "" ,db = "", user = "" , passwd = "")
    cursor = connection.cursor()

    cursor.execute("select * from pagelinks where pl_from=" + str(id) + " and pl_namespace=0")
    result = cursor.fetchall()

    link_target_page_ids = []

    for row in result:
        targetid = GetIdFromTitle.GetId(row[2])
        if (targetid != ''):
            link_target_page_ids.append(targetid)

    return link_target_page_ids
