"""
Programming Assignment: Классы и наследование

Как правило задачи про классы носят не вычислительный характер. Обычно нужно написать классы,
которые отвечают определенным интерфейсам. Насколько удобны эти интерфейсы и как сильно связаны
классы между собой, определит легкость их использования в будущих программах.

Предположим есть данные о разных автомобилях и спецтехнике. Данные представлены в виде таблицы
с характеристиками. Обратите внимание на то, что некоторые колонки присущи только легковым автомобилям,
например, кол-во пассажирских мест. В свою очередь только у грузовых автомобилей есть длина, ширина и высота кузова.

Вам необходимо создать свою иерархию классов для данных, которые описаны в таблице.

BaseCar
Car(BaseCar)
Truck(BaseCar)
SpecMachine(BaseCar)

У любого объекта есть обязательный атрибут car_type. Он означает тип объекта и может принимать одно из
значений: car, truck, spec_machine.

Также у любого объекта из иерархии есть фото в виде имени файла — обязательный атрибут photo_file_name.

В базовом классе нужно реализовать метод get_photo_file_ext для получения расширения файла (“.png”, “.jpeg” и т.д.)
с фото. Расширение файла можно получить при помощи os.path.splitext.

Для грузового автомобиля необходимо разделить характеристики кузова на отдельные составляющие body_length,
body_width, body_height. Разделитель — латинская буква x. Характеристики кузова могут быть заданы в виде
пустой строки, в таком случае все составляющие равны 0. Обратите внимание на то, что характеристики кузова
должны быть вещественными числами.

Также для класса грузового автомобиля необходимо реализовать метод get_body_volume, возвращающий объем
кузова в метрах кубических.

Все обязательные атрибуты для объектов Car, Truck и SpecMachine перечислены в таблице ниже, где 1 - означает,
что атрибут обязателен для объекта, 0 - атрибут должен отсутствовать.

Далее необходимо реализовать функцию, на вход которой подается имя файла в формате csv. Файл содержит данные
аналогичные строкам из таблицы. Вам необходимо прочитать этот файл построчно при помощи модуля стандартной
библиотеки csv. Затем проанализировать строки и создать список нужных объектов с автомобилями и специальной
техникой. Функция должна возвращать список объектов.

Не важно как вы назовете свои классы, главное чтобы их атрибуты имели имена:
car_type
brand
passenger_seats_count
photo_file_name
body_width
body_height
body_length
carrying
extra

И методы:

get_photo_file_ext иget_body_volume

У каждого объекта из иерархии должен быть свой набор атрибутов и методов. У класса легковой автомобиль
не должно быть метода get_body_volume в отличие от класса грузового автомобиля.

Функция, которая парсит строки входного массива, должна называться get_car_list. Для проверки работы своей
реализации функции get_car_list и всех созданных классов вам необходимо использовать следующий csv-файл:
week03_02.csv

Первая строка в исходном файле — это заголовок csv, который содержит имена колонок. Нужно пропустить первую
строку из исходного файла. Обратите внимание на то, что исходный файл с данными содержит некорректные строки,
которые нужно пропустить. Если возникают исключения в процессе создания объектов из строк csv-файла, то требуется
их корректно обработать стандартным способом. Проверьте работу вашего кода с входным файлом, прежде чем
загружать задание для оценки.

Также обратите внимание, что все значения в csv файле при чтении будут python-строками. Нужно преобразовать
строку в int для passenger_seats_count, во float для carrying, а также во float для body_width body_height,
body_length.

Также ваша программа должна быть готова к тому, что в некоторых строках данные могут быть заполнены некорректно.
Например, число колонок меньше . В таком случае нужно проигнорировать подобные строки и не создавать объекты.
Строки с пустым значением для body_whl игнорироваться не должны. Вы можете использовать механизм исключений
для обработки ошибок.

Вам необходимо расширить функционал исходных классов, дополнить методы нужным кодом и реализовать функцию get_car_list.
"""

import os, csv


class CarBase:
    def __init__(self, brand, car_type, photo_file_name, carrying):
        self.brand = brand
        self.car_type = car_type
        self.carrying = float(carrying)
        self.photo_file_name = photo_file_name

    def get_photo_file_ext(self):
        get = os.path.splitext(self.photo_file_name)
        return get[1]


class Car(CarBase):
    def __init__(self, brand, car_type, photo_file_name, carrying, passenger_seats_count):
        CarBase.__init__(self, brand, car_type, photo_file_name, carrying)
        self.passenger_seats_count = int(passenger_seats_count)


class Truck(CarBase):
    def __init__(self, brand, car_type, photo_file_name, carrying, body_whl):
        CarBase.__init__(self, brand, car_type, photo_file_name, carrying)
        arr = body_whl.split('x')
        if len(arr) == 3:
            self.body_length = float(arr[0])
            self.body_width = float(arr[1])
            self.body_height = float(arr[2])
        else:
            self.body_length = float(0)
            self.body_width = float(0)
            self.body_height = float(0)

    def get_body_volume(self):
        body_volume = float(self.body_length * self.body_width * self.body_height)
        return body_volume


class SpecMachine(CarBase):
    def __init__(self, brand, car_type, photo_file_name, carrying, extra):
        CarBase.__init__(self, brand, car_type, photo_file_name, carrying)
        self.extra = extra


def get_car_list(csv_filename):
    car_list = []
    try:
        with open(csv_filename) as csv_fd:
            reader = csv.DictReader(csv_fd, delimiter=';')
            for row in reader:
                if row['car_type'] == 'car':
                    newcar = Car(brand=row['brand'],
                                 car_type=row['car_type'],
                                 photo_file_name=row['photo_file_name'],
                                 carrying=row['carrying'],
                                 passenger_seats_count=row['passenger_seats_count'])
                    car_list.append(newcar)
                elif row['car_type'] == 'truck':
                    newtruck = Truck(brand=row['brand'],
                                     car_type=row['car_type'],
                                     photo_file_name=row['photo_file_name'],
                                     carrying=row['carrying'],
                                     body_whl=row['body_whl'])
                    car_list.append(newtruck)
                elif row['car_type'] == 'spec_machine':
                    newscm = SpecMachine(brand=row['brand'],
                                         car_type=row['car_type'],
                                         photo_file_name=row['photo_file_name'],
                                         carrying=row['carrying'],
                                         extra=row['extra'])
                    car_list.append(newscm)
    except IOError:
        print('file does not exist')
    return car_list
