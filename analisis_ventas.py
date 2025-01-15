import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Leer los datos del archivo CSV
datos = pd.read_csv("C:/Users/INTEL/Documents/intro_python/Notebook/ventas.csv")

# 2. Agregar una columna de ingresos
datos["Ingresos"] = datos["Precio"] * datos["Cantidad"]

# 3. Calcular métricas básicas
total_ingresos = datos["Ingresos"].sum()
ventas_por_producto = datos.groupby("Producto")["Cantidad"].sum()

# 4. Mostrar los resultados en consola
print("Total de ingresos:", total_ingresos)
print("Ventas por producto:\n", ventas_por_producto)

# 5. Crear gráficos
# a. Gráfico de barras para ventas por producto
plt.figure(figsize=(8, 5))
sns.barplot(x=ventas_por_producto.index, y=ventas_por_producto.values, palette="viridis")
plt.title("Ventas por Producto")
plt.xlabel("Producto")
plt.ylabel("Cantidad Vendida")
plt.show()

# b. Gráfico de torta para distribución de ingresos
ingresos_por_producto = datos.groupby("Producto")["Ingresos"].sum()
plt.figure(figsize=(8, 5))
ingresos_por_producto.plot.pie(autopct="%1.1f%%", startangle=90, colors=["#ff9999", "#66b3ff", "#99ff99"])
plt.title("Distribución de Ingresos por Producto")
plt.ylabel("")
plt.show()
