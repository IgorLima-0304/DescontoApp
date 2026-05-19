from abc import ABC, abstractmethod
from src.app.entities.pedido import Pedido
from typing import List

class IPedidoGateway(ABC):
    """Gateway - Interface que define o contrato do repositório (DIP)"""
    
    @abstractmethod
    def salvar(self, pedido: Pedido) -> None:
        pass

    @abstractmethod
    def listar(self) -> List[Pedido]:
        pass