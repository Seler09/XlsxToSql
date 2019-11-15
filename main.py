import argparse
import os
import sqlQueries
import sqlFileManager
import excelFileManager
import excelFileManagerSec
import structs


def parse_args():
    p = argparse.ArgumentParser(description='Process some integers.')
    p.add_argument('--group', type=int, help='Group number')
    p.add_argument('--number', type=int, help='Number of items in one group')
    p.add_argument('--streamType', default='a' , help='Stream type (r/r+/w/w+/a/a+')
    p.add_argument('--fileNameTxt', default='./queries', help='Name or path of  txt file')
    p.add_argument('--fileNameExcel', default='none', help='Name or path of excel sheet', required=True)
    p.add_argument('--overrideTxtFile', default='n', help='Override default txt file ([y]es or [n]o)?')
    p.add_argument('--schemaType','-scht', type=int, help='Type of schema',required=True)
    # p.add_argument('--sheetType','-sht', typ=int, required=True)
    return p.parse_args()


if __name__ == '__main__':
    args = parse_args()       

    indexList = excelFileManagerSec.sheetsNumber(args.fileNameExcel)

    for index in range(indexList):
        commands = excelFileManagerSec.fileStream(args.fileNameExcel,index)
        
        insertQueries0 = sqlQueries.insertUP_SchematyOcenOpisowychNaglowekFor(commands[0])
        insertQueries1 = sqlQueries.insertUP_SchematyOcenOpisowychWierszFor(commands[1])
        insertQueries2 = sqlQueries.insertUP_SchematyOcenOpisowychZawartoscFor(commands[2])
        insertQueries3 = sqlQueries.insertUP_SchematyOcenOpisowych(args.schemaType,commands[3])
    
        sqlFileManager.outputFileStream("a",f"tmpTable{index}.sql",insertQueries3)
        sqlFileManager.outputFileStream("a",f"tmpTable{index}.sql",insertQueries0)
        sqlFileManager.outputFileStream("a",f"tmpTable{index}.sql",insertQueries1)
        sqlFileManager.outputFileStream("a",f"tmpTable{index}.sql",insertQueries2)
        