class MenuItem:
    def __init__(self, name: str, price: float, is_vegan: bool = False):
        self.name = name
        self.price = price
        self.is_vegan = is_vegan

    def get_name(self):
        return self.name

    def set_name(self, name: str):
        self.name = name

    def get_price(self):
        return self.price

    def set_price(self, price: float):
        self.price = price

    def get_is_vegan(self):
        return self.is_vegan

    def set_is_vegan(self, is_vegan: bool):
        self.is_vegan = is_vegan

    def is_vegan_item(self):
        return self.is_vegan


class Appetizer(MenuItem):
    def __init__(self, name: str, price: float):
        super().__init__(name, price)

    def __str__(self):
        return f"Appetizer: {self.name}, Price: {self.price}"


class MainCourse(MenuItem):
    def __init__(self, name: str, price: float, protein: str, grains: str, vegetables: str):
        super().__init__(name, price)
        self.protein = protein
        self.grains = grains
        self.vegetables = vegetables

    def get_protein(self):
        return self.protein

    def set_protein(self, protein: str):
        self.protein = protein

    def get_grains(self):
        return self.grains

    def set_grains(self, grains: str):
        self.grains = grains

    def get_vegetables(self):
        return self.vegetables

    def set_vegetables(self, vegetables: str):
        self.vegetables = vegetables

    def __str__(self):
        return (f"Main Course: {self.name}, Price: {self.price}, "
                f"Protein: {self.protein}, Grains: {self.grains}, Vegetables: {self.vegetables}")


class Beverage(MenuItem):
    def __init__(self, name: str, price: float, size: str, beverage_type: str):
        super().__init__(name, price)
        self.size = size
        self.beverage_type = beverage_type

    def get_size(self):
        return self.size

    def set_size(self, size: str):
        self.size = size

    def get_beverage_type(self):
        return self.beverage_type

    def set_beverage_type(self, beverage_type: str):
        self.beverage_type = beverage_type

    def __str__(self):
        return (f"Beverage: {self.name}, Price: {self.price}, "
                f"Size: {self.size}, Type: {self.beverage_type}")


class Dessert(MenuItem):
    def __init__(self, name: str, price: float):
        super().__init__(name, price)

    def __str__(self):
        return f"Dessert: {self.name}, Price: {self.price}"


class Order:
    def __init__(self, items: list[MenuItem]):
        self.items = items

    def add_item(self, item: MenuItem):
        self.items.append(item)
    #discount1: 10% for 15 items, 0.5% for each additional item, max 30%
    def discount1(self) -> float:
        n = len(self.items)
        if n > 15:
            extra_items = n - 15
            discount_percent = 10 + (extra_items * 0.5)
            if discount_percent > 30:
                discount_percent = 30
            return discount_percent
        return 0.0
    #discount2: 50% on beverages (applied later) for more than 3 main courses 
    def discount2(self) -> float:
        main_courses = [item for item in self.items if isinstance(item, MainCourse)]
        if len(main_courses) > 3:
            return 50.0
        return 0.0

    def get_bill(self) -> float:
        total = 0.0
        beverage_discount = self.discount2()
        for item in self.items:
            if isinstance(item, Beverage) and beverage_discount > 0:
                total += item.price * 0.5  # 50% off
            else:
                total += item.price
        discount_percent = self.discount1()
        if discount_percent > 0:
            total -= total * (discount_percent / 100)
        return total

    def __str__(self):
        order_str = "Order\n-------------------\n"
        for item in self.items:
            order_str += str(item) + "\n"
        order_str += f"-------------------\nBeverages: {len([item for item in self.items if isinstance(item, Beverage)])}\n"
        order_str += f"-------------------\nBeverages Price: {sum(item.price for item in self.items if isinstance(item, Beverage))}\n"
        order_str += f"-------------------\nAppetizers: {len([item for item in self.items if isinstance(item, Appetizer)])}\n"
        order_str += f"-------------------\nAppetizers Price: {sum(item.price for item in self.items if isinstance(item, Appetizer))}\n"
        order_str += f"-------------------\nMain Courses: {len([item for item in self.items if isinstance(item, MainCourse)])}\n"
        order_str += f"-------------------\nMain Courses Price: {sum(item.price for item in self.items if isinstance(item, MainCourse))}\n"
        order_str += f"-------------------\nDesserts: {len([item for item in self.items if isinstance(item, Dessert)])}\n"
        order_str += f"-------------------\nDesserts Price: {sum(item.price for item in self.items if isinstance(item, Dessert))}\n"
        order_str += f"-------------------\nTotal Items: {len(self.items)}\n"
        order_str += f"-------------------\nTotal Price: {sum(item.price for item in self.items)}\n"
        order_str += f"-------------------\nOverall Discount: {self.discount1()}%\n"
        order_str += f"-------------------\nNet Total: {self.get_bill():.2f}\n-------------------"
        return order_str
    
class Payment:
    def __init__(self):
        pass

    def pay(self, amount: float):
        raise NotImplementedError("pay() should be implemented in subclasses.")
    
class CardPayment(Payment):
    def __init__(self, card_number: str, cvv: str):
        super().__init__()
        self.__card_number = card_number
        self.__cvv = cvv

    def set_card_number(self, card_number: str):
        self.__card_number = card_number

    def get_card_number(self) -> str:
        return self.__card_number

    def set_cvv(self, cvv: str):
        self.__cvv = cvv

    def get_cvv(self) -> str:
        return self.__cvv

    def pay(self, amount: float):
        print(f"Paid {amount:.2f} using card ************{self.__card_number[-4:]}")

class CashPayment(Payment):
    def __init__(self, amount_given: float):
        super().__init__()
        self.amount_given = amount_given

    def pay(self, amount: float):
        if self.amount_given >= amount:
            print(f"Paid {amount:.2f} in cash. Change: {(self.amount_given - amount):.2f}")
        else:
            print(f"Not enough cash provided. Amount due: {(amount - self.amount_given):.2f}")
#Usage case
if __name__ == "__main__":

    order = Order([
        Appetizer("Empanadas", 3.50),
        Appetizer("Cheese Sticks", 4.00),
        Appetizer("Mini Burgers", 5.00),
        Appetizer("Mini Waffles", 2.50),
        Appetizer("Salchipapa", 5.00),
        MainCourse("Baby Beef", 10.00, "Beef", "Rice", "Salad"),
        MainCourse("Cordon Blue", 12.00, "Chicken", "Potatoes", "Salad"),
        MainCourse("Salmon", 15.00, "Fish", "Quinoa", "Lettuce"),
        MainCourse("Burger", 8.00, "Beef", "Bread", "Onion"),
        Beverage("Coca Cola", 2.00, "Medium", "Soda"),
        Beverage("Orange Juice", 3.00, "Large", "Juice"),
        Beverage("Quatro", 2.50, "Small", "Soda"),
        Beverage("Chocolate Milkshake", 4.00, "Large", "Milkshake"),
        Dessert("Chocolate Cake", 5.00),
        Dessert("Nutella Waffles", 6.00),
        Dessert("Flan", 4.00),
        Dessert("Lemon Cheesecake", 5.00)
    ])
    # 17 items, should apply an 11% discount

    print(order)

    CardPayment("1234-5678-9012-3456", "123").pay(order.get_bill())
    CashPayment(50.00).pay(order.get_bill())

    #testing private attributes
    c1 = CardPayment("1234-5678-9012-3456", "123")
    #print(c1.__card_number)
    #print(c1.__cvv)

    #testing setters and getters
    c1.set_card_number("9876-5432-1098-7654")
    c1.set_cvv("456")
    print(c1.get_card_number())
    print(c1.get_cvv())



