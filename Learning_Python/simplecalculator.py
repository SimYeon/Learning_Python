#a simple basic calculator using python
def add(a, b):
    answer = a + b
    print(f"{str(a)} + {str(b)} = {str(answer)}")

def sub(a, b):
    answer = a - b
    print(f"{str(a)} - {str(b)} = {str(answer)}")

def mul(a, b):
    answer = a*b
    print(f"{str(a)} * {str(b)} = {str(answer)}")

def div(a, b):
    answer = a/b
    print(f"{str(a)} / {str(b)} = {str(answer)}")

print("A. Addition")
print("B. Subtraction")
print("C. Multiplication")
print("D. Division")
print("E. Exit")

x = ""

while x != "e" or x != "E":
    choice = input("input your choice: ")
    
    if choice == "a" or choice == "A":
        print("Addition")
        a = int(input("input first number: "))
        b = int(input("input second number: "))
        add(a, b)
    
    elif choice == "b" or choice == "B":
        print("Subtraction")
        a = int(input("input first number: "))
        b = int(input("input second number: "))
        sub(a, b)
    
    elif choice == "c" or choice == "C":
        print("Multiplication")
        a = int(input("input first number: "))
        b = int(input("input second number: "))
        mul(a, b)
    
    elif choice == "d" or choice == "D":
        print("Division")
        a = int(input("input first number: "))
        b = int(input("input second number: "))
        div(a, b)
    
    else:
        x = "e"
        print("Program Ended")
        quit()
