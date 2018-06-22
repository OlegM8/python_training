from model.calculator import Calculator


def test_addition(app):
    first = 4
    second = 5
    app.calculator.open_calculator()
    app.calculator.fill(first, second)
    app.calculator.select_operator(4)
    app.calculator.click_button()
    assert first + second == int(app.calculator.text_result())


def test_addition_float(app):
    first = 4.5
    second = 5.5
    app.calculator.open_calculator()
    app.calculator.fill(str(first), str(second))
    app.calculator.select_operator(4)
    app.calculator.click_button()
    assert first + second == float(app.calculator.text_result())


def test_addition_minus(app):
    first = -4
    second = 5
    app.calculator.open_calculator()
    app.calculator.fill(first, second)
    app.calculator.select_operator(4)
    app.calculator.click_button()
    assert first + second == int(app.calculator.text_result())


def test_subtraction(app):
    first = 44
    second = 55
    app.calculator.open_calculator()
    app.calculator.fill(first, second)
    app.calculator.select_operator(3)
    app.calculator.click_button()
    assert first - second == int(app.calculator.text_result())


def test_division(app):
    first = 55
    second = 3
    app.calculator.open_calculator()
    app.calculator.fill(first, second)
    app.calculator.select_operator(1)
    app.calculator.click_button()
    assert first / second == float(app.calculator.text_result())


def test_multiplication_float(app):
    first = 55
    second = 3.4
    app.calculator.open_calculator()
    app.calculator.fill(str(first), str(second))
    app.calculator.select_operator(2)
    app.calculator.click_button()
    assert first * second == float(app.calculator.text_result())


def test_multiplication(app):
    first = 55
    second = 333
    app.calculator.open_calculator()
    app.calculator.fill(first, second)
    app.calculator.select_operator(2)
    app.calculator.click_button()
    assert first * second == float(app.calculator.text_result())


def test_modulo(app):
    first = 55
    second = 4
    app.calculator.open_calculator()
    app.calculator.fill(first, second)
    app.calculator.select_operator(5)
    app.calculator.click_button()
    assert first % second == float(app.calculator.text_result())