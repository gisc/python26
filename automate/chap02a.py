'''
Fixing the Safe Temperature Program
The following program reports whether a given temperature is safe. It asks
the user to enter a temperature in two parts. First, they should enter C or F
to indicate the Celsius or Fahrenheit scale; second, they should enter the
number of degrees. If the temperature is between 16 and 38 degrees Celsius
(inclusive of 16 and 38) or between 60.8 and 100.4 degrees Fahrenheit (inclusive of 60.8 and 100.4), the program prints Safe. Outside of these temperature ranges, the program prints Dangerous.
This program has bugs, however. Rewrite the code to fix the errors. You
may assume the user always enters valid inputs and not, say, X for the scale
or hello for the number of degrees.
'''
print('Enter C or F to indicate Celsius or Fahrenheit:')
scale = input()
print('Enter the number of degrees:')
degrees = int(input())
if scale == 'C':
    if degrees >= 16 or degrees <= 38:
        print('Dangerous')
    else:
        print('Dangerous')
elif scale == 'F':
    if degrees > 60.8 and degrees >= 100.4:
        print('Safe')
    else:
        print('Dangerous')
'''
Test this program by entering a temperature in both the safe and dangerous ranges and in both the Celsius and Fahrenheit scales.
'''