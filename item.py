import random
import itertools
from datetime import datetime, timedelta

class Item:
    _id_count = 1 #начальное значение id предмета

# Переопределение метода __init__ и создание предмета
    def __init__(self, name, description, dispatch_time, tags=None, cost=0):
        self._id = Item._id_count
        Item._id_count += 1
        self.name = name
        self.description = description
        def random_dispatch_time():
            start_date = datetime(day=1, month=1, year=2025)
            end_date = datetime(day=1, month=1, year=2026)
            delta_days = (end_date - start_date).days
            random_days = random.randint(0, delta_days - 1)
            random_date = start_date + timedelta(days=random_days)
            return random_date.strftime("%Y.%m.%d")
        self.dispatch_time = random_dispatch_time()
        self._tags = set(tags) if tags else set()
        self._cost = cost

# Переопределение метода __str__ и вывод информации о предмете
    def __str__(self):
        return (f" Item(id={self._id}, name={self.name}, desc={self.description}, cost={self._cost}, "
                f"dispatch_time={self.dispatch_time}, tags={self._tags})")

# Переопределение метода __repr__ и вывод первых 3 тегов на экран
    def __repr__(self):
        tags_list = list(self._tags)
        first_tags = tags_list[:3]
        tags_str = ', '.join(first_tags)
        return (f"<Item id={self._id}, name={self.name}, desc={self.description}, cost={self._cost} "
            f"dispatch_time={self.dispatch_time}, tags=[{tags_str}]>")

# Переопределение метода __len__ и вывод количества тегов предмета
    def __len__(self):
        return len(self._tags)

#Переопределение метода __iter__ и итерация по тегам
    def __iter__(self):
        return iter(self._tags)

    def __lt__(self, other):
        if not isinstance(other, Item):
            return NotImplemented
        return self.cost < other.cost
#________________________________________________________________

    def add_tag(self, tag):
        if isinstance(tag, str) and tag.strip():
            self._tags.add(tag)

    def remove_tag(self, tag):
        self._tags.discard(tag)

    def add_tags(self, tags):
        self._tags.update(tags)

    def rm_tags(self, tags):
        self._tags.difference_update(tags)

    def is_tagged(self, tags):
        if isinstance(tags, str):
            return tags in self._tags
        else:
            return all(tag in self._tags for tag in tags)

    def set_cost(self, cost):
        self._cost = cost


    def copy(self):
        return Item(
            name=self.name,
            description=self.description,
            dispatch_time=self.dispatch_time,
            tags=self._tags.copy(),
            cost=self._cost
        )

    def random_item_gen(min_cost, max_cost):

        count = 1

        names = [
            "Processor",
            "CPU",
            "DDR",
            "HDD",
            "SSD",
            "Case",
            "Mouse",
            "Keyboard",
            "Monitor",
            "Audiocard",
            "Lamp",
            "Phone",
            "Laptop",
        ]

        computer_tags = [
            "CPU",
            "GPU",
            "RAM",
            "SSD",
            "HDD",
            "Motherboard",
            "Power Supply",
            "Cooling",
            "Gaming",
            "Overclocking",
            "RGB",
            "Wireless",
            "Bluetooth",
            "USB-C",
            "Mechanical Keyboard",
            "Monitor",
            "4K",
            "VR Ready",
            "Laptop",
            "Desktop",
            "Networking",
            "Ethernet",
            "Wi-Fi 6",
            "Thunderbolt",
            "Portable",
            "High Performance",
            "Silent",
            "Compact",
            "Water Cooling",
            "Fan",
            "Case",
            "Peripheral",
            "Audio",
            "Headset",
            "Microphone",
            "Webcam"
        ]

        def random_tags(tags_list):
            count = random.randint(2, 5)
            return random.sample(tags_list, count)

        descriptions = [
            "High quality item",
            "Limited edition",
            "Best seller",
            "New arrival",
            "Discounted product",
            "Exclusive offer"
        ]

        def random_dispatch_time_2025():
            start_date = datetime(day=1, month=1, year=2025)
            end_date = datetime(day=1, month=1, year=2026)
            delta_days = (end_date - start_date).days
            random_days = random.randint(0, delta_days - 1)
            random_date = start_date + timedelta(days=random_days)
            return random_date.strftime("%Y.%m.%d")

        while True:
            cost = random.randint(min_cost, max_cost)
            name = random.choice(names) + str(count)
            description = random.choice(descriptions)
            dispatch_time = random_dispatch_time_2025()
            tags = random_tags(computer_tags)
            yield Item(name=name, description=description, dispatch_time=dispatch_time, tags=tags, cost=cost)
            count += 1

    @property
    def cost(self):
        return self._cost




