import sys
class GetNode:
    def __init__(self):
        self.data=None
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def append(self):
        data=int(input("enter data"))
        newNode=GetNode()
        newNode.data=data
        if self.head==None:
            self.hesd=newNode
        else:
            ptr=self.head
            while ptr.next!=None:
                ptr=ptr.next
            ptr.next=newNode
            print(data,"is added")
    def traverse(self):
        if self.head==None:
            print("linked list not present")
        else:
            ptr=self.head
            while ptr!=None:
                print(ptr.data," ->",end="")
                ptr=ptr.next
    def addAtBegin(self):
        data=int(input("enter data"))
        newNode=GetNode()
        newNode.data=data
        if self.head==None:
            self.head=newNode
        else:
            ptr=self.head
            newNode.next=ptr
            self.head=newNode

    def addAtBetween(self):
        data=int(input("enter data: "))
        key=int(input("enter data after inserted: "))
        newNode=GetNode()
        newNode.data=data
        if self.head==None:
            self.head=newNode
        else:
            ptr=self.head
            while ptr.next!=None:
                if key==ptr.data:
                    break;
                else:
                    ptr=ptr.next
            if ptr.next==None:
                print("Key not found")
            else:
                ptr1=ptr.next
                ptr.next=newNode
                newNode.next=ptr1
                print(data,"is added")
    
    def deleteAtBegin(self):
        if head==None:
            print("list not present")
        else:
            ptr=self.head
            ptr1=ptr.next
            ptr.next=None
            head=ptr1
            print(ptr.data,"is deleted.")
        

if __name__ == '__main__':
    obj=LinkedList()
    while True:
        print("1.Append")
        print("2.Traverse")
        print("3. addAtBegin")
        print("4. addAtBetween")
        print("5. deleteAtbegin")
        print("0.Exit")
        n=int(input("select any choice: "))
        if n==1:
            obj.append()
        elif n==2:
            obj.traverse()
        elif n==3:
            obj.addAtBegin()
        elif n==4:
            obj.addAtBetween()
        elif n==5:
            obj.deleteAtBegin()

        elif n==0:
            sys.exit(0)
