
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


def insertUP_SchematyOcenOpisowychZawartosc(IdScheamtyOcenOpisowych,Wartosc,Kolejnosc):
    commands = []
    commands.append(f"""
    INSERT INTO [dbo].[UP_SchematyOcenOpisowychNaglowek] ([IdScheamtyOcenOpisowych], [Wartosc], [Kolejnosc]) VALUES ({IdScheamtyOcenOpisowych}, '{Wartosc}', {Kolejnosc}) GO""")
    return commands
