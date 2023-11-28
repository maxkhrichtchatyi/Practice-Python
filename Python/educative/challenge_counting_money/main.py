def find_min_coins(v, coins_available):
    """
    This function finds the minimum number of coins
    :param v: Total amount
    :param coins_available: Coins available in the machine
    :return: A list of total coins
    """

    result = []

    for coin in reversed(coins_available):
        mod_remainder = v // coin
        if mod_remainder:
            list_of_coins = [coin] * mod_remainder
            result.extend(list_of_coins)
            v -= sum(list_of_coins)

    return result


# Main program to test the above code
if __name__ == "__main__":

    coins_available = [1, 5, 10, 25]  # The available coins are in increasing order
    print(find_min_coins(19, coins_available))
