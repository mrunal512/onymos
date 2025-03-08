# This file contains the class definition of the min and max heap 
# used for the stock trading engine

# Encapsulate the order
class Order:
    def __init__(self, id, price, quantity):
        self.id = id
        self.price = price
        self.quantity = quantity

def parent(i):
        return (i-1)//2

def left(i):
    return 2*i + 1

def right(i):
    return 2*i + 2

class MinHeap:

    def __init__(self):
        # Initialize object
        self.heap = []
        self.size = 0

    
    def heapPush(self, key):
        # Push the key into head and heapify if required
        if not isinstance(key, Order):
            raise Exception("Need the key to be an object of class Order")
        
        self.heap.append(key)
        self.size +=1 
        idx = self.size - 1
        while (idx != 0 and self.heap[parent(idx)].price > self.heap[idx].price):
            # Swap the parent and child
            self.heap[parent(idx)], self.heap[idx] = self.heap[idx], self.heap[parent(idx)]
            idx = parent(idx)

    def heapPop(self):
        # Pop the key from the heap and heapify if required
        if self.size <= 0:
            raise Exception("Trying to pop 0 size heap")
        
        if self.size == 1:
            self.size -=1 
            return self.heap[0]
        
        self.heap[0] = self.heap[self.size - 1]
        self.size -= 1
        self.heapify(0)

    def heapify(self, i):
        l = left(i)
        r = right(i)
        smallest = i
        if(l<self.size and self.heap[l].price < self.heap[i].price):
            smallest = l
        if(r<self.size and self.heap[r].price < self.heap[smallest].price):
            smallest = r
        if(smallest != i):
            self.heap[smallest], self.heap[i] = self.heap[i], self.heap[smallest]
            self.heapify(smallest)
    
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
        self.size = 0

    def heapPush(self, key):
        # Push the key into head and heapify if required
        if not isinstance(key, Order):
            raise Exception("Need the key to be an object of class Order")
        
        self.heap.append(key)
        self.size +=1 
        idx = self.size - 1
        while (idx != 0 and self.heap[parent(idx)].price < self.heap[idx].price):
            # Swap the parent and child
            self.heap[parent(idx)], self.heap[idx] = self.heap[idx], self.heap[parent(idx)]
            idx = parent(idx)

    def heapPop(self):
        # Pop the key from the heap and heapify if required
        if self.size <= 0:
            raise Exception("Trying to pop 0 size heap")
        
        if self.size == 1:
            self.size -=1 
            return self.heap[0]
        
        self.heap[0] = self.heap[self.size - 1]
        self.size -= 1
        self.heapify(0)

    def heapify(self, i):
        l = left(i)
        r = right(i)
        smallest = i
        if(l<self.size and self.heap[l].price > self.heap[i].price):
            smallest = l
        if(r<self.size and self.heap[r].price > self.heap[smallest].price):
            smallest = r
        if(smallest != i):
            self.heap[smallest], self.heap[i] = self.heap[i], self.heap[smallest]
            self.heapify(smallest)
    
    def top(self):
        return self.heap[0]
    
    def editTop(self, newQuant):
        if newQuant <= 0:
            raise Exception("Cannot change new quantity to <= 0, please use heapPop to remove element")
        self.heap[0].quantity = newQuant




    