from collections import defaultdict


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.freq = 1
        self.prev = None
        self.next = None


class DLL:
    def __init__(self):
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def add(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
        self.size += 1

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1

    def removeLast(self):
        if self.size == 0:
            return None
        node = self.tail.prev
        self.remove(node)
        return node


class LFUCache(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.minFreq = 0
        self.nodes = {}
        self.freqMap = defaultdict(DLL)

    def update(self, node):
        freq = node.freq
        self.freqMap[freq].remove(node)

        if freq == self.minFreq and self.freqMap[freq].size == 0:
            self.minFreq += 1

        node.freq += 1
        self.freqMap[node.freq].add(node)

    def get(self, key):

        if key not in self.nodes:
            return -1

        node = self.nodes[key]
        self.update(node)
        return node.value

    def put(self, key, value):

        if self.capacity == 0:
            return

        if key in self.nodes:
            node = self.nodes[key]
            node.value = value
            self.update(node)
            return

        if self.size == self.capacity:
            node = self.freqMap[self.minFreq].removeLast()
            del self.nodes[node.key]
            self.size -= 1

        node = Node(key, value)
        self.nodes[key] = node
        self.freqMap[1].add(node)
        self.minFreq = 1
        self.size += 1
        