""" @Author: Deven Gupta
    @Date: 23-07-2024
    @Last Modified by: Deven Gupta
    @Last Modified time: 23-07-2024
    @Title : Python program to Calculate the percentage of heads and tails
"""

import random

def flip_coin(num):

    """
        Description :
            This function is used to find the number of time head come 
        Parameters :
            num : It is a input taken by user that many time coin with flip 
        return :
            float:percentage of head ((number of time head/total number)*100 )
            
    """
    head_count=0
    for i in range(num):
        flip=random.random()
        if flip < 0.5:
            head_count+=1
        
    return (head_count/num)*100

def main():
    num=int(input("Enter the number of times to Flip Coin : "))
    if num>0:
        head_perc=flip_coin(num)
        print(f"The Percentage of Head is {head_perc}%")
        print(f"The Percentage of tail is {100 - head_perc}%")
    else:
        print(f"Invalid input {num},Enter positive integer only")
    

if __name__ == "__main__":
    main()