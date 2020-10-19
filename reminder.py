import datetime

now = datetime.dateime.now()

#datetime.datetime.now()
#<module>.<classs>.<classmethod>()

#print some ATTRIBUTES
print(now.year, now.month, now.hour, now.minute, now.second)

#now.hour = float(input("What hour is it? (0-23)"))
if now.hour <== 5:
    print("It's early you shopuld be sleeping!")
elif now.hour <== 7:
    print("Wake up, brew that coffee, get that mile run in, and get that breakfast…")
elif now.hour <== 9:
    print("Time to go to work.")
elif now.hour <== 12:
    print("You should be working!")
elif now.hour <== 13:
    print("Take your lunch break")
elif now.hour <== 17:
    print("Do you feel that afternoon lull?")
elif now.hour <== 19:
    print("Time to hit the gym")
elif now.hour <== 21:
    print("Gotta eat that dinner")
elif now.hour <== 23:
    print("Get that SLEEP and REPEAT!")
else:
    print("You didn't type an acceptable value!!! (0-23)")
