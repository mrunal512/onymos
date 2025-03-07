# This file contains the code for the trading engine functionality

# Author: Mrunalini Gaikwad
# Contact: mkgaikwa@uci.edu

# TODO: Remove the import and move the class definition to this file

from heap import *
from random import randint

class StockEngine:

    def __init__(self, numTickers = 1024):
        # Initialize trading engine and heaps
        
        # Support 1024 stocks
        self.maxTickers = numTickers

        self.buyBook = [MaxHeap() for _ in range(self.maxTickers)] # Array of MaxHeap objects

        self.sellBook = [MinHeap() for _ in range(self.maxTickers)] # Array of MinHeap objects
        
        raise NotImplementedError("Please define initialization of trading engine")
    
    def addOrder(self, orderType, tickerSymbol, quantity, price):
        '''
        Function: addOrder
        orderType: type of order, Buy/Sell
        tickerSymbol: Id of the stock being traded
        quantity: quantity of stock being traded
        price: price per share of stock
        '''

        # Create Order object
        order = Order(tickerSymbol, price, quantity)

        # Identify the heap based on order type and stock id
        if orderType == 'Buy':
            orderBook = self.buyBook[tickerSymbol]
            orderBook.heapPush(order)

        elif orderType == 'Sell':
            orderBook = self.sellBook[tickerSymbol]
            orderBook.heapPush(order)
        else:
            raise Exception("Unknown transaction type... Reissue correct order")
        
    def matchOrder(self):
        '''
        Function: matchOrder
        This function matches buy and sell orders for the 
        same stock id and executed the trade if the buy price is greater or
        equal to the sell price
        '''

        # Compare orders for each ticker in succession
        for id in range(self.maxTickers):

            # Compare top of buy and sell heaps until condition is not satisfied or either is empty
            while(self.buyBook[id].size > 0 and self.sellBook[id].size > 0):
                
                buyOrder = self.buyBook[id].top()
                sellOrder = self.sellBook[id].top()

                if(buyOrder.price >= sellOrder.price):
                    # Execute the trade
                    numSharesSold = min(buyOrder.quantity, sellOrder.quantity)

                    if numSharesSold == buyOrder.quantity:
                        # Remove order from book
                        self.buyBook[id].heapPop()
                    else:
                        # Edit top order to reflect remaining quantity
                        self.buyBook[id].editTop(buyOrder.quantity - numSharesSold)

                    if numSharesSold == sellOrder.quantity:
                        # Remove order from book
                        self.sellBook[id].heapPop()
                    else:
                        # Edit top order to reflect remaining quantity
                        self.buyBook[id].editTop(sellOrder.quantity - numSharesSold)

                else:
                    # No possible trades to execute
                    break

        # TODO: Maybe convert to while loop instead of traversal to mimic continous matchOrder thread

    


                    
                    


    



