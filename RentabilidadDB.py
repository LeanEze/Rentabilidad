import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

#CONECTAMOS CON LA BASE DE DATOS DESEADA
conn = sqlite3.connect("Northwind.db")

#Obteniendo los 10 productos mas rentables

query = ''' 
    SELECT ProductName, SUM(Price * Quantity) as Revenue
    FROM OrderDetails od
    JOIN Products p ON p.ProductID = od.ProductID
    GROUP BY od.ProductID
    ORDER BY Revenue DESC
    LIMIT 10
'''

#CREAMOS VARIABLE UTILIZADO LA VARIABLE DE CONN Y QUERY
top_products = pd.read_sql_query(query,conn)

#DEFINIMOS PARAMETROS DEL GRAFICO
top_products.plot(x="ProductName", y="Revenue", kind="bar", figsize=(10,5), legend=False)

plt.title("10 Productos mas rentables")
plt.xlabel("Productos")
plt.ylabel("Revenue")
plt.xticks(rotation=90)
plt.show()

#Obteniendo los 10 empleados mas efectivos

query2 = '''
    SELECT FirstName || " " || LastName as Employees, COUNT(*) as Total
    FROM Orders o
    JOIN Employees e
    ON e.EmployeeID = o.EmployeeID
    GROUP BY o.EmployeeID
    ORDER BY Total DESC
    LIMIT 10
'''
top_employees = pd.read_sql_query(query2,conn)
top_employees.plot(x="Employees", y="Total", kind="bar", figsize=(10,5), legend=False)

plt.title("Empleados mas efectivos")
plt.xlabel("Empleados")
plt.ylabel("Total vendido")

plt.xticks(rotation=45)
plt.show()

#Obteniendo los 3 empleados menos efectivos

query3 = '''
    SELECT FirstName  || " " || LastName as Employees, COUNT(*) as Total
    FROM Orders o
    JOIN Employees e
    ON e.EmployeeID = o.EmployeeID
    GROUP BY o.EmployeeID
    ORDER BY Total ASC
    LIMIT 3
'''
top_employees = pd.read_sql_query(query3,conn)
top_employees.plot(x="Employees", y="Total", kind="bar", figsize=(10,5), legend=False)

plt.title("Empleados mas efectivos")
plt.xlabel("Empleados")
plt.ylabel("Total vendido")

plt.xticks(rotation=45)
plt.show()