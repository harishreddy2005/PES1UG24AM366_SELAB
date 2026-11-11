"""Lab 6 branch coverage tests: G Harish Reddy, PES1UG24AM366.

Run from Lab 6 with:
python -m coverage run --branch --source=shopping_cart -m pytest BranchCoverageTest_shopping_cart_application.py
python -m coverage report -m

The module has no loops. These tests exercise both outcomes of each decision,
including short-circuit validation, quantity and price boundaries, discount
tiers, coupon eligibility, and every Prime/express shipping combination.
"""

import pytest

from shopping_cart import cart_discount, item_total, shipping_fee


@pytest.mark.parametrize(
    "category,price,qty,expected",
    [
        ("food", 100, 9, 945),
        ("food", 100, 10, 945),
        ("food", 100, 11, 1039),
        ("electronics", 100, 9, 1062),
        ("electronics", 100, 10, 1062),
        ("electronics", 100, 11, 1168),
        ("clothing", 100, 9, 1008),
        ("clothing", 100, 10, 1008),
        ("clothing", 100, 11, 1108),
        ("food", 0, 1, 0),
        ("electronics", 0, 10, 0),
        ("clothing", 99, 11, 1098),
        ("food", 1, 1, 1),
        ("food", 1, 11, 10),
    ],
)
def test_gst_bulk_threshold_and_integer_rounding(category, price, qty, expected):
    assert item_total(category, price, qty) == expected


@pytest.mark.parametrize("category", ["books", "", "Food", None])
def test_unknown_category_raises_before_price_validation(category):
    with pytest.raises(ValueError, match="^unknown category$"):
        item_total(category, -1, 0)


@pytest.mark.parametrize("price,qty", [(-1, 1), (-1, 0), (0, 0), (100, -1)])
def test_either_invalid_price_or_invalid_quantity_raises(price, qty):
    with pytest.raises(ValueError, match="^invalid price or quantity$"):
        item_total("food", price, qty)


@pytest.mark.parametrize(
    "value,tier_discount,coupon_discount",
    [
        (0, 0, 0),
        (999, 0, 0),
        (1000, 0, 100),
        (1001, 0, 100),
        (1999, 0, 199),
        (2000, 200, 200),
        (2001, 200, 200),
        (4999, 200, 499),
        (5000, 500, 500),
        (5001, 500, 500),
    ],
)
@pytest.mark.parametrize("prime,prime_discount", [(False, 0), (True, 100)])
@pytest.mark.parametrize("coupon", [None, "INVALID", "FLAT10"])
def test_cart_thresholds_prime_and_coupon_paths(
    value, tier_discount, coupon_discount, prime, prime_discount, coupon
):
    # Expected tier and coupon amounts are explicit in the boundary table.
    expected = tier_discount + prime_discount
    if coupon == "FLAT10":
        expected += coupon_discount
    assert cart_discount(value, prime, coupon) == expected


@pytest.mark.parametrize(
    "value,standard_fee,express_fee",
    [(0, 40, 140), (499, 40, 140), (500, 0, 100), (501, 0, 100)],
)
@pytest.mark.parametrize("prime", [False, True])
@pytest.mark.parametrize("express", [False, True])
def test_shipping_threshold_and_all_prime_express_paths(
    value, standard_fee, express_fee, prime, express
):
    if prime:
        expected = 50 if express else 0
    else:
        expected = express_fee if express else standard_fee
    assert shipping_fee(value, prime, express) == expected
