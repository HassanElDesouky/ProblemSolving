from node import Node

def remove_dups1(head):
    li = []
    temp = head
    while temp.next:
        if temp.next.data not in li:
            li.append(temp.next.data)
            temp = temp.next
        else:
            temp.next = temp.next.next

def remove_dups(head):
    cur = head
    while cur.next:
        run = cur
        while run.next:
            if run.next.data == cur.data:
                run.next = run.next.next
            else:
                run = run.next
        cur = cur.next

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
remove_dups(head)
print(head)
