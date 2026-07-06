#temperature converter
from unittest import result

Result = 0      #set result variable ,that is used to store result of conversion, to zero
print("Welcome sir")
print("I can help you convert temperature units")
print("But first tell me which unit,are you currently in ?")
coice = int(input("--1. celsius --2.Fahrenheit  --3. Kelvin...choose 1 2 or 3"))
value = int(input("enter value in whole number::"))
convert = int(input("which unit you want to convert to;--1. celsius --2.Fahrenheit  --3. Kelvin...choose 1 2 or 3"))
if coice == 1 and convert == 2:     #responding based on input.
    Result = value * 9/5 +32
    print("The",value,"Celsius in Fahrenheit is-->",Result)
elif coice == 2 and convert == 1:
    Result = (value - 32) * 5/9
    print("The", value, "Fahrenheit in celsius is-->", Result)
elif coice == 1 and convert == 3:
    Result = value + 273.15
    print("The", value, "celsius in kelvin is-->", Result)
elif coice == 3 and convert == 2:
    Result = (value - 273.15) * 9 / 5 + 32
    print("The", value, "K in Fahrenheit is-->", Result)
elif coice == 2 and conver == 3:
    Result = (value - 273.15) * 9/5 + 32
elif coice == 3 and convert == 1:
    Result = value - 273.15
    print("This value in celsius is:",Result)
if convert == 3 and Result == 0:
    print("This temperature is known as absolute zero or near to it the point where no more energy can be taken out of matter and this is lowest point of the universe")






