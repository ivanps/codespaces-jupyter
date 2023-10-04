# %% [markdown]
# # Fechas en Python

# %%
#Fecha al día de hoy con horas
from datetime import datetime
now = datetime.now()
print(now)

# %%
#importamos  libreria para trabajar con fechas
from datetime import datetime, date, time, timedelta

#fecha del día de hoy
#Por defecto Python escribe las fechas en formato año-mes-día
hoy = date.today()
print(hoy)
#Para cambiar el formato a día/mes/año
print(hoy.strftime('%d/%m/%Y'))

# %%
#tipo de variable para hoy
type(hoy)

# %%
#Si queremos extraer solo el día de la semana
#version larga
dia_semanal= hoy.strftime('%A')
print(dia_semanal)
#version corta
dia_semanac= hoy.strftime('%a')
print(dia_semanac)
#Si queremos el día de la semana con número
dia_semanan=hoy.strftime('%w')
print(dia_semanan)

# %%
#Si queremos extraer el mes
#version corta
mes=hoy.strftime('%b')
print(mes)
#Versión larga
mesl= hoy.strftime('%B')
print(mesl)
#Si queremos el mes con número
mesn=hoy.strftime('%m')
print(mesn)

# %%
#Construir una fecha en especifico
#1 de diciembre de 2020
#año- mes -día
mi_fecha = date(2020, 12, 1)
print(mi_fecha)
#Cambiar el formato a la fecha
print(mi_fecha.strftime('%d/%m/%Y'))

# %%
#Escribir una hora en específico
mi_hora = time(14, 30,2)
print(mi_hora)

# %%
#Convinar fecha y hora
fecha_hora = datetime(2023, 3, 17, 7, 20)
print(fecha_hora)
#Cambiar el formato de una fecha y hora determinada
print(fecha_hora.strftime('%d/%m/%Y %H:%M'))

# %%
#Convertir una cadena de texto en fecha
#from datetime import datetime
texto = '2023-03-17 7:20:03'

# %%
type(texto)

# %%
texto_fecha = datetime.strptime(texto, '%Y-%m-%d %H:%M:%S')
print(texto_fecha)

# %%
type(texto_fecha)

# %%
#Calcular la diferencia entre dos fechas
#from datetime import date
primera_fecha = date(2020, 1, 1)
segunda_fecha = date(2020, 1, 20)
diferencia = segunda_fecha - primera_fecha
print(diferencia)
print('diferencia en días',diferencia.days)
print('diferencia en segundos', diferencia.total_seconds())

# %%
#sumar o restar una cantidad de tiempo a una fecha
#from datetime import datetime, timedelta
fecha_inicial = datetime(2022, 1, 1, 0, 30)
incremento = timedelta(days=1,hours=3, minutes=15)
nueva_fecha = fecha_inicial + incremento
print(nueva_fecha)


