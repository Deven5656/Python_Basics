""" @Author: Deven Gupta
    @Date: 23-07-2024
    @Last Modified by: Deven Gupta
    @Last Modified time: 23-07-2024
    @Title : Python program to check whether a number is even or odd
"""

def even_odd(number):

    """
        Description :
            This function is used check whether a number is even or odd
        Parameters :
            number : input by user which has to be checked
        return :
            string: even or odd
     """
    if number % 2 == 0:
        return f"Number is Even"
    else:
        return f"Number is Odd"



def main():
 number = int(input("Enter the Number : "))
 print(even_odd(number))


if __name__ == "__main__":
    main()