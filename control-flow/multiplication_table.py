number = int(input("Enter a number to see its multiplication table: "))

for factor in range(1, 11):
    product = number * factor
    print(f"{number} * {factor} = {product}")
