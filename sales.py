import csv
import argparse


def main():
    parser = argparse.ArgumentParser(description="Sales analytics")
    parser.add_argument("--top", type=int, default=5, help="Number of top products")
    parser.add_argument("--product", help="Filter by priduct name")
    parser.add_argument("file", nargs="?", default="sales.csv", help="filename")
    parser.add_argument(
        "--min-revenue", dest="min_revenue", type=float, help="Filter by min revenue"
    )
    parser.add_argument("--contains", help="Filter by text in product")
    args = parser.parse_args()

    TOP_N = args.top
    file_name = args.file

    revenue = {}

    with open(file_name, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            product = row["product"]
            price = int(row["price"])
            quantity = int(row["quantity"])
            total = price * quantity

            revenue[product] = revenue.get(product, 0) + total

    if args.product is not None:
        revenue = {
            k: v for k, v in revenue.items() if k.lower() == args.product.lower()
        }

    if args.min_revenue is not None:
        revenue = {k: v for k, v in revenue.items() if v >= args.min_revenue}

    if args.contains is not None:
        revenue = {
            k: v for k,v in revenue.items() if args.contains.lower() in k.lower()
        }
    
    sorted_revenue = sorted(revenue.items(), key=lambda x: x[1], reverse=True)[:TOP_N]
    if not revenue:
        print("No items to display")
        return
    else:
        print("Top products:\n")
        for product, total in sorted_revenue:
            print(f"{product}: {total}")


if __name__ == "__main__":
    main()
