""" @Author: Deven Gupta
    @Date: 23-07-2024
    @Last Modified by: Deven Gupta
    @Last Modified time: 23-07-2024
    @Title : Python program to simulate lottery coupon
"""


import random

def generate_distinct_coupons(number):

    """
        Description :
            This function is used to convert seconds into hours/minutes
        Parameters :
            number : its specfied number of coupons to be generated
        return :
            list: contains all unique generated numbers 
            
    """
    generated_coupon=[]
    while len(generated_coupon)!=number:
        random_coupon_no = random.randint(1000,9999)
        if random_coupon_no not in generated_coupon:
            generated_coupon.append(random_coupon_no)
    return generated_coupon



def main():
    number = int(input("Enter the number of coupons required :"))
    user_coupon = int(input("Enter your coupon number : "))

    coupon_list = generate_distinct_coupons(number)

    print("\nLucky coupons who won are : ")
    for i in coupon_list:
        print(i,end=" ")

    if user_coupon not in coupon_list:
        print("\n\nSorry you lose, Better Luck next time!")
    else:
        print("\n\nCongratulation, you are the lucky winners")


if __name__ == "__main__":
    main()