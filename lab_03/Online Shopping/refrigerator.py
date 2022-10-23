import product

class Refrigerator(product.Product):
    def __init__(self, name, price, energy_label):
        product.Product.__init__(self, name, price)
        self.energy_label = energy_label

    def __str__(self):
        """
        TODO: 
            * supraincarca metoda str

        Returns:
            * str:    un string ce va contine informatiile
                      specifice frigiderului (nume, energy label)
                    
        """
    
        return "Enjoy fresh food with {}, energy label {}.".format(self.name, self.energy_label)