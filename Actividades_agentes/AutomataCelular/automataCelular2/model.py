# Code used to define model for automataCell2
# Ana Paula Katsuda, A01025303

# imports
from mesa import Model
from mesa.space import Grid
from mesa.time import SimultaneousActivation

from agent import Cell

# Define automataCell2 with model as parent
class AutomataCell2(Model):
    # Initialize
    def __init__(self, height=50, width=50, density=0.1):
        # Set up model objects
        self.schedule = SimultaneousActivation(self) # behave at the same time
        self.grid = Grid(height, width, torus=True)
        for (contents, x, y) in self.grid.coord_iter():
            # Create a cell
            new_cell = Cell((x, y), self)
            # Place a cell in each cell with Prob = density
            if self.random.random() < density:
                # set random cell as alive
                new_cell.state = new_cell.ALIVE
            # place agent on grid
            self.grid.place_agent(new_cell, (x, y))
            self.schedule.add(new_cell)
        self.running = True

    # update
    def step(self):
        """
        Advance the model by one step.
        """
        self.schedule.step()
