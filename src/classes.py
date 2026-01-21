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
    name = str
    description = str
    products = list
    count_categories = int
    product_count = int

    def __init__(
        self, name, description, products, product_count=0, count_categories=0
    ):
        self.name = name
        self.description = description
        self.products = products
        self.product_count = len(products)
        self.count_categories = count_categories
