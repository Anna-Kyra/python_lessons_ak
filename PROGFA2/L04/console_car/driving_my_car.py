import time

from car import Car
from time import sleep

my_car = Car(20)
my_carcar = Car(50)


while my_car.speed < my_car.road_length:
    my_car.vroom()
    print(my_car)
    time.sleep(0.2)
print(my_carcar)
