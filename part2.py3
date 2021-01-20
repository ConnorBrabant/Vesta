'''
The United States Federal Reserve has collapsed. Anarchy has ensued. As numerous military dictatorships take over
control of our country, each installs their own currency system. Alter your above algorithm to produce the same output but
for an arbitrary set of currency names and denominations and for an arbitrary total sum. Your solution should take a
command line parameter in the following format:

"Quarter, 4, Dime, 10, Nickel, 20, Penny, 100"
The argument is a comma delimited list which specifies the name of each denomination along with the number required of
that denomination to reach our target sum. The above example arguments should mimic the output you produced in
Question 1.

Examples:
    Quarter,4,Dime,10,Nickel,20,Penny,100
    Coin,1.5,Arrowhead,3,Button,150
'''
from prettytable import PrettyTable
import math 
from decimal import * 

def change_combos():
    def coin_change(curr, coins, amount, curr_combo):
        if int(round(amount)) == 0:
            coin_combos.append(curr_combo)
            return 
        elif curr >= len(coins):
            return 
        max_coin = math.ceil(amount / coins[curr])
        for x in range(0, max_coin+1):
            if amount >= x * coins[curr] or amount >= int(round(x * coins[curr])):
                res = coin_change(curr+1, coins, amount - (x * coins[curr]), curr_combo + [x])

    def convert_coins(coins, amount):
        conversion = []
        for coin in coins:
            conversion.append(amount/Decimal(str(coin)))
        return conversion 

    user_input = input("Please enter your currency: ").split(",")
    coin_names = []
    coin_values = []
    amount = 100
    
    for i, val in enumerate(user_input):
        if i == len(user_input) - 1 and len(user_input) % 2 == 1:
            amount = int(val)
        elif i % 2 == 0:
            coin_names.append(val)
        else:
            coin_values.append(float(val))


    coin_combos = []
    converted_coins = convert_coins(coin_values, amount)
    coin_change(0, converted_coins, amount, [])

    for index in range(len(coin_combos)):
        if len(coin_combos[index]) < len(coin_values):
            not_used_coins = [0] * (len(coin_values) - len(coin_combos[index]))
            coin_combos[index] = coin_combos[index] + not_used_coins
    
    table = PrettyTable()
    table.field_names = coin_names
    table.add_rows(coin_combos)
    print(table)
    print('Count: %i' % (len(coin_combos)))
        
change_combos()

