def createListOfComands(group, numebrOfItems):
    commands = []
    for i in range(int(numebrOfItems)):
      commands.append(f"""
      UPDATE UP_SchematyOcenOpisowychZawartosc
      SET Wartosc = ''
      WHERE IdSchematyOcenOpisowych = 20
      AND Grupa = {group}
      AND Kolejnosc = {i+1};
      """)
    return commands


def create(group, numebrOfItems):
    commands = []
    commands.append("""
    INSERT INTO dbo.UP_SchematyOcenOpisowychWiersz (
    IdSchematOcenOpisowych,
    Wartosc,
    Wyroznienie,
    Kolejnosc)
    """)
    for i in range(int(numebrOfItems)):
      commands.append(f"""
      UPDATE UP_SchematyOcenOpisowychZawartosc
      SET Wartosc = ''
      WHERE IdSchematyOcenOpisowych = 20
      AND Grupa = {group}
      AND Kolejnosc = {i+1};
      """)
    return commands 


def insertUP_SchematyOcenOpisowychNaglowek(IdScheamtyOcenOpisowych,Wartosc,Kolejnosc):
    commands = []
    commands.append(f"""
    INSERT INTO [dbo].[UP_SchematyOcenOpisowychNaglowek] ([IdScheamtyOcenOpisowych], [Wartosc], [Kolejnosc]) VALUES ({IdScheamtyOcenOpisowych}, '{Wartosc}', {Kolejnosc}) GO""")
    return commands

