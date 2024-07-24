""" @Author: Deven Gupta
    @Date: 23-07-2024
    @Last Modified by: Deven Gupta
    @Last Modified time: 23-07-2024
    @Title : Python program to reverse a number
"""

def reverse_number(number):

    """
        Description :
            This function is used to reverse a number
        Parameters :
            number : number which has to be reverse
        return :
            int : reversed number
            
    """
    reverse_num = 0
    while number > 0:
        digit = number % 10
        reverse_num = reverse_num*10 + digit
        number//=10
    return reverse_num

       

def main():
   number=int(input("Enter the number: "))
   print(f"Number Entered is {number} and reverse of number is {reverse_number(number)}")

if __name__ == "__main__":
    main()