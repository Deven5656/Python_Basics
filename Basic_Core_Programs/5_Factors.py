""" @Author: Deven Gupta
    @Date: 23-07-2024
    @Last Modified by: Deven Gupta
    @Last Modified time: 23-07-2024
    @Title : Python program to find prime factors of number
"""


def get_prime_factors(number) :
  
  """
        Description :
            This function is used to find the prime factors of number
        Parameters :
            number : It is a input taken by user for which prime factors need to be find
        return :
            list : which contain prime factors of number
   """
  prime_factors=[]
  
  for i in range(2,int(number**0.5)+1):
   
    while number % i==0:
        prime_factors.append(i)
        number //= i

  if number>0:
    prime_factors.append(number)
       
  return prime_factors

def main():
 print(f"The Prime Factors are {get_prime_factors(int(input("Enter The number : ")))}")

if __name__ == "__main__":
    main()