# Definition for singly-linked list.
#class ListNode(object):
#    def __init__(self, val=0, next=None):
#        self.val = val
#        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        #variable assignment
        tempTotal=("")
        num1=("")
        num2=("")
        array1=[]
        array2=[]

        print(l1)
        print(l2)

        listEnd=False
        while listEnd==False:
            tempVal=l1.val if l1 is not None else None
            if tempVal==None:
                listEnd==True
                break
            else:
                array1.append(tempVal)
                l1=l1.next if l1 is not None else None
        
        listEnd==False
        while listEnd==False:
            tempVal=l2.val if l2 is not None else None
            if tempVal==None:
                listEnd==True
                break
            else:
                array2.append(tempVal)
                l2=l2.next if l2 is not None else None

        array1.reverse()
        length=len(array1)
        for item in range(0,length):
            num1=num1+str(array1[item])

        array2.reverse()
        length=len(array2)
        for item in range(0,length):
            num2=num2+str(array2[item])

        num3=int(num1)+int(num2)
        print(num3)

#using inbuilt OOP
        length=len(str(num3))
        for item in range(length):
            if item==0:
                temp=str(num3)[item]
                ListNode(int(temp),None)
                PreVal=ListNode(int(temp),None)
            else:
                temp=str(num3)[item]
                ListNode(int(temp),PreVal)
                PreVal=ListNode(int(temp),PreVal)

        l3=PreVal
        print(l3)
        print(PreVal)
        return l3
