print("Hello World!")

str = "abc"

print(str[::-1])

arr = ['a','b','c','d'];
print(arr[::-1])

userName = input("Enter the Username")
password = input("Enter the Password");

hiddenPassword = '*' * len(password);
print(f"hi, {userName}, Your password {hiddenPassword} is {len(password)}")