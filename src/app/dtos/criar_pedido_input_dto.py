from dataclasses import dataclass

@dataclass
class CriarPedidoInputDTO:
    """DTO - Objeto usado apenas para transportar dados entre camadas"""
    cliente: str
    valor_original: float
    tipo_desconto: str = "normal"