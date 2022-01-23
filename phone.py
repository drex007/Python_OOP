from item import Item

class Phone(Item):
    all = [] # You can remove this so far as youve called the super method, it ca;; give you acess to the 'all' List 
    def __init__(self, name: str, price: float,quantity=0, broken_phones = 0):
        # A call to super for child class to have access to attributes and methods of the parent class 
        super().__init__(
            name, price, quantity 
        )
       
        assert broken_phones >=0 ,f"Make sure your  broken_phones {broken_phones} is greater or equal to zero"

        # assigining attributes to object 
    
        self.broken_phones = broken_phones
        Phone.all.append(self) # You can remove this so far as youve called the super method, it ca;; give you acess to the 'all' List 




phone1 = Phone("Smasung", 1000, 4)
phone1.broken_phones = 1
phone2 = Phone("Itel", 15, 21)
phone2.broken_phones= 2