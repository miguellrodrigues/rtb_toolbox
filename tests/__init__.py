from rtb_toolbox.robots.ur3 import ur3_fk
from rtb_toolbox.inverse_kinematics import evolutive_ik, full_ik
from rtb_toolbox.forward_dynamics import ForwardDynamics

import numpy as np
from math import pi
import sympy as sp

ee_pos = ur3_fk.compute_ee_position(np.random.rand(6))[:, 0]

theta, f = evolutive_ik(
	np.array([*ee_pos, 0, pi, pi / 4]),
	ur3_fk,
	max_iterations=1024
)

print(' ')
print(theta, f)
print(' ')

print(ur3_fk.compute_ee_position(theta)[:, 0], ee_pos)