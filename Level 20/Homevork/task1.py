num = input("Enter your number: ")

for i in num:
    print(i)
    
    
    
    
    num = int(input("Enter your number: "))

if num % 2 == 0:
    print("Even!")
else:
    print("Odd!")
    
    
    
    my_name = "vano"
user_name = input("Enter your name: ")

if my_name == user_name:
    print("Hello!")
else:
    print("Bye!")



score = int(input("Enter your number: "))

if score >= 90:
    print("A")
elif score < 90 and score > 70:
    print("B")
elif score < 70 and score > 50:
    print("C")
else:
    print("D")
    
    
    i = 1

while i <= 100:
    if i % 2 == 0:
        print(i, "is Even!")
    else:
        print(i, "is Odd!")
    i = i + 1