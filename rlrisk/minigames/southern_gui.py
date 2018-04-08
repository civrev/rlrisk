'''
This class is the GUI for the minigame southern warfare
'''

import pygame, os
from rlrisk.environment.gui import GUI
from rlrisk.environment.risk import Risk

class SGUI(GUI):

    def __init__(self):
        super().__init__()

        #filter out stuff we don't use in this minigame
        board, continents, cards = Risk.gen_board()
        concerned = set(continents['Africa']+continents['S_America'])
        to_pop = set(board) - concerned
        [self.positions.pop(x) for x in to_pop]

        #crop screen
        left, top, right_offset, bottom_offset = (300, 250, 420, 350)
        self.background = self.background.subsurface((left, top, right_offset, bottom_offset))
        for p in self.positions:
            x,y = self.positions[p]
            self.positions[p]=(x-left,y-top)
        self.init_draw()
        
        
        
