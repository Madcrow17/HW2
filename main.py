import unittest
import datetime




from hub import Hub
from item import Item



# Проверка класса Hub
class TestHub(unittest.TestCase):
    def test_01_hub_singleton(self):
        'Проверка того что hub - синглтон'
        hub1 = Hub()
        hub2 = Hub()
        print(hub1)
        self.assertTrue(Hub() is Hub())

    def test_02_len(self):
        'Проверка того что при добавлении предметов меняется значение len(item)'
        h = Hub()
        for i in range(5):

            item = Item(
                name=f"Предмет № {i+1}",
                description=f"Описание для предмета {i+1}",
                dispatch_time=datetime.datetime.now(),
                tags=[f"Тег{i+1}"])

            h.add_item(item)
            print(f"---\nItem {Item._id_count - 1}: {item!r}\n Всего предметов на складе: {len(h)}\n---")
        self.assertEqual(len(h), 5)

    def test_03_rm_item(self):
        h = Hub()
        item = Item(name="Motherboard", description="PC part", dispatch_time="01.01.2025", tags=[""])
        h.add_item(item)
        print('\n', str(h))
        h.rm_item(2)
        print('\n', str(h))


    def test_04_drop_items(self):
        h = Hub()
        item1 = Item(name="Motherboard", description="PC part", dispatch_time="01.01.2025", tags=[""])
        h.add_item(item1)
        item2 = Item(name="GPU", description="PC part", dispatch_time="01.01.2025", tags=[""])
        h.add_item(item2)
        item3 = Item(name="Processor", description="PC part", dispatch_time="01.01.2025", tags=[""])
        h.add_item(item3)
        print('\n', str(h))
        h.drop_items([item2, item3])
        print('\n', str(h))

    def test_05_clear_items(self):
        h = Hub()
        print('\n', str(h))
        h.clear()
        print('\n', "Пустой список предметов: ", str(h))

    def test_06_date(self):
        h = Hub()
        print('\n', h.get_date())
        h.set_date("12.12.2012")
        print('\n', h.get_date())

    def test_07_add_item(self):
        h = Hub()
        item1 = Item(name="Motherboard", description="PC part", dispatch_time="01.01.2025", tags=[""])
        h.add_item(item1)  # работает
        h.add_item("not an item")  # вызовет TypeError

    def test_08_most_value(self):
        h = Hub()
        item1 = Item(name="Motherboard", description="PC part", dispatch_time="01.01.2025", tags=[""], cost=10)
        h.add_item(item1)
        item2 = Item(name="GPU", description="PC part", dispatch_time="01.01.2025", tags=[""], cost=20)
        h.add_item(item2)
        item3 = Item(name="Processor", description="PC part", dispatch_time="01.01.2025", tags=[""], cost=15)
        h.add_item(item3)



        print('\n', h.find_most_valuable()) #Вернет 1 предмет тк начальное значение amount=1
        print('\n', h.find_most_valuable(2)) #Вернет 2 предмета
        print('\n', h.find_most_valuable(10)) #Вернет все предметы тк на складе предметов меньше 10


    def test_09_final_hub_test(self):
        h = Hub()
        h.clear()
        item1 = Item(name="Motherboard", description="PC part", dispatch_time="01.01.2025", tags=[""], cost=60)
        h.add_item(item1)
        item2 = Item(name="GPU", description="Nvidia", dispatch_time="01.01.2025", tags=[""], cost=200)
        h.add_item(item2)
        item3 = Item(name="Processor", description="Intel Core", dispatch_time="01.01.2025", tags=[""], cost=70)
        h.add_item(item3)
        item4 = Item(name="SSD", description="Disk M.2", dispatch_time="01.01.2025", tags=[""], cost=40)
        h.add_item(item4)
        item5 = Item(name="HDD", description="Disk 3.5", dispatch_time="01.01.2025", tags=[""], cost=20)
        h.add_item(item5)
        item6 = Item(name="alarm", description="clock", dispatch_time="01.01.2023", tags=[""], cost=10)
        h.add_item(item6)
        item7 = Item(name="Artifact", description="lamp", dispatch_time="01.01.2024", tags=[""], cost=120)
        h.add_item(item7)
        item8 = Item(name="HDD", description="Disk 3.5", dispatch_time="01.01.2025", tags=[""], cost=5)
        h.add_item(item8)
        item9 = Item(name="M.2", description="Disk 3.5", dispatch_time="01.01.2025", tags=[""], cost=12)
        h.add_item(item9)
        item10 = Item(name="SSD", description="Disk 3.5", dispatch_time="01.01.2025", tags=[""], cost=250)
        h.add_item(item10)
        item11 = Item(name="Mouse", description="Disk 3.5", dispatch_time="01.01.2025", tags=[""], cost=300)
        h.add_item(item11)
        item12 = Item(name="HDD", description="Disk 3.5", dispatch_time="01.01.2012", tags=[""], cost=25)
        h.add_item(item12)
        item13 = Item(name="HDD", description="Disk 3.5", dispatch_time="01.01.2011", tags=[""], cost=11)
        h.add_item(item13)
        item14 = Item(name="HDD", description="Disk 3.5", dispatch_time="01.01.2015", tags=[""], cost=15)
        h.add_item(item14)
        item15 = Item(name="HDD", description="Disk 3.5", dispatch_time="01.01.2015", tags=[""], cost=15)
        h.add_item(item15)

        print(f"--- \n{str(h)} ---")
        print("\n", "Дата создания Hub:", "\n", )
        print( h.get_date())

        outdated = h.remove_itesm_by_date()
        print("\n", "Позиции с датой создания раньше даты хаба:", "\n", )
        for item in outdated:
            print(item)
        print("\n","Оставшиеся позиции:","\n",str(h))

        removed_with_a = h.remove_items_with_a()
        print("\n", "Удаленные позиции:", "\n", )
        for item in removed_with_a:
            print(item)
        print("\n","Оставшиеся позиции:","\n",str(h))

        most_valuable_10_items = h.drop_most_valuable_10()
        print("\n", "10 Самых дорогих:", "\n", )
        for item in most_valuable_10_items:
            print(item)
        others = str(h)
        print("\n", "Оставшиеся позиции:", "\n", others)

        # Генерация случайных позиций в хабе
        generate_items = Item.random_item_gen(50, 100)
        print("\n","Новые позиции:","\n")
        for i in range(10):
            item = next(generate_items)
            print(item)


# Проверка класса Item
class TestItem(unittest.TestCase):

    def test_01_item_id(self):
        h = Hub()
        'Проверка того что у разных Items разные id'
        item1 = Item("TV", "Samsung Qled", "01.07.2025")
        h.add_item(item1)
        item2 = Item("PC", "MSI", "01.07.2025")
        h.add_item(item2)
        item3 = Item("Notebook", "Dell Inspirion", "01.07.2025")
        h.add_item(item3)
        item4 = Item("Monitor", "MSI", "01.07.2025")
        h.add_item(item4)
        item5 = Item("Mouse", "HyperX", "01.07.2025")
        h.add_item(item5)
        ids = {item1._id, item2._id, item3._id, item4._id, item5._id}
        self.assertEqual(len(ids), 5, "ID должны быть уникальными у разных объектов Item")
        print(f"---\nItem {item1._id}: {item1}\nItem {item2._id}: {item2}\nItem {item3._id}: {item3}\nItem {item4._id}: {item4}\nItem {item5._id}: {item5}\n---")

    def test_02_len(self):
        h = Hub()
        'Проверка того что при добавлении тэгов меняется значение len(item)'
        item = Item("Keyboard", "Gigabyte", "01.07.2025")
        h.add_item(item)
        initial_len = len(item)
        print(f"---\nЗначение до добавления тегов: {len(item)}\n---")

        item.add_tag('mechanical')
        assert len(item) == initial_len + 1

        item.add_tag('RGB Strip')
        assert len(item) == initial_len + 2

        item.add_tag('Wireless')
        assert len(item) == initial_len + 3

        print(f"---\nItem {item._id}: {item}\n---")
        print(f"---\nЗначение после добавления тегов: {len(item)}\n---")

    def test_03_equal_tags(self):
        'Проверка того что если к предмету добавить два идентичных тега - их колчество будет один'
        h = Hub()
        item = Item("Camera", "Sony FX-3", "01.07.2025")
        h.add_item(item)
        item.add_tag("FullHD")
        item.add_tag("FullHD")  # добавляем тот же тег второй раз
        print(f"---\nItem {item._id}: {item}\n---")
        self.assertEqual(len(item), 1)
        print("Количество тегов у предмета:", len(item._tags))

    def test_04_get_item(self):
        'Проверка получения предмета по id'
        h = Hub()

        print(f"---\nПредмет с id=3:\n {h[2]}\n---")
        print(f"---\nПредмет с id=4:\n {h[3]}\n---")
        print(f"---\nПредмет с id=1:\n {h[0]}\n---")
        print(f"---\nПредмет с id=11:\n {h[11]}\n---")


    def test_05_find_tags(self):
        h = Hub()

        item1 = Item("TV", "Samsung Qled", "01.07.2025", ['OLED', '16:9', 'big', '75', 'another'])
        h.add_item(item1)
        item2 = Item("PC", "MSI", "01.07.2025", ['core i5', 'RTX', 'big', '1200W'])
        h.add_item(item2)
        item3 = Item("Notebook", "Dell Inspirion", "01.07.2025", ['laptop', '14', 'keyboard', 'another'])
        h.add_item(item3)
        item4 = Item("Monitor", "MSI", "01.07.2025", ['32', 'ips', 'curved', 'small'])
        h.add_item(item4)
        item5 = Item("Mouse", "HyperX", "01.07.2025", ['Gaming', 'Wireless', 'white', 'another'])
        h.add_item(item5)
        #print(str(h))
        found_items = h.find_by_tags(["Wireless", "another"])
        for item in found_items:
            print('\n'f"{item.name} с тегами {list(item._tags)}")

        found_items = h.find_by_tags(["big"])
        for item in found_items:
            print('\n'f"{item.name} с тегами {list(item._tags)}")


    def test_06_find_by_id(self):
        h = Hub()
        pos, found_item = h.find_by_id(1)
        if found_item:
            print('\n'f"Найден объект: ID={found_item._id} : {found_item.name}, {found_item.description}")
        else:
            print("Объект не найден.")

        pos, found_item = h.find_by_id(11)
        if found_item:
            print('\n'f"Найден объект: ID={found_item._id} : {found_item.name}, {found_item.description}")
        else:
            print("Объект не найден.")

        #print('\n', str(h))

    def test_07_set_cost_get_cost(self):
        h = Hub()
        item = Item("Camera", "Sony FX-3", "01.07.2025", "", 10)
        print('\n',"Цена позиции", item._id, item.name, ':', item.cost)
        item.set_cost(500)
        print('\n', "Цена позиции", item._id, item.name, ':', item.cost)

    def test_08_lt(self):
        h = Hub()
        item1 = Item("TV", "Sony", "01.09.2025", "", 1000)
        item2 = Item("PC", "Intel", "01.10.2025", "", 2000)
        print('\n', item1 < item2, "Товар", item2.name, "стоит дороже, чем ", item1.name, "т.к", item2.cost, ">", item1.cost)
        print('\n', item2 < item1, "Товар", item1.name, "НЕ стоит дороже, чем ", item2.name, "т.к", item1.cost, "НЕ >", item2.cost)

    def test_09_many_tags(self):
        h = Hub()
        item1 = Item("Projector", "ViewSonic", "01.09.2025", tags=["LCD", "4K", "16:9"], cost=1500)
        print('\n', item1)
        item1.add_tags(["white", "kronshtain"])
        print('\n', item1)
        item1.rm_tags(["4K", "16:9"])
        print('\n', item1)

    def test_10_tagged(self):
        h = Hub()
        item = Item("Phone", "Apple", "01.08.2025", tags=["16 Pro", "iphone", "white"], cost=10000)
        print('\n', item.is_tagged("16 Pro")) #вернет True т.к. тег есть у предмета
        print('\n', item.is_tagged(["16 Pro", "iphone"])) #вернет True т.к. все теги есть у предмета, передаем строку
        print('\n', item.is_tagged(["16 Pro", "samsung"])) #вернет False т.к. одного из тегов нет у предмета,  передаем строку

    def test_11_copy(self):
        h = Hub()
        item1 = Item("TelePhone", "Samsung", "21.08.2025_18:00", tags=["S24", "6.7 inches", "green"], cost=50000)
        item2 = item1.copy()

        print('\n',item1)
        print('\n',item2)


class TestFindByDate(unittest.TestCase):

    def test_01_set_list_of_items(self):
        gen = Item.random_item_gen(100, 1000)
        for i in range(15):
            item = next(gen)
            print('\n',item)


    def test_02_range_date(self):
        h = Hub()
        results1 = h.find_by_date("2025.01.01", "2025.04.10")
        print('\n', "Печать всех Итемов, оторые попадают в промежуток: ", '\n', results1)
        dates_in_result1 = {item.dispatch_time for item in results1}
        print('\n', "Только даты выдачи промежутка дат: ", dates_in_result1)

    def test_03_one_date(self):
        h = Hub()
        # Печать результатов в конкретную дату если есть
        results2 = h.find_by_date("2025.03.15")
        print('\n', "Печать результатов в конкретную дату если есть: ", '\n', results2)
        dates_in_result2 = {item.dispatch_time for item in results2}
        print('\n', "Только даты выдачи конкретной даты: ", dates_in_result2)

    def test_04_empty_res(self):
        h = Hub()
        #Заведомо пустой результат
        results3 = h.find_by_date("2033.05.02", "2035.07.15")
        print('\n', "Заведомо пустой результат: ", results3)

    def test_05_too_many_args(self):
        h = Hub()
        # Ошибка - более 2х аргументов
        results3 = h.find_by_date("01.01.2027", "10.01.2028", "10.01.2029")
        print(results3)

    def test_06_no_args(self):
        h = Hub()
        # Ошибка - более 2х аргументов
        results4 = h.find_by_date()
        print(results4)




# TESTS FOR HOMEWORK # 3 (DECORATORS)


from decorators import even
from decorators import clip
from decorators import repeat
from decorators import cash
import random


class TestDecorators(unittest.TestCase):

    #Test of @even decorator
    def test_12_even(self):
        @even
        def even_test(a, b):
            return (a, b)

        result1 = even_test(1, b=2)
        print('\n', "Result: ", result1)
        self.assertEqual(None, result1)

        result2 = even_test(1, b=2)
        print('\n', "Result: ", result2)
        self.assertEqual((1, 2), result2)



    #Test of @clip decorator
    def test_13_clip(self):
        @clip
        def clip_test(a=1, b=2, c='~', d=4):
            return (a, b, c, d)

        result = clip_test(2, 3, c=4, d=5)
        print('\n', "Result: ", result) # 2, 3 , '~', 4

        self.assertEqual((2, 3, '~',4), result)

    # Test of @repeat decorator
    def test_14_repeat(self):
        @repeat(4)
        def repeat_test(a, b):
            print("Executed! with args:", (a, b))

        print('\n',"Need to execute 4 times")
        repeat_test(1, b=2)

        @repeat(10)
        def random_sum(n):
            print(sum(random.random() for i in range(n)))
        random_sum(1000000)


    # Test of @cash decorator
    def test_15_cash(self):
        exec_count = 0
        @cash
        def cash_test(a, b):
            nonlocal exec_count
            exec_count += 1
            return (a, b)

        self.assertEqual((1, 2), cash_test(1, b=2))
        self.assertEqual((1, 2), cash_test(1, b=2))
        self.assertEqual(1, exec_count)
        self.assertEqual((3, 2), cash_test(3, b=2))
        self.assertEqual((3, 2), cash_test(3, b=2))
        self.assertEqual(2, exec_count)
        self.assertEqual((1, 3), cash_test(1, b=3))
        self.assertEqual((1, 3), cash_test(1, b=3))
        self.assertEqual(3, exec_count)


        @cash
        def fib(x):
            print('\n', f"вызвана фунция Фибоначчи f({x})")
            if x < 2:
                return 1
            else:
                return fib(x-1) + fib(x-2)

        fib(10) # вызовет все функции Фибоначчи
        print(fib(10)) # выдаст только результат от 10



