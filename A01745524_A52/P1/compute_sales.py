
"""
A01745524 - Oscar Nava Jiménez
MNA - TC4017 A5.2
"""
import argparse
import time
import json


def match_sale_catalog(catalog, product):
    """
    :param catalog:dict product catalog
    :param product:dict product information
    :return:
    """
    match = None
    for item in catalog:
        if item["title"] == product["Product"]:
            match = item
            return match
    return match


def main(sales_path: str, catalog_path: str):
    """
    :param sales_path:str File path of sales to be received
    :param catalog_path:str File path of catalog prices to be received
    :return:
    """
    start_time = time.perf_counter()
    total_sales = 0
    with open(sales_path, "r+", encoding="UTF-8") as f:
        sales_data = json.load(f)
    with open(catalog_path, "r+", encoding="UTF-8") as f:
        catalog_data = json.load(f)

    for sale in sales_data:
        price_data = match_sale_catalog(catalog_data, sale)
        if not price_data:
            print(f"No data found in catalog for: {sale["Product"]}")
            continue
        sale_amount = float(price_data["price"]) * sale["Quantity"]
        total_sales += sale_amount

    end_time = time.perf_counter()
    exec_time = end_time-start_time
    with open("../SalesResults.txt", "w", encoding="UTF-8") as f:
        f.write(f"TOTAL SALES: ${total_sales}\n")
        f.write(f"EXECUTION TIME: {exec_time} s\n")
    print(f"TOTAL SALES:{total_sales}\n")
    print(f"EXECUTION TIME: {exec_time} s")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("sales_file", type=str)
    parser.add_argument("catalog_file", type=str)
    args = parser.parse_args()
    sales_file = args.sales_file
    catalog_file = args.catalog_file
    main(sales_file, catalog_file)
