import pandas as pd

columns = ['City', 'Customer type', 'Gender','Product line', 'Unit price',
           'Quantity', 'Tax 5%', 'Total', 'Date', 'Payment', 'cogs',
           'gross margin percentage', 'gross income','Rating']



def Import(path, columns = columns):
    data = pd.read_csv(path)
    return data[columns]

def Mapper(dataFrame, column, mapKeys):
    dataFrame[column] = dataFrame[column].map(mapKeys)
    return dataFrame


