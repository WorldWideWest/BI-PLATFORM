import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import MinMaxScaler

columns = ['Date', 'City', 'Customer type', 'Gender','Product line', 'Unit price',
           'Quantity', 'Tax 5%', 'Total', 'Payment', 'cogs',
           'gross margin percentage', 'gross income','Rating']



class Application:
    def __init__(self, columns = columns):
        self.columns = columns

    def Import(self, path):
        data = pd.read_csv(path)
        return data[self.columns]

    def PiePlot(self, dataFrame, column, colors, title):
        data = []
        values = dataFrame.groupby(column).count()
        indicies = [col for col in values.index]
            
        for index in indicies:
            data.append(dataFrame[dataFrame[column] == index].count()[0])
                    
        fig, ax = plt.subplots()
        plt.pie(data, colors = colors, autopct = '%1.2f%%', startangle = 90, textprops = {'color': 'white', 'fontsize': 14, 'fontweight': 'bold'})
                                
        fig.patch.set_facecolor('blue')
        fig.patch.set_alpha(0)

        plt.title(f'{ title }', fontdict = {'fontsize': 14, 'fontweight': 'bold', 'color': 'white'})
                                            
        plt.legend(indicies)

        return fig

    def LineData(self, dataFrame, columns):
        dataFrame['Date'] = pd.to_datetime(dataFrame['Date']).dt.date

        data = dataFrame.groupby('Date').sum()
        # colIndex = data.columns.get_loc(column)
        colIndicies = [data.columns.get_loc(index) for index in columns]
        
        return pd.DataFrame(data.iloc[:, colIndicies])

    def GetUnique(self, dataFrame, column):
        data = dataFrame.groupby(column).count()

        value = ['All']
        for val in data.index:
            value.append(val)
        return value
    
    def Filter(self, dataFrame, columns, city = 'all', customer = 'all', gender = 'all', product = 'all', payment = 'all'):
        defaultColumns = ["Date", "City", "Customer type", "Gender", "Product line", "Payment"]
        
        for col in columns:
            defaultColumns.append(col)

        data = dataFrame
            
        if city.capitalize() != "All":
            data = dataFrame[dataFrame['City'] == city]
                            
        if customer.capitalize() != "All":
            data = data[data['Customer type'] == customer]
                                                    
        if gender.capitalize() != "All":
            data = data[data['Gender'] == gender]

        if product.capitalize() != "All":
            data = data[data['Product line'] == product]

        if payment.capitalize() != "All":
            data = data[data['Payment'] == payment]


        return data[defaultColumns]

    def Preprocessing(self, dataFrame, columnName = "cogs", trainingPct = 0.8):
        scaler = MinMaxScaler()
        
        colIndex = dataFrame.columns.get_loc(columnName)
        index = int(len(dataFrame) * trainingPct)

        return np.array(dataFrame.iloc[:index, colIndex]), np.array(dataFrame.iloc[index:, colIndex]) # x, y Training Sets

    def TrainingSplit(self, trainingSet, days = 1):
        xTrain, yTrain = [], []

        for i in range(days, trainingSet.shape[0])
            xTrain.append(trainingSet[i - days:i, 0])
            yTrain.append(trainingSet[i, 0])

        return np.array(xTrain), np.array(yTrain)

    def TestingSplit(self, inputs, days, dataLen):
        xTest, yTest = [], []
        
        for i in range(days, days + dataLen):
            xTest.append(inputs[i - days:i, 0])
            yTest.append(inputs[i, 0])

        return np.array(xTest), np.array(yTest)

    #def GetInputs(self, )
        
