from rtb_toolbox.robots.SCARA import scara_fk
import sympy as sp


sp.pprint(
    scara_fk.get_transformation(2,3)
)