from src.app.usecases.criar_pedido_usecase import CriarPedidoUseCase
from src.app.dtos.criar_pedido_input_dto import CriarPedidoInputDTO
from src.app.entities.pedido import Pedido

class PedidoController:
    """Controller - Recebe dados da entrada e orquestra o UseCase"""
    
    def __init__(self, criar_pedido_use_case: CriarPedidoUseCase):
        self.criar_pedido_use_case = criar_pedido_use_case

    def criar_pedido(self, dto: CriarPedidoInputDTO) -> Pedido:
        """Recebe DTO e delega para o UseCase"""
        return self.criar_pedido_use_case.executar(
            cliente=dto.cliente,
            valor_original=dto.valor_original,
            tipo_desconto=dto.tipo_desconto
        )