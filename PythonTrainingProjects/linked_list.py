class ObjList:
    def __init__(self, data=''):
        self.__data = data
        self.__prev = None
        self.__next = None

    def get_data(self):
        return self.__data

    def set_data(self, data):
        if type(data) == str:
            self.__data = data

    data = property(get_data, set_data)

    def get_prev(self):
        return self.__prev

    def set_prev(self, prev):
        if type(prev) in (ObjList, type(None)):
            self.__prev = prev

    prev = property(get_prev, set_prev)

    def get_next(self):
        return self.__next

    def set_next(self, next):
        if type(next) in (ObjList, type(None)):
            self.__next = next

    next = property(get_next, set_next)


class LinkedList:
    def __init__(self):
        self.__head = None
        self.__tail = None

    def get_head(self):
        return self.__head

    def set_head(self, head):
        self.__head = head

    head = property(get_head, set_head)

    def get_tail(self):
        return self.__tail

    def set_tail(self, tail):
        self.__tail = tail

    tail = property(get_tail, set_tail)

    def add_obj(self, obj):
        obj.prev = self.tail
        if self.__tail:
            self.__tail.next = obj
        self.__tail = obj
        if not self.__head:
            self.__head = obj   


    def __get_obj_by_index(self, indx):
        h = self.__head
        n = 0
        while h and n < indx:
            h = h.next
            n += 1
        return h
    

    def remove_obj(self, indx):
        obj = self.__get_obj_by_index(indx)
        if obj is None:
            return
        
        p, n = obj.prev, obj.next
        if p:
            p.next = n
        if n:
            n.prev = p

        if self.__head == obj:
            self.__head = n
        if self.__tail == obj:
            self.__tail = p


    def __len__(self):
        curr = self.__head
        i = 0
        while curr:
            i += 1
            curr = curr.next
        return i

    def __call__(self, indx, *args, **kwargs):
        i = 0
        curr = self.__get_obj_by_index(indx)

        return curr.data if curr else None


def main():
    linked_lst = LinkedList()
    linked_lst.add_obj(ObjList("Sergey"))
    linked_lst.add_obj(ObjList("Balakirev"))
    linked_lst.add_obj(ObjList("Python"))
    linked_lst.remove_obj(2)
    linked_lst.add_obj(ObjList("Python ООП"))
    n = len(linked_lst)  # n = 3
    s = linked_lst(1) # s = Balakirev
    print(n, ' - ', s)


if __name__ == '__main__':
    main()
