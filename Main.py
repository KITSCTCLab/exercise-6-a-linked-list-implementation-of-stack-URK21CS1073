class node:
    def __init__(s,x):
        s.data=x
        s.next=None
class stackList:
    def __init__(self):
        self.top=None
    def push(self,x):
        n=node(x)
        n.next=self.top
        self.top=n
    def displayIO(self):
        self.displayInorder1(self.top)
    def displayInorder1(self,t):
        if t!=None:
            self.displayInorder1(t.next)
            print(t.data)
    def display(self):
        if self.top==None:
            print("Stack has no element")
        else:
            temp=self.top
            while temp!=None:
                print(temp.data)
                temp=temp.next
    def pop(self):
        if self.top==None:
            print("Stack has no element")
        else:
            pops = self.top
            self.top = self.top.next
            pops.next = None
            return pops.data
sul=stackList()
while(1):
    print("1.Push,\n2.pop,\n3.Display In_order,\n4.Display in last in first out order,\n5. Exit")
    h=int(input("enter your choice to be done:"))
    if h==1:
        x=int(input("Enter the data to be pushed:"))
        sul.push(x)
    elif h==2:
        sul.pop()
    elif h==3:
        sul.displayIO()
    elif h==4:
        sul.display()
    else:
        break
