prices = [7,1,5,3,6,4]

## Buy at low
## Sell at high

def share_trade_simulator(prices:list):
    low = 0
    profit = 0
    
    for i in prices:
        if prices.index(i) == 0:
            low = i
        else:
            low = min(low,i)
        
        profit = max(profit, i-low)
    return profit

print(share_trade_simulator(prices))