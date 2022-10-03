class Product:
    def __init__(self, name, price):
        """ 
        TODO 1:
            * completeaza constructorul clasei Product
        
        Args:
            * name (str):    numele produsului instantiat 
            * price (int):    pretul produsului instantiat

        """

    def __add__(self, other):
        """
        TODO 2:
            * completeaza supraincarcare operatorului "+"
            * va returna suma preturilor celor doua produse

        Args:
            * self (Product):    primul termen al operatiei de adunare
            * other (Product):    cel de-al doilea termen

        Return:
            * int:  suma preturilor celor doua produse
            
        """