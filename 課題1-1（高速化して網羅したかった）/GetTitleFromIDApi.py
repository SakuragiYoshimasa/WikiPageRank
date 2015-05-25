# -*- coding: utf-8 -*-
import MySQLdb
import time
import numpy as np

#under 0.001s
def GetTitle(page_id):
    connection = MySQLdb.connect(db = "wiki", user = "root")
    cursor = connection.cursor()

    cursor.execute("select * from page where page_id=" + str(page_id) + " and page_namespace=0")
    result = cursor.fetchall()

    #titleを返す
    if(len(result) > 0):
        return result[0][2]

    return ''
