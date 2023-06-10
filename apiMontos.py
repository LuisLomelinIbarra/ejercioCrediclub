from fastapi import FastAPI
from fastapi.responses import FileResponse
import sqlite3
import csv

conexionDB = sqlite3.connect("montosRegistrados.db")
cursorDB = conexionDB.cursor()

app = FastAPI()

@app.get("/")
def read_root():
    return {"Prueba": "Funciona"}
    
@app.get("/montos/suma")
async def suma_montos():
    query = cursorDB.execute("SELECT SUM(monto) as SUMA FROM montos").fetchone()
    return {"Suma Montos": query}

@app.get("/montos/", response_class=FileResponse)
async def regresar_csv():
    query = cursorDB.execute("SELECT * FROM montos").fetchall()
    archivo = "montos.csv"
    with open(archivo,mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(i[0] for i in cursorDB.description)
        writer.writerows(query)
    response = FileResponse(archivo, media_type="text/csv")
    response.headers["Content-Disposition"] = "attachment; filename=Montos.csv"
    return response

@app.get("/errores/", response_class=FileResponse)
async def regresar_csv_err():
    query = cursorDB.execute("SELECT * FROM errores").fetchall()
    archivo = "errores.csv"
    with open(archivo,mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(i[0] for i in cursorDB.description)
        writer.writerows(query)
    response = FileResponse(archivo, media_type="text/csv")
    response.headers["Content-Disposition"] = "attachment; filename=Errores.csv"
    return response