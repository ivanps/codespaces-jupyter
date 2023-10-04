# %% [markdown]
# # Condicionales
# Los condicionales son instrucciones que permiten que se ejecute una acción dependiendo de una prueba lógica.
# 
# Los principales condicionales en programación son: if, else, if else

# %% [markdown]
# **Simbolos de condiciones**
# * igual a ==
# * Diferente a !=
# * Mayor que >
# *Menor que <
# * Mayor o igual que >=
# * Menor que o igual que <=

# %%
edad=int(input("Ingresa tu edad: "))

# %%
if edad >=18:
  print("Puedes votar")

# %%
edad=1
print(edad)

# %%
if edad >=18:
  print("Puedes votar")

# %% [markdown]
# Ejemplo else

# %%
if edad >=18:
  print('Puedes votar')
else:
  print('No puedes votar')  

# %% [markdown]
# Ejemplo else if

# %%
numero=int(input('ingresa un número: '))

# %%
if numero >0:
  print('El numero es positivo')
elif numero <0:
  print('El número es negativo')
else:
  print('El número es cero')

# %%
numero=-1
print(numero)

# %%
if numero >0:
  print('El numero es positivo')
elif numero <0:
  print('El número es negativo')
else:
  print('El número es cero')

# %%
numero=0
print(numero)

# %%
if numero >0:
  print('El numero es positivo')
elif numero <0:
  print('El número es negativo')
else:
  print('El número es cero')

# %% [markdown]
# Utilizar condicionales en cadenas de texto

# %%
list_nom=['Ana','Lucas','Catalina','Javier']

# %%
nombre=list_nom[3]

# %%
if nombre in list_nom:
   print('¡Hola ',nombre,'!')

# %% [markdown]
# A partir de la versión 3.6 se introdujeron las f-string para imprimir texto con sus variables el formato es el siguiente:
# 
# **f"Esta es una f-string {nombre_var} y {nombre_var}."**
# 
# Vamos reescribir el último bloque usando f-strings.

# %%
if nombre in list_nom:
   print(f'¡Hola {nombre}!')

# %% [markdown]
# Buscar una letra en una cadena de texto usando condicionales

# %%
cadena=input('Ingresa una cadena de texto: ')

# %%
letra=input('Ingresa una letra: ')

# %%
if letra in cadena:
  print(f'La letra {letra} está dentro de la cadena de texto')
else:
  print(f'La letra {letra} No está dentro de la cadena de texto')

# %%
from string import punctuation
punctuation

# %% [markdown]
# ## Ecuaciones en LaTex

# %% [markdown]
# Podemos insertar fórmula en el notebook si usamos LaTex. Así por escribir fracciones $\frac{1}{2} + \frac{4}{9}$, letras griegas
# $\pi + \theta + \alpha$, fórmulas de cálculo $\frac{dy}{dx} + \int_0^5 (x^3+x-8) dx$, y muchas más.

# %% [markdown]
# Escribe las siguientes fórmulas usando la notación de LaTex.    

# %% [markdown]
# ![latex1.png](attachment:latex1.png)

# %%



