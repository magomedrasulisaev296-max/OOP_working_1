class Product:
    name = str
    description = str
    price = float
    quantity = int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @property
    def price(self):
        return self.__price

    @classmethod
    def new_product(cls, product):
        return Product(
            product["name"],
            product["description"],
            product["price"],
            product["quantity"],
        )

    @price.setter
    def price(self, value):
        if value > 0 and type(value) in [float, int]:
            self.__price = value
        else:
            print("Цена не должна быть нулевая или отрицательная")


class Category:
    product_count = 0
    category_count = int
    name = str
    description = str
    products = list

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        self.product_count =+ len(products)
        self.category_count =+ 1

    @property
    def products(self):
        return "".join(
            [
                f"{i.name}, {i.price}руб. Остаток: {i.quantity}шт.\n"
                for i in self.__products
            ]
        )

    def add_product(self, product):
        self.__products.append(product)
        Category.product_count += 1
