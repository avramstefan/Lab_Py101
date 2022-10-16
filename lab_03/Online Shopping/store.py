import cart

class Store:
    def __init__(self, stock):
        self.stock = stock
        self.customer_carts = dict() #! de explicat in enunt: dict(customer_id, cart)

    def login(self, customer_id):
        self.customer_carts[customer_id] = cart.Cart()

    def add_to_cart(self, customer_id, product_name):
        """
        TODO:
            * adauga un produs in cart-ul unui cumparator cu id-ul dat
                - daca cumparatorul nu este logat (id-ul lui nu se gaseste
                  in lista), operatia nu se va realiza (cart-ul ramane neschimbat)
            * odata ce un produs a fost adaugat in cart, este sters din stoc
        
        Args:
            * customer_id (int):    id-ul customer-ului (fiecare
                                    customer are cate un cart)

            * product_name (str):    numele produslui ce va fi
                                     adaugat in cart    
                                        
        """ 
        if customer_id in self.customer_carts:
           for product in self.stock.view():
                if product.name == product_name:
                    self.customer_carts[customer_id].add(product)
                    self.stock.remove(product_name)
    
    def remove_from_cart(self, customer_id, product_name):
        """
        TODO:
            * sterge un produs din cart-ul cumparatorului
                - daca cumparatorul nu este logat (id-ul lui nu se gaseste
                  in lista), operatia nu se va realiza (cart-ul ramane neschimbat)
            * produsul va fi adaugat iar in stocul magazinului
        
        Args:
            * customer_id (int):    id-ul customer-ului (fiecare
                                    customer are cate un cart)

            * product_name (str):    numele produslui ce va fi
                                     scos din cart
                                
        """
        if customer_id in self.customer_carts: 
            for product in self.customer_carts[customer_id].view():
                if product.name == product_name:
                    self.customer_carts[customer_id].remove(product_name)
                    self.stock.add(product)

    def view_cart(self, customer_id):
        """
        TODO:
            * returneaza lista produselor(nume si pret) din cart
        
        Args:
            * customer_id (int):    id-ul customer-ului (fiecare
                                    customer are cate un cart)

        Return:
            * [(str, int)]:    lista de tupluri (nume_produs, pret_produs)
                               a produselor din cart

        """
        
        if customer_id in self.customer_carts:
            return [(product.name, product.price) for product in self.customer_carts[customer_id].view()]
        else:
            return []
    
    def checkout(self, customer_id):
        """
        TODO:
            * realizeaza plata produselor
        
        Args:
            * customer_id (int):    id-ul customer-ului (fiecare
                                    customer are cate un cart)

        Returns:
            * int:    pretul total al produselor din cart
        
        TIP: 
            * folositi-va de metoda cart_checkout din clasa Cart

        """
        if customer_id in self.customer_carts: 
            return self.customer_carts[customer_id].cart_checkout()
        else:
            return 0
