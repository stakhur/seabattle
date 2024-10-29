from enum import Enum

import copy

from .rules import Rules, State
from .guess_the_number_rules import GuessTheNumberRules
from .player import Player

class Game:
    class State(Enum):
        WAITING_FOR_PLAYERS = 2
        WAITING_FOR_PLAYERS_READY = 3
        READY_FOR_GAME = 4
        GAME_IN_PROGRESS = 5

    def __init__(self, rules: Rules):
        self._players = []
        self._state = self.State.WAITING_FOR_PLAYERS
        self.change_rules(rules)

    
    def change_rules(self, rules: Rules):
        assert self._state != self.State.GAME_IN_PROGRESS, "Cannot change the rules. Game is in progress!"

        self._rules = rules
        self._min_num_of_players = rules.limits["min_players"]
        self._max_num_of_players = rules.limits["max_players"]
        if (len(self._players) > self._max_num_of_players):
            self._players = self._players[:self._max_num_of_players]

        if (len(self._players) < self._min_num_of_players):
            self._state = self.State.WAITING_FOR_PLAYERS
        else:
            self._state = self.State.WAITING_FOR_PLAYERS_READY

        for player in self._players:
            player.set_rules(self._rules)


    def add_player(self, player: Player):
        assert self._state != self.State.GAME_IN_PROGRESS, "Cannot add player. Game is in progress!"

        is_player_added = False

        if (len(self._players) < self._max_num_of_players):
            player.set_rules(self._rules)
            self._players.append(player)
            is_player_added = True

        if (len(self._players) >= self._min_num_of_players):
            self._state = self.State.WAITING_FOR_PLAYERS_READY

        return is_player_added


    def prepare_players(self):
        assert self._state == self.State.WAITING_FOR_PLAYERS_READY, "Cannot prepare the players. "

        for player in self._players:
            player.prepare_to_game()

        self._state = self.State.READY_FOR_GAME


    def start(self):
        assert self._state == self.State.READY_FOR_GAME, "Cannot start the game. Players are not ready!"

        for player in self._players:
            player.start_game()

        self._players_queue = copy.copy(self._players)

        self._state = self.State.GAME_IN_PROGRESS


    def loop(self):
        # current_player = next_player()
        # state = TURN_AGAIN
        # while state == TURN_AGAIN:
        # turn = current_player.make_turn()
        # result, state = next_player.check(turn)
        # current_player.update(result)
        # 
        # TURN_AGAIN, NEXT_PLAYER_TURN, LOSE
        pass


    @property
    def state(self):
        return self._state