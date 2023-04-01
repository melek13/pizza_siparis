# Pizza Üst Sınıfı
class Pizza:
    def __init__(self, cesit, ucret):
        self.cesit = cesit
        self.ucret = ucret

    def get_cesit(self):
        return self.cesit

    def get_cost(self):
        return self.prices


# Pizza Alt Sınıfları
class KlasikPizza(Pizza):
    def __init__(self):
        cesit = f"Klasik pizza"
        prices = 120.00
        super().__init__(cesit, prices)


class MargheritaPizza(Pizza):
    def __init__(self):
        cesit = f"Margherita pizza"
        prices = 115.00
        super().__init__(cesit, prices)


class TurkPizza(Pizza):
    def __init__(self):
        cesit = f"Turk pizza"
        prices = 170, 00
        super().__init__(cesit, prices)


class JambonluPizza(Pizza):
    def __init__(self):
        cesit = f"Jambonlu pizza"
        prices = 215.00
        super().__init__(cesit, prices)


class TavukluPizza(Pizza):
    def __init__(self):
        cesit = f"Tavuklu pizza"
        prices = 155.00
        super().__init__(cesit, prices)


# Boyut Üst Sınıfı
class DecoratorSize(Pizza):
    def __init__(self, pizza, size_multiplier):
        self.pizza = pizza
        self.size_multiplier = size_multiplier
        self.prices = self.pizza.get_cost() * self.size_multiplier

    def get_cesit(self):
        return self.pizza.get_cesit()

    def get_cost(self):
        return self.prices


# Boyut Alt Sınıfları
class SmallSize(DecoratorSize):
    def __init__(self, pizza):
        super().__init__(pizza, 0.5)
        self.cesit = "Small"

    def get_cesit(self):
        return self.cesit


class MediumSize(DecoratorSize):
    def __init__(self, pizza):
        super().__init__(pizza, 1)
        self.price_multiplier = 1
        self.cesit = "Medium"

    def get_cesit(self):
        return self.cesit


class LargeSize(DecoratorSize):
    def __init__(self, pizza):
        super().__init__(pizza, 1.5)
        self.cesit = "Large"

    def get_cesit(self):
        return self.cesit


class XLargeSize(DecoratorSize):
    def __init__(self, pizza):
        super().__init__(pizza, 2)
        self.cesit = "XLarge"

    def get_cesit(self):
        return self.cesit


# Sos Üst Sınıfı
class DecoratorSos(Pizza):
    def __init__(self, pizza):
        self.pizza = pizza

    def get_cesit(self):
        return self.pizza.get_cesit()

    def get_cost(self):
        return self.pizza.get_cost()


# Sos Alt Sınıfları
class ZeytinSos(DecoratorSos):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.price = 8
        self.cesit = " Zeytin Sosu"

    def get_cesit(self):
        return self.description

    def get_cost(self):
        return self.price


class MantarSos(DecoratorSos):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.price = 12
        self.cesit = " Mantar Sosu"

    def get_cesit(self):
        return self.cesit

    def get_cost(self):
        return self.price


class KeciPeyniriSos(DecoratorSos):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.price = 20
        self.cesit = " Keçi Peyniri Sosu"

    def get_description(self):
        return self.cesit

    def get_cost(self):
        return self.price


class EtSos(DecoratorSos):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.price = 25
        self.cesit = " Et Sosu"

    def get_cesit(self):
        return self.cesit

    def get_cost(self):
        return self.price


class SoganSos(DecoratorSos):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.price = 6
        self.cesit = " Soğan Sosu"

    def get_cesit(self):
        return self.cesit

    def get_cost(self):
        return self.price


class MisirSos(DecoratorSos):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.price = 6
        self.cesit = " Mısır Sosu"

    def get_cesit(self):
        return self.cesit

    def get_cost(self):
        return self.price


class BarbekuSos(DecoratorSos):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.price = 10
        self.cesit = " Barbekü Sosu"


# Siparişimizin Veritabanına Yazdırılması
import csv
import os
from datetime import datetime


def add_order_to_database(name, id_no, card_no, cesit, card_cvv, total_cost):
    # Sipariş tarihini ve saatinin alınması
    now = datetime.now()
    order_time = now.strftime("%Y-%m-%d %H:%M:%S")

    # Yeni bir sipariş satırı oluşturulması
    new_order = [name, id_no, card_no, cesit, order_time, card_cvv, total_cost]

    file_exists = os.path.isfile("Orders_Database.csv")

    # Orders_Database.csv dosyasına sipariş satırının eklenmesi
    with open("Orders_Database.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        if file_exists:
            writer.writerow(new_order)
        else:
            header = (["Name", "Id", "Card Number", "Order Cesit", "Order Time", "Card Password", "Total Price"])
            writer.writerow(header)
            writer.writerow(new_order)


# Siparişi Sağlayacak main() Fonksiyonu
def main():
    with open('Menu.txt', 'r') as f:
        menu_items = f.readlines()
    for item in menu_items:
        print(item.strip())

    """print("*************************************/n")
    print("* Lütfen Bir Pizza Tabanı Seçiniz:")
    print("1.Klasik - 8.99
")
    print("3.Turk - 13.99
\n")
    print("* Pizzanızın boyutunu seçiniz:")
    print("5.Small - 0.75 * Pizza Fiyatı")
    print("6.Medium - 1 * Pizza Fiyatı")
    print("7.Large - 1.25 * Pizza Fiyatı\n")
    print("* ve seçeceğiniz sos:")
    print("11.Zeytin Sosu - +0.99
")
    print("13.Keçi Peyniri - +2.99
")
    print("15.Soğan Sosu - +0.99
\n")
    print("* Teşekkür ederiz!\n")
    print("******************************************")"""

    # Kullanıcıdan pizza seçimini al
    pizza_choice = input("Lütfen pizza seçiniz (1-5): ")
    while pizza_choice not in ["1", "2", "3", "4", "5"]:
        pizza_choice = input("Lütfen geçerli bir pizza numarası seçiniz (1-5): ")

    # Seçilen pizzayı al
    if pizza_choice == "1":
        pizza = KlasikPizza()
    elif pizza_choice == "2":
        pizza = MargheritaPizza()
    elif pizza_choice == "3":
        pizza = TurkPizza()
    elif pizza_choice == "4":
        pizza = JambonluPizza()
    else:
        pizza = TavukluPizza()

    # Kullanıcıdan pizza seçimini al
    size_choice = input("Lütfen pizza boyutunuzu seçiniz (6-9): ")
    while size_choice not in ["6", "7", "8", "9"]:
        size_choice = input("Lütfen geçerli bir pizza boyutu numarası seçiniz (6-9): ")

    # Seçilen pizzayı al
    if size_choice == "6":
        size = SmallSize(pizza)
    elif size_choice == "7":
        size = MediumSize(pizza)
    elif size_choice == "8":
        size = LargeSize(pizza)
    else:
        size = XLargeSize(pizza)

    # Kullanıcıdan sos seçimini al
    sos_choice = input("Lütfen sos seçiniz (11-16): ")
    while sos_choice not in ["11", "12", "13", "14", "15", "16"]:
        sos_choice = input("Lütfen geçerli bir sos harfi seçiniz (11-16): ")
    # Seçilen sosu al
    if sos_choice == "11":
        sos = ZeytinSos(pizza)
    elif sos_choice == "12":
        sos = MantarSos(pizza)
    elif sos_choice == "13":
        sos = KeciPeyniriSos(pizza)
    elif sos_choice == "14":
        sos = EtSos(pizza)
    elif sos_choice == "15":
        sos = SoganSos(pizza)
    elif sos_choice == "16":
        sos = MisirSos(pizza)
    else:
        sos = BarbekuSos(pizza)

    # Kullanıcı bilgilerinin alınması
    name = input("Adınız: ")
    id_no = input("TC Kimlik Numaranız: ")
    card_no = input("Kredi Kartı Numaranız: ")
    card_cvv = input("Kredi Kartı Şifreniz: ")

    # Siparişin açıklamasının oluşturulması
    order_description = size.get_description() + " " + pizza.get_description() + " with" + sos.get_description()

    # Siparişin fiyatının hesaplanması
    total_cost = size.get_cost() + sos.get_cost()

    # Siparişin veritabanına kaydedilmesi
    add_order_to_database(name, id_no, card_no, order_description, card_cvv, total_cost)

    # Kullanıcıya sipariş detaylarının gösterilmesi
    print("Sipariş Detayları:")
    print("------------------")
    print("Ad: ", name)
    print("TC Kimlik Numarası: ", id_no)
    print("Kredi Kartı Numarası: ", card_no)
    print("Sipariş Açıklaması: ", order_description)
    print("Toplam Fiyat: ", total_cost)
    print("Sipariş Zamanı: ", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    # Siparişi onayla
    print("\nSiparişiniz alınmıştır. Teşekkür ederiz!")
