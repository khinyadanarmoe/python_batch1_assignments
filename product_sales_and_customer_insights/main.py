from sales_data import SalesData
from sales_view import SalesView
from sales_service import SalesService

sales_data = SalesData('product_sales_and_customer_insights/product_sales.csv', 'product_sales_and_customer_insights/customers.csv')
merged_data = sales_data.get_data()

sales_service = SalesService(merged_data)
merged_data = sales_service.cal_total_sales()

def main():
    
    while(True):
        print('------Sales Analysis and Customer Insights--------\n')
        menu()
        choice = input('Choose Action')
        match choice:
            case '1':
                n = int(input('How many top products would you like to see?\n'))
                top_products(n)
            case '2':
                total_sales_per_product()
            case '3':
                total_sales_per_customer()
            case '4':
                total_sales_per_country()
            case '5':
                sales_summary()
            case '6':
                overall_sales()
            case '7':
                print('Exiting.......')
                break
            case _:
                print('Invalid input.')
                choice = input('Choose Action')
              

def menu():
    print('1. Show the list of top sales products.')
    print('2. Show total sales per product.')
    print('3. Show total sales per customer.')
    print('4. Show total sales per country.')
    print('5. Show sales summary.')
    print('6. Show overall sales.')
    print('7.Exit.')


def top_products(n):
    top_sales_product = sales_service.top_products(n)  
    SalesView.display_top_products(top_sales_product)

def total_sales_per_product():
    total_sales_per_product = sales_service.cal_total_sales_per_product()
    SalesView.display_total_sales_per_product(total_sales_per_product)

def total_sales_per_customer():
    total_sales_per_customer = sales_service.cal_total_sales_per_customer()
    SalesView.display_total_sales_per_customer(total_sales_per_customer)

def total_sales_per_country():
    total_sales_per_country = sales_service.cal_total_sales_per_country()
    SalesView.display_total_sales_per_country(total_sales_per_country)

def sales_summary():
    sales_summary = sales_service.cal_sale_summary()
    SalesView.display_sale_summary(sales_summary)

def overall_sales():
    overall_sales = sales_service.cal_total_sales()
    SalesView.display_overall_sales(overall_sales)


    

main()