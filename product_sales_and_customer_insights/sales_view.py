import pandas as pd

class SalesView:

    @staticmethod
    def display_overall_sales(overall_sales):
        print("\nOverall Sales: ")
        print(overall_sales)

    @staticmethod
    def display_top_products(top_products: pd.Series):
        print("\n Top Products: ")
        print(top_products)

    @staticmethod
    def display_total_sales_per_country(sales_by_country: pd.Series):
        print("\n Sales by Country: ")
        print(sales_by_country)

    @staticmethod
    def display_total_sales_per_product(sales_per_product):
        print("\n Sales per Product: ")
        print(sales_per_product)

    @staticmethod
    def display_total_sales_per_customer(sales_per_customer):
        print("\n Sales per Customer: ")
        print(sales_per_customer)

    @staticmethod
    def display_sale_summary(sale_summary):
        print("\nSale Summary: ")
        print(sale_summary)

    