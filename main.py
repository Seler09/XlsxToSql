import argparse
import os
import sqlQueries
import sqlFileManager
import excelFileManager
import structs


def parse_args():
    p = argparse.ArgumentParser(description='Process some integers.')
    p.add_argument('--group', type=int, help='Group number')
    p.add_argument('--number', type=int, help='Number of items in one group')
    p.add_argument('--streamType', default='a' , help='Stream type (r/r+/w/w+/a/a+')
    p.add_argument('--fileNameTxt', default='./queries', help='Name or path of  txt file')
    p.add_argument('--fileNameExcel', default='none', help='Name or path of excel sheet', required=True)
    p.add_argument('--overrideTxtFile', default='n', help='Override default txt file ([y]es or [n]o)?')  
    return p.parse_args()


if __name__ == '__main__':
    args = parse_args()       

    commands = excelFileManager.fileStream(args.fileNameExcel)       
    insertQueries1 = sqlQueries.insertUP_SchematyOcenOpisowychNaglowekFor(commands[0])
    insertQueries2 = sqlQueries.insertUP_SchematyOcenOpisowychWierszFor(commands[1])
    sqlFileManager.outputFileStream("a","tmpTable.sql",insertQueries1)
    sqlFileManager.outputFileStream("a","tmpTable.sql",insertQueries2)
    
    # excelFileManager.fileInfo(sheet[1])    
    # excelManager.fileStream(sheet[0])
    # print(UP_SchematyOcenOpisowych.nazwa)