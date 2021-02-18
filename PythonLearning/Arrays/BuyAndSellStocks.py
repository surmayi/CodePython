def buy_and_sell_stock_once(prices,method):
    if method==1:
        maxProfit =0
        for i in range(len(prices)-1):
            for j in range(i+1,len(prices)):
                if prices[i]<prices[j]:
                    maxProfit=max(maxProfit,prices[j]-prices[i])
    else:
        maxProfit,minV = 0,float('inf')
        for val in prices:
            minV= min(minV,val)
            diff = val - minV
            maxProfit = max(maxProfit,diff)
    return maxProfit

print(buy_and_sell_stock_once([310,315,275,295,260,270,290,300],1))
print(buy_and_sell_stock_once([310,315,275,295,260,270,290,300],2))