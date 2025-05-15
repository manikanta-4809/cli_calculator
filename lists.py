def add(*nums): return sum(nums)
def sub(*nums): return nums[0] - sum(nums[1:]) if nums else 0
def mul(*nums):
    res = 1
    for n in nums: res *= n
    return res
def div(*nums):
    try:
        return nums[0] / nums[1] if len(nums) >= 2 else "Need at least 2 numbers"
    except ZeroDivisionError:
        return "Error: Division by zero"

ops = {'1': add, '2': sub, '3': mul, '4': div}

while True:
    try:
        n = int(input("How many numbers? "))
        if n < 1:
            print("Enter at least one number.")
            continue
        nums = [float(input(f"Enter number {i+1}: ")) for i in range(n)]

        print("\n1. Add  2. Sub  3. Mul  4. Div  5. Exit")
        choice = input("Choose operation (1-5): ")

        if choice == '5':
            print("Goodbye!")
            break
        elif choice in ops:
            result = ops[choice](*nums)
            print("Result:", result)
        else:
            print("Invalid operation.")
    except ValueError:
        print("Enter valid numeric values.")
