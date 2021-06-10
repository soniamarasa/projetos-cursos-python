class GameStats():
    """Armazena dados estátisticos da Invasão Alienígena"""

    def __init__(self, ai_settings):
        """Inicializa os dados estátísticos."""
        self.ai_settings = ai_settings
        self.reset_stats()

        #Inicia o jogo em um estado inativo
        self.game_active = False

        #Inicia a invasão Alienígena em um estado ativo
        self.game_active = True

        # A pontuação máxima jamais deverá ser reiniciada
        self.high_score = 0

    def reset_stats(self):
        """Inicializa os dados estatísticos que podem mudar durante o jogo."""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
