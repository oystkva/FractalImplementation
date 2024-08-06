import torch
import numpy as np
import matplotlib.pyplot as plt

def sierpinski_arrowhead_curve(order -> int, length -> float) -> None:
    if order % 2 == 0:
        # curve(order, length, +60)
        return
    else:
        # curve(order, length, -60)
        return

def curve(order -> int, length -> float, angle -> int) -> None:
    if order == 0:
        # draw(length)
        return
    else:
        segment1 = curve(order - 1, length / 2, -angle)
        turn1 = turn(angle)
        segment2 = curve(order - 1, length / 2, angle)
        turn2 = turn(angle)
        segment3 = curve(order - 1, length / 2, -angle)

        return torch.cat(segment1 @ turn1, segment2, segment3 @ turn2)