from cadquery import *
from ocp_vscode import *
from add_number import add_number
import math

short_side = 15
long_side = 30
font_size = 16
number_depth = 2

r = Workplane("XY").box(short_side, long_side, short_side)

# 4 on top
r = add_number(4,
               r.faces(">Z"), 
               font_size=font_size, 
               number_depth=number_depth)

# 1 on bottom
r = add_number(1, 
               r.faces("<Z"), 
               font_size=font_size, 
               number_depth=number_depth,
               rotate=180)

# 2 on right
r = add_number(2, 
               r.faces(">X"), 
               font_size=font_size, 
               number_depth=number_depth, 
               rotate=-90)

# 3 on left
r = add_number(3, 
               r.faces("<X"), 
               font_size=font_size, 
               number_depth=number_depth, 
               rotate=90)

# add pyramids to the short sides
pyramid_height = short_side / 2
draft_angle = math.degrees(math.atan((short_side/ 2) / pyramid_height))

# bottom pyramid
r = ( r.faces("<Y").workplane(centerOption="CenterOfMass")
      .rect(short_side, short_side)
      .extrude(pyramid_height, taper=draft_angle)
)

# top pyramid
r = ( r.faces(">Y").workplane(centerOption="CenterOfMass")
      .rect(short_side, short_side)
      .extrude(pyramid_height, taper=draft_angle)
)

# show_object(pyramid)
show_object(r)