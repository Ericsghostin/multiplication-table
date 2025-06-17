n = int(input("Enter a number to generate multiplication table: "))

print("\nMultiplication Table")
print("     ", end="")
for i in range(1, n + 1):
    print(f"{i:4}", end="")
print()

print("    +" + "----" * n)

for i in range(1, n + 1):
    print(f"{i:3} |", end="")
    for j in range(1, n + 1):
        print(f"{i * j:4}", end="")
    print()
