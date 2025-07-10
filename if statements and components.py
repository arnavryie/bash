def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1 
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3
    
    print(max_num(300, 40, 5))
# This function takes three numbers as input and returns the maximum of the three.
# It uses conditional statements to compare the numbers and determine which one is the largest.