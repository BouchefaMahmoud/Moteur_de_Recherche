#!/usr/bin/env python3

import sys
import re


lsttermes ={}

def splitWord(s):
    s= s.replace('-','')
    s= s.replace('.','')
    s = s.replace(',','')
    s = s.replace('?','')
    s = s.replace('!','')
    s = s.replace(')','')
    s = s.replace('(','')
    s = s.replace('{','')
    s = s.replace('}','')

    return s


def rmWord(d, name):
    with open(name) as fd:
        for n in fd:
            n=n.strip()
            if(d.get(n,"")!=""):
                del d[n]
    return d


def main(name):
    with open(name) as fd:
        for t in fd:
            t=t.lower()
            t=t.replace("'"," ")
            t = t.strip().split(' ')
            for m in t:
                m=splitWord(m)
                if lsttermes.get(m,'not found')=='not found':
                    lsttermes[m]=1
                else:
                    lsttermes[m]+=1
    return(rmWord(lsttermes,"stopwords.txt"))


if __name__=="__main__":
    print(main(sys.argv[1]))
