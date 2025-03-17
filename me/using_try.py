# Using Try / Except Blocks for Rebuts Error Handling


try:
    num = int(input("Enter a Number:"))
    print(f"You Entered{num}")
except ValueError:
    print("that is a not valid number!")

    