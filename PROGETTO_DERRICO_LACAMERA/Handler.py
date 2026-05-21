import time

from Azienda import Azienda
from PROGETTO_DERRICO_LACAMERA import IdGen
from Consegna import Delivery
from Veicolo import Bicycle, Car, ElectricScooter, Status, Truck, VehicleType
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
        self.__id_gen = IdGen()

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

        n_v = Handler.__PROPS["vehicles"]

        self.__vehicles = {
            VehicleType.BYCICLE: [Bicycle(id=self.__get_id()) for _ in range(n_v)],
            VehicleType.ELECTRICSCOOTER: [ElectricScooter(id=self.__get_id()) for _ in range(n_v)],
            VehicleType.CAR: [Car(id=self.__get_id()) for _ in range(n_v)],
            VehicleType.TRUCK: [Truck(id=self.__get_id()) for _ in range(n_v)]
        }

    def __get_id(self):
        return self.__id_gen.next()

    def __assign_vehicles(self, n_available):
        for _, vehicles in self.__vehicles.items():
            for v in vehicles:
                available_vehicles = random.sample(
                        list(filter(lambda v: v.is_available, self.__vehicles)), n_available
                )
                print_elements(available_vehicles)

                f_function = lambda rider: v.driving_license in rider.driving_licenses
                enabled_riders = list(filter(f_function, self.__riders))
                n_eriders = len(enabled_riders)
                vehicles_in_use = random.sample(available_vehicles, n_eriders)

                for r, v in zip(enabled_riders, vehicles_in_use):
                    r.add_vehicle(v)
                    v.change_status(Status.IN_USE)
                print_elements(available_vehicles)

    def start(self):
        n_available = Handler.__PROPS['vehicles']
        #n_giorno = 0
        while True:
            self.__assign_vehicles(n_available=n_available)

            # consegne
            for r in self.__riders:
                companies = random.sample(self.__companies, Handler.__PROPS['n_delivery'])
                deliveries = [
                    Delivery(
                        id_rider=r.id,
                        id_azienda=c.id,
                        start=r.position if i == 0 else companies[i-1].coord,
                        arrive=c.coord,
                        #TODO: extra_info={"weight": }
                    )
                for i, c in enumerate(companies)]
                #r.add_companies(deliveries)

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
