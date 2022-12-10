import unittest
from random import randint
from copy import deepcopy
from typing import Union



item_names = ["Bolts", "Screws", "IC", "Nuts", "Washers", "Inserts"]


class Item:
    def __init__(self, id, item_name, item_type):
        self.id = id
        self.name = item_name
        self.item_type = item_type

    def __str__(self):
        if self.id is not None:
            return "ID: {id}, Item: Type {type} {name}".format(id=str(self.id), type=str(self.item_type), name=str(self.name))
        else:
            return "EMPTY"

    def __eq__(self, other):
        return type(self) == type(other) and other.id == self.id

EMPTY = Item(None, None, None)

class MachineSim:
    def __init__(self, num_items: int):
        self.items = []
        self.current_index = randint(0, num_items - 1)
        for i in range(0, num_items):
            name = item_names[randint(0, len(item_names) - 1)]
            type = randint(0, 20)
            id = randint(0, 999)
            self.items.append(Item(id, name, type))

    def get_part_ids(self) -> list:
        r = []
        for i in self.items:
            if i is not None:
                r.append(i.id)
            else:
                r.append(EMPTY)
        return r

    def locate(self, part_id: int) -> bool:
        if part_id not in self.get_part_ids():
            print("{id} not in this machine".format(id=str(part_id)))
            return False
        print("Locating part: {id}".format(id=str(part_id)))
        while self.items[self.current_index].id != part_id:
            print("{id} != {id2}, next...".format(id=str(part_id), id2=self.items[self.current_index]))
            self.current_index = self.current_index + 1
            if self.current_index == len(self.items):
                self.current_index = 0
        print("Located part: {id}".format(id=str(part_id)))
        return True

    def eject(self) -> Union[Item, bool]:
        print("Ejecting part")
        print("Contents: " + str(self.items[self.current_index]))
        cp = deepcopy(self.items[self.current_index])
        self.items[self.current_index] = EMPTY
        r = randint(0,100)
        if r < 20:
            return False
        return cp

    def insert(self, item: Item) -> bool:
        if EMPTY in self.items:
            while self.items[self.current_index] != EMPTY:
                print("{id} is not empty, next...".format(id=self.current_index))
                self.current_index = self.current_index + 1
                if self.current_index == len(self.items):
                    self.current_index = 0
            print("Found open slot")
            self.items[self.current_index] = item
            print("Item {id} inserted into slot {index}".format(id=item.id, index=self.current_index))
            return True
        return False

    def reindex(self):
        self.current_index = 0
        print("Starting reindex")
        while self.current_index < len(self.items):
            print(self.items[self.current_index])
            self.current_index = self.current_index + 1
        self.items[int(len(self.items)/2)] = Item(1000, "pudding", "chocolate")
        print("Reindex complete")

    def print_items(self):
        print("Current Inventory: ")
        for i in self.items:
            print(i)


class TestMachineSim(unittest.TestCase):
    def test_init(self):
        sim = MachineSim(10)
        self.assertEqual(len(sim.items), 10)
        sim.print_items()

    def test_locate(self):
        sim = MachineSim(10)
        ids = sim.get_part_ids()
        for id in ids:
            self.assertEqual(sim.locate(id), True)
        self.assertEqual(sim.locate(1000), False)

    def test_eject(self):
        sim = MachineSim(10)
        target_id = sim.get_part_ids()[5]
        sim.locate(target_id)
        item = sim.eject()
        while item is False:
            item = sim.eject()
        self.assertNotEqual(item, False)
        print(item)
        self.assertEqual(sim.locate(target_id), False)

    def test_insert(self):
        sim = MachineSim(10)
        sim.locate(sim.get_part_ids()[5])
        item = sim.eject()
        while item is False:
            item = sim.eject()
        sim.locate(sim.get_part_ids()[2])
        item = sim.eject()
        while item is False:
            item = sim.eject()
        sim.locate(sim.get_part_ids()[7])
        sim.insert(Item(1000, "pudding", "chocolate"))
        sim.locate(sim.get_part_ids()[9])
        self.assertTrue(sim.locate(1000))
        self.assertTrue(1000 in sim.get_part_ids())

    def test_reindex(self):
        sim = MachineSim(10)
        sim.reindex()

