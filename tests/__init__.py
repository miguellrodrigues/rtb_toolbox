from rtb_toolbox.robots.comau import comau_fk
from rtb_toolbox.inverse_kinematics import evolutive_ik, full_ik

import numpy as np
from math import pi

theta, f = evolutive_ik(
	np.array([537.95, -537.95, 295.96, 0, pi, pi / 4]),
	comau_fk,
	max_iterations=1024
)

print(theta, f)
