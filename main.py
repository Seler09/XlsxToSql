import argparse
import os
import createFile
import fileManager
import excelManager



class UP_SchematyOcenOpisowych:
    typSchematu = 0
    nazwa = ''
    poziom = 0
    opis = ''


class UP_SchematyOcenOpisowychNaglowek:
    idSchematyOcenOpisowych = 0
    wartosc = ''
    kolejnosc = 0


class UP_SchematyOcenOpisowychWiersz:
    idSchematyOcenOpisowych = 0
    wartosc = ''
    wyroznienie = 0
    kolejnosc = 0


class UP_SchematyOcenOpisowychZawartosc:
    idSchematyOcenOpisowych = 0
    idSchematyOcenOpisowychWiersz = ''
    idSchematyOcenOpisowychNaglowek = None
    wartosc = ''
    grupa = 0
    kolejnosc = 0


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
    
    naglowek = UP_SchematyOcenOpisowychNaglowek()

    sheet = excelManager.fileStream(args.fileNameExcel)       
    
    excelManager.fileInfo(sheet[1])    
    excelManager.fileStream(sheet[0])
    print(UP_SchematyOcenOpisowych.nazwa)