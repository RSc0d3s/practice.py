# comparison operators, see bat and ball for application
# == is equal to
# >= greater or equal to
# <= less than or equal to
# != not equal to
def max_num (num1, num2, num3):
    if num1 >= num2 and num1 >= num3: #true or false value using comparison
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(max_num(3,4,5))
