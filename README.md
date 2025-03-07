# Onymos Coding challenge

## TODO: Add intro

## addOrder explanation

## matchOrder explanation

The matchOrder function checks the highest buy price and the lowest sell price in the order book and executes the trade if the buy price is greater than or equal to the sell price and adjusts the order books after the trade is executed. 

### Time complexity analysis
The matchOrder function only compares the buy and sell orders of each ticker. Since each ticker has its own heaps for buy and sell, we can check and execute trades by comparing only the top of the heaps. In the worst case, where all buy and sell orders are matched for a ticker, the time complexity will be O(number of orders of ticker x), and traversing through all the tickers is O(1024) = O(1), therefore the worst case time complexity of the matchOperation will be O(number of orders of ticker i) * O(1024) = O(number of total orders in the address book)

