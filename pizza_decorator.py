from abc import ABC, abstractmethod

class Pizza(ABC):
    @abstractmethod
    def get_description(self) -> str:
        pass

    @abstractmethod
    def get_cost(self) -> float:
        pass

class PizzaBase():
    def get_description(self) -> str:
        return "Pizza Simples"

    def get_cost(self) -> float:
        return 30.00

class PizzaDecorator(Pizza):
    def __init__(self, pizza: Pizza):
        self.decorated_pizza = pizza

    def get_description(self) -> str:
        return self.decorated_pizza.get_description()

    def get_cost(self) -> float:
        return self.decorated_pizza.get_cost()

class Queijo(PizzaDecorator):
    def get_description(self) -> str:
        return f"{self.decorated_pizza.get_description()}, Queijo"

    def get_cost(self) -> float:
        return self.decorated_pizza.get_cost() + 2.50

class Calabresa(PizzaDecorator):
    def get_description(self) -> str:
        return f"{self.decorated_pizza.get_description()}, Calabresa"

    def get_cost(self) -> float:
        return self.decorated_pizza.get_cost() + 6.00

class Frango(PizzaDecorator):
    def get_description(self) -> str:
        return f"{self.decorated_pizza.get_description()}, Frango"

    def get_cost(self) -> float:
        return self.decorated_pizza.get_cost() + 5.50

class CarneSeca(PizzaDecorator):
    def get_description(self) -> str:
        return f"{self.decorated_pizza.get_description()}, Carne Seca"

    def get_cost(self) -> float:
        return self.decorated_pizza.get_cost() + 6.50

class Catupiry(PizzaDecorator):
    def get_description(self) -> str:
        return f"{self.decorated_pizza.get_description()}, Catupiry"

    def get_cost(self) -> float:
        return self.decorated_pizza.get_cost() + 3.50

class Azeitona(PizzaDecorator):
    def get_description(self) -> str:
        return f"{self.decorated_pizza.get_description()}, Azeitona"

    def get_cost(self) -> float:
        return self.decorated_pizza.get_cost() + 2.00

class BordaCatupiry(PizzaDecorator):
    def get_description(self) -> str:
        return f"{self.decorated_pizza.get_description()}, Borda de Catupiry"

    def get_cost(self) -> float:
        return self.decorated_pizza.get_cost() + 4.25

class BordaCheddar(PizzaDecorator):
    def get_description(self) -> str:
        return f"{self.decorated_pizza.get_description()}, Borda de Cheddar"

    def get_cost(self) -> float:
        return self.decorated_pizza.get_cost() + 4.25

class BordaChocolate(PizzaDecorator):
    def get_description(self) -> str:
        return f"{self.decorated_pizza.get_description()}, Borda de Chocolate"

    def get_cost(self) -> float:
        return self.decorated_pizza.get_cost() + 6.25
