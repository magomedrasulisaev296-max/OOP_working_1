from abc import ABC, abstractmethod


class Log_mixin:
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        print(repr(self))

    def __repr__(self):
        name = self.__class__.__name__
        _dict = self.__class__.__dict__
        return f"{name}, {_dict['__static_attributes__']}"


class BaseProduct(ABC):
    @abstractmethod
    def new_product(self):
        pass

    @abstractmethod
    def price(self):
        pass


class Product(Log_mixin, BaseProduct):
    name = str
    description = str
    price = float
    quantity = int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        super().__init__()
        if quantity <= 0:
            raise ValueError
        else:
            return


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

    def __str__(self):
        return f"{self.name}, {self.__price}руб, остаток: {self.quantity}"

    def __add__(self, other):
        if isinstance(self, type(other)):
            return (self.__price * self.quantity) + (other.__price * other.quantity)
        else:
            return TypeError


class Smartphone(Product):
    def __init__(
        self, name, description, price, quantity, efficiency, model, memory, color
    ):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    def __init__(
        self, name, description, price, quantity, country, germination_period, color
    ):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color


class Category(Log_mixin):
    product_count = 0
    category_count = int
    name = str
    description = str
    products = list

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        self.product_count = +len(products)
        self.category_count = +1

    @property
    def products(self):
        return "".join(
            [
                f"{i.name}, {i.price}руб. Остаток: {i.quantity}шт.\n"
                for i in self.__products
            ]
        )

    def add_product(self, product):
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1


    def middle_price(self):
        middle = 0
        try:
            for product in self.__products:
                middle += product.price
            if len(self.__products) > 0:
                answer = middle / len(self.__products)
                return round(answer)
            else:
                return 0
        except ZeroDivisionError:
            print("check product quantity it's must be 0")


    def __str__(self):
        return f"{self.name}, количество продуктов: {len(self.__products)}шт.\n"




