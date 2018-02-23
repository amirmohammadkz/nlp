# -*- coding: utf-8 -*-

import sys

import pandas
import xlrd

df = pandas.read_excel('PersianWords.xlsx')
df = df[u'*Total farsi Word (Moin+openoffice.fa+wikipedia)']
print(type(df))
yourInput = input("Input your word: ")
charList = [[i,yourInput.count(i)] for i in set(yourInput)]
df = [i for i in df if all(i.count(k[0]) == k[1] for k in charList) and len(i) == len(yourInput)]
print(df)
