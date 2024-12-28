#string interpolation using format method.....
#method is nothing but a function.....


make='hero honda'
cost=99999.99999
gears=4
print("company name:{}\ncost of the vehicle:{}\nno of gears:{}".format(make,cost,gears))
print(25*"*")
print("company name:{}\ncost of the vehicle:{}\tno of gears:{}".format(make,cost,gears))
print(25*"*")


# % formatting method......


print("company name:%s\ncost of the vehicle:%f\nno of gears:%d"%(make,cost,gears))
print(25*"*")
print("company name:%s\ncost of the vehicle:%f\tno of gears:%d"%(make,cost,gears))
print(25*"*")
print("company name:",make,"cost of the vehicle:",cost,"no of gears:",gears)
print(25*"*")
print("company name:",make,"\n cost of the vehicle:",cost,"\n no of gears:",gears)
