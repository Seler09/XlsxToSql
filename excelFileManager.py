import xlrd 
from prettytable import PrettyTable

import sqlFileManager
import sqlQueries
import structs

idStruct = 21

def fileStream(fileName):
    fileObject = xlrd.open_workbook(f"{fileName}", on_demand = True)        
    # for sheetName in fileObject.sheet_names():
    #print('-----------------------', sheetName, '-----------------------')
    print('-----------------------4_LATEK_OPIS-----------------------')
    currentSheet = fileObject.sheet_by_name('4_LATEK_OPIS') #sheetName        
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


def fileRead(sheet):
    # schemaName = sheet.cell_value(0,0)
    # level = sheet.cell_value(1,0)
    # description = sheet.cell_value(2,0)
    commandsN = []
    commandsW = []
    commandsZ = []
    print("Begin")
    for row in range(3,sheet.nrows):               
        for col in range(0,sheet.ncols):            
            if col == 0:
                emptyRow = chceckIfRowEmpty(row,col,sheet)                
            if row == 3 and col >= 2: #Naglowek                
                structs.UP_SchematyOcenOpisowychNaglowek.kolejnosc = col -1
                structs.UP_SchematyOcenOpisowychNaglowek.wartosc = sheet.cell_value(row,col).strip()
                commandsN.append(f"({idStruct},'{structs.UP_SchematyOcenOpisowychNaglowek.wartosc}',{structs.UP_SchematyOcenOpisowychNaglowek.kolejnosc})")                      
                print(row, " ", col)           
            if row >= 4 and col <= 1: #Wiersz
                print(col," ",row," ",emptyRow)
                if emptyRow == True:                    
                    continue                
                
    print("Done")
    return commandsN     