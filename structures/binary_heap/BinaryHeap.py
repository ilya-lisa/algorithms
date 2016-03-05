# binary min heap
class BinaryHeap:
    def __init__(self):
        self.elements = [0]
        self.heap_size = 0

    def insert(self, value):
        self.elements.append(value)
        self.heap_size += 1
        self.__heapify_up(self.heap_size)

    def __heapify_up(self, i):
        while i // 2 > 0:
            if self.elements[i] < self.elements[i // 2]:
                tmp = self.elements[i // 2]
                self.elements[i // 2] = self.elements[i]
                self.elements[i] = tmp
            i //= 2

    def __heapify_down(self, i):
        while (i * 2) <= self.heap_size:
            mc = self.__min_child(i)
            if self.elements[i] > self.elements[mc]:
                tmp = self.elements[i]
                self.elements[i] = self.elements[mc]
                self.elements[mc] = tmp
            i = mc

    def __min_child(self, i):
        if i * 2 + 1 > self.heap_size:
            return i * 2
        else:
            if self.elements[i * 2] < self.elements[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def remove_min(self):
        if len(self.elements) < 2:
            raise ValueError('heap is empty')
        result = self.elements[1]
        self.elements[1] = self.elements[self.heap_size]
        self.heap_size -= 1
        self.elements.pop()
        self.__heapify_down(1)
        return result

    def build_heap(self, values):
        i = len(values) // 2
        self.heap_size = len(values)
        self.elements = [0] + values[:]
        while i > 0:
            self.__heapify_down(i)
            i -= 1

    def __str__(self):
        return str(self.elements[1:])

