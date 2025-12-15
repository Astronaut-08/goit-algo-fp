'''Для реалізації однозв'язного списку (приклад реалізації можна взяти з конспекту) необхідно:

написати функцію, яка реалізує реверсування однозв'язного списку, змінюючи посилання між вузлами;
розробити алгоритм сортування для однозв'язного списку, наприклад, сортування вставками або злиттям;
написати функцію, що об'єднує два відсортовані однозв'язні списки в один відсортований список.'''

############################ Приклад реалізації з конспекту #######################################
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def search_element(self, data: int) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=' --> ')
            current = current.next
        print(None)

######################################################################################################

def reverse_list():
    pass

def sort_list():
    pass

def merge_list(ll1: LinkedList, ll2: LinkedList) -> LinkedList:
    '''Зливає два посортовані списки'''
    merged = LinkedList() # злитий список
    l1 = ll1.head # перша нода першого списку
    l2 = ll2.head # перша нода другого списку

    while l1 and l2: # поки списки не пусті
        if l1.data < l2.data:
            merged.insert_at_end(l1.data) # вставляємо в кінець
            l1 = l1.next # переходим на наступну ноду
        else:
            merged.insert_at_end(l2.data)
            l2 = l2.next
    
    while l1: # перевіряємо чи залишились ноди
        merged.insert_at_end(l1.data)
        l1 = l1.next

    while l2: # перевіряємо чи залишились ноди
        merged.insert_at_end(l2.data)
        l2 = l2.next

    return merged # попертаємо злитий список
            

# TESTING
l1 = LinkedList()
l2 = LinkedList()

l1.insert_at_end(1)
l1.insert_at_end(2)
l1.insert_at_end(3)

l2.insert_at_end(1)
l2.insert_at_end(3)

l3 = merge_list(l1, l2)

l3.print_list()
