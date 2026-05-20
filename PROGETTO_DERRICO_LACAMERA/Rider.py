from Azienda import Azienda
from Veicolo import Vehicle


class Rider:
    def __init__(self, id, name):
        self.__id = id
        self.__name = name
        self.__vehicle = None
        self.__companies = []
        self.__driving_licenses = []

    def __str__(self):
        return f"id {self.__id}, name {self.__name}"

    @property
    def vehicle(self):
        return Vehicle(**self.__vehicle.__dict__)

    @property
    def driving_licenses(self):
        return self.__driving_licenses[:]

    @property
    def companies(self):
        return self.__companies[:]

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    def add_vehicle(self, vehicle):
        self.__vehicle = vehicle

    def is_company_present(self, company: Azienda):
        mapping_function = lambda saved_company: saved_company.id
        aziende_presenti = list(map(mapping_function, self.__companies))
        return company.id in aziende_presenti

    def has_driving_license(self, d_license):
        return d_license in self.__driving_licenses

    def add_driving_license(self, add_driving_license):
        self.__driving_licenses.append(add_driving_license)

    def add_company(self, company):
        self.__companies.append(company)

    def add_companies(self, companies):
        self.__companies.extend(companies)

    def clear_companies(self):
        self.__companies.clear()
