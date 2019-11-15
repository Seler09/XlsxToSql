import xlrd 
from prettytable import PrettyTable
from termcolor import colored

import sqlFileManager
import sqlQueries
import structs


idStruct = 23


def fileStream(fileName):
    fileObject = xlrd.open_workbook(f"{fileName}", on_demand = True)        
    # for sheetName in fileObject.sheet_names():
    #print('-----------------------', sheetName, '-----------------------')    
    currentSheet = fileObject.sheet_by_name('6_LATEK_OPIS') #sheetName        
    sheetData = fileRead(currentSheet)           

    return sheetData


def fileInfo(fileObject):
    tableSheetInfo = PrettyTable(['Sheets in workbook',
    'Numbers of columns',
    'Numbers of rows',
    'Selected sheet', 
    'Visable sheet'])
    
    for sheet in fileObject.sheets():
        tableSheetInfo.add_row([sheet.name, sheet.ncols, sheet.nrows, sheet.sheet_selected, sheet.sheet_visible])
    print(tableSheetInfo)


def chceckIfRowEmpty(row,col,sheet):
    isEmpty = False
    for i in range (0,sheet.ncols):
        if(sheet.cell_type(row,i) == xlrd.XL_CELL_EMPTY):
            isEmpty = True
        else:
            isEmpty = False
    return isEmpty


def emptyOnLeftCell(row,col,sheet):
    isEmpty = False    
    if((sheet.cell_type(row,col) == xlrd.XL_CELL_EMPTY and sheet.cell_type(row,1) != xlrd.XL_CELL_EMPTY) 
    or (sheet.cell_type(row,col) == xlrd.XL_CELL_EMPTY and sheet.cell_type(row,col+1) == xlrd.XL_CELL_EMPTY)):
        print("aaa")
        isEmpty = True
    else:
        isEmpty = False
    return isEmpty


def fileRead(sheet):    
    commandsOP = []
    commandsN = []
    commandsW = []
    commandsZ = []
    rowNumber = 1

    commandsOP.append(sheet.cell_value(0,0).strip().capitalize())
    commandsOP.append(int(sheet.cell_value(1,0)))
    commandsOP.append(sheet.cell_value(2,0).strip())

    print("Begin")
    for row in range(3,sheet.nrows): 
        print("\n")        
        for col in range(0,sheet.ncols):
            if col == 0:
                emptyRow = chceckIfRowEmpty(row,col,sheet)
            if row == 3 and col >= 2: #Naglowek
                structs.UP_SchematyOcenOpisowychNaglowek.kolejnosc = col -1
                structs.UP_SchematyOcenOpisowychNaglowek.wartosc = sheet.cell_value(row,col).strip()
                commandsN.append(f"(@id,'{structs.UP_SchematyOcenOpisowychNaglowek.wartosc}',{structs.UP_SchematyOcenOpisowychNaglowek.kolejnosc})")                                      
            if row >= 4 and col <= 1: #Wiersz

                emptyLeftCell = emptyOnLeftCell(row,col,sheet)

                if emptyRow == True or  emptyLeftCell == True:
                    print(colored((row+1,col+1,"Pominięte"),"yellow"))
                    continue

                structs.UP_SchematyOcenOpisowychWiersz.kolejnosc = row-3 if col == 0 else row-2
                structs.UP_SchematyOcenOpisowychWiersz.wartosc = sheet.cell_value(row,col).strip().capitalize()
                structs.UP_SchematyOcenOpisowychWiersz.wyroznienie = 1 if col == 0 else 0
                print(colored((row+1,col+1, "Dodany"),"magenta"))
                print(colored( structs.UP_SchematyOcenOpisowychWiersz.kolejnosc,"red"))
                commandsW.append(f"(@id,'{structs.UP_SchematyOcenOpisowychWiersz.wartosc}',{structs.UP_SchematyOcenOpisowychWiersz.wyroznienie},{structs.UP_SchematyOcenOpisowychWiersz.kolejnosc})")
                
            if row >= 4 and col > 1: #Zawartość
                # print(colored(rowNumber,"green"))
                # print(row+1,col+1,rowNumber,sheet.cell_value(row,col).strip())                
                structs.UP_SchematyOcenOpisowychZawartosc.idSchematyOcenOpisowychWiersz = sqlQueries.selectIdUP_SchematyOcenOpisowychWiersz(rowNumber,structs.UP_SchematyOcenOpisowychWiersz.wartosc)
                structs.UP_SchematyOcenOpisowychZawartosc.idSchematyOcenOpisowychNaglowek = sqlQueries.selectIdUP_SchematyOcenOpisowychNaglowek(sheet.cell_value(3,col).strip())      
                structs.UP_SchematyOcenOpisowychZawartosc.wartosc = sheet.cell_value(row,col).strip()
                structs.UP_SchematyOcenOpisowychZawartosc.grupa = 1
                structs.UP_SchematyOcenOpisowychZawartosc.kolejnosc = 1
                commandsZ.append(f"(@id,{structs.UP_SchematyOcenOpisowychZawartosc.idSchematyOcenOpisowychWiersz},{structs.UP_SchematyOcenOpisowychZawartosc.idSchematyOcenOpisowychNaglowek},'{structs.UP_SchematyOcenOpisowychZawartosc.wartosc}',{structs.UP_SchematyOcenOpisowychZawartosc.grupa},{structs.UP_SchematyOcenOpisowychZawartosc.kolejnosc})")
        rowNumber += 1              
    print("Done")
    return commandsN, commandsW, commandsZ, commandsOP    