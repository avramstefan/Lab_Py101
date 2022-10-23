import product

class Phone(product.Product):
    def __init__(self, name, price, ram, cpu):
        product.Product.__init__(self, name, price)
        self.ram = ram
        self.cpu = cpu

    def __str__(self):
        """
        TODO:
            * supraincarca metoda str

        Returns:
            * str:    un string ce va contine informatiile 
                      specifice telefonului (nume, CPU, RAM)

        """
        return "The new {} is an unforgettable experience, CPU {}, RAM {}.".format(self.name, self.cpu, self.ram)