#use to prevent errors when input from use is invalid

try:
    answer = 10/0
    #value = 10 / 0 will cause error
    number = int(input("Enter a number: ")) #use enters a number and convert into an integer
    print(number)

except ZeroDivisionError as err: #specify error
    print("err")

except ValueError:
    print("Invalid Input.")
