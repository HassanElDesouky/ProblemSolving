from node import Node

def kth_element1(head, k):
    cur = head
    n = 0
    while cur.next:
        cur = cur.next
        n += 1
    if k > n:
        return head
    cur = head
    counter = 1
    while counter != n-k+1:
        cur = cur.next
        counter += 1
    return cur

def kth_element(head, k):
    p1 = head
    p2 = head
    for i in range(k):
        if p2 == None:
            return None
        p2 = p2.next
    while p2 != None:
        p2 = p2.next
        p1 = p1.next
    return p1

head = Node(1)
head.append(2)
head.append(2)
head.append(4)
head.append(2)
head.append(5)
head.append(5)
head.append(7)
head.append(9)
print(head)
print(kth_element(head, 3))
