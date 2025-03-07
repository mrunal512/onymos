# This file contains the class definition of the min and max heap 
# used for the stock trading engine

# Encapsulate the order
class Order:
    def __init__(self, id, price, quantity):
        self.id = id
        self.price = price
        self.quantity = quantity


class MinHeap:

    def __init__(self):
        # Initialize object
        self.heap = []
        self.size = 0

    def heapPush(self, key):
        # Push the key into head and heapify if required
        raise NotImplementedError("Please define heapPush function")

    def heapPop(self):
        # Pop the key from the heap and heapify if required
        raise NotImplementedError("Please define heapPop function")
    
    def top(self):
        return self.heap[0]
    
    def editTop(self, newQuant):
        if newQuant <= 0:
            raise Exception("Cannot change new quantity to <= 0, please use heapPop to remove element")
        self.heap[0].quantity = newQuant


class MaxHeap:

    def __init__(self):
        # Initialize object
        self.heap = []

    def heapPush(self, key):
        # Push the key into head and heapify if required
        raise NotImplementedError("Please define heapPush function")

    def heapPop(self, key):
        # Pop the key from the heap and heapify if required
        raise NotImplementedError("Please define heapPop function")
    
    def top(self):
        return self.heap[0]
    
    def editTop(self, newQuant):
        if newQuant <= 0:
            raise Exception("Cannot change new quantity to <= 0, please use heapPop to remove element")
        self.heap[0].quantity = newQuant




    