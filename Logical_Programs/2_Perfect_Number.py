""" @Author: Deven Gupta
    @Date: 23-07-2024
    @Last Modified by: Deven Gupta
    @Last Modified time: 23-07-2024
    @Title : Python program to check whether a number is perfect number or not
"""

def perfect_number(number):

    """
        Description :
            This function is used to check whether a number is perfect number or not
        Parameters :
            number : number which has to be check
        return :
            none
            
    """
    divisor_sum = 0
    for i in range(1,number):
        if number % i ==0 :
            divisor_sum += i
    
    if number == divisor_sum:
        print("Entered number is perfect Number")
    else:
        print("Entered number is not perfect Number")
       

def main():
   number=int(input("Enter the number : "))
   perfect_number(number)

if __name__ == "__main__":
    main()