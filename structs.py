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