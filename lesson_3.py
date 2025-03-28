#1
#class BankAccount:
 #   def __init__(self, account_number, balance=0):
  #      self.__account_number = account_number
   #     self.__balance = balance
#
 #   def deposit(self, amount):
  #      if BankAccount.is_positive(amount):
   #         self.__balance += amount
    #    else:
     #       print("сумма пополнения должна быть положительной")
#
 #   def withdraw(self, amount):
  #      if BankAccount.is_positive(amount):
   #         if self.__balance >= amount:
    #            self.__balance -= amount
     #       else:
      #          print("недостаточно средств на счете")
       # else:
        #    print("сумма снятия должна быть положительной")
#
 #   def get_balance(self):
  #      return self.__balance
#
 #   @staticmethod
  #  def is_positive(amount):
   #     if amount > 0: return True
    #    else: return False
#
 #   @classmethod
  #  def create_empty_account(cls, account_number):
   #     return cls(account_number)



# 2
#class User:
 #   def __init__(self, username, password):
  #      self.__username = username
   #     self.__password = password

 #   def get_username(self):
  #      return self.__username
#
 #   def set_password(self, new_password):
  #      if User.is_password_strong(new_password):
   #         self.__password = new_password
    #        print("пароль успешно изменён")
     #   else:
      #      print("пароль слишком короткий")
#
 #   @staticmethod
  #  def is_password_strong(password):
   #     return len(password) >= 6
#
 #   @classmethod
  #  def create_default_user(cls, username):
   #     return cls(username, "defaultPassword") 



#3
class Book:
    def __init__(self, title, author, year):
        self.__title = title
        self.__author = author
        self.__year = year

    def get_info(self):
        return f"{self.__title}, автор: {self.__author}, год: {self.__year}"

    @staticmethod
    def is_valid_year(year):
        import datetime
        current_year = datetime.datetime.now().year
        return isinstance(year, int) and year <= current_year

    @classmethod
    def create_default_year(cls, title, author):
        return cls(title, author, 2024)
