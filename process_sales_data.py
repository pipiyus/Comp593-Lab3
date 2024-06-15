""" 
Description: 
  Divides sales data CSV file into individual order data Excel files.

Usage:
  python process_sales_data.py sales_csv_path

Parameters:
  sales_csv_path = Full path of the sales data CSV file
"""
import pandas as pd
import os
import sys
from datetime import data

def main():
    sales_csv_path = get_sales_csv_path()
    orders_dir_path = create_orders_dir(sales_csv_path)
    process_sales_data(sales_csv_path, orders_dir_path)

def get_sales_csv_path():
    """Gets the path of sales data CSV file from the command line

    Returns:
        str: Path of sales data CSV file
    """
    # TODO: Check whether command line parameter provided
    # TODO: Check whether provide parameter is valid path of file
    # TODO: Return path of sales data CSV file
    return 

def create_orders_dir(sales_csv_path):
    """Creates the directory to hold the individual order Excel sheets

    Args:
        sales_csv_path (str): Path of sales data CSV file

    Returns:
        str: Path of orders directory
    """
    # TODO: Get directory in which sales data CSV file resides
    # TODO: Determine the path of the directory to hold the order data files
    # TODO: Create the orders directory if it does not already exist
    # TODO: Return path of orders directory
    return

def process_sales_data(sales_csv_path, orders_dir_path):
    """Splits the sales data into individual orders and save to Excel sheets

    Args:
        sales_csv_path (str): Path of sales data CSV file
        orders_dir_path (str): Path of orders directory
    """
    # TODO: Import the sales data from the CSV file into a DataFrame
    sales_df = pd.read_csv(sales_csv_path)
    
    # TODO: Insert a new "TOTAL PRICE" column into the DataFrame
    sales_df.insert(
        7, "TOTAL PRICE", sales_df["ITEM QUANTITY"] * sales_df["ITEM PRICE"]
    )
    
    # TODO: Remove columns from the DataFrame that are not needed
    sales_df.drop(colums=["ADDRESS", "CITY", "STATE","POSTAL CODE", "COUNTRY"], inplace=True)
     
    # TODO: Groups orders by ID and iterate
    group_dataorder = sales_df.groupby("ORDER_ID")
     
        # TODO: Remove the 'ORDER ID' column
    order_data = order_data.Remove("ORDER ID", axis=1)
        
        # TODO: Sort the items by item number
    order_data = order_data.sort.by("ITEM NUMBER")
        # TODO: Append a "GRAND TOTAL" row
        # TODO: Determine the file name and full path of the Excel sheet
        # TODO: Export the data to an Excel sheet
        # TODO: Format the Excel sheet
        # TODO: Define format for the money columns
        # TODO: Format each colunm
        # TODO: Close the Excelwriter 
    return

if __name__ == '__main__':
    main()