#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Square Numbers and Return Their Sum:
class point:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    def sqSum(self):
        a = x*self.x
        b = y*self.y
        c = z*self.z
        d = a+b+c
        return a,b,c,d
x = int(input("Enter the number: "))
y = int(input("Enter the number: "))
z = int(input("Enter the number: "))
obj = point(x,y,z)
h = obj.sqSum()
print(h)


# In[8]:


#Implement a Calculator Class:
class calculator:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
    def add(self):
        return num1 + num2
    def subtract(self):
        return num1-num2
    def multiply(self):
        return num1 * num2
    def divide(self):
        return num1/num2
num1 = int(input("Enter the number: "))
num2 = int(input("Enter the number: "))
obj =  calculator(num1,num2)
a = obj.add()
print(a)
b = obj.subtract()
print(b)
c = obj.multiply()
print(c)
d = obj.divide()
print(d)


# In[21]:


#Implement the Complete Student Class:
class student:
    def setName(self,setName):
        self.setName = setName
    def getName(self,getName):
        self.getName = getName
    def setRollNumber(self,RollNumber):
        self.setRollNumber = RollNumber
    def getRollNumber(self,RollNumber):
        self.getRollNumber = RollNumber
    def display(self):
        print("setName: ",self.setName)
        print("getName: ",self.getName)
        print("setRollNumber: ",self.setRollNumber)
        print("getRollNumber: ",self.getRollNumber)
        
obj = student()
obj.setName("shubham")
obj.getName("Shubham")
obj.getRollNumber(12)
obj.setRollNumber(12)
obj.display()


# In[19]:


# Implement a Banking Account:
class Account:
    def __init__(self,title = None, Balance = 0):
        self.title = title
        self.Balance = Balance
class SavingAccount(Account):
    def __init__(self,title = None, Balance = 0):
        super().__init__(title,Balance)
    def interestRate(self,interestRate):
        self.interestRate = interestRate
        
obj = SavingAccount("Shubham",5000)
h = SavingAccount()
h.interestRate(5)
print("Account",(obj.title,obj.Balance,h.interestRate))


# In[7]:


#Handling a Bank Account:
class Account:
    def __init__(self,title = None,balance = 0):
        self.title = title
        self.balance = balance
    def deposite(self):
        amount = float(input("Enter the Amount To be Deposite: "))
        self.balance +=amount
        print("\n Amount Deposite:" , amount )
    def withdrawl(self):
        amount = float(input("Enter the amount to be withdrawl: "))
        
        if self.balance>=amount:
            self.balance -=amount
            
            print("\n Your Withdrawl Amount is : ",amount)
        else:
            print("\n Insufficient balance: ")
            
    def getbalance(self):
        print("\n Net Available balance : ",self.balance)
        
class SavingAccount(Account):
    def __init__(self,title = None,balance = 0, interestRate = 0):
        super().__init__(title,balance)
        self.interestRate = interestRate
    def interestAmount(self):
        return ((self.balance*self.interestRate)/100)


# In[10]:


obj = Account("Shubham",5000)
obj.deposite()
obj.getbalance()


# In[11]:


obj.withdrawl()
obj.getbalance()


# In[12]:


obj = SavingAccount("Shubham",5000,5)
obj.interestAmount()


# In[ ]:




