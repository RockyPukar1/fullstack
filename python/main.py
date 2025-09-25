# Int -> pure number
# Float -> decimal points
# Boolean -> True False
# String -> ""
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

choice = input("Enter +, -, *, /: ")

if choice == "+":
  print(num1 + num2)
elif choice == "-":
  print(num1 - num2)
elif choice == "*":
  print(num1 * num2)
elif choice == "/":
  print(num1 / num2)
else:
  print("Invalid choice")