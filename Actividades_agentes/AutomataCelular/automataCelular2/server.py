# Code used to define server for automataCell2
# Ana Paula Katsuda, A01025303

#import modules
from mesa.visualization.modules import CanvasGrid # where we draw
from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.UserParam import UserSettableParameter # set params

from model import AutomataCell2 # import model to use server --> model.py

# show agent "cell"
def portrayCell(cell):
    """
    This function is registered with the visualization server to be called
    each tick to indicate how to draw the cell in its current state.
    :param cell:  the cell in the simulation
    :return: the portrayal dictionary.
    """
    assert cell is not None
    # specify how will the agent be visualized
    return {
        "Shape": "rect",
        "w": 0.8,
        "h": 0.8,
        "Filled": "true",
        "Layer": 0,
        "x": cell.x,
        "y": cell.y,
        "Color": "black" if cell.isAlive() else "white",
    }

# Make a world that is 50x50, on a 500x500 display.
canvas_element = CanvasGrid(portrayCell, 50, 50, 500, 500)

#Create server
server = ModularServer(AutomataCell2, [canvas_element], "Automata Celular 2", {"height": 50, "width": 50, "density": UserSettableParameter("slider", "Cell density", 0.1, 0.01, 0.5, 0.01)})

server.launch() # launch server