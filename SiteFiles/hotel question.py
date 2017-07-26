def nights(sleep) :
    return (nights *150)   
nights = input("Input amount of nights")




chicago = 183
london = 222
toronto = 220
tokyo = 475

def vacation(city) :
    if city == "chicago":
        return (183)
    elif city == "london":
        return (222)
    elif city == "toronto":
        return (220)
    elif city == "tokyo":
        return (475)

    else:
        print("city not valid")

city = input("input city")



def car(x) :
    cost = (x *150)   

    if x >= 7:
        return car - 50
    elif x >= 3:
        return car - 20
    return cost 
    
car = input("Input amount of days")

def total_cost(city, x):
    total = nights(x) + vacation(city) + car(x)
    print (total)



def total_cost():

    days = int(input("how many days?"))
    if city == "toronto" or city = "tokyo":
    city = input("which city are goin to?")
    total = nights(sleep) + vacation(city) + car(x)
    print (total)
    else: 
    print ("enter a valid city")

    
