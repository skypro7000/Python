from address import Address
from mailing import Mailing
to_addr = Address("123456", "Хабаровск", "Ленина", "86", "28")
from_addr = Address("654321", "Сургут", "Разина", "23", "36")
mail = Mailing(to_addr, from_addr, 250, "AB123456789")
print(f"Отправление {mail.track} из {mail.from_address.index}, {mail.from_address.city}, {mail.from_address.street}, {mail.from_address.house} - {mail.from_address.apartment} "
      f"в {mail.to_address.index}, {mail.to_address.city}, {mail.to_address.street}, {mail.to_address.house} - {mail.to_address.apartment}. "
      f"Стоимость {mail.cost} рублей.")