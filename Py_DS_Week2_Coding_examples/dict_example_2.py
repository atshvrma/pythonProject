if __name__ == '__main__':
    # Product inventory as nested dictionary
    product_catalog = {
        "P001": {"name": "Laptop", "price": 55000},
        "P002": {"name": "Mouse", "price": 450},
        "P003": {"name": "Keyboard", "price": 1200},
        "P004": {"name": "Monitor", "price": 7500},
        "P005": {"name": "USB Hub", "price": 999}
    }

    # Filter products priced above ₹1000
    print("Products priced above ₹1000:")
    for pid, details in product_catalog.items():
        if details["price"] > 1000:
            print(f"{details['name']} (₹{details['price']})")