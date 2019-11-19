def weather_condi(temperature):
    if temperature > 10:
        return "warm"
    else:
        return "cold" 


user_input = float(input("enter the temp:"))
print(weather_condi(user_input))