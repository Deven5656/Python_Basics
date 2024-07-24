""" @Author: Deven Gupta
    @Date: 23-07-2024
    @Last Modified by: Deven Gupta
    @Last Modified time: 23-07-2024
    @Title : Python program to check whether a number is prime number or not
"""

def prime_number(number):

    """
        Description :
            This function is used to check whether a number is prime number or not
        Parameters :
            number : number which has to be check
        return :
            boolean : true or false
            
    """
    
    if (number <= 1):
        return False

    # Check from 2 to sqrt(number)
    for i in range(2, int(number**0.5)+1):
        if (number % i == 0):
            return False

    return True

def main():
    number=int(input("Enter the number: "))
    if prime_number(number):
        print("Its is a prime number")
    else:
        print("Its is not a prime number")

if __name__ == "__main__":
    main()