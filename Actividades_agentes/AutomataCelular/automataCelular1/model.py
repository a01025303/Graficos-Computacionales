# Code used to define model for automataCell1
# Ana Paula Katsuda, A01025303

# imports
from mesa import Model
from mesa.space import Grid
from mesa.time import SimultaneousActivation

from agent import Cell

# Define AutomataCell1 with Model as parent
class AutomataCell1(Model):
    # Initialize
    def __init__(self, height=50, width=50, density=0.1):
        # Set up model objects
        self.schedule = SimultaneousActivation(self) # will behave at the same time
        self.grid = Grid(height, width, torus=True) # Circular grid (torus)

        for (contents, x, y) in self.grid.coord_iter():
            # Create a cell
            new_cell = Cell((x, y), self)
            # Place cells in first row (49) with Prob = density
            if self.random.random() < density and y == 49:
                # Alive cell
                new_cell.state = new_cell.ALIVE
            # add agent into grid pos
            self.grid.place_agent(new_cell, (x, y))
            # move simulation thru time
            self.schedule.add(new_cell)

        self.running = True

    # update 
    def step(self):
        """
        Advance the model by one step.
        """
        self.schedule.step()
