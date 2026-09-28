class Queue:
    def __init__(self):
        self._data = []

    def enqueue(self, item):
        self._data.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from an empty queue")
        return self._data.pop(0)

    def front(self):
        if self.is_empty():
            raise IndexError("Front on an empty queue")
        return self._data[0]

    def is_empty(self):
        return len(self._data) == 0

    def size(self):
        return len(self._data)

    def __len__(self):
        return len(self._data)

    def __str__(self):
        return f"Queue({self._data})"
