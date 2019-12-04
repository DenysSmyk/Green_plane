class GameStats():
    def __init__(self, game_settings):
        self.game_settings = game_settings
        self.reset_stats()
        self.game_active = False
        self. score = 0
        self.game_over = False

        self.enemies_life = 1

    def reset_stats(self):
        self.ships_left = 2