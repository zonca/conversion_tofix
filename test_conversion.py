import conversion

assert conversion.dollars2cents(1) == 100
assert conversion.dollars2cents(.1) == 10
assert conversion.dollars2cents(0) == 0

assert conversion.gallons2liters(1) == 3.78541
assert conversion.gallons2liters(2) == 7.57082
assert conversion.gallons2liters(0) == 0

print("Testing completed")
