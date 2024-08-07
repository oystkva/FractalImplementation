import torch
import numpy as np
import matplotlib.pyplot as plt

# Device configuration
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

X, Y = np.mgrid[-4.0:4.0:0.01, -4.0:4.0:0.01]
x = torch.tensor(X).to(device)
y = torch.tensor(Y).to(device)

golden_ratio = (1 + np.sqrt(5))/2
r1 = np.power(1/golden_ratio, 1/golden_ratio)
r2 = np.power(1/golden_ratio, 2)
log_base = np.power(golden_ratio, 1/golden_ratio)