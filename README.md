Análisis de Datos de la Base de Datos Northwind
Este proyecto consiste en un análisis de datos utilizando Python, SQLite, Pandas y Matplotlib para visualizar información relevante de la base de datos "Northwind". El análisis se centra en la determinación de los productos más rentables y la evaluación del desempeño de los empleados en términos de ventas.

Requisitos
Python 3.x
SQLite
Pandas
Matplotlib
Instrucciones de Uso
Asegúrate de tener instalados los requisitos mencionados anteriormente.
Descarga el archivo Northwind.db, que contiene la base de datos que será utilizada para el análisis.
Ejecuta el script analysis.py proporcionado en este repositorio.
Funcionalidades
1. Productos más Rentables
Este análisis muestra los diez productos más rentables en términos de ingresos generados. Utiliza la tabla OrderDetails y Products para calcular los ingresos totales por producto.

2. Empleados más Efectivos
Este análisis identifica a los diez empleados más efectivos en términos de total de ventas. Utiliza la tabla Orders y Employees para calcular el número total de ventas por empleado.

3. Empleados Menos Efectivos
Este análisis destaca a los tres empleados menos efectivos en términos de total de ventas. Utiliza la misma lógica que el análisis de empleados más efectivos, pero ordena los resultados en orden ascendente.

Resultados
Los resultados de cada análisis se presentan mediante gráficos de barras, que muestran la relación entre los productos o empleados y el total de ingresos o ventas, respectivamente.