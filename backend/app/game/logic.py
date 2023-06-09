import random
import string

class Player:
    def __init__(self, connection):
        self.connection = connection
        self.score = 0

class Game:
    def __init__(self, player1_connection, player2_connection):
        self.player1 = Player(player1_connection)
        self.player2 = Player(player2_connection)
        self.current_turn = random.choice([self.player1, self.player2])
        self.current_word = self._generate_word()
        self.game_over = False

    def _generate_word(self):
        # This simple method generates a random word by selecting three random letters.
        # Replace this with your own method of generating words, e.g. from a list of words.
        return ''.join(random.choice(string.ascii_lowercase) for _ in range(3))

    async def play_turn(self, player, word):
        # A player's turn is valid if the word starts with the last letter of the current word
        if word[0] != self.current_word[-1]:
            self.game_over = True
            self.winner = self.player1 if player == self.player2 else self.player2
        else:
            player.score += 1
            self.current_word = word
            self.current_turn = self.player1 if player == self.player2 else self.player2

    async def send_game_state(self):
        # Send the current game state (current word, scores, and whose turn it is) to both players
        game_state = f"Current word: {self.current_word}. Scores: Player 1 - {self.player1.score}, Player 2 - {self.player2.score}. It is {self.current_turn.connection.websocket}'s turn."
        await self.player1.connection.websocket.send_text(game_state)
        await self.player2.connection.websocket.send_text(game_state)
