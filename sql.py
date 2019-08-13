import pyodbc 
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DPO-00962014;'
                      'Database=EFEB_POWIATMYSLENICKI;'
                      'Trusted_Connection=yes;')

def test():
    cursor = conn.cursor()
    cursor.execute("""SELECT Id FROM EFEB_POWIATMYSLENICKI.dbo.UP_SchematyOcenOpisowychWiersz
    WHERE IdSchematyOcenOpisowych = 14 """)
    
    for row in cursor:
        print(row)
        
        