# 
# main.py
#
# Created by Persephone on 19.09.23 at 8.55
#

from mymath import add, subtract, multiply, divide, power, square

def main():
    while(True):
        print("Hello and welcome to pycalc!\nPlease choose from the list below what operation you'd like to do: \n")
        print("1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Power\n6.Square root\n7. Exit\n")
    

        match input():
            case "1":
                print(f"Type in the numbers you want to use:")
                z = add(int(input()),int(input()))
                print(f"Your result became {z}!\n")
            case "2":
                print(f"Type in the numbers you want to use:")
                z = subtract(int(input()),int(input()))
                print(f"Your result became {z}!\n")
            case "3":
                print(f"Type in the nymbers you want to use:")
                z = multiply(int(input()),int(input()))
                print(f"Your result became {z}!\n")
            case "4":
                print(f"Type in the numbers you want to use:")
                z = divide(int(input()),int(input()))
                print(f"Your result became {z}!\n")
            case "5":
                print(f"Type in the numbers you want to use:")
                z = power(int(input()),int(input()))
                print(f"Your result became {z}!\n")
            case "6":
                print(f"Type in the number(1) you want to use:")
                z = square(int(input()))
                print(f"Your result became {z}!\n")
            case "7":
                print(f"Thank you for using my calculator!")
                return 0
    
          
       






if __name__ == "__main__":
    main()

