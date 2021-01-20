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

    # function finds all possible combinations of currency given an amount
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

    # function converts the coins into how much they are individually worth according to amount
    # for example, when given Penny,100 for an amount 100 it outputs pennies as 1 
    def convert_coins(coins, amount):
        conversion = []
        for coin in coins:
            conversion.append(amount/Decimal(str(coin)))
        return conversion 

    coin_names = []
    coin_values = []
    amount = 100
    
    #parses user input to break up the currency into its names, values, and amount
    #if invalid input, will prompt user to re enter or exit 
    while True:
        try:
            user_input = input("Please enter your currency or type exit to quit: ")
            if user_input == 'exit':
                return 
            else:
                user_input = user_input.split(",")
            for i, val in enumerate(user_input):
                if i == len(user_input) - 1 and len(user_input) % 2 == 1:
                    amount = int(val)
                elif i % 2 == 0:
                    coin_names.append(val)
                else:
                    coin_values.append(float(val))
            break
        except:
            print('Invalid input. Please format it like so:\nCoin,1.5,Arrowhead,3,Button,150,300')
            continue


    coin_combos = []
    converted_coins = convert_coins(coin_values, amount)
    coin_change(0, converted_coins, amount, [])

    #if any combo doesn't use a coin, it fills in a zero for that coin
    for index in range(len(coin_combos)):
        if len(coin_combos[index]) < len(coin_values):
            not_used_coins = [0] * (len(coin_values) - len(coin_combos[index]))
            coin_combos[index] = coin_combos[index] + not_used_coins
    
    #populate table
    table = PrettyTable()
    table.field_names = coin_names
    table.add_rows(coin_combos)
    print(table)
    print('Count: %i' % (len(coin_combos)))
        
change_combos()

