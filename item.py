import csv

#Assigning attributes to python insatnces 
class Item:
    pay_rate = 0.8
    all = []

    def __init__(self, name: str, price: float,quantity=0):
        #Check arguments received validations

        assert price >=0, f"Make sure your {price} is greater or equal to zero"
        assert quantity >=0 ,f"Make sure your {quantity} is greater or equal to zero"

        # assigining attributes to object 
        self.name = name 
        self.price = price
        self.quantity = quantity
        Item.all.append(self)
    def calculate(self):
        total= self.quantity * self.price 
        return total

    @classmethod # class method that instantiate from csv file into the class Item directly
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as file:
            reader = csv.DictReader(file)
            items = list(reader)
        
        for item in items:
            print(item.get('name'), item.get('price'),item.get('quantity'))
        #    Item (
        #        name= item.get('name'),
        #        price= item.get('price'),
        #        quantity= item.get('quantity'))
        #    )



    def add_payrate(self):
        self.price= self.price * Item.pay_rate
        return self.price
    
    # a representation of the output, when a class Object is called 
    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}','{self.price}',{self.quantity})"




item1 = Item("Phone", 1000, 4)
item2 = Item("Pen", 15, 21)
item3 = Item("Mouse", 100, 8)
item4 = Item("Bag", 140, 7)
item5 = Item("Laptop", 120, 12)


