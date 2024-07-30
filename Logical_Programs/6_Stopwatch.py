""" @Author: Deven Gupta
    @Date: 23-07-2024
    @Last Modified by: Deven Gupta
    @Last Modified time: 23-07-2024
    @Title : Python program to simulate stopwatch
"""

import time
def time_convert(seconds):

    """
        Description :
            This function is used to convert seconds into hours/minutes
        Parameters :
            seconds : Time_lapsed (start time and end time)
        return :
            tuple : contain hours,minutes and seconds
            
    """
    mins = seconds // 60
    seconds = seconds % 60
    hours = mins // 60
    mins = mins % 60
    return hours,mins,seconds



def main():
    input("Press Enter to start")
    start_time = time.time()
    input("Press Enter to stop")
    end_time = time.time()
    time_lapsed = end_time - start_time
    hours,mins,sec=time_convert(time_lapsed)

    print(f"Time Lapsed = {int(hours)}:{int(mins)}:{int(sec)}")


if __name__ == "__main__":
    main()