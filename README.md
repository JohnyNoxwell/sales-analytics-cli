# Sales Analytics CLI

Command-line tool for analyzing product sales from CSV files.

## Features
- Aggregate revenue per product
- Show TOP-N products
- Filter by product name
- Filter by minimum revenue
- Search products by text

## Usage

python sales.py sales.csv<br>
python sales.py sales.csv --top 3<br>
python sales.py sales.csv --min-revenue 5000<br>
python sales.py sales.csv --product "Phone"<br>
python sales.py sales.csv --contains pro<br>


## CSV format

product,price,quantity<br>
Phone,500,3<br>
Laptop,1000,2<br>
