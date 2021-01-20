'''
1. Write an algorithm that outputs the number of ways pennies, nickels, dimes, and quarters can be combined to sum
exactly $1. For instance, 4 quarters, 0 dimes, 0 nickels, and 0 pennies is one combination, 0 quarters, 0 dimes, 1 nickel,
and 95 pennies is another. Your algorithm should output all the valid combinations as well as a total count of the
combinations. Please have your solution output in the following format (the order of the combinations is not important):
'''
from prettytable import PrettyTable

def change_combos(amount, coins):

    # function finds all possible combinations of currency given an amount
    def coin_change(curr, coins, amount, curr_combo):
        if amount == 0.0:
            coin_combos.append(curr_combo)
            return
        elif curr >= len(coins):
            return
        max_coin = amount // coins[curr]
        for x in range(0, max_coin+1):
            if amount >= (x * coins[curr]):
                res = coin_change(curr+1, coins, amount -
                                  (x * coins[curr]), curr_combo + [x])
                                  
    coin_names = ['Quarter', 'Dime', 'Nickel', 'Penny']

    coin_combos = []
    coin_change(0, [25,10,5,1], 100, [])

    #for any combo that does not require all coins, fills in not used coins with a zero value
    for index in range(len(coin_combos)):
        if len(coin_combos[index]) < len(coins):
            not_used_coins = [0] * (len(coins) - len(coin_combos[index]))
            coin_combos[index] = coin_combos[index] + not_used_coins

    #populates table 
    table = PrettyTable()
    table.field_names = coin_names
    table.add_rows(coin_combos)
    print(table)
    print('Count: %i'%(len(coin_combos)))

change_combos(100, [25,10,5,1])
