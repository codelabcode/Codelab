import os 
import time as t
os.system("clear")
os.system("figlet CodeLab")
print("PLEASE SUBSCRIBE TO OUR YOUTUBE CHANNEL CodeLab\n")
t.sleep(2)
os.system("termux-open-url https://youtube.com/channel/UCZBxbVR5DD17PHme3Ggb7IA")
x=0
while x<=1:
    num=str(input("enter the mobile number [press e to exit] \n")) 
    if num=="e":
        break
    ti=int(input("enter the time in seconds\n"))
    print("call will sent automatically to", num,"after", ti, "seconds")
    t.sleep(ti)
    try:
        os.system("termux-telephony-call "+num)
        t.sleep(1)
        print("call sent successfully \n")
    except Exception as inputerror:
        raise inputerror
    