# Class made to permutate a list of integers from 1 to n
# Python OOP implementation of Heap's Algorithm https://en.wikipedia.org/wiki/Heap%27s_algorithm

class Permutation:
    def __init__(self, high, low=1):
        self.list = list(range(low,high + 1,1))
        self.subqueue = []
        self.queue = []
        self.__init_queue_recurse(high - low + 1)
        # print(self.queue)
        
    def __init_queue_recurse(self, n):
        self.__next_perm_recurse(0,n)
        self.__extend_queue()
                
    def __next_perm_recurse(self, i, n):
        stop = False
        if n <= 1:
            return True
        
        if (not stop):
            stop = self.__next_perm_recurse(0, n - 1)
            if i < n - 1:
                self.subqueue.append([i, n])
            i += 1
        
    def __extend_queue(self):
        self.subqueue.extend(self.queue)
        self.queue = self.subqueue.copy()
        self.subqueue.clear()

    def next_permutation(self):
        if (len(self.queue) == 0):
            return self.list
        
        p = self.queue.pop(0)
        i = p[0]
        n = p[1]
        self.__next_perm_recurse(i + 1, n)
        self.__extend_queue()
        # print(i, n, self.queue)
        
        copy_list = self.list.copy()
        if n % 2 == 0:
            self.list[i], self.list[n - 1] = self.list[n - 1], self.list[i]
        else:
            self.list[0], self.list[n - 1] = self.list[n - 1], self.list[0]
            
        return copy_list