import numpy as np
import matplotlib.pyplot as plt

# 1. Definir la función
def f(t):
    return 3.5 * t + 3

# 2. Definir los límites de integración y el número de rectángulos
a = 60  # Límite inferior
b = 120 # Límite superior
n = 6   # Número de rectángulos, como en tu ejercicio

# 3. Calcular el ancho de cada rectángulo (delta t)
delta_t = (b - a) / n

# 4. Generar los puntos 't' para las alturas de los rectángulos (puntos derechos)
# Los puntos derechos de los subintervalos son: a + delta_t, a + 2*delta_t, ..., b
t_rects_right = np.linspace(a + delta_t, b, n)
f_rects_heights = f(t_rects_right) # Altura de cada rectángulo basada en el punto derecho

# 5. Generar los puntos 't' para la base de los rectángulos (puntos izquierdos)
# Estos son los puntos donde comienza cada barra en el gráfico
t_rects_base = np.linspace(a, b - delta_t, n)

# 6. Generar puntos para la curva suave de la función
t_curve = np.linspace(a - 10, b + 10, 400) # Rango extendido para ver más de la curva
f_curve = f(t_curve)

# 7. Crear el gráfico
plt.figure(figsize=(12, 8)) # Aumentamos el tamaño para mejor visualización

# Plotear la curva de la función
plt.plot(t_curve, f_curve, color='blue', linewidth=2, label=r'$f(t) = 3.5t + 3$')

# Plotear los rectángulos
# Usamos plt.bar para dibujar los rectángulos
for i in range(n):
    # La posición x de la barra es el punto de inicio del subintervalo
    # La altura es el valor de la función en el punto DERECHO del subintervalo
    plt.bar(t_rects_base[i], f_rects_heights[i], width=delta_t, align='edge',
            color='lightsalmon', edgecolor='brown', alpha=0.8,
            label='Rectángulos (Suma de Riemann Derecha)' if i == 0 else "")

    # Opcional: Añadir el valor de f(ti) en la parte superior de cada barra
    plt.text(t_rects_base[i] + delta_t, f_rects_heights[i] + 5,
             f'{f_rects_heights[i]:.0f}', ha='center', va='bottom', fontsize=9, color='darkred')


# Añadir líneas verticales punteadas para los límites de los rectángulos
# Estos corresponden a los 'h' o 'delta_t' de tu imagen
t_grid_lines = np.linspace(a, b, n + 1) # a, a+dt, a+2dt, ..., b
for t_line in t_grid_lines:
    plt.axvline(t_line, color='purple', linestyle=':', linewidth=0.8, alpha=0.7)


# Añadir líneas verticales para los límites de integración principales
plt.axvline(a, color='gray', linestyle='--', linewidth=1, label=f'Límite Inferior $a={a}$')
plt.axvline(b, color='gray', linestyle='--', linewidth=1, label=f'Límite Superior $b={b}$')

# Añadir etiquetas de texto para los límites
plt.text(a - 1, plt.ylim()[0] + 5, f'$a={a}$', horizontalalignment='right', fontsize=12)
plt.text(b + 1, plt.ylim()[0] + 5, f'$b={b}$', horizontalalignment='left', fontsize=12)


# Añadir el eje t (y=0) para referencia
plt.axhline(0, color='black', linewidth=0.8)

# Título y etiquetas de ejes
plt.title(f'Aproximación de Integral con {n} Rectángulos (Suma de Riemann Derecha)')
plt.xlabel('t (min)') # Según tu gráfico, la variable es 't' y unidades 'min'
plt.ylabel('f(t)')
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(loc='upper left')

# Ajustar los límites del gráfico para una mejor visualización
plt.ylim(bottom=0) # Asegurar que el eje y comienza desde 0
plt.xlim(t_curve.min(), t_curve.max())


plt.show()

# Calcular y mostrar el resultado numérico exacto de la suma de Riemann (como verificación)
sum_riemann_right = np.sum(f_rects_heights * delta_t)
print(f"El valor de la suma de Riemann derecha calculada es: {sum_riemann_right:.0f}")
print(f"El valor que obtuviste en tu cuaderno es: 20130")