""" @Author: Deven Gupta
    @Date: 23-07-2024
    @Last Modified by: Deven Gupta
    @Last Modified time: 23-07-2024
    @Title : Python program to find the fibonacci series 
"""

def fibonacci(number):

    """
        Description :
            This function is used to find the fibonacci series 
        Parameters :
            number : number of element present in list
        return :
            list: containing fibonacci series 
            
    """
    fibo_seq= [0,1]

    for i in range(2,number):
        fibo_seq.append(fibo_seq[-1]+fibo_seq[-2])
    return fibo_seq

def main():
   number=int(input("Enter the number of elements : "))
   print(fibonacci(number))

if __name__ == "__main__":
    main()