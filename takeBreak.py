"""Mini prject to remind you to take a break and play your best song """


import time 
import webbrowser

total_breaks = 3  
break_count = 0

print("This program started on "+time.ctime())  # started on computer time
while(break_count < total_breaks):
    time.sleep(2*60*60)             # wite two hour befor openning the URL
    webbrowser.open("https://www.youtube.com/watch?v=GYhf-bWS2KM")  # open the URL
    break_count += 1