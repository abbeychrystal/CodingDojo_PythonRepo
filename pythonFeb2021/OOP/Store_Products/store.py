class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price 
        self.category = category

    def update_price(self, percent_change, is_increased):
        if is_increased == True:
            self.price += self.price * percent_change
        else:
            self.price -= self.price * percent_change
        return self
    
    def print_info(self):
        print(self.name, self.category, self.price)
        return self

class Store:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, new_product):
        self.products.append(new_product)
        return self

    def sell_product(self, id):
        products[id].print_info()
        self.products.pop[id]
        return self

    # def inflation(self, percent_increase):


#-------------------------------------------------------------------------------------
ralphs = Store("Ralph's")
apple = Product("Apple", 0.25, "Produce")
banana = Product("Banana", 0.30, "Produce")
battery = Product("Battery", 2.00, "Supplies")

ralphs.add_product(apple).add_product(banana).add_product(battery)

apple.update_price(0.02, True).print_info()
print(ralphs.products)
