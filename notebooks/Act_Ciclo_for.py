# %% [markdown]
# # Ciclos for
# 
# Repiten una instrucción varias veces (hasta que existan elementos en una lista)

# %%
# Impreme los elementos de una lista
numeros=[10,20,30,40,50,60]
for num in numeros:
    print(num)

# %%
lista1=['Ana',23,'Catalina', [29,18]]
for nom in lista1:
  print(nom)

# %%
nombres = ['Pedro', 'Eduardo', 'Antonio', 'Margarito']
for nom in nombres:
  print(f'!Hola {nom}!')

# %%
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
for planet in planets:
    print(planet, end=' ') # print all on same line

# %%
print(range(2,5))

# %%
for n in range(2,5):
  print(n)

# %%
n = 5
for k in range(1,11):
  print(f' 3 x {k} = {n*k}')

# %%
for k in range(1,11):
  print('*'*k)

# %%
squares = []
for n in range(10):
    squares.append(n**2)
squares

# %%
# Usando list comprehension
squares = [n**2 for n in range(10)]
squares

# %%
# Termina un ciclo cuando se da una condición
for i in range(6):
    if i == 3:
        break
    print(i)

# %%
# Salta un caso bajo una condición
for i in range(6):
    if i in [1,4]:
        continue
    print(i)

# %%
# Otro ejemplo usando list comprehension
lista2 = [ 8, 21, 40, 2, 45, 27, 15 ]
impares = [i for i in lista2 if i%2 == 1]
impares

# %%
s = ''' Imagina que este establecimiento desea contruir un indicador de desempeño (KIP) para sus ventas.  
Imagina que tu equipo y tú son los responsables de construir dicho indicador. ¿qué datos analizarás?. 
¿qué medidas estadisticas tomarás en cuenta?. Ejemplo: para medir el desempeño de las ventas puedes analizar 
¿cuál es el promedio de las ventas, la varianza de las mismas, ¿qué producto es el que más se consume?, 
¿cuál es el producto más vendido?, ¿qué carrera o especialidad es la que más consume en el negocio?'
# print all the uppercase letters in s, one at a time'''
for char in s:
    if char.isupper() or not(char.isalpha()):
        print(char, end='')

# %%



