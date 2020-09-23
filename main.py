class Goose:
  def __init__(self, name, weight):
    self.name = name
    self.weight = weight
  sound = 'honk'

  def feed(self, food_weight):
    self.weight += food_weight

  def collect_egg(self):
    return 1;

class Chicken:
  def __init__(self, name, weight):
    self.name = name
    self.weight = weight
  sound = 'cluck'

  def feed(self, food_weight):
    self.weight += food_weight
  
  def collect_egg(self):
    return 1;

class Cow:
  def __init__(self, name, weight):
    self.name = name
    self.weight = weight
  sound = 'moo'

  def feed(self, food_weight):
    self.weight += food_weight

  def milk(self, milk_volume):
    self.weight -= milk_volume  

class Sheep:
  def __init__(self, name, weight):
    self.name = name
    self.weight = weight
  sound = 'baa'

  def feed(self, food_weight):
    self.weight += food_weight

  def sheare(self, wool_weight):
    self.weight -= wool_weight
  
class Goat:
  def __init__(self, name, weight):
    self.name = name
    self.weight = weight
  sound = 'maa'

  def feed(self, food_weight):
    self.weight += food_weight
  
  def milk(self, milk_volume):
    self.weight -= milk_volume 

class Duck:
  def __init__(self, name, weight):
    self.name = name
    self.weight = weight

  sound = 'quack'

  def feed(self, food_weight):
    self.weight += food_weight
  
  def collect_egg(self):
    return 1;


def create_farm():

  uncle_joe_farm = []
  uncle_joe_farm.append(Goose('Серый', 10))
  uncle_joe_farm.append(Goose('Белый', 11))
  uncle_joe_farm.append(Chicken('Коко', 3))
  uncle_joe_farm.append(Chicken('Кукареку', 2))
  uncle_joe_farm.append(Sheep('Барашек', 14))
  uncle_joe_farm.append(Sheep('Кудрявый', 16))
  uncle_joe_farm.append(Goat('Рога', 22))
  uncle_joe_farm.append(Goat('Копыта', 21))
  uncle_joe_farm.append(Cow('Манька', 350))
  uncle_joe_farm.append(Duck('Кряква', 5))

  def find_animal_type():
    sound = input('Input animal sound: ')
    for animal in uncle_joe_farm:
      if animal.sound == sound:
        print(type(animal).__name__)
        return

  def find_haviest_animal():
    print(f'The haviest animal is {sorted(uncle_joe_farm, key=lambda x: x.weight, reverse = True)[0].name}.')

  def find_total_weight():
    total_weight = 0
    for animal in uncle_joe_farm:
      total_weight += animal.weight
    print(f'Total weight of all the animals in the farm: {total_weight} kgs.')

  find_haviest_animal()
  find_total_weight()
  find_animal_type()

create_farm()