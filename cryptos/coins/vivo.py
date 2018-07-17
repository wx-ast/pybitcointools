from .base import BaseCoin
from ..explorers import blockchain

class Vivo(BaseCoin):
    coin_symbol = "VIVO"
    display_name = "Vivo"
    segwit_supported = False
    magicbyte = 70
    explorer = blockchain
    testnet_overrides = {
        'display_name': "Vivo Testnet",
        'coin_symbol': "VIVOTEST",
        'magicbyte': 140,
    }
