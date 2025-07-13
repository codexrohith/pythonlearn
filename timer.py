import time
import winsound
tim=int(input("enter no of seconds : "))
s=tim+1
for i in reversed(range(1,s)):
    sec=i%60
    min=int(i/60)%60
    hour=int(i/3600)%24
    print(f"{hour:02}:{min:02}:{sec:02}")
    time.sleep(1)
winsound.Beep(1000, 5000)
