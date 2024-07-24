""" @Author: Deven Gupta
    @Date: 23-07-2024
    @Last Modified by: Deven Gupta
    @Last Modified time: 23-07-2024
    @Title : Python program to swap the numbers
"""


def swap(number1,number2):

    """
        Description :
            This function is used to swap the numbers using 3rd variable
        Parameters :
            number1,number2 : are the 2 integer value entered ny user
        return :
            tuple : number after swapping
     """
    temp=number1
    number1=number2
    number2=temp

    return number1,number2


def main():
 number1=int(input("Enter 1st number : "))
 number2=int(input("Enter 2nd number : "))

 print(f"Numbers before Swapping  are {number1} ,{number2}")

 first_number,second_number=swap(number1,number2)

 print(f"Numbers after Swapping  are {first_number} ,{second_number}")

if __name__ == "__main__":
    main()
