import torch
import numpy as np
import matplotlib.pyplot as plt

def sierpinski_arrowhead_curve(order: int, length: float) -> torch.Tensor:
    if order % 2 == 0:
        return curve(order, length, +60)
    else:
        return curve(order, length, -60)

def curve(order: int, length: float, angle: int) -> torch.Tensor:
    if order == 0:
        # draw(length)
        return torch.tensor([[length, 0]]).reshape(1, 2)
    else:
        segment1 = curve(order - 1, length / 2, -angle)
        turn1 = turn(angle)
        segment2 = curve(order - 1, length / 2, angle)
        turn2 = turn(angle)
        segment3 = curve(order - 1, length / 2, -angle)

        return torch.cat((segment1 @ turn1, segment2, segment3 @ turn2))

def turn(angle: int) -> torch.Tensor:
    rad = torch.deg2rad(torch.tensor(angle, dtype=torch.float32))
    return torch.tensor(
        [[torch.cos(rad), -torch.sin(rad)],
         [torch.sin(rad),  torch.cos(rad)]]
        )




order = 3
length = 1.0
points = sierpinski_arrowhead_curve(order, length)