class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

    def append(self, data):
        tm = self
        while tm.next:
            tm = tm.next
        tm.next = Node(data)

    def __repr__(self):
        resp = ''
        tm = self
        while tm.next:
            resp += str(tm.data) + ' -> '
            tm = tm.next
        resp += str(tm.data)
        return resp
