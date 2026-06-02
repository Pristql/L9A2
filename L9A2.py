units=int(input("Enter the ammount of units you consumed: "))
if(units < 50):
    ammount = units*2.60
    surcharge = 25
elif(units <= 100):
    ammount = 130+((units - 50)*3.25)
    surcharge = 35
elif(units <= 200):
    ammount = 130 + 162.50+((units - 100)*5.26)
    surcharge = 45
else:
    ammount=130+160.5+526+((units-200)*8.45)
total=ammount+surcharge
print("electricity bill=%.2f"   %total)