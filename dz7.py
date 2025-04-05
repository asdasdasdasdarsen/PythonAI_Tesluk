def calculate(expression):
    try:
        result = eval(expression)
        return result
    except Exception as e:
        return f"Неправильно: {e}"

    print("Напишіть свій математичний приклад який треба розв'язати")
    while True:
        expression = input("Введіть вираз: ")

        if expression.lower() == 'вихід':
            break
        result = calculate(expression)
        print(f": {result}")
calculate(expression)
