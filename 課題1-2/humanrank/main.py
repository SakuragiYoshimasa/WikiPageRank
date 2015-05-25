# -*- coding: utf-8 -*-
import calcPagerank
import sys
import time


if __name__ == '__main__':

    t = time.time()

    #depth固定(server)
    #自機にこのアルゴリズムだとdepth2が限界
    calcPagerank.calc(5)
    print "time :" + str(time.time() - t)
