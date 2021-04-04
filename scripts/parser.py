import pandas as pd
import matplotlib.pyplot as plt

columns = ['City', 'Customer type', 'Gender','Product line', 'Unit price',
           'Quantity', 'Tax 5%', 'Total', 'Date', 'Payment', 'cogs',
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

    def DateSum(self, dataFrame, column):
        dataFrame[f'{ column }'] = pd.to_datetime(dataFrame[f'{ column }'], format='%m/%d/%Y')
        return [date for date in dataFrame[f'{ column }']]

