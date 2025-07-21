import matplotlib.pyplot as plt

# Datos
tipos = ['Funcionales', 'No Funcionales', 'Seguridad', 'Validaciones']
valores = [159, 8, 2, 1]

# Gráfico
plt.figure(figsize=(6, 6))
plt.pie(valores, labels=tipos, autopct='%1.1f%%', startangle=140, colors=plt.cm.Pastel1.colors)
plt.title('Distribución por Tipo de Prueba')
plt.axis('equal')  # Círculo perfecto
plt.show()



# Datos
estados = ['Pasaron', 'Fallaron', 'Pendientes']
cantidad = [47, 112, 11]

# Gráfico
plt.figure(figsize=(8, 5))
plt.bar(estados, cantidad, color=['green', 'red', 'orange'])
plt.title('Estado de Pruebas Ejecutadas')
plt.ylabel('Cantidad de Pruebas')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
