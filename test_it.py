# # import csv
# # from asyncio import create_task
# # import pandas as pd
# #
# # def read_csv(data,mode):
# #     with open (data,mode) as file:
# #         reader=csv.reader(file)
# #         counter=0
# #         for row in reader:
# #             if counter==0:
# #                 print(f'header :\n {" |".join(row)} \n')
# #                 counter+=1
# #             else:
# #                 if row.__contains__('-'):
# #                     continue
# #                 print(' ',counter,'|',',|'.join(row))
# #                 counter+=1
# #
# # def create_and_write_csv(filepath,mode,newline,header_data,data):
# #     with open(filepath,mode,newline=newline) as writer:
# #
# #         writer=csv.writer(writer)
# #         writer.writerow(header_data)
# #         writer.writerows(data)
# #
# # def read_using_pandas():
# #     try:
# #          temp_df=pd.read_csv('data/employee.csv')
# #          if not temp_df.empty:
# #              pandas_csv=temp_df
# #              print(f'type of object is : {type(pandas_csv)}\n and the data the pandas object holds is :\n {pandas_csv}')
# #
# #
# #     except Exception as e:
# #         print('An error occured : ',(e))
# #
# # if __name__=="__main__":
# #     #read_csv(data='data/created_csv.csv',mode='r+')
# #     header=['name','odour','colour']
# #     data=[['lemon','sour','yellow'],
# #           ['guava','sourly sweet','green']]
# #     #create_and_write_csv('data/temp_fruits.csv',mode='w',newline='',header_data=header,data=data)
# #     # with open('data/created_csv.csv','r+') as file:
# #
# #     #read_using_pandas()
# #
# # ########################################################################################################
# #
# # #######################################################
# # ######### TESTING OOPS CONCEPTS #######################
# # #######################################################
# #
# # ## DEFAULT CONSTRUCTOR
# # class Person:
# #     def __init__(self):
# #         self.name='Atharva'
# #         self.age=24
# #     def display_info(self):
# #         print(f"Name of the person is {self.name} age of person is {self.age}")
# #
# # person1 = Person()
# # person1.display_info()
# #
# # ##PARAMETERIZED CONSTRUCTOR
# # class Person:
# #     def __init__(self,name,age):
# #         self.name=name
# #         self.age=age
# #     def display_info(self):
# #         print(f"Name of the person is {self.name} age of person is {self.age}")
# #
# # person1=Person("alice",29)
# # person23=Person("bob",55)
#
#
#
#
#
#
#
# #This program is about Library where we can see the
# #:available books : Books we want to lend : Books we want to return
# # Class Library & Class customer
#
# class Library:
#     def __init__(self,list_of_books):
#         self.list_of_books=list_of_books
#
#     def available_books(self):
#         print("Below are the list of available books.")
#         itr=0
#         for book in self.list_of_books:
#             print(itr,')',book)
#             itr+=1
#     def lend_book(self,remove_book):
#         if remove_book in self.list_of_books:
#             self.list_of_books.remove(remove_book)
#             print('Thanks For lending ',remove_book,'! ')
#         else:
#             print('The book you are requesting is not in the library \nBelow are the books that are available to Lend :')
#             print(self.list_of_books)
#
#     def add_book(self,add_book):
#         self.list_of_books.append(add_book)
#         print('Thanks for returning ',add_book)
#
# class Customer:
#     def lend_book(self):
#         print('Enter the book name you are borrowing :')
#         self.book=input()
#         return self.book
#     def return_book(self):
#         print('Enter the book you are returning :')
#         self.book=input()
#         return self.book
#
# library=Library(['Book1','Book2','Book3'])
# customer=Customer()
# while True:
#     print("Enter your choice")
#     print("1.Display all the books\n2.Lend A book\n3.Return the book\n4.Exit")
#     try:
#         ch=int(input())
#         if ch==1:
#             library.available_books()
#         elif ch==2:
#             remove_book=customer.lend_book()
#             library.lend_book(remove_book)
#         elif ch==3:
#             add_book=customer.return_book()
#             library.add_book(add_book)
#         else:
#             exit()
#     except Exception as e:
#         print('You caught exception i.e.\n',e)


class BankAccount:
    def __init__(self, account_holder, initial_balance):
        self.__account_holder = account_holder  # Private attribute
        self.__balance = initial_balance        # Private attribute

    # Public method to view the account balance
    def get_balance(self):
        return self.__balance

    # Public method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"${amount} deposited successfully.")
        else:
            print("Deposit amount must be positive.")

    # Public method to withdraw money
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"${amount} withdrawn successfully.")
        else:
            print("Invalid withdrawal amount or insufficient balance.")

# Example usage
account = BankAccount("John Doe", 1000)

# Accessing the account balance using a method
print("Current Balance:", account.get_balance())  # Output: Current Balance: 1000

# Depositing money
account.deposit(500)  # Output: $500 deposited successfully.

# Withdrawing money
account.withdraw(300)  # Output: $300 withdrawn successfully.

# Attempting to directly access the private attribute (will raise an error)
# print(account.__balance)  # AttributeError: 'BankAccount' object has no attribute '__balance'

