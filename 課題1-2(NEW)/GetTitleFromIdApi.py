# -*- coding: utf-8 -*-
import MySQLdb
import sys



def GetTitle(Id):

    
    connection = MySQLdb.connect(host = "mysql496.db.sakura.ne.jp" ,db = "ysrhsp_nextvanguard", user = "ysrhsp" , passwd = "nextvanguard0")
    cursor = connection.cursor()

    cursor.execute("select * from page where page_id=" + str(Id) + " and page_namespace=0")
    result = cursor.fetchall()

    #titleを返す
    if(len(result) > 0):
        return result[0][2]

    return ''

if __name__ == '__main__':
    param = sys.argv
    print param[1]
    id = int(param[1])
    print GetTitle(id)

