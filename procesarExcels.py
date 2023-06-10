# %%
# Importar librerías
import sqlite3
import pandas as pd

detectoErrores = False

# %%
# Generar base de datos
conexionDB = sqlite3.connect("montosRegistrados.db")


# %%
cursorDB = conexionDB.cursor()
# Código para crear la primera tabla
# Si ya se genero se puede comentar y continuar ejecutando
# Como este es una actividad se borran las tablas para asegurar que este funcionando correctamente
# En un ambiente real no se realizaría este paso
cursorDB.execute("DROP TABLE montos")
cursorDB.execute("DROP TABLE errores")
cursorDB.execute("CREATE TABLE montos(fecha, cliente, monto, proveedor)")
cursorDB.execute("CREATE TABLE errores(fecha, cliente, monto, proveedor, archivo)")


# %%
# Leer los Exceles
def leer_archivo_excel(nombreArchivo, colTypes=None, na_values=["-"]):
    """" Función que lee archivos de excel
        Parameters:
            nombreArchivo: El nombre del archivo a leer 
            colTypes: Un dict con los tipos de las columnas. En caso de no ser proporcionado, se asumen los tipos
            na_values: Una lista con los valores considerados vacios
        Returns:
            Regresa un dataFrame con todos los renglones con valores y un dataframe con los renglones con valores faltantes"""
    df = pd.read_excel(nombreArchivo, dtype=colTypes, na_values=na_values)
    
    return df.dropna(), df[df.isnull().any(axis=1)]


# %%
def procesarArchivos(listaDeArchivos):
    """Procesa los archivos separando las entradas con valores validos
        Parameters:
        listaDeArchivos: Una lista que contiene los archivos a procesar"""
    for archivo in listaDeArchivos:
        valValidos, valInvalidos = leer_archivo_excel(archivo, colTypes={"Monto":float})
        if len(valInvalidos.index):
            print("Se encontraron valores erroneos, checar la tabla de errores para revisar las entradas detectadas")
            valInvalidos["Archivo"] = archivo
            detectoErrores = True
            valInvalidos.to_sql(name="errores", con=conexionDB,if_exists='append',index=False)
        valValidos.to_sql(name="montos", con=conexionDB,if_exists='append',index=False)
    

# %%

procesarArchivos(["Banamex.xlsx","Bancomer.xlsx","Santander.xlsx"])
print("Mostrando los valores erroneos detectados en el proceso:\n**NOTA** Estos se pueden revisar también directamente en la base de datos")
print(cursorDB.execute("SELECT * FROM errores").fetchall())

# %%


# %%



