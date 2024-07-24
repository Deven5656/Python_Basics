""" @Author: Deven Gupta
    @Date: 23-07-2024
    @Last Modified by: Deven Gupta
    @Last Modified time: 23-07-2024
    @Title : Python program to find the harmonic number
"""

def harmonic(number):
    
    """
        Description :
            This function is used to compute harmonic number (1/1 + 1/2 + 1/3 + ... + 1/N)
        Parameters :
            number : It is a input taken by user that describe upto which harmonic value is to be calculate
        return :
            None
    """
    
    total=0
    print(f"Harmonic number of {number} is")
    for i in range(1,number+1):
      total+=1/i

      #to print series only eg 1+1/2+1/3......+1/n
      print(f"1/{i} {"+" if i!=number else "=" }",end=" ")
    print(f"{total:.2f}")



def main():
    number= int(input("Enter a value greater than 0: "))
    if number > 0 :
        harmonic(number)
    else:
        print(f"Invalid input {number}. Please enter a value greater than 0")

if __name__ == "__main__":
    main()