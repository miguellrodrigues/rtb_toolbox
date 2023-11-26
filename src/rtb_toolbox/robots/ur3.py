import numpy as np
import sympy as sp
from sympy import pi

from rtb_toolbox.forward_kinematics import ForwardKinematic
from rtb_toolbox.link import Link

q1, q2, q3, q4, q5, q6 = sp.symbols('q_1 q_2 q_3 q_4 q_5 q_6')

I_1 = np.diag([0, -.02, 0])
I_2 = np.diag([0.13, 0, 0.1157])
I_3 = np.diag([0.05, 0, 0.0238])
I_4 = np.diag([0, 0, 0.01])
I_5 = np.diag([0, 0, 0.01])
I_6 = np.diag([0, 0, -0.02])

m_1 = 1.98
m_2 = 3.4445
m_3 = 1.437
m_4 = .871
m_5 = .805
m_6 = .261

j0 = Link([q1,       0, 150,     pi / 2], inertia_tensor=I_1, mass=m_1)
j1 = Link([q2,       0, 590,     pi    ], inertia_tensor=I_2, mass=m_2)
j2 = Link([q3,       0, 130,    -pi / 2], inertia_tensor=I_3, mass=m_3)
j3 = Link([q4, -647.07,   0,    -pi / 2], inertia_tensor=I_4, mass=m_4)
j4 = Link([q5,       0,   0,     pi / 2], inertia_tensor=I_5, mass=m_5)
j5 = Link([q6,     -95,   0,     0     ], inertia_tensor=I_6, mass=m_6)

comau_fk = ForwardKinematic(
		[j0, j1, j2, j3, j4, j5],
)
