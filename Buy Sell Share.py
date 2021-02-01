prices = [7,1,5,3,6,4]

def maximizeProfit(prices:list):
    low = prices[0]
    profit = 0
    for price in prices:
        low = min(price,low)
        profit = max(profit,price-low)
    return profit
    
print(maximizeProfit(prices))