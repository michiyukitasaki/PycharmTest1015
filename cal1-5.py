import glob
import os
import re
import codecs
import pandas as pd
import os

def changeDir():
    os.chdir('/Volumes/SSD-PUTU3C/Python_会社/PycharmTest1015')

def readCSV():
    df = pd.read_csv('半年間のデータ_Rev_NA有.csv', encoding="shift-jis", dtype = object)
    return df

def deleteNA():
    changeDir()
    df = readCSV()
    df.fillna("")
    df.to_csv('半年間のデータ_Rev_NA削除_1015-2.csv', index=False, encoding='shift-jis')
    print("CSVへの書き込みが完了しました")