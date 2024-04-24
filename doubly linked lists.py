class DblList:
  class Node:
    previous_node = None
    next_node = None
    element = 0

    def init(self, element, next_node = None, previous_node = None):
      self.element = element
      self.next_node = next_node
      self.previous_node = previous_node

  head = None
  tail = None
  length = 0
    
  def add(self, element):
    self.length += 1
    if not self.head:
      self.head = self.Node(element)
      return element
    elif not self.tail:
      self.tail = self.Node(element, None, self.head)
      self.head.next_node = self.tail
      return element
    else:
      self.tail = self.Node(element, None, self.tail)
      self.tail.previous_node.next_node = self.tail
      return element

  def _del(self, index, reverse = False):
    if index == 0:
      el = self.head.element

      if self.head.next_node:
        self.head = self.head.next_node
        self.head.previous_node = None
      else:
        self.head = None
      return el
    elif index == self.length - 1:
      el = self.tail.element
      self.tail = self.tail.previous_node
      self.tail.next_node = None
      return el
    elif reverse:
      i = self.length - 1
      node = self.tail

      while i != index:
        node = node.previous_node
        i -= 1

      el = node.element
      node.previous_node.next_node, node.next_node.previous_node = node.next_node, node.previous_node
      del node

      return el
    else:
      i = 0
      node = self.head

      while i != index:
        node = node.next_node
        i += 1

      el = node.element
      node.previous_node.next_node, node.next_node.previous_node = node.next_node, node.previous_node
      del node

      return el
    
  def delete(self, index):
    if self.head:
      if index > self.length // 2:
        el = self._del(index, reverse = True)
      elif index <= self.length // 2:
        el = self._del(index, reverse = False)
      self.length -= 1
      return el

  def _assign(self, index, element, reverse = False):
    if index == 0:
      self.head.element = element
    elif index == self.length - 1:
      self.tail.element = element
    elif reverse:
      i = self.length - 1
      node = self.tail

      while i != index:
        node = node.previous_node
        i -= 1

      node.element = element
    else:
      i = 0
      node = self.head

      while i != index:
        node = node.next_node
        i += 1

      node.element = element

  def is_empty(self):
    return self.length == 0
  
  def assign(self, index, element):
    if self.head:
      if index > self.length // 2:
        self._assign(index, element, reverse = True)
      elif index <= self.length // 2:
        self._assign(index, element, reverse = False)
      self.length -= 1
  
  def iter(self):
    node = self.head

    while node:
      yield node.element
      node = node.next_node


if name == "main":
  dblList = DblList()

  ## Добавление в двусвязный список
  dblList.add(4)
  dblList.add(-3)
  dblList.add(11)
  dblList.add(5)
  dblList.add(8)
  dblList.add(17)

  ## Удаление элемента из двусвязного списка по индексу
  dblList.delete(1)

  ## Вставка элемента в двусвязный список по индексу
  dblList.assign(0, 12)

  ## Вывод каждого элемента
  for e in dblList:
    print(e)

## Проверка на пустоту
print(dblList.is_empty())