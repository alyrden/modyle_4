def test_function():
    def inner_function():
        x = "Я в области видимости функции test_function"
        print(x)

    inner_function()
# в области видемости
test_function()
# в закрытой области
inner_function()