# -*- coding: utf-8 -*-
import calcPagerank
import sys
import time


if __name__ == '__main__':

    t = time.time()
    argv = sys.argv
    #argv[1] is key word argv[2] is depth
    #自機にこのアルゴリズムだとdepth2が限界
    #１階層周辺とのPageRankである程度の指標とできるのでは？
    calcPagerank.calc(argv[1],argv[2])
    print "time :" + str(time.time() - t)
