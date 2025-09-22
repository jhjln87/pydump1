##def convertFtC(fahrenheit):
##    return (fahrenheit - 32) * 0.555555
def convertCtF(celsius):
    return (celsius)*1.8+32
whatTemp = float(input("What is the temperature?"))
fahOrCel = (input("Fahrenheit or celsius (F/C)?"))
if fahOrCel == "C":
    whatTemp = convertCtF(whatTemp)
recommendCoat = 0
for windSpeed in range(5, 61, 5):
    windChill = 35.74 + 0.6215*whatTemp - 35.75*windSpeed**0.16 + 0.4275*whatTemp*windSpeed**0.16
    windChill = windChill*100
    windChill = round(windChill)/100
    if windChill <= 40 and recommendCoat == 0:
        recommendCoat = 1
        print("~It's quite cold outside, I'd recommend a coat past this point")
    if windChill >= 100 and recommendCoat == 0:
        recommendCoat = 1
        print("~It's quite hot outside, I'd recommend staying indoors past this point")
    print(f"At temperature {whatTemp}, and wind speed {windSpeed}, the windchill is {windChill}F")