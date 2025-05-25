# RETO_4

Desarrollo del reto propuesto en clase.

A continuacion los usage cases de cada punto, el codigo esta adjunto en el repo.

Ejercicio clase SHAPE

```python
#Usage example
if __name__ == "__main__":
    t1 = RightTriangle([Point(0, 0), Point(3, 0), Point(0, 4)], None)
    print("Triángulo Rectángulo")
    print("Área:", t1._area)
    print("Perímetro:", t1._perimeter)
    print("Ángulos internos:", t1._inner_angles)
    print("Vértices:", t1._vertices)
    print("Lados:", t1._edges)
    print("¿Es regular?:", t1.is_regular)
    print("\n")

    t2 = Scalene([Point(0, 0), Point(3, 0), Point(1, 4)], None)
    print("Triángulo Escaleno")
    print("Área:", t2._area)
    print("Perímetro:", t2._perimeter)
    print("Ángulos internos:", t2._inner_angles)
    print("Vértices:", t2._vertices)
    print("Lados:", t2._edges)
    print("¿Es regular?:", t2.is_regular)
    print("\n")

    t3 = Isosceles([Point(0, 0), Point(3, 0), Point(1.5, 4)], None)
    print("Triángulo Isósceles")
    print("Área:", t3._area)
    print("Perímetro:", t3._perimeter)
    print("Ángulos internos:", t3._inner_angles)
    print("Vértices:", t3._vertices)
    print("Lados:", t3._edges)
    print("¿Es regular?:", t3.is_regular)
    print("\n")

    t4 = Equilateral([Point(0, 0), Point(3, 0), Point(1.5, 2.598)], None)
    print("Triángulo Equilátero")
    print("Perímetro:", t4._perimeter)
    print("Ángulos internos:", t4._inner_angles)
    print("Vértices:", t4._vertices)
    print("Lados:", t4._edges)
    print("¿Es regular?:", t4.is_regular)
    print("\n")

    r1 = Rectangle(False, [Point(0, 0), Point(3, 0), Point(3, 4), Point(0, 4)], None)
    print("Rectángulo")
    print("Área:", r1._area)
    print("Perímetro:", r1._perimeter)
    print("Ángulos internos:", r1._inner_angles)
    print("Vértices:", r1._vertices)
    print("Lados:", r1._edges)
    print("¿Es regular?:", r1.is_regular)
    print("\n")

    s1 = Square([Point(0, 0), Point(3, 0), Point(3, 3), Point(0, 3)], None)
    print("Cuadrado")
    print("Área:", s1._area)
    print("Perímetro:", s1._perimeter)
    print("Ángulos internos:", s1._inner_angles)
    print("Vértices:", s1._vertices)
    print("Lados:", s1._edges)
    print("¿Es regular?:", s1.is_regular)
    print("\n")
```
output:
```
Triángulo Rectángulo
Área: 6.0
Perímetro: 12.0
Ángulos internos: [36.87, 90.0, 53.13]
Vértices: [Point(0, 0), Point(3, 0), Point(0, 4)]
Lados: [Line(Point(0, 0), Point(3, 0)), Line(Point(3, 0), Point(0, 4)), Line(Point(0, 4), Point(0, 0))]
¿Es regular?: False


Triángulo Escaleno
Área: 6.000000000000003
Perímetro: 11.595241580617241
Ángulos internos: [40.6, 75.96, 63.43]
Vértices: [Point(0, 0), Point(3, 0), Point(1, 4)]
Lados: [Line(Point(0, 0), Point(3, 0)), Line(Point(3, 0), Point(1, 4)), Line(Point(1, 4), Point(0, 0))]
¿Es regular?: False


Triángulo Isósceles
Área: 5.999999999999999
Perímetro: 11.54400374531753
Ángulos internos: [41.11, 69.44, 69.44]
Vértices: [Point(0, 0), Point(3, 0), Point(1.5, 4)]
Lados: [Line(Point(0, 0), Point(3, 0)), Line(Point(3, 0), Point(1.5, 4)), Line(Point(1.5, 4), Point(0, 0))]
¿Es regular?: False


Triángulo Equilátero
Perímetro: 8.999867998547968
Ángulos internos: [60.0, 60.0, 60.0]
Vértices: [Point(0, 0), Point(3, 0), Point(1.5, 2.598)]
Lados: [Line(Point(0, 0), Point(3, 0)), Line(Point(3, 0), Point(1.5, 2.598)), Line(Point(1.5, 2.598), Point(0, 0))]
¿Es regular?: True


Rectángulo
Área: 12.0
Perímetro: 14.0
Ángulos internos: [90, 90, 90, 90]
Vértices: [Point(0, 0), Point(3, 0), Point(3, 4), Point(0, 4)]
Lados: [Line(Point(0, 0), Point(3, 0)), Line(Point(3, 0), Point(3, 4)), Line(Point(3, 4), Point(0, 4)), Line(Point(0, 4), Point(0, 0))]
¿Es regular?: False


Cuadrado
Área: 9.0
Perímetro: 12.0
Ángulos internos: [90, 90, 90, 90]
Vértices: [Point(0, 0), Point(3, 0), Point(3, 3), Point(0, 3)]
Lados: [Line(Point(0, 0), Point(3, 0)), Line(Point(3, 0), Point(3, 3)), Line(Point(3, 3), Point(0, 3)), Line(Point(0, 3), Point(0, 0))]
¿Es regular?: True
```
Ejercicio Restaurant revisited

```python
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
```
Output: (se omite el print de los atributos privados ya que genera error al ser encapsulados de esta manera)
```
Order
-------------------
Appetizer: Empanadas, Price: 3.5
Appetizer: Cheese Sticks, Price: 4.0
Appetizer: Mini Burgers, Price: 5.0
Appetizer: Mini Waffles, Price: 2.5
Appetizer: Salchipapa, Price: 5.0
Main Course: Baby Beef, Price: 10.0, Protein: Beef, Grains: Rice, Vegetables: Salad
Main Course: Cordon Blue, Price: 12.0, Protein: Chicken, Grains: Potatoes, Vegetables: Salad
Main Course: Salmon, Price: 15.0, Protein: Fish, Grains: Quinoa, Vegetables: Lettuce
Main Course: Burger, Price: 8.0, Protein: Beef, Grains: Bread, Vegetables: Onion
Beverage: Coca Cola, Price: 2.0, Size: Medium, Type: Soda
Beverage: Orange Juice, Price: 3.0, Size: Large, Type: Juice
Beverage: Quatro, Price: 2.5, Size: Small, Type: Soda
Beverage: Chocolate Milkshake, Price: 4.0, Size: Large, Type: Milkshake
Dessert: Chocolate Cake, Price: 5.0
Dessert: Nutella Waffles, Price: 6.0
Dessert: Flan, Price: 4.0
Dessert: Lemon Cheesecake, Price: 5.0
-------------------
Beverages: 4
-------------------
Beverages Price: 11.5
-------------------
Appetizers: 5
-------------------
Appetizers Price: 20.0
-------------------
Main Courses: 4
-------------------
Main Courses Price: 45.0
-------------------
Desserts: 4
-------------------
Desserts Price: 20.0
-------------------
Total Items: 17
-------------------
Total Price: 96.5
-------------------
Overall Discount: 11.0%
-------------------
Net Total: 80.77
-------------------
Paid 80.77 using card ************3456
Not enough cash provided. Amount due: 30.77
9876-5432-1098-7654
456
```





