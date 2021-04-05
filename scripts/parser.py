import pandas as pd
import matplotlib.pyplot as plt

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

    def LineData(self, dataFrame, column, name = 'Per Day Sales'):
        dataFrame['Date'] = pd.to_datetime(dataFrame['Date'], format='%m/%d/%Y').dt.date
        
        data = dataFrame.groupby('Date').sum()
        colIndex = data.columns.get_loc(column)
        
        return pd.DataFrame(data.iloc[:, colIndex]).rename(columns = {'cogs': name})

    def GetUnique(self, dataFrame, column):
        data = dataFrame.groupby(column).count()

        value = ['Any']
        for val in data.index:
            value.append(val)
        return value
    
    def Filter(self, dataFrame, city = 'any', customer = 'any', gender = 'any', product = 'any', payment = 'any'):
        filters = [city, customer, gender, product, payment]
        
        data = dataFrame
            
        if filters[0].capitalize() != "Any":
            data = dataFrame[dataFrame['City'] == filters[0]]
                            
        if filters[1].capitalize() != "Any":
            data = data[data['Customer type'] == filters[1]]
                                                    
        if filters[2].capitalize() != "Any":
            data = data[data['Gender'] == filters[2]]

        if filters[3].capitalize() != "Any":
            data = data[data['Product line'] == filters[3]]

        if filters[4].capitalize() != "Any":
            data = data[data['Payment'] == filters[4]]

        return data
