class Product:
    name = str
    description = str
    price = float
    quantity = int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Category:
    product_count = int
    category_count = int
    name = str
    description = str
    products = list

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products
        self.product_count =+ len(products)
        self.category_count =+ 1
