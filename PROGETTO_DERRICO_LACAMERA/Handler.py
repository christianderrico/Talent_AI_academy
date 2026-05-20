import time

from Azienda import Azienda
from Veicolo import Bicycle, ElectricScooter, Status
from utils import print_elements, read_file
from Rider import Rider
import random
import json


class Handler:
    with open(r".\resources\conf.json", "r") as f:
        __PROPS = json.load(f)

    def __init__(self, riders_path, companies_path):
        self.__riders_path = riders_path
        self.__companies_path = companies_path

        self.__companies = [
            Azienda(
                id=company_info[0],
                name=company_info[1],
                coord=(company_info[2], company_info[3]),
            )
            for company_info in read_file(self.__companies_path, sep=",")
        ]

        self.__riders = [
            Rider(id=rider_info[0], name=rider_info[1])
            for rider_info in read_file(self.__riders_path)
        ]

        self.__vehicles = [
            ElectricScooter(id=i) if i % 2 == 0 else Bicycle(id=i)
            for i in range(Handler.__PROPS['n_bikes'])
        ]

    def start(self):
        n_available = Handler.__PROPS['n_bikes']
        n_giorno = 0
        while True:
            print(f"GIORNO {n_giorno}")

            available_vehicles = random.sample(
                list(filter(lambda v: v.is_available, self.__vehicles)), n_available
            )
            print_elements(available_vehicles)

            n_riders = len(self.__riders)
            vehicles_in_use = random.sample(available_vehicles, n_riders)
            for r, v in zip(self.__riders, vehicles_in_use):
                r.add_vehicle(v)
                v.change_status(Status.IN_USE)
            print_elements(available_vehicles)

            # consegne
            for r in self.__riders:
                deliveries = random.sample(self.__companies, Handler.__PROPS['n_delivery'])
                r.add_companies(deliveries)

            ### TUTTI I RIDER ESEGUONO CONSEGNE
            time.sleep(3)
            print("FINE CONSEGNE!!!")

            for r in self.__riders:
                r.clear_companies()

            # BICI RIPARATE
            if n_available < self.__PROPS['n_bikes']:
                for v in broken_bikes:
                    v.change_status(Status.AVAILABLE)

            print_elements(available_vehicles)

            broken_bikes = random.sample(vehicles_in_use, Handler.__PROPS['broken_bikes'])
            for v in broken_bikes:
                v.change_status(Status.BROKEN)

            print_elements(available_vehicles)

            n_available = Handler.__PROPS['n_bikes'] - Handler.__PROPS['broken_bikes']
            n_giorno += 1
