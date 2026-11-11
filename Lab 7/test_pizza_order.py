from hypothesis import given, strategies as st, assume
from pizza_order import toppings_price, pizza_inches, split_bill


@given(st.text())
def test_toppings_price_no_crash(s):
    """toppings_price should not crash for any text input."""
    try:
        result = toppings_price(s)
        assert isinstance(result, (int, float)), f"Expected numeric result, got {type(result)}"
    except Exception:
        # It's acceptable to raise an error for truly invalid input,
        # but the function should handle it gracefully
        raise


@given(st.text())
def test_pizza_inches_no_crash(s):
    """pizza_inches should not crash for any text input."""
    try:
        result = pizza_inches(s)
        assert result is None or isinstance(result, int), f"Expected int or None, got {type(result)}"
    except Exception:
        raise


@given(st.text())
def test_split_bill_no_crash(s):
    """split_bill should not crash for any text input."""
    try:
        result = split_bill(s)
        assert result is None or isinstance(result, float), f"Expected float or None, got {type(result)}"
    except Exception:
        raise