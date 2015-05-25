# -*- coding: utf-8 -*-
import MySQLdb
import GetParsonIdsListAPi


def InsertPageRank(pageRankVector):
    #insert失敗用backup
    np.savetxt('pageRankBackup',np.array(pageRankVector))
    humanIDs = GetPersonIdsListAPi.GetPersonList()

    connection = MySQLdb.connect(host = "mysql496.db.sakura.ne.jp" ,db = "ysrhsp_nextvanguard", user = "ysrhsp" , passwd = "nextvanguard0")
    cursor = connection.cursor()

    for i in range(0,len(humanIDs)):
        cursor.execute("insert into humanrank set page_id="+ str(humanIDs[i]) + ",pagerank="+ str(pageRankVector[i]))

    connection.commit()
    cursor.close()
    connection.close
