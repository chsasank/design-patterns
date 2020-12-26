class Equipment:
    """Interface for all equipment in the part-whole heirarchy."""
    def __init__(self, name):
        self._name = name

    def name(self):
        return self._name

    def price(self):
        pass


class FloppyDisk(Equipment):
    """Equipment subclass that represent leaf. Floppy in this case."""
    def price(self):
        return 100


class Card(Equipment):
    """Another leaf equipment."""
    def price(self):
        return 500


class CompositeEquipment(Equipment):
    """Baseclass for equipment that contain other equipment."""
    def __init__(self, name):
        self._equipment = []
        super().__init__(name)

    def price(self):
        return sum(equipment.price() for equipment in self)

    def add(self, equipment):
        self._equipment.append(equipment)

    def remove(self, equipment):
        self._equipment.remove(equipment)

    def __iter__(self):
        for x in self._equipment:
            yield x


class Cabinet(CompositeEquipment):
    pass

class Chassis(CompositeEquipment):
    pass

class Bus(CompositeEquipment):
    pass


if __name__ == "__main__":
    cabinet = Cabinet('PC Cabinet')
    chassis = Chassis('PC Chassis')
    cabinet.add(chassis)

    bus = Bus('MCA Bus')
    bus.add(Card('16 MBs Token Ring'))

    chassis.add(bus)
    chassis.add(FloppyDisk('3.5 in Floppy'))

    print(f'Total price is {cabinet.price()}')