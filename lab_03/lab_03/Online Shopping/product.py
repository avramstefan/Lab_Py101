class Product:
    def __init__(self, name, price):
        """ 
        TODO:
            * completeaza constructorul clasei Product
        
        Args:
            * name (str):    numele produsului instantiat 
            * price (int):    pretul produsului instantiat

        """

        self.name = name
        self.price = price

    def __add__(self, other):
        """
        TODO:
            * completeaza supraincarcare operatorului "+"
            * va returna suma preturilor celor doua produse

        Args:
            * self (Product):    primul termen al operatiei de adunare
            * other (Product):    cel de-al doilea termen

        Return:
            * int:  suma preturilor celor doua produse
            
        """
        return self.price + other.price