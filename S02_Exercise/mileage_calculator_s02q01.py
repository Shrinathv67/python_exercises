#Script to calculate the mileage of the aar

start_mileage = int(input("Please enter the starting odometer mileage: "))
end_mileage = int(input("Please enter the ending odometer mileage: "))
distance_travelled = end_mileage - start_mileage
gas_used = int(input("Please enter the amount of fuel used: "))
mileage = distance_travelled/gas_used
print("Mileage of the car: ", mileage, "km/lts")

