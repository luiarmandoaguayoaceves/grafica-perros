from tkinter import *
from tkinter import ttk
import pandas as pd
import matplotlib.pyplot as plt

excel = 'perros.xlsx'
datos = pd.read_excel(excel, "Sheet1")
df=pd.DataFrame(datos)
plt.title("Media de edad de perros")
#df.groupby('raza')['edad'].sum().plot(kind='bar', legend='reverse')#Suma de edades de cada raza
# plt.show()
df.groupby('raza')['edad'].mean().plot(kind='bar', legend='reverse')#Media
# plt.show()
# df.groupby('raza')['edad'].value_counts().plot(kind='bar', legend='reverse')#Moda
plt.show()
