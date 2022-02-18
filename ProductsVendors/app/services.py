

from abc import ABC,abstractmethod
from app.product_info import Product

class productservices(ABC):
    @abstractmethod
    def add_product(self, prod: Product) -> str:
        pass

    @abstractmethod
    def delete_product(self, pid:int) -> bool:
        pass

    @abstractmethod
    def get_all_products(self) -> list:
        pass

    @abstractmethod
    def search_by_id(self, pid:int) -> Product:
        pass

    @abstractmethod
    def search_by_vendor(self, ven:str) -> list:
        pass

    @abstractmethod
    def search_by_catagories(self, pcat: str) -> list:
        pass

    @abstractmethod
    def min_product_price(self) -> Product:
        pass

    @abstractmethod
    def max_product_price(self) -> Product:
        pass

    @abstractmethod
    def total_product_price(self) -> float:
        pass

    @abstractmethod
    def avg_product_price(self) -> float:
        pass