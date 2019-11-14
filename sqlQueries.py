
def insertUP_SchematyOcenOpisowychNaglowek(IdScheamtyOcenOpisowych,Wartosc,Kolejnosc):
    commands = []    
    commands.append(f"""
    INSERT INTO [dbo].[UP_SchematyOcenOpisowychNaglowek] ([IdScheamtyOcenOpisowych], [Wartosc], [Kolejnosc]) VALUES ({IdScheamtyOcenOpisowych}, '{Wartosc}', {Kolejnosc});""")
    return commands

def insertUP_SchematyOcenOpisowychNaglowekFor(data):
    commands = []
    for i in data:
        commands.append(f"""
    INSERT INTO [dbo].[UP_SchematyOcenOpisowychNaglowek] VALUES {i};""")
    return commands

def insertUP_SchematyOcenOpisowychWiersz(IdScheamtyOcenOpisowych,Wartosc,Wyroznienie,Kolejnosc):
    commands = []
    commands.append(f"""
    INSERT INTO [dbo].[UP_SchematyOcenOpisowychWiersz] ([IdScheamtyOcenOpisowych], [Wartosc], [Wyroznienie], [Kolejnosc]) VALUES ({IdScheamtyOcenOpisowych}, '{Wartosc}', {Wyroznienie},{Kolejnosc}) GO""")
    return commands

    
def insertUP_SchematyOcenOpisowychWierszFor(data):
    commands = []
    for i in data:
        commands.append(f"""
    INSERT INTO [dbo].[UP_SchematyOcenOpisowychWiersz] VALUES {i};""")
    return commands


def insertUP_SchematyOcenOpisowychZawartoscFor(data):
    commands = []
    for i in data:
        commands.append(f"""
    INSERT INTO [dbo].[UP_SchematyOcenOpisowychZawartosc] VALUES {i};""")
    return commands


def selectIdUP_SchematyOcenOpisowychNaglowek(data):
    command = f"""(SELECT Id FROM [dbo].[UP_SchematyOcenOpisowychNaglowek] WHERE Wartosc = '{data}' AND IdSchematyOcenOpisowych = @id)"""
    return command


def selectIdUP_SchematyOcenOpisowychWiersz(Kolejnosc,data):
    command = f"""(SELECT Id FROM [dbo].[UP_SchematyOcenOpisowychWiersz] WHERE Wartosc = '{data}' AND IdSchematyOcenOpisowych = @id AND Kolejnosc = {Kolejnosc})"""
    return command

def insertUP_SchematyOcenOpisowych(typSchematu,data):
    commands = []
    commands.append(f"""
    INSERT INTO [dbo].[UP_SchematyOcenOpisowych] VALUES ({typSchematu},'{data[0]}',{data[1]},'{data[2]}');
    
    DECLARE @id int;
    SET @id = (Select Id from UP_SchematyOcenOpisowych where Nazwa = '{data[0]}' AND Opis = '{data[2]}');
    """)
    commands.append(f"")
    return commands