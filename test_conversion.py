import conversion

assert conversion.dollars2cents(1) == 100
assert conversion.dollars2cents(.1) == 10
assert conversion.dollars2cents(0) == 0
