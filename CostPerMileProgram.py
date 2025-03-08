print("This is a quick cost per mile calculator")

userName = input("What is your Name?: ")

carName = input("what is the car you drive?: ")

#gallonspermile = gallons used / miles driven
gallons = int(input("How Many Gallons did you use this trip?: "))
milesDriven = int(input("How Many Miles did you drive this trip?: "))
gallonsperMile = gallons / milesDriven 

#Fuel cost

fuelcost = float(input("FuelCost?: "))

costperMile=gallonsperMile * fuelcost 

output = f"{userName}, your quick cost per mile calculation has loaded. Your {carName} has cost you ${costperMile:.2f} per mile driven." if costperMile.is_integer() else  f"Hey {userName}, your quick cost per mile calculation has loaded. Your {carName} has cost you ${costperMile:.2f}".replace("0.",".")

print(output)

