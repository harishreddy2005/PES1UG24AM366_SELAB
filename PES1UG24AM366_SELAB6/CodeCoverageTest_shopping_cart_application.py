"""Lab 6 line coverage tests: G Harish Reddy, PES1UG24AM366.

Run from Lab 6 with:
python -m coverage run --source=shopping_cart -m pytest CodeCoverageTest_shopping_cart_application.py
python -m coverage report -m
"""

import pytest

from shopping_cart import cart_discount, item_total, shipping_fee


@pytest.mark.parametrize(
    "category,price,qty,expected",
    [
        ("food", 100, 2, 210),
        ("electronics", 100, 1, 118),
        ("clothing", 100, 1, 112),
        ("food", 100, 10, 945),
        ("food", 0, 1, 0),
        ("clothing", 99, 11, 1098),
    ],
)
def test_item_totals(category, price, qty, expected):
    assert item_total(category, price, qty) == expected


@pytest.mark.parametrize(
    "category,price,qty,message",
    [
        ("books", 100, 1, "unknown category"),
        ("food", -1, 1, "invalid price or quantity"),
        ("food", 100, 0, "invalid price or quantity"),
        ("food", 100, -1, "invalid price or quantity"),
    ],
)
def test_invalid_items(category, price, qty, message):
    with pytest.raises(ValueError, match=f"^{message}$"):
        item_total(category, price, qty)


@pytest.mark.parametrize(
    "value,prime,coupon,expected",
    [
        (0, False, None, 0),
        (2000, False, None, 200),
        (5000, False, None, 500),
        (5000, True, "FLAT10", 1100),
        (1000, False, "FLAT10", 100),
    ],
)
def test_cart_discounts(value, prime, coupon, expected):
    assert cart_discount(value, prime, coupon) == expected


@pytest.mark.parametrize(
    "value,prime,express,expected",
    [
        (0, False, False, 40),
        (500, False, False, 0),
        (0, True, False, 0),
        (0, True, True, 50),
    ],
)
def test_shipping_fees(value, prime, express, expected):
    assert shipping_fee(value, prime, express) == expected
