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
            return cur
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        return cur

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

def reverse_list(ll: LinkedList) -> LinkedList:
    '''Обертаємо список методом берем початкову ноду і вставляємо на кінець
    початок видаляємо і тд'''
    prev = None # попередня нода
    cur = ll.head

    while cur: # по суті міняємо посилання в протилежну сторону
        next_cur = cur.next 
        cur.next = prev # наступна нода тепер попередня
        prev = cur # а попередня тепер актуальна
        cur = next_cur

    ll.head = prev # тепер берем початок з кінця
    return ll


def sort_list(ll: LinkedList) -> LinkedList:
    '''Застосовуємо сортування злиттям, використовуючи нашу функцію злиття'''
    # розраховуємо довжину списку
    cur = ll.head
    len_ll = 0
    while cur:
        len_ll += 1
        cur = cur.next

    if len_ll <= 1: # базовий випадок
        return ll
    
    cur = ll.head # повертаємось на початок списку
    middle = len_ll // 2

    left = LinkedList()
    for _ in range(middle): # ліву сторону проставляємо до середини
        left.insert_at_end(cur.data)
        cur = cur.next

    right = LinkedList()
    while cur: # праву сторону доходим до кінця
        right.insert_at_end(cur.data)
        cur = cur.next

    left = sort_list(left) # рекурсивні розбиття
    right = sort_list(right)

    return merge_list(left, right)

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
print('Merge list:')
l3 = merge_list(l1, l2)

l3.print_list()

l4 = LinkedList()
l4.insert_at_end(1)
l4.insert_at_end(5)
l4.insert_at_end(8)
l4.insert_at_end(6)
l4.insert_at_end(3)
print('Sort list:')
l4 = sort_list(l4)
l4.print_list()

print('Reverse list:')
l4 = reverse_list(l4)
l4.print_list()
