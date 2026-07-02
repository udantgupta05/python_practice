class Atm:
  def __init__(self):
    self.__pin = ""
    self.__balance = 0

    self.__menu()


  def get_pin(self):
      return self.__pin


  def set_pin(self, new_pin):
      if type(new_pin) == int and 1000 <= new_pin <= 9999:
          self.__pin = new_pin
          print("PIN Changed")

      else:
          print("Not Allowed")


  def __menu(self):
    print("Welcome User to the ATM Machine, how would you like to proceed?")
    while True:
        user_input = input("""
        1. Create Pin
        2. Deposit
        3. Withdraw
        4. Check Balance
        5. Exit
        """)
        
        if user_input == "1":
            self.create_pin()
            
        elif user_input == "2":
            self.deposit()
            
        elif user_input == "3":
            self.withdraw()
        
        elif user_input == "4":
            self.check_balance()
        
        elif user_input == "5":
            print("")
            print("Thank You for using the ATM, visit again!")
            break
              
        else:
            print("")
            print("Invalid Choice, please try again!")
  
  
  def create_pin(self):
     print("")
     self.__pin = input("Enter the PIN you want to set: ")
     if len(self.__pin) == 4:
         print("PIN set up successful")
     
     else:
        print("Please enter 4 digit PIN only")
        self.__pin = ""
        print("")
  

  def deposit(self):
      print("")
      if self.__pin == "":
          print("Please Set-Up your pin first")
          return
      
      temp = input("Enter your PIN: ")
      if temp == self.__pin:
          print("PIN Verification Successful")
          print("")
          amount = int(input("Enter the amount: "))
          self.__balance = self.__balance + amount
          print("Deposit Successful")
          
            
      else:
          print("Invalid PIN entered")
          


  def withdraw(self):
      print("")
      if self.__pin == "":
          print("Please Set-Up your pin first")
          return
      
      temp = input("Enter your PIN: ")
      if temp == self.__pin:
          print("Pin Verification Successful")
          print("")
          amount = int(input("Enter the amount: "))
          if amount <= self.__balance:
              self.__balance = self.__balance - amount
              print("Amount Withdrawn Successfully")
              
      
          else: 
              print("Amount entered exceeds balance")
              
                
      else:
          print("Invalid PIN")
          
    

  def check_balance(self):
      print("")
      temp = input("Enter your pin: ")
      if temp == self.__pin:
          print("Print Verification Successful")
          print(f"Your Balance is ${self.__balance}")
    
      else: 
          print("Invalid PIN")
