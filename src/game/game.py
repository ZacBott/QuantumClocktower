from characters.base import BaseCharacter

class Game:
    '''
    This is a class

    Args:
        player_count (int): Number of players
    '''   
    def __init__(
        self,
        player_count: int,
    ):
        self.player_count = player_count

    def initialise_game(
        self,
    ):
        self.player_state = [BaseCharacter() for player in range(self.player_count)]