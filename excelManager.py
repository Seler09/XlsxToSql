import xlrd 
from prettytable import PrettyTable

import fileManager
import sqlQueries

def fileStream(fileName):
    fileObject = xlrd.open_workbook(f"{fileName}", on_demand = True)     
   
    for sheetName in fileObject.sheet_names():
        print('-----------------------', sheetName, '-----------------------')
        currentSheet = fileObject.sheet_by_name('4_LATEK_OPIS') #sheetName        
        sheetData = fileRead(currentSheet)           

    return sheetData, fileObject


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

    for row in range(3,sheet.nrows):               
        for col in range(0,sheet.ncols):            
            if col == 0:
                emptyRow = chceckIfRowEmpty(row,col,sheet)                
            if emptyRow == True:                
                continue     

            if row == 4 and col >= 2: #read row with headers
                fileManager.outputFileStream('a', 'd.txt', 'y' , f"Nagłówek {row} {col-1} {sheet.cell_value(row,col)}\n")            
          
            fileManager.outputFileStream('a', 'd.txt', 'y' , f"{row} {col} {sheet.cell_value(row,col)}\n")

    return schemaName      