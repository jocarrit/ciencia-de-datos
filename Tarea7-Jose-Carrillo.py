#%% [markdown]
# #Tarea 7 - Jose Carrillo
# ##Imports
#%%
import pandas as pd
#%% [markdown]
# ## Ejercicio N 1
# Supongamos que tenemos un modelo predictivo para detectar Fraude
# en Tarjetas de Credito, la variable a predecir es Fraude con dos posibles valores Sı (para el
# caso en que sı fue fraude) y No (para el caso en que no fue fraude). Supongamos la matriz de
# confusion es:
#%%
data = [[83254, 12],[889, 3]]
mc = pd.DataFrame(data, index = ['No', 'Si'], columns = ['Si', 'No'])

print(mc)