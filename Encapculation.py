# PUBLIC - Public attibutrs and methods are accessible fron anywhere in the code

# class AI:
#     def __init__(self):
#         self.name="uma"
    
#     # def display(self):
#     #     print(self.name)

# x=AI()
# # x.display()
# print(x.name)

# PROTECTED

# class NSTI:
#     def __init__(self):
#         self._trade="AI"

# class CTS(NSTI):
#     def display(self):
#         print(self._trade)



# y=NSTI()
# x=CTS()
# x.display()


# PRIVATE

# class Trainer:
#     def __init__(self):
#         self.__salary="1000"

#     def disp(self):
#         print(self.__salary)

#         return self.__salary
# x=Trainer()

# print(x.disp())


# class Public:
#     def __init__(self,name):   public attribute
#         self.name=name

#     def greet(self):            public method
#         print(f"Hello, {self.name}")


# p=Public("uma")

# print(p.name)

# p.greet()

# PROTECTED

# class Prot:
#     def __init__(self,age):
#         self._age=age


#     def _show_age(self):
#         print(f"age: {self._age}")


# a=Prot(27)
# print(a._age)
# a._show_age()



# class Hospital:
#     def __init__(self):
#         self.__patients=[]

#     def add(self,patients):
#         self.__patients.append(patients)
#         print(f'patient {patients} added')

#     def remove(self,patients):
#         if patients in self.__patients:
#                 self.__patients.remove(patients)
#                 print(f'patient (patient) removed from list')

#         else:
    
#             print(f'{patients} not found')

#     def disp(self):
#          for patients in self.__patients:
#               print(patients)
            

# x=Hospital()


# x.add("uma")
# x.add("alli")
# x.add("vally")
# x.remove("vally")
# x.disp()



# class NSTI:
#     def __init__(self):
#         self.__students=[]

#     def add(self,students):
#         self.__students.append(students)
#         print(f'students {students} added')

#     def remove(self,students):
#         if students in self.__students:
#                 self.__students.remove(students)
#                 print(f'students (students) removed from list')

#         else:
    
#             print(f'{students} not found')

#     def disp(self):
#          for students in self.__students:
#               print(students)
            

# x=NSTI()


# x.add("uma")
# x.add("alli")
# x.add("vally")

# x.remove("vally")
# x.disp()


# lab52


# class Bank:

#     def __init__(self,accountnumber,holdername,initialbalance=0):
#         self.__accountnumber=accountnumber
#         self.__holdername=holdername
#         self.__initialbalance=initialbalance
    # def Deposit(self,amount):
    #     if amount>0:
    #         self.__initialbalance += amount
    #         print(f'deposited: {amount}')
    #     else:
    #         print("Amount must be greater than zero.")

#     def withdraw(self,amount):
#         if amount > 0 and amount <= self.__initialbalance:
#             self.__initialbalance -= amount
#             print(f'amount withdraw: {amount}')
#         else:
#             print("insufficient funds")

#     def __checkbalance(self):
#         return self.__checkbalance
    

# if __name__=="__main__":


#     x=Bank("123456","uma",1000)
#     # print(f"Account holder: {x.__accountnumber},{x.__holdername},{x.__initialbalance}")
#     print(x)
#     x.Deposit(500)
#     x.withdraw(200)
#     print(f"Balance: {x.__checkbalance()}")



# class Movie:
#     def __init__(self,id,title,price):
#         self.id=id
#         self.__title=title
#         self.__price=price


#     def s_title(self,title):
#         self.__title=title


#     # def t_price(self,price):
#     #     if price >0:
#     #         self.__price=price
#     #     else:
#     #         print("enter price more than 0.")

#     def g_title(self):
#         return self.__title

#     def g_ticket(self):
#         return self.__price

#     def abc(self):
#         print(f'Id :{self.id}')
#         print(f'Title :{self.__title}')
#         print(f'Price :{self.__price}')

# def movie():
    # id=input("enter id:")
    # title=input("enter movie name:")
    # while True:
    #     price=int(input("enter the price:"))
    #     if price>0:
    #         break
    #     else:
    #         print("price must more than Rs.0")

#     return Movie(id,title,price)

# x=movie()
# x.abc()


# task1


# class Book:
#     def __init__(self,title,author,price):
#         self.__title=title
#         self.__author=author
#         self.__price=price

#     def g_title(self):
#         return self.__title

#     def s_title(self,title):
#          self.__title=title

#     def g_author(self):
#         return self.__author
        

#     def s_author(self,author):
#         self.__author=author


#     def g_price(self):
#         return self.__price
        

#     def s_price(self,price):
#         self.__price=price
        
        
#     def abc(self):
#       print(f'title :{self.__title}')
#       print(f'author :{self.__author}')
#       print(f'price :{self.__price}')


# def book():
#     title=input("enter title:")
#     author=input("enter author:")
#     while True:
#         price=int(input("enter the price:"))
#         if price>0:
#             break
#         else:
#             print("price must more than Rs.0")
     


    
#     return Book(title,author,price)
    

# a=book()
# a.abc()

# task2


# class Employee:
#     def __init__(self,name,position,salary):
#         self.__name=name
#         self.__position=position
#         self.__salary=salary

#     def g_name(self):   ///access the private attribute///
#         return self.__name

#     def s_title(self,name):   ///modify the private attribute///
#          self.__title=name

#     def g_position(self):
#         return self.__position
        

#     def s_author(self,position):
#         self.__position=position


#     def g_salary(self):
#         return self.__salary
        

#     def s_salary(self,salary):
#         self.__salary=salary
        
        
#     def abc(self):
#       print(f'name :{self.__name}')
#       print(f'position :{self.__position}')
#       print(f'salary :{self.__salary}')



# def employee():
#     name=input("enter name:")
#     position=input("enter position:")
#     while True:
#         salary=int(input("enter the salary:"))
#         if salary>0:
#             break
#         else:
#             print("salary must more than Rs.0")
     


    
#     return Employee(name,position,salary)
    

# a=employee()
# a.abc()