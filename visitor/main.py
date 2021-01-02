class Equipment:
    """Taken from Composite tutorial. Added accept method."""
    def __init__(self, name):
        self._name = name

    def name(self):
        return self._name

    def price(self):
        raise NotImplementedError

    def accept(self, equipment_visitor):
        pass


class EquipmentVisitor:
    """Abstract class for all visitors of equipment."""
    def __init__(self):
        pass

    def visit_floppy_disk(self, floppy_disk):
        pass

    def visit_card(self, card):
        pass

    def visit_chassis(self, chassis):
        pass


class FloppyDisk(Equipment):
    """Leaf node in Composite."""
    def price(self):
        return 100

    def accept(self, equipment_visitor):
        equipment_visitor.visit_floppy_disk(floppy_disk=self)


class Card(Equipment):
    """Another leaf node in Composite."""
    def price(self):
        return 200

    def discount_price(self):
        return 180

    def accept(self, equipment_visitor):
        equipment_visitor.visit_card(card=self)


class Chassis(Equipment):
    """Composite of equipment."""
    def __init__(self, name):
        self._components = []
        super().__init__(name)

    def add(self, equipment):
        self._components.append(equipment)

    def price(self):
        return 40

    def accept(self, equipment_visitor):
        for component in self._components:
            component.accept(equipment_visitor)

        equipment_visitor.visit_chassis(chassis=self)


class PricingVisitor(EquipmentVisitor):
    """Simple price calculator."""
    def __init__(self):
        self._total_price = 0
        super().__init__()

    def visit_floppy_disk(self, floppy_disk):
        self._total_price += floppy_disk.price()

    def visit_card(self, card):
        # you can set discount policy for each component as you wish
        self._total_price += card.discount_price()

    def visit_chassis(self, chassis):
        self._total_price += chassis.price()

    def get_total_price(self):
        return self._total_price


class InventoryVisitor(EquipmentVisitor):
    def __init__(self):
        self._inventory = {}
        super().__init__()

    def visit_floppy_disk(self, floppy_disk):
        try:
            self._inventory['floppy'] += 1
        except KeyError:
            self._inventory['floppy'] = 1

    def visit_card(self, card):
        try:
            self._inventory['card'] += 1
        except KeyError:
            self._inventory['card'] = 1

    def visit_chassis(self, chassis):
        try:
            self._inventory['chassis'] += 1
        except KeyError:
            self._inventory['chassis'] = 1

    def get_inventory(self):
        return self._inventory


if __name__ == "__main__":
    chassis = Chassis('Chassis')
    f1 = FloppyDisk('Floppy disk 1')
    chassis.add(f1)

    f2 = FloppyDisk('Floppy disk 2')
    chassis.add(f2)

    card = Card('Motherboard')
    chassis.add(card)

    price_visitor = PricingVisitor()
    chassis.accept(price_visitor)
    print('Chassis price', price_visitor.get_total_price())

    inventory_visitor = InventoryVisitor()
    chassis.accept(inventory_visitor)
    print('Chassis inventory', inventory_visitor.get_inventory())
