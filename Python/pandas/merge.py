import pandas

# Crea columnas.
col1 =['client','id','more']
col2 =['client','id','more2']

# Data para el primer data frame.
data1 = [
    ['AB','1','a'],
    ['AB','2','a'],
    ['AB','3','a'],
    ['AB','4','a'],
    ['AB','5','a'],
    ['AB','6','a'],
    ['AB','7','a'],
    ['AB','8','a'],
    ['AB','9','a'],
    ['AB','10','a'],
    ['AB','11','a'],
    ['CD','1','a'],
]

# Data para el segundo data frame.
data2 = [
    ['CD','1','b'],
    ['CD','2','b'],
    ['CD','3','b'],
    ['CD','4','b'],
    ['CD','5','b'],
    ['CD','6','b'],
    ['CD','7','b'],
    ['CD','8','b'],
    ['CD','9','b'],
    ['CD','10','b'],
    ['CD','12','b'],
    ['AB','11','b'],
]

# DataFrames.
df1 = pandas.DataFrame(data1,columns=col1)
df2 = pandas.DataFrame(data2,columns=col2)

# Crea los merges.
rs1 = df1.merge(df2,how='inner')
rs2 = df1.merge(df2,how='outer')
rs3 = df1.merge(df2,how='left')
rs4 = df1.merge(df2,how='right')
rs5 = df1.merge(df2,how='outer',indicator=True,on=['client','id']).query("_merge=='left_only'").drop('_merge',axis=1)
rs6 = df1.merge(df2,how='outer',indicator=True,on=['client','id']).query("_merge=='right_only'").drop('_merge',axis=1)

# Imprime los resultados.
print('Inner: Selecciona solo lo que coincide entre las 2 columnas.')
print(rs1.to_markdown())
print('Outer: Selecciona todo uniendolo si encuentra coincidencias.')
print(rs2.to_markdown())
print('Left: Selecciona toda primera tabla con lo que encuentre de la segunda.')
print(rs3.to_markdown())
print('Right: Selecciona toda la segunda tabla con lo que encuentre de la primera.') 
print(rs4.to_markdown())
print('Left Exclusive: Selecciona todo lo que esta en la primera tabla y no esta en la segunda.')
print(rs5.to_markdown())
print('Right Exclusive: Selecciona todo lo que esta en la seugnda table y no esta en la primera.')
print(rs6.to_markdown())
