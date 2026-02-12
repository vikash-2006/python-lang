# ==========================================================
# ATM CLASS – Encapsulation, Getter & Setter, Private Members
# ==========================================================

class Atm:

    # Constructor (special function)
    def __init__(self):
        print("Object ID:", id(self))
        self.pin = ""            # public attribute
        self.__balance = 0       # private attribute (encapsulation)
        # self.__menu()

    # Getter method (to access private balance)
    def get_balance(self):
        return self.__balance

    # Setter method (to modify private balance safely)
    def set_balance(self, new_value):
        if type(new_value) == int:
            self.__balance = new_value
        else:
            print("Invalid balance type")

    # Private menu method (cannot be accessed outside class)
    def __menu(self):
        user_input = input("""
        Hi, how can I help you?
        1. Press 1 to create pin
        2. Press 2 to change pin
        3. Press 3 to check balance
        4. Press 4 to withdraw
        5. Anything else to exit
        """)

        if user_input == '1':
            self.create_pin()
        elif user_input == '2':
            self.change_pin()
        elif user_input == '3':
            self.check_balance()
        elif user_input == '4':
            self.withdraw()
        else:
            exit()

    # Create PIN and set balance
    def create_pin(self):
        self.pin = input("Enter your pin: ")
        self.__balance = int(input("Enter balance: "))
        print("Pin created successfully")

    # Change existing PIN
    def change_pin(self):
        old_pin = input("Enter old pin: ")
        if old_pin == self.pin:
            self.pin = input("Enter new pin: ")
            print("Pin change successful")
        else:
            print("Incorrect pin")

    # Check balance
    def check_balance(self):
        user_pin = input("Enter your pin: ")
        if user_pin == self.pin:
            print("Your balance is:", self.__balance)
        else:
            print("Wrong pin")

    # Withdraw money
    def withdraw(self):
        user_pin = input("Enter the pin: ")
        if user_pin == self.pin:
            amount = int(input("Enter the amount: "))
            if amount <= self.__balance:
                self.__balance -= amount
                print("Withdrawal successful. Balance is:", self.__balance)
            else:
                print("Insufficient balance")
        else:
            print("Invalid pin")


# obj = Atm()
# obj.set_balance(1000)
# obj.withdraw()


# ==========================================================
# COLLECTION OF OBJECTS
# ==========================================================

# -------- List of Objects --------
class Person:

    def __init__(self, name, gender):
        self.name = name
        self.gender = gender


p1 = Person("nitish", "male")
p2 = Person("ankit", "male")
p3 = Person("ankita", "female")

people_list = [p1, p2, p3]

for person in people_list:
    print(person.name, person.gender)


# -------- Dictionary of Objects --------
people_dict = {
    "p1": p1,
    "p2": p2,
    "p3": p3
}

for key in people_dict:
    print(people_dict[key].gender)


# ==========================================================
# STATIC VARIABLES vs INSTANCE VARIABLES
# ==========================================================

class AtmStatic:

    __counter = 1      # static (class) variable

    def __init__(self):
        self.pin = ""
        self.__balance = 0
        self.cid = AtmStatic.__counter
        AtmStatic.__counter += 1

    # Static method (utility function)
    @staticmethod
    def get_counter():
        return AtmStatic.__counter


c1 = AtmStatic()
c2 = AtmStatic()

print("Customer ID:", c2.cid)
print("Next Counter Value:", AtmStatic.get_counter())


# ==========================================================
# STATIC METHODS & STATIC ATTRIBUTES
# ==========================================================

"""
Points to remember about static members:
- Created at class level
- Accessed using ClassName
- Shared among all objects
- Object independent
"""

class Lion:

    __water_source = "well in the circus"   # static attribute

    def __init__(self, name, gender):
        self.__name = name
        self.__gender = gender

    def drinks_water(self):
        print(self.__name, "drinks water from the", Lion.__water_source)

    @staticmethod
    def get_water_source():
        return Lion.__water_source


# Object creation
simba = Lion("Simba", "Male")
simba.drinks_water()
print("Water source of lions:", Lion.get_water_source())
