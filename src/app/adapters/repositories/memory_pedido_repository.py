from src.app.gateways.pedido_gateway import IPedidoGateway
from src.app.entities.pedido import Pedido
from typing import List

class MemoryPedidoRepository(IPedidoGateway):
    """Repository Adapter - Implementação concreta (in-memory)"""
    
    def __init__(self):
        self.pedidos: List[Pedido] = []

    def salvar(self, pedido: Pedido) -> None:
        self.pedidos.append(pedido)

    def listar(self) -> List[Pedido]:
        return self.pedidos