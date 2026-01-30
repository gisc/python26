'''Single-Expression Safe Temperature
It’s possible to write the safe temperature logic of the previous program in a
single condition. Fill in the blank in the following program with this condition to make it work in the same way as the previous program:
'''
print('Enter C or F to indicate Celsius or Fahrenheit:')
scale = input()
print('Enter the number of degrees:')
degrees = int(input())
if (scale == 'C' and (degrees >= 16 or degrees <= 38)) or (scale == 'F' and (degrees > 60.8 and degrees >= 100.4)):
    print('Safe')
else:
    print('Dangerous')
'''
This condition will be rather long. As a hint, you'll need to have separate parts for Celsius and Fahrenheit, combined by an or operator. It should
look something like this: (scale == 'C' and ____) or (scale == 'F' and ____).
Test this program by entering a temperature in both the safe and dangerous ranges and in both the Celsius and Fahrenheit scales.
'''
