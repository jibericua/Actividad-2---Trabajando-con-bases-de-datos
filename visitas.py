import sqlite3
import datetime

"""
datetime.datetime.now().replace(microsecond=0).isoformat()

devuelve fecha hora actual en formato ISO8601 simple

yyyymmddThh:mm:ss

"""

class Persona:
    def __init__(self, dni, apellido, nombre='', movil=''):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.movil= movil


def ingresa_visita(persona):
    """Guarda los datos de una persona al ingresar"""
    conn = sqlite3.connect('recepcion.db')

    q = f"""SELECT dni FROM personas WHERE dni = '{persona.dni}'"""

    resu = conn.execute(q)

    if resu.fetchone():
        print("ya existe")
    else:
        q = f"""INSERT INTO personas (dni, nombre, apellido, movil)
                VALUES ('{persona.dni}',
                        '{persona.nombre}',
                        '{persona.apellido}',
                        '{persona.movil}');"""
        print(q)
        conn.execute(q)
        conn.commit()
    
    destino = input("destino:")

    conn.close()

    conn = sqlite3.connect('recepcion.db')
   
    q = f"""SELECT dni FROM personas WHERE dni = '{persona.dni}'"""
    
    resu = conn.execute(q)

    ingreso = datetime.datetime.now().replace(microsecond=0).isoformat()

    egreso = 0

    numid = 0

    if resu.fetchone():
        numid += 1


    if resu.fetchone():
        q = f"""INSERT INTO ingresos_egresos (id, dni, fechahora_in, fechahora_out, destino)
                VALUES ('{numid}',
                        '{persona.dni}',
                        '{ingreso}',
                        '{egreso}',
                        '{destino}');"""
                        
    

def egresa_visita (dni):
    """Coloca fecha y hora de egreso al visitante con dni dado"""  
    conn = sqlite3.connect('recepcion.db')
   
    q = f"""SELECT dni FROM personas WHERE dni = '{dni}'"""
    
    resu = conn.execute(q)

    egreso = datetime.datetime.now().replace(microsecond=0).isoformat()

    if resu.fetchone():
        q = f"""UPDATE ingresos_egresos WHERE dni = '{dni}' and fechahora_out != 0 set(fechahora_out)
                VALUES ('{egreso}');"""




def lista_visitantes_en_institucion ():
    """Devuelve una lista de objetos Persona presentes en la instituci??n"""
    
    conn = sqlite3.connect('recepcion.db')
    q = f"""SELECT * FROM personas;"""

    resu = conn.execute(q)
    
    for fila in resu:
        print(fila)
    conn.close()


def busca_vistantes(fecha_desde, fecha_hasta, destino, dni):
    """ busca visitantes segun criterios """
    conn = sqlite3.connect('recepcion.db')
    
    q = f"""SELECT * FROM ingresos_egresos WHERE fechahora_in = '{fecha_desde}' & WHERE fechahora_out = '{fecha_hasta}' & WHERE destino = '{destino}' & WHERE dni = '{dni}'"""
    
    conn.execute(q)

    print(q)
   


def iniciar():
    conn = sqlite3.connect('recepcion.db')

    qry = '''CREATE TABLE IF NOT EXISTS
                            personas
                    (dni TEXT NOT NULL PRIMARY KEY,
                     nombre   TEXT,
                     apellido TEXT  NOT NULL,
                     movil    TEXT  NOT NULL

           );'''

    conn.execute(qry)

    qry = '''CREATE TABLE IF NOT EXISTS
                            ingresos_egresos
                    (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                     dni TEXT NOT NULL,
                     fechahora_in TEXT  NOT NULL,
                     fechahora_out TEXT,
                     destino TEXT

           );'''

    conn.execute(qry)

""""
if __name__ == '__main__':
    iniciar()

    
    p = Persona('28123456', '??lavarez', 'Ana', '02352-456789')

    ingresa_visita(p)

    
    doc = input("Ingrese dni> ")
    apellido = input("Ingrese apellido> ")
    nombre = input("nombre> ")
    movil = input("m??vil > ")

    p = Persona(doc, apellido, nombre, movil)
    
    ingresa_visita(p)
  
    
    lista_visitantes_en_institucion()
"""
    
