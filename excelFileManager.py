import xlrd 
from prettytable import PrettyTable

import sqlFileManager
import sqlQueries
import structs

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
    schemaName = sheet.cell_value(0,0)
    level = sheet.cell_value(1,0)
    description = sheet.cell_value(2,0)
    
    print("Begin")
    for row in range(3,sheet.nrows):               
        for col in range(0,sheet.ncols):            
            if col == 0:
                emptyRow = chceckIfRowEmpty(row,col,sheet)
                print(col," ",row," ",emptyRow)
            if row == 3 and col >= 2: #Naglowek
                sqlFileManager.outputFileStream('a', 'skrypt.sql', 'y' , sqlQueries.insertUP_SchematyOcenOpisowychNaglowek(21,sheet.cell_value(row,col),col-1))      
                print(row, " ", col)           
            if row >= 4 and col <= 1: #Wiersz
                if emptyRow == True:                    
                    continue                
                sqlFileManager.outputFileStream('a', 'skrypt.sql', 'y' , sqlQueries.insertUP_SchematyOcenOpisowychWiersz(21,sheet.cell_value(row,col), 1 if col==0 else 0,f"{col} {row}"))      
    print("Done")
    return schemaName      