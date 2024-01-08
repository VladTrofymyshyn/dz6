# Базовий клас

class BaseClass:

   def __init__(self, base_attr):

       self.base_attr = base_attr

   def base_method(self):

       print("Це метод базового класу")

# Перший дочірній клас

class ChildClass1(BaseClass):

   def __init__(self, base_attr, child1_attr):

       super().__init__(base_attr)

       self.child1_attr = child1_attr

   def child1_method(self):

       print("Це метод першого дочірнього класу")

# Другий дочірній клас

class ChildClass2(BaseClass):

   def __init__(self, base_attr, child2_attr):

       super().__init__(base_attr)

       self.child2_attr = child2_attr

   def child2_method(self):

       print("Це метод другого дочірнього класу")

# Створюємо об'єкти класів

obj1 = ChildClass1("Атрибут базового класу", "Атрибут першого дочірнього класу")

obj2 = ChildClass2("Атрибут базового класу", "Атрибут другого дочірнього класу")

# Викликаємо методи та отримуємо доступ до атрибутів

obj1.base_method()  # Викликаємо метод базового класу з першого об'єкту

obj1.child1_method()  # Викликаємо метод першого дочірнього класу з першого об'єкту

print(obj1.base_attr)  # Отримуємо доступ до атрибуту базового класу з першого об'єкту

print(obj1.child1_attr)  # Отримуємо доступ до атрибуту першого дочірнього класу з першого об'єкту

obj2.base_method()  # Викликаємо метод базового класу з другого об'єкту

obj2.child2_method()  # Викликаємо метод другого дочірнього класу з другого об'єкту

print(obj2.base_attr)  # Отримуємо доступ до атрибуту базового класу з другого об'єкту

print(obj2.child2_attr)  # Отримуємо доступ до атрибуту другого дочірнього класу з другого об'єкту

