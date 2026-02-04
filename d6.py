from cadquery import *
from ocp_vscode import *
from add_number import add_number

side_length = 20
font_size = 16
number_depth = 2
# font = "Impact"
# font = "Arial Rounded MT Bold"
# font = "Chalkboard SE"


r = Workplane("XY").box(side_length, side_length, side_length)

# 6 on top
r = add_number(6, r.faces(">Z"))

# 1 on bottom
r = add_number(1, r.faces("<Z"))

# 2 on front
r = add_number(2, r.faces("<Y"))

# 5 on back
r = add_number(5, r.faces(">Y"))

# 3 on right
r = add_number(3, r.faces(">X"))

# 4 on left
r = add_number(4, r.faces("<X"))

show_object(r)