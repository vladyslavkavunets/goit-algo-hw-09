def find_coins_greedy(amount):
    coins = [50, 25, 10, 5, 2, 1]
    result = {}
    
    for coin in coins:
        if amount >= coin:
            count = amount // coin
            if count > 0:
                result[coin] = count
                amount = amount % coin
    
    return result


def find_min_coins(amount):
    coins = [1, 2, 5, 10, 25, 50]
    
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    
    coin_used = [0] * (amount + 1)
    
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                coin_used[i] = coin
    
    result = {}
    current_amount = amount
    
    while current_amount > 0:
        coin = coin_used[current_amount]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        current_amount -= coin
    
    return result


def compare_algorithms(test_amounts):
    import time
    
    print("Порівняння алгоритмів видачі решти\n")
    print("=" * 60)
    
    for amount in test_amounts:
        print(f"\nСума решти: {amount} грн")
        print("-" * 40)
        
        start_time = time.perf_counter()
        greedy_result = find_coins_greedy(amount)
        greedy_time = time.perf_counter() - start_time
        greedy_coins = sum(greedy_result.values())
        
        print(f"Жадібний алгоритм:")
        print(f"  Результат: {greedy_result}")
        print(f"  Кількість монет: {greedy_coins}")
        print(f"  Час виконання: {greedy_time:.6f} сек")
        
        start_time = time.perf_counter()
        dp_result = find_min_coins(amount)
        dp_time = time.perf_counter() - start_time
        dp_coins = sum(dp_result.values())
        
        print(f"\nДинамічне програмування:")
        print(f"  Результат: {dp_result}")
        print(f"  Кількість монет: {dp_coins}")
        print(f"  Час виконання: {dp_time:.6f} сек")
        
        if greedy_coins == dp_coins:
            print(f"\n Обидва алгоритми дають однаковий результат")
        else:
            print(f"\n Жадібний алгоритм не оптимальний!")
            print(f"  Різниця: {greedy_coins - dp_coins} монет(и)")
        
        if greedy_time < dp_time:
            print(f"  Жадібний алгоритм швидший в {dp_time/greedy_time:.2f} разів")
        else:
            print(f"  DP швидший в {greedy_time/dp_time:.2f} разів")


if __name__ == "__main__":
    print("Приклад видачі решти 113 грн:")
    print("\nЖадібний алгоритм:")
    greedy_113 = find_coins_greedy(113)
    print(f"find_coins_greedy(113) = {greedy_113}")
    
    print("\nДинамічне програмування:")
    dp_113 = find_min_coins(113)
    print(f"find_min_coins(113) = {dp_113}")
    
    print("\n" + "=" * 60)
    test_amounts = [113, 999, 1000, 5000, 10000]
    compare_algorithms(test_amounts)