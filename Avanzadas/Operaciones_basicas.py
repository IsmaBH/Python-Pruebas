#from __future__ import division
#import numpy as np
import matplotlib.pyplot as plt
print("Introduzca a z1 = ")
z1 = complex(input())
print("Introduzca a z2 = ")
z2 = complex(input())

z3 = z1 + z2
z4 = z1 - z2
z5 = z1 * z2
z6 = z1 / z2

print("La suma es: ", z3)
print("La resta es: ", z4)
print("La multiplicacion es: ", z5)
print("La division es: ", z6)

def move_spines():
    fix, ax = plt.subplots()
    for spine in ["left", "bottom"]:
        ax.spines[spine].set_position("zero")
    
    for spine in ["right", "top"]:
        ax.spines[spine].set_color("none")
    
    return ax

ax = move_spines()
ax.set_xlim(-100, 100)
ax.set_ylim(-100, 100)
ax.grid()
ax.scatter(z3.real, z3.imag)
ax.scatter(z4.real, z4.imag)
ax.scatter(z5.real, z5.imag)
ax.scatter(z6.real, z6.imag)
plt.title("RESULTADOS")
plt.show()