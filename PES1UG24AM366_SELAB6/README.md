# L6_L7_23_shopping_cart — Shopping Cart

Lab 6: Code and Branch Coverage

## About

A small Python module that works out item totals with GST and bulk discounts, calculates cart discounts and works out shipping fees.

## Files

| File | Description |
|------|-------------|
| `shopping_cart.py` | The module under test |
| `test_shopping_cart.py` | Starter test file |

Refer to the lab handout for instructions.

## Lab 6 submission

G Harish Reddy — PES1UG24AM366

Run commands from **PES1UG24AM366_SELAB6** in this repository. The application is unchanged.
Use Python 3 with `python -m pip install pytest coverage`. In the prepared
workspace, activate the environment first using
`C:\se_lab\.venv\Scripts\Activate.ps1`.

### Code coverage

```powershell
python -m coverage run --source=shopping_cart -m pytest CodeCoverageTest_shopping_cart_application.py
python -m coverage report -m --fail-under=90
```

Result: **19 tests pass; 32/32 statements covered (100% line coverage)**.
The tests cover each GST category, zero price, integer rounding, bulk pricing,
invalid items, cart discount tiers, Prime benefits, coupons, and shipping.
`CodeCoverage_shopping_cart.png` captures the actual final terminal output.

### Branch coverage

```powershell
python -m coverage run --branch --source=shopping_cart -m pytest BranchCoverageTest_shopping_cart_application.py
python -m coverage report -m --fail-under=90
```

Result: **98 tests pass; 32/32 statements and 22/22 branches covered (100%)**.
The report shows `Miss = 0`, `Branch = 22`, and `BrPart = 0`.
Tests exercise both outcomes of every conditional, validation short circuits,
quantities 9/10/11, cart boundaries 999/1000/1001, 1999/2000/2001 and
4999/5000/5001, shipping boundaries 499/500/501, and every Prime/express
combination. Expected amounts account for the application's integer rounding.
There are no loops in this application.
`BranchCoverage_shopping_cart.png` captures the actual final terminal output.

### Run all Lab 6 tests

```powershell
python -m pytest
```

Expected: **119 tests pass**, including the two starter tests. `pytest.ini`
enables discovery of the handout's required filenames and disables optional
pytest caching to avoid Windows cache permission issues.

The screenshots already include the test command, passing test summary, report
command, and final application-only coverage table. If retaking them, capture
that same output after running each pair of commands above.
Do not submit `.coverage`, `__pycache__`, `.pytest_cache`, or the virtual environment.
