POUNDS_PER_TALENT = 20
LOTS_PER_POUND = 32
GRAMS_PER_LOT = 13.3
talents = int(input("Enter the number of talents: "))
pounds = int(input("Enter the number of pounds: "))
lots = int(input("Enter the number of lots: "))
total_grams = (talents * POUNDS_PER_TALENT * LOTS_PER_POUND * GRAMS_PER_LOT) + \
              (pounds * LOTS_PER_POUND * GRAMS_PER_LOT) + \
              (lots * GRAMS_PER_LOT)
kilograms = total_grams // 1000
grams = total_grams % 1000
print("The mass is equivalent to", kilograms, "kilograms and", grams, "grams.")
