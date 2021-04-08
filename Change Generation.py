"""
Change Generation for a Particular Currency

Author: Electra Bree
Username: rbre269
User ID: 574069100
"""

currency_value = int(input("Value: ")) #Enter currency_value here
lots_of_equals = "=" * 19
number_of_hundreds = currency_value // 100
number_of_fifties = (currency_value - 100 * number_of_hundreds) // 50
number_of_quarters = (currency_value -(100 * number_of_hundreds + 50
                                       * number_of_fifties)) // 25 
number_of_tens = (currency_value - (100 * number_of_hundreds + 50
                                    * number_of_fifties + 25
                                    * number_of_quarters)) // 10  
number_of_fives = (currency_value - (100 * number_of_hundreds + 50
                                     * number_of_fifties + 25
                                     * number_of_quarters + 10
                                     * number_of_tens)) // 5 
number_of_ones = (currency_value - (100 * number_of_hundreds + 50
                                    * number_of_fifties + 25
                                    * number_of_quarters + 10
                                    * number_of_tens + 5
                                    * number_of_fives)) // 1

print()
print("You will need:")
print(lots_of_equals)
print("  100s: ", number_of_hundreds)
print("  50s: ", number_of_fifties)
print("  25s: ", number_of_quarters)
print("  10s: ", number_of_tens)
print("  5s: ", number_of_fives)
print("  1s: ", number_of_ones)
print(lots_of_equals)


