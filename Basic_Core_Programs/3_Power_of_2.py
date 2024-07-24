""" @Author: Deven Gupta
    @Date: 23-07-2024
    @Last Modified by: Deven Gupta
    @Last Modified time: 23-07-2024
    @Title : Python program to find the power of 2 values
"""

def power_of_2(number):

    """
        Description :
            This function is used to find the power of 2 (2^n)
        Parameters :
            number : It is a input taken by user that describe upto which power value to be calculated
        return :
            None
   """

    for number in range(number+1):
        print(f"2^{number} = {2**number}")


def main():
    number= int(input("Enter a value between 0 to 32: "))
    if 0 <= number <= 31 :
        power_of_2(number)
    else:
        print(f"Invalid input {number}. Please enter a value between 0 to 32")

if __name__ == "__main__":
    main()