#coding=utf-8
import os
import random
import csv

#随机生成整数
def makeNumber():
    n = random.randint(0, 10)
    return n

#随机加减
def run():
    #打开文件记录
    csvfile = open('maths.csv','a+',newline='')
    csvwriter = csv.writer(csvfile)

    a = makeNumber()
    b= makeNumber()
    strmaths = str(a)+'-'+str(b)+'='
    print(strmaths+'?')
    resulte = input('请输入答案：')
    if a-b is int(resulte):
        print('答案：√')
        csvwriter.writerow((strmaths, resulte, 1))
    else:
        print('答案：X 你怎么会错的，你个猪头!!!')
        csvwriter.writerow((strmaths, resulte, 0))
    csvfile.close()

    #循环
    run()

run()
