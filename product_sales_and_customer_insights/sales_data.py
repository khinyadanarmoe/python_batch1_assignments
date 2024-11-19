import csv
import pandas as pd

class SalesData:
    def __init__(self, sales_file, customers_file):
        self.sales_file = sales_file
        self.customers_file = customers_file
        self.merged_data = None

    def load_data(self):
        sales_data = pd.read_csv(self.sales_file)
        customers_data = pd.read_csv(self.customers_file)
        self.merged_data = pd.merge(sales_data, customers_data, on = 'CustomerID')

    def get_data(self):
        if self.merged_data is None:
            self.load_data()

        return self.merged_data