""" @Author: Deven Gupta
    @Date: 23-07-2024
    @Last Modified by: Deven Gupta
    @Last Modified time: 23-07-2024
    @Title : Python program to check year is leap year or not
"""


def check_leap_year(year_input):
  
  """
        Description :
            This function is used to valid the enter value is digit and if it is digit check leap year
        Parameters :
            year_input : It is a input taken by user (e.g 2004)
        return :
            string:entered year is Leap year or not
   """
  if year_input.isdigit()==False:
    return f"Invalid year {year_input} entered, Please enter an valid year"

  year =int(year_input)

  if year < 1582:
    return f"The entered {year} must be 1528 or later"

  if(year % 100 == 0)and(year % 400 == 0):
    return f"The year {year} is Leap year"

  if(year % 4 == 0)and(year % 100 != 0):
    return f"The year {year} is Leap year"

  return f"The year {year} is not Leap year"

def main():
  print(check_leap_year(input("Enter a year: ")))

if __name__ == "__main__":
    main()