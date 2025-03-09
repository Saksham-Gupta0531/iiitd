import os
import pandas as pd
from django.core.wsgi import get_wsgi_application

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project.settings')
application = get_wsgi_application()

# Now import your models after Django is set up
from sales.models import SalesData, MySQLSalesData, PostgresSalesData

def populate_data():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Get the script's directory
    csv_path = os.path.join(BASE_DIR, "sales_data30000.csv")  # Full path to the CSV file

    df = pd.read_csv(csv_path, parse_dates=['Sale_Date'])

    # Convert DataFrame rows to dictionaries for better performance
    data_list = df.to_dict(orient='records')

    # Insert into SQLite (First 10000 rows)
    SalesData.objects.bulk_create([
        SalesData(
            product_id=row['Product_ID'],
            sale_date=row['Sale_Date'],
            sales_rep=row['Sales_Rep'],
            region=row['Region'],
            sales_amount=row['Sales_Amount'],
            quantity_sold=row['Quantity_Sold'],
            product_category=row['Product_Category'],
            unit_cost=row['Unit_Cost'],
            unit_price=row['Unit_Price'],
            customer_type=row['Customer_Type'],
            discount=row['Discount'],
            payment_method=row['Payment_Method'],
            sales_channel=row['Sales_Channel'],
            region_and_sales_rep=row['Region_and_Sales_Rep']
        )
        for row in data_list[:10000]
    ])

    # Insert into MySQL (10000 to 20000 rows)
    MySQLSalesData.objects.using('mysql').bulk_create([
        MySQLSalesData(
            product_id=row['Product_ID'],
            sale_date=row['Sale_Date'],
            sales_rep=row['Sales_Rep'],
            region=row['Region'],
            sales_amount=row['Sales_Amount'],
            quantity_sold=row['Quantity_Sold'],
            product_category=row['Product_Category'],
            unit_cost=row['Unit_Cost'],
            unit_price=row['Unit_Price'],
            customer_type=row['Customer_Type'],
            discount=row['Discount'],
            payment_method=row['Payment_Method'],
            sales_channel=row['Sales_Channel'],
            region_and_sales_rep=row['Region_and_Sales_Rep']
        )
        for row in data_list[10000:20000]
    ])

    # Insert into PostgreSQL (20000+ rows)
    PostgresSalesData.objects.using('postgresql').bulk_create([
        PostgresSalesData(
            product_id=row['Product_ID'],
            sale_date=row['Sale_Date'],
            sales_rep=row['Sales_Rep'],
            region=row['Region'],
            sales_amount=row['Sales_Amount'],
            quantity_sold=row['Quantity_Sold'],
            product_category=row['Product_Category'],
            unit_cost=row['Unit_Cost'],
            unit_price=row['Unit_Price'],
            customer_type=row['Customer_Type'],
            discount=row['Discount'],
            payment_method=row['Payment_Method'],
            sales_channel=row['Sales_Channel'],
            region_and_sales_rep=row['Region_and_Sales_Rep']
        )
        for row in data_list[20000:]
    ])

    print("Data successfully inserted into all databases")

if __name__ == "__main__":
    populate_data()
else:
    # This allows the script to be imported or executed directly
    populate_data()