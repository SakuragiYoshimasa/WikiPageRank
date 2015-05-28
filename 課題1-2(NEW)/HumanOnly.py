# -*- coding: utf-8 -*-
import MySQLdb
import GetParsonIdsListAPi
import GetTitleFromIdApi

if __name__ == '__main__':

    ids = GetParsonIdsListAPi.GetParsonList()

    connection = MySQLdb.connect(host = "" ,db = "", user = "" , passwd = "")
    cursor = connection.cursor()

    for i in range(0,len(ids)):
        try:
            #dbの名前を間違えてつけてしまった
            cursor.execute("select * from humanrank where page_id="+str(ids[i])+";")
            result = cursor.fetchall()
            if(result is None):continue

            cursor.execute("insert into humanonlyranking set page_id="+str(ids[i])+",pagerank="+str(result[0][1])+";")
            print i
        except:
            pass

    connection.commit()


    try:
        cursor.execute("select * from humanonlyranking order by pagerank DESC limit 20")
        result = cursor.fetchall()

        for n in range(0,len(result)):
            print "PageRankRanking:"+str(n)+"  ID:"+str(result[n][0])+"  pagerank:"+str(result[n][1])+"  name" + GetTitleFromIdApi.GetTitle(result[n][0])
    except:
        print "Error!"
    

    cursor.close()
    connection.close()
