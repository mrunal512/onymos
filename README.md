# Onymos Coding challenge

## Introduction

This repository contains the code for the Onymos coding challenge. This repo implements a stock trading engine according to the specifications mentioned below:
1. Write an ‘addOrder’ function that will have the following parameters:\
      ‘Order Type’ (Buy or Sell), ‘Ticker Symbol’, ‘Quantity’, ‘Price’ \
      Support 1,024 tickers (stocks) being traded. \
      Write a wrapper to have this ‘addOrder’ function randomly execute with different parameter values to simulate active stock transactions.

2. Write a ‘matchOrder’ function, that will match Buy & Sell orders with the following criteria:\
      Buy price for a particular ticker is greater than or equal to lowest Sell price available then.\
      Write your code to handle race conditions when multiple threads modify the Stock order book, as run in real-life, by multiple stockbrokers. Also, use lock-free data structures.\

Do not use any dictionaries, maps or equivalent data structures. Essentially there should be no ‘import’-s nor ‘include’-s nor similar construct relevant to the programming language you are using that provides you dictionary, map or equivalent data structure capability. In essence, you are writing the entire code. Standard language-specific non data structure related items are ok, but try to avoid as best as you can.

Write your ‘matchOrder’ function with a time-complexity of O(n), where 'n' is the number of orders in the Stock order book.

### Structure
trade.py contains the implementation of the stock trading engine. Please note that the imports are only for the custom implementation of the heap in heap.py and for random number generation for the wrapper function
The implementation of the heap is defined in a seperate file to aid code readability only. 

## addOrder explanationpr

The addOrder function adds an order in the trade book based on the order type and the ticker id of the order. This structure has been chosen to handle race conditions from multi-threading

### Race condition prevention
A buy and sell heap has been implemented for each ticker supported in the engine. This will cause multiple threads pushing orders to different tickers to access different data structures and prevent race conditions. 
In the event of multiple threads adding orders for the same ticker, the heapify function will maintain the heap property even when 2 threads push keys

## matchOrder explanation

The matchOrder function checks the highest buy price and the lowest sell price in the order book and executes the trade if the buy price is greater than or equal to the sell price and adjusts the order books after the trade is executed. 

### Time complexity analysis
The matchOrder function only compares the buy and sell orders of each ticker. Since each ticker has its own heaps for buy and sell, we can check and execute trades by comparing only the top of the heaps. In the worst case, where all buy and sell orders are matched for a ticker, the time complexity will be O(number of orders of ticker x), and traversing through all the tickers is O(1024) = O(1), therefore the worst case time complexity of the matchOperation will be O(number of orders of ticker i) * O(1024) = O(number of total orders in the address book)

