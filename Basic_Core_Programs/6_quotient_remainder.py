""" @Author: Deven Gupta
    @Date: 23-07-2024
    @Last Modified by: Deven Gupta
    @Last Modified time: 23-07-2024
    @Title : Python program to find quotient and remainder
"""

def quotient_remainder(dividend,divisor):

    """
        Description :
            This function is used to find the quotient and remainder
        Parameters :
            dividend :number which has to be divided
            divisor : number which divide other number
        return :
            tuple : quotient and remainder
     """
    quotient=dividend // divisor
    remainder=dividend % divisor
    return quotient,remainder


def main():
 dividend=int(input("Enter Dividend : "))
 divisor=int(input("Enter Divisor : "))
 quotient,remainder=quotient_remainder(dividend,divisor)
 print(f"Quotient = {quotient} and Remainder = {remainder}")

if __name__ == "__main__":
    main()