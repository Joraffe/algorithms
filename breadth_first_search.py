class Tree:
  def __init__(self, value):
    self.value = value
    self.children = []

  def __str__(self):
    return "Value: %s | Children: %s" % (self.value, self.children)

  def __repr__(self):
    return str(self)

  def breadth_first_search(self, target):
    q = Queue()
    q.enqueue(self)

    while q.size() > 0:
      cur = q.dequeue()
      if cur.value == target:
        return cur
      for child in cur.children:
        q.enqueue(child)

    raise TreeError("Tree does not contain target value")

  def add_child(self, value=None):
    if value is None:
      value = 0

    child = Tree(value)
    if not self.is_descendant(child):
      self.children.append(child)
    else:
      raise TreeError("That child is already a child of this Tree")

    return child

  def is_descendant(self, child):
    if child in self.children:
      return True
    else:
      for c in self.children:
        if c.is_descendant(child):
          return True

    return False

    def remove_child(child):
      if child in self.children:
        self.children.remove(child)
      else:
        raise TreeError("Input node is not a child of this Tree")


class TreeError(Exception):
  pass


# Other Data Structures used specifically for breadth_first_search:

class Stack:
  def __init__(self):
    self.items = []

  def isEmpty(self):
    return self.items == []

  def push(self, item):
    self.items.append(item)

  def pop(self):
    return self.items.pop()

  def peek(self):
    return self.items[len(self.items) - 1]

  def size(self):
    return len(self.items)


class Queue:
  def __init__(self):
    self.inbox = Stack()
    self.outbox = Stack()

  def enqueue(self, item):
    self.inbox.push(item)

  def dequeue(self):
    if self.outbox.size() == 0:
      while self.inbox.size() != 0:
        self.outbox.push(self.inbox.pop())

    return self.outbox.pop()

  def size(self):
    return self.inbox.size() + self.outbox.size()
