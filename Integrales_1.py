import numpy as np
import matplotlib.pyplot as plt
from sympy import integrate, Symbol 

# 1. Definir la función (el integrando)
def f(t):
    return 3.5 * t + 3

# 2. Definir los límites de integración
a = 60  # Límite inferior
b = 120 # Límite superior

# 3. Generar valores de t para la curva de la función
# Extendemos un poco el rango para ver mejor la línea
t_curve = np.linspace(a - 10, b + 10, 400)
f_curve = f(t_curve)

# 4. Generar valores de t para el área sombreada (solo dentro de los límites)
t_fill = np.linspace(a, b, 400)
f_fill = f(t_fill)

# 5. Crear el gráfico
plt.figure(figsize=(10, 7))

# Plotear la curva de la función
plt.plot(t_curve, f_curve, color='green', linewidth=2, label=r'$f(t) = 3.5t + 3$')

# Rellenar el área bajo la curva
# Como la función es positiva en todo el rango, solo necesitamos un fill_between
plt.fill_between(t_fill, f_fill, color='lightgreen', alpha=0.6, label='Área de la integral')

# Añadir líneas verticales para los límites de integración
plt.axvline(a, color='gray', linestyle='--', linewidth=1)
plt.axvline(b, color='gray', linestyle='--', linewidth=1)

# Añadir etiquetas de texto para los límites
# Ajustamos la posición vertical de las etiquetas para que no se superpongan con el eje t
min_f_val_visible = plt.ylim()[0] # Obtener el límite inferior del eje y actual
plt.text(a, min_f_val_visible * 0.9, f'$a={a}$', horizontalalignment='center', fontsize=12)
plt.text(b, min_f_val_visible * 0.9, f'$b={b}$', horizontalalignment='center', fontsize=12)


# Añadir el eje t (y=0) para referencia
plt.axhline(0, color='black', linewidth=0.8)

# Título y etiquetas de ejes
# Usamos 't' en el eje x para reflejar la variable de integración
plt.title(r'Representación Gráfica de $\int_{60}^{120} (3.5t + 3)dt$')
plt.xlabel('t')
plt.ylabel('f(t)')
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()

# Ajustar los límites del gráfico para una mejor visualización
# Asegurar que el eje y comienza desde 0 ya que los valores de f(t) son positivos y grandes
plt.ylim(bottom=0)
plt.xlim(t_curve.min(), t_curve.max())

# Mostrar
plt.show()

# Opcional: Calcular y mostrar el valor numérico de la integral (usando SymPy)
t_sym = Symbol('t')
integrand_sym = 3.5 * t_sym + 3
definite_integral_sym = integrate(integrand_sym, (t_sym, a, b))

print(f"El valor exacto de la integral calculada por SymPy es: {definite_integral_sym}")
print(f"El valor calculado en la imagen es: 19080 litros")