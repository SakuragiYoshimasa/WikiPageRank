# -*- coding: utf-8 -*-
import calcPagerank
import sys


if __name__ == '__main__':

    argv = sys.argv
    #argv[1] is key word argv[2] is depth
    calcPagerank.calc(argv[1],argv[2])
