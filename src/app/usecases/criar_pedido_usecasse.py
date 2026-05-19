from src.app.entities.pedido import Pedido
from src.app.gateways.pedido_gateway import IPedidoGateway
from datetime import datetime

class CriarPedidoUseCase:
    """Use Case - Regras de aplicação (orquestra Entity + Gateway)"""
    
    def __init__(self, pedido_gateway: IPedidoGateway):
        self.pedido_gateway = pedido_gateway

    def executar(self, cliente: str, valor_original: float, tipo_desconto: str = "normal") -> Pedido:
        """Cria um novo pedido aplicando as regras de negócio"""
        pedido = Pedido(
            cliente=cliente,
            valor_original=valor_original,
            tipo_desconto=tipo_desconto
        )
        
        # Aqui virá a lógica de desconto (vamos adicionar nos próximos passos)
        self.pedido_gateway.salvar(pedido)
        
        return pedido