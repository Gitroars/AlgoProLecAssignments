def convertTemp():
  #User inputs fahrenheit
  fahrenheit =eval(input("Enter the temperature in Fahrenheit: "))
  def convertToCelsius(Fahrenheit):
    Celsius=(5/9)*(Fahrenheit-32)
    return Celsius
  def convertToKelvin(Celsius):
    Kelvin=Celsius+273.15
    return Kelvin
  #Calls the helper function with known temperature values
  celsius = convertToCelsius(fahrenheit)
  kelvin = convertToKelvin(celsius)
  #Prints out the temperatures
  print("The temperature in Fahrenheit is: ",fahrenheit)
  print("The temperature in Celsius is: ",celsius)
  print("The temperature in Kelvin is: ",kelvin)
#Calls the function
convertTemp()

