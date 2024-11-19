import pandas as pd

class SalesService:
    def __init__(self, data: pd.DataFrame):
        self.data = data.copy()

    def cal_total_sales(self):
        #add 'TotalSales' column to the table
        self.data['TotalSales'] = self.data['UnitsSold'] * self.data['UnitPrice']
        return self.data
    
    def cal_total_sales_per_product(self):
        return self.data.groupby('ProductName')['TotalSales'].sum()
    
    def cal_total_sales_per_customer(self):
        return self.data.groupby('CustomerID')['TotalSales'].sum()
    
    def cal_sale_summary(self):
        total_units_sold = self.data['UnitsSold'].sum()
        total_revenue = self.data['TotalSales'].sum()
        average_sale_price = self.data['UnitPrice'].mean()

        return{
            # "key" : value,
            "total_units_sold" : total_units_sold,
            "total_revenue" : total_revenue,
            "average_sale_price": average_sale_price
        }
    
    def top_products(self, n = 3):
        return self.cal_total_sales_per_product().sort_values(ascending = False).head(n)
    
    def cal_total_sales_per_country(self):
        return self.data.groupby('Country')['TotalSales'].sum()
    
    