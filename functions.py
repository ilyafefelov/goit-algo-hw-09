import time


def find_coins_greedy(amount):
    coins = [50, 25, 10, 5, 2, 1]
    result = {}

    for coin in coins:
        count = amount // coin
        if count > 0:
            result[coin] = count
            amount -= coin * count

    return result

# Приклад використання:
print(find_coins_greedy(113))  # Вихід: {50: 2, 10: 1, 2: 1, 1: 1}



def find_min_coins(amount):
    coins = [50, 25, 10, 5, 2, 1]
    # Створимо масив для зберігання мінімальної кількості монет для кожної суми до 'amount'
    min_coins = [float('inf')] * (amount + 1)
    min_coins[0] = 0

    # Створимо масив для відстеження номіналів монет, що використовуються
    coin_used = [0] * (amount + 1)

    for coin in coins:
        for higher_amount in range(coin, amount + 1):
            if min_coins[higher_amount - coin] + 1 < min_coins[higher_amount]:
                min_coins[higher_amount] = min_coins[higher_amount - coin] + 1
                coin_used[higher_amount] = coin

    # Побудуємо словник із номіналами монет та їх кількістю
    result = {}
    while amount > 0:
        coin = coin_used[amount]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        amount -= coin

    return result

# Приклад використання:
print(find_min_coins(113))  # Вихід: {50: 2, 10: 1, 2: 1, 1: 1}


def compare_algorithms(amount):
    # Час виконання жадібного алгоритму
    start_time = time.time()
    greedy_result = find_coins_greedy(amount)
    greedy_time = time.time() - start_time

    # Час виконання алгоритму динамічного програмування
    start_time = time.time()
    dp_result = find_min_coins(amount)
    dp_time = time.time() - start_time

    return {
        "amount": amount,
        "greedy_result": greedy_result,
        "greedy_time": greedy_time,
        "dp_result": dp_result,
        "dp_time": dp_time
    }

# Приклад використання:
comparison = compare_algorithms(113)
print(f"Greedy Algorithm: {comparison['greedy_result']} (Time: {comparison['greedy_time']:.15f} seconds)")
print(f"DP Algorithm: {comparison['dp_result']} (Time: {comparison['dp_time']:.15f} seconds)")

# Тестування на великих сумах
large_comparison = compare_algorithms(112134423)
print(f"Greedy Algorithm (Large Sum): {large_comparison['greedy_result']} (Time: {large_comparison['greedy_time']:.15f} seconds)")
print(f"DP Algorithm (Large Sum): {large_comparison['dp_result']} (Time: {large_comparison['dp_time']:.15f} seconds)")
