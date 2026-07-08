
import pygame


class InputHandler:
    """Class maps input events to actions"""

    def __init__(self, keydown_map, keyup_map):
        self.keydown_actions = keydown_map
        self.keyup_actions = keyup_map

    def handle_input(self, event):
        if event.type == pygame.KEYDOWN:
            action_func = self.keydown_actions.get(event.key)
            if action_func:
                action_func()

        if event.type == pygame.KEYUP:
            action_func = self.keyup_actions.get(event.key)
            if action_func:
                action_func()