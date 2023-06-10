# Ejercicio Crediclub

Este es un ejercicio en el que se procesan exceles a una base de datos y se genera un api para accesarlas

Con fines de simplificar el ejercicio se utilizo SQLite como base de datos SQL pero en un ambiente real se utilizaría otros motores de base de datos.

## Tecnologías y Librerías Utilizadas
- Python 3
- FastAPI
- SQLite
- Pandas

## Como correr el código

Para correr el código primero se requiere procesar los datos esto se logra haciendo lo siguiente en una terminal:

```
python procesarExcels.py
```

Esto lee y guarda los archivos a la base de datos

Para correr el servidor del api se puede ejecutar de la siguiente manera:

```
uvicorn apiMontos:app --reload
```

Para ello se tiene que asegurar que se tenga uvicorn si no se tiene se puede instalar de la siguiente manera:
```
 pip install "uvicorn[standard]"
```

Para accesar el API se utiliza la documentación generada por FastAPI en la liga
[http://http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## Explicación de la solucion

Antes de generar procesos de automatización hay que entender bien primero cuales son las entradas y cual es la salida esperada del proceso. En este caso se empezo analizando los exceles de ejemplo que se proporcionaron. Como uno de los objetivos de la prueba es guardar la información de estos archivos (simulando lo que sería un proceso manual) primero se vio que tenían en común todos los archivos y que podría ser de interes guardar. Igual se examino los archivos por posibles errores que se pudieran encontrar en ellos como son falta de datos, valores erroneos o falta de valores. Afortunadamente los archivos se encontraban muy uniformes simplificando la estructura que tomaría la base de datos. Esta estructura sería la siguente tabla:

Fecha | Cliente | Monto | Provedor
------|---------|-------|---------
2023-03-17 00:00:00| Luciano|5678.9|Banamex
....|....|....|....

A pesar de que los archivos eran uniformes, uno de ellos presentaba errores. Especificamente el archivo de Bancomer, el cual tenía una columna en el que el monto era un guion. Pensandolo como si fuera un proceso automático, con el manejo de dinero no es bueno asumir y crear valores, entonces solo las entradas sin errores se deben de registrar en la tabla anteriormente mostrada. Para tener un mejor registro de posibles errores y facilitar un futuro proceso de correción, decidí crear una tabla hermana a la anterior donde se muestra la información erronea y registra el archivo en el que se encontro el error. Esto para facilitar un futuro proceso de correción de errores.

Con este esquema en mente me puse a codificar la solución. Utilizando el lenguaje de Python es fácil de manipular información estructurada como lo es un archivo de Excel, especificamente utilizando la librería de Pandas. Para facilitar la ejecución de este código se decidio implementar una base de datos en SQLite en vez de generar una base de datos con otro motor.

Finalmente para accesar a la información de la base de datos se utilizo la teconlogía de FastAPI.

## Concluciones

Para este ejercicio se hicieron asumpciones sobre la naturaleza de los datos, pero creo que es importante que se definan más reglas de negocio para evitar ambiguedad en un tipo de sistema similar. Con esto me refiero a definir unos minimos requerimentos que se busca de cada fuente. En este caso se asumio que todas las fuentes de los archivos generan archivos similares, pero en un ambiente vivo diferentes sistemas generan archivos de diferentes formatos que talvez cada uno requiera su propio proceso de formateo antes de buscar agregarlo a una base de datos. De la misma manera reglas de negocio más claras ayudan tambien a definir que lo que se guarde en la base de datos sea de mayor relevancia a quien lo vaya a utilizar.

También para la creación del API ayudaría tener definido que es lo que se planea consumir de la base de datos, para tener un api mejor enfocado al uso verdadero que se le va a dar.