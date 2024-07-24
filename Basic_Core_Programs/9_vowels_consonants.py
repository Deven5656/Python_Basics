""" @Author: Deven Gupta
    @Date: 23-07-2024
    @Last Modified by: Deven Gupta
    @Last Modified time: 23-07-2024
    @Title : Python program to check alphabet is vowel or consonant
"""


def vowels(letter):
    """
        Description :
            This function is used to check whether a alphabet is vowel or consonant
        Parameters :
            letter : alphabet entered by user 
        return :
            string : vowel or consonant
     """
    vowel =["A","E","I","O","U"]

    if letter.upper() in vowel:
         return f"Alphabet is Vowel"
    else:
        return f"Alphabet is Consonant"
    

def main():
 alphabet=input("Enter the alphabet : ")
 print(vowels(alphabet))

if __name__ == "__main__":
    main()