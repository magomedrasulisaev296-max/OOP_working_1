from src.classes import Category, Product


def test_product_creation():
    product = Product("Samsung Galaxy S23 Ultra", "256GB, Серый, 200MP", 180000.0, 5)
    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.description == "256GB, Серый, 200MP"
    assert product.price == 180000.0
    assert product.quantity == 5

def test_category_creation():
    product1 = Product("S23 Ultra", "...", 180000.0, 5)
    product2 = Product("Iphone 15", "...", 210000.0, 8)
    category = Category("Смартфоны", "Описание категорий", [product1, product2])

    assert category.name == "Смартфоны"
    assert category.description == "Описание категорий"
    assert len(category.products) == 2
    assert category.product_count == 2


def test_empty_category():
    category = Category("Пустая", "Нет товаров", [])
    assert len(category.products) == 0
    assert category.product_count == 0
