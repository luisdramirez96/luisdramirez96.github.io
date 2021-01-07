import pandas as pd

df = pd.read_csv('BreakfastFiestaOrderLog.csv', usecols = ['Cliente', 'Orden', 'Delivery Address'], index_col='Cliente')

print(df)
