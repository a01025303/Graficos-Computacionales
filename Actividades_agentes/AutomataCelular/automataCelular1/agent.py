# Code used to define agent for automataCell1
# Ana Paula Katsuda, A01025303

# Import mesa
from mesa import Agent

# define agent cell class
class Cell(Agent):
    # either dead or alive
    DEAD = 0
    ALIVE = 1
    # initialize
    def __init__(self, pos, model, init_state=DEAD): # dead by default
        """
        Create a cell, in the given state, at the given x, y position.
        """
        super().__init__(pos, model)
        self.x, self.y = pos # possition
        self.state = init_state # state from model
        self._nextState = None # next state --> los estados dependen de los estados de los vecinos 
    
    # determine if it is alive
    def isAlive(self):
        return self.state == self.ALIVE
   
    # return iterator for neighbors
    def neighbors(self):
        return self.model.grid.neighbor_iter((self.x, self.y), True) # true=allow diagonals

    # update --> steps
    def step(self):
        # Dictionary that saves values from neighbors on top of current cell
        neighbor_list = {'left': 0, 'top': 0, 'right': 0}
        # Iterate through neighbors
        for neighbor in self.neighbors():
            # if neighbor is alive and is on top of current cell
            if(neighbor.isAlive() and neighbor.y == (self.y + 1)%50):
                # If neighbor is on the top-left
                if(neighbor.x == (self.x - 1)%50): 
                    # update dictionary on left
                    neighbor_list['left'] = 1
                # if neighbor is on the top-center
                if(neighbor.x == (self.x)%50):
                    # update dictionary on top
                    neighbor_list['top'] = 1
                # if neighbor is on the top right
                if(neighbor.x == (self.x + 1)%50): 
                    # update dictionary on right
                    neighbor_list['right'] = 1
        # Assume nextState is unchanged, unless changed below.
        self._nextState = self.state
        # change each agent to next states depending on change conditions
        if not self.isAlive(): # when self is not alive, check conditions
            if neighbor_list == {'left': 0, 'top': 0, 'right': 0}:
                self._nextState = self.DEAD
            elif neighbor_list == {'left': 0, 'top': 0, 'right': 1}: 
                self._nextState = self.ALIVE
            elif neighbor_list == {'left': 0, 'top': 1, 'right': 0}: 
                self._nextState = self.DEAD
            elif neighbor_list == {'left': 0, 'top': 1, 'right': 1}: 
                self._nextState = self.ALIVE
            elif neighbor_list == {'left': 1, 'top': 0, 'right': 0}: 
                self._nextState = self.ALIVE
            elif neighbor_list == {'left': 1, 'top': 0, 'right': 1}: 
                self._nextState = self.DEAD
            elif neighbor_list == {'left': 1, 'top': 1, 'right': 0}: 
                self._nextState = self.ALIVE
            elif neighbor_list == {'left': 1, 'top': 1, 'right': 1}: 
                self._nextState = self.DEAD
    # Advance function --> go to next state
    def advance(self):
        self.state = self._nextState