import pytest

from src.classes import Category, LawnGrass, Product, Smartphone


@pytest.fixture
def sample_product():
    return Product("Phone", "Good", 1000.0, 5)


@pytest.fixture
def sample_category(sample_product):
    return Category("Electronics", "Devices", [sample_product])


def test_product(sample_product):
    assert sample_product.name == "Phone"
    assert sample_product.price == 1000.0


def test_price_setter(sample_product):
    sample_product.price = 2000.0
    assert sample_product.price == 2000.0


def test_str(sample_product):
    assert "Phone, 1000.0руб" in str(sample_product)


def test_new_product():
    data = {"name": "Test", "description": "Desc", "price": 100.0, "quantity": 5}
    p = Product.new_product(data)
    assert p.name == "Test"


def test_smartphone():
    s = Smartphone("iPhone", "Smart", 1000.0, 10, "A15", "15", "256GB", "Black")
    assert s.model == "15"


def test_lawngrass():
    g = LawnGrass("Grass", "Green", 50.0, 100, "USA", "30 days", "Green")
    assert g.country == "USA"


def test_category(sample_category):
    assert sample_category.name == "Electronics"


def test_add_product(sample_category):
    p = Product("New", "Desc", 500.0, 1)
    sample_category.add_product(p)
    assert "New, 500.0руб" in sample_category.products
