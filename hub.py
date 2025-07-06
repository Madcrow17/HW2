from item import Item #Импорт класса Item
import datetime #Импорт библиотеки дата



class Hub:
    _instance = None #Переменная для хранения хаба
    _initialized = False #Переменная инициализирован ли класс?

#Переопределение метода __new__ и задание параметра синглтон для класса hub
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._items = []
            cls._instance._date = kwargs.get('date', datetime.datetime.now())
        return cls._instance

# Переопределение метода __init__ и проверка есть ли такой объект
    def __init__(self, date=None, items=None):

        if not self.__class__._initialized:
            self._items = items if items else []
            self._date = datetime.datetime.now()
            self.__class__._initialized = True
            print("Hub инициализирован")

# Переопределение метода __str__ и вывод даты и количества предметов
    def __str__(self):
        return "\n".join(str(item) for item in self._items)


# Переопределение метода __repr__ и добавление в строку первых 3 предметов
    def __repr__(self):
        first_items = self._items[:3]
        items_str = ', '.join(repr(item) for item in first_items)
        return f"<Hub id={id(self)} date={self._date}, items=[{items_str}]>"

# Переопределение метода __len__ и вывод количества предметов
    def __len__(self):
        return len(self._items)

# Переопределение метода __getitem__ и получение номера предмета
    def __getitem__(self, index):
        if 0 <= index < len(self._items):
            return self._items[index]
        else:
            return None


    def __iter__(self):
        return iter(self._items)

#___________________________________________________________

    def add_item(self, item, index=None):
        if not isinstance(item, Item):
            raise TypeError(f"Ожидался объект типа Item или его наследник, а получен {type(item).__name__}")
        self._items.append(item)

    def find_by_id(self, id):
        for pos, item in enumerate(self._items):
            if item._id == id:
                return pos, item
        return -1, None

    def find_by_tags(self, tags):
        tags = set(tags)
        result = []
        for item in self._items:
            if tags.issubset(set(item)):
                result.append(item)
        return result

    def rm_item(self, i):
        if isinstance(i, int):
            for pos, item in enumerate(self._items):
                if item._id == i:
                    del self._items[pos]
                    return True
            return False

        elif isinstance(i, Item):
            try:
                self._items.remove(i)
                return True
            except ValueError:
                return False
        else:
            raise TypeError("Аргумент должен быть int (id) или Item")


    def drop_items(self, items):
        items_dropped = set(items)
        self._items = [item for item in self._items if item not in items_dropped]

    def clear(self):
        self._items.clear()

    def set_date(self, date):
        self._date = date

    def get_date(self):
        return self._date

    def find_by_date(self, *args):
        if len(args) == 0:
            raise ValueError("Должна быть передана хотя бы одна дата")
        if len(args) > 2:
            raise ValueError("Метод принимает не более двух дат")

    def find_most_valuable(self, amount=1):
        sorted_items = sorted(self._items, key=lambda item: item._cost, reverse=True)
        return sorted_items[:amount]


    def drop_most_valuable_10(self, amount=10):
        sorted_items = sorted(self._items, key=lambda item: item._cost, reverse=True)
        most_valuable_10 = sorted_items[:amount]
        self._items = [item for item in self._items if item not in most_valuable_10]
        return most_valuable_10

    def remove_items_with_a(self):
        a_letter = [item for item in self._items if item.name.lower().startswith('a')]
        self._items = [item for item in self._items if not item.name.lower().startswith('a')]
        return a_letter

    def remove_itesm_by_date(self):
        if not self._date:
            raise ValueError("В Hub отсутствует дата")

        def str_date(date_str):
            return datetime.datetime.strptime(date_str, "%d.%m.%Y").date()

        hub_date = str_date(self._date)

        Outdated = [item for item in self._items if str_date(item.dispatch_time) < hub_date]
        self._items = [item for item in self._items if str_date(item.dispatch_time) >= hub_date]

        return Outdated

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        self._date = value



