""" @Author: Deven Gupta
    @Date: 23-07-2024
    @Last Modified by: Deven Gupta
    @Last Modified time: 23-07-2024
    @Title : Python program to find largest number among 3 number
"""    


def largest(number1,number2,number3):
    """
        Description :
            This function is used find the largest number among 3 numbers
        Parameters :
            number1,number2,number3 : are the 3 integer value entered ny user
        return :
            string with largest value 
     """


    if number1 > number2 and number1 > number3:
        return f"The largest number is {number1}"
    
    elif number2 > number1 and number2 > number3:
        return f"The largest number is {number2}"
    
    else:
        return f"The largest number is {number3}"
    



def main():
    number1=int(input("Enter 1st number : "))
    number2=int(input("Enter 2nd number : "))
    number3=int(input("Enter 3rd number : "))

    print(largest(number1,number2,number3))

if __name__ == "__main__":
    main()