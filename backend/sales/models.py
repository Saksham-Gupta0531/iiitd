from django.db import models

# SQLite3 model
class SalesData(models.Model):
    product_id = models.CharField(max_length=100)
    sale_date = models.DateField()
    sales_rep = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    sales_amount = models.FloatField()
    quantity_sold = models.IntegerField()
    product_category = models.CharField(max_length=100)
    unit_cost = models.FloatField()
    unit_price = models.FloatField()
    customer_type = models.CharField(max_length=100)
    discount = models.FloatField()
    payment_method = models.CharField(max_length=50)
    sales_channel = models.CharField(max_length=50)
    region_and_sales_rep = models.CharField(max_length=255)

    class Meta:
        db_table = 'sales_data_sqlite_fixed'
        app_label = 'sales'  # Updated app name

    def __str__(self):
        return f"{self.product_id} - {self.sales_rep}"


# MySQL model
class MySQLSalesData(models.Model):
    product_id = models.CharField(max_length=100)
    sale_date = models.DateField()
    sales_rep = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    sales_amount = models.FloatField()
    quantity_sold = models.IntegerField()
    product_category = models.CharField(max_length=100)
    unit_cost = models.FloatField()
    unit_price = models.FloatField()
    customer_type = models.CharField(max_length=100)
    discount = models.FloatField()
    payment_method = models.CharField(max_length=50)
    sales_channel = models.CharField(max_length=50)
    region_and_sales_rep = models.CharField(max_length=255)

    class Meta:
        db_table = 'mysql_salesdata'
        app_label = 'sales'  # Updated app name

    def __str__(self):
        return f"{self.product_id} - {self.sales_rep}"


# PostgreSQL model
class PostgresSalesData(models.Model):
    product_id = models.CharField(max_length=100)
    sale_date = models.DateField()
    sales_rep = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    sales_amount = models.FloatField()
    quantity_sold = models.IntegerField()
    product_category = models.CharField(max_length=100)
    unit_cost = models.FloatField()
    unit_price = models.FloatField()
    customer_type = models.CharField(max_length=100)
    discount = models.FloatField()
    payment_method = models.CharField(max_length=50)
    sales_channel = models.CharField(max_length=50)
    region_and_sales_rep = models.CharField(max_length=255)

    class Meta:
        db_table = 'postgres_salesdata'
        app_label = 'sales'  # Updated app name

    def __str__(self):
        return f"{self.product_id} - {self.sales_rep}"
