num = int(input("Enter a number to see its multiplication table: "))

for factor in range(1, 11):
    product = num * factor
    print(f"{num} * {factor} = {product}")
