# Sales Analytics CLI

Command-line tool for analyzing product sales from CSV files.

## Features
- Aggregate revenue per product
- Show TOP-N products
- Filter by product name
- Filter by minimum revenue
- Search products by text

## Usage

python sales.py sales.csv
python sales.py sales.csv --top 3
python sales.py sales.csv --min-revenue 5000
python sales.py sales.csv --product "Phone"
python sales.py sales.csv --contains pro


## CSV format

product,price,quantity
Phone,500,3
Laptop,1000,2