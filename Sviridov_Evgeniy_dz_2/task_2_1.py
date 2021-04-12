class ItemDiscount:
    def __init__(self, name, cost):
        self.__name = name
        self.__cost = cost

    def change_cost(self, new_cost):
        self.__cost = new_cost

    @property
    def get_name(self):
        return self.__name

    @property
    def get_cost(self):
        return self.__cost


class ItemDiscountReport(ItemDiscount):
    def get_parent_data(self):
        return f'The cost of {self.get_name} is {self.get_cost} euro.'

    def get_info(self):
        return self.get_name


class ItemDiscountSale(ItemDiscount):
    def __init__(self, sale, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sale = sale

    def __str__(self):
        new_cost = self.get_cost * (100 - self.sale) / 100
        return f'The cost of {self.get_name} is {new_cost} euro.'

    def get_info(self):
        return self.get_cost


item = ItemDiscountSale(10, 'Solt', 2)
print(ItemDiscountReport.get_parent_data(item))
print()
item.change_cost(1)
print(ItemDiscountReport.get_parent_data(item))
print(item._ItemDiscount__cost)
print(item)
print()
print(item.get_info())
print(ItemDiscountReport.get_info(item))
print(ItemDiscountSale.get_info(item))
