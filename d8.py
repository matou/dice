from cadquery import *
from ocp_vscode import *
from add_number import add_number
import math

width = 20
font_size = 8

c = math.sqrt(width**2 + width**2)
height = math.sqrt(width**2 - (c/2)**2)
draft_angle = math.degrees(math.atan((width/2) / height))

# top pyramid
r = ( Workplane("XY")
        .rect(width, width)
        .extrude(height, taper=draft_angle)
)

# bottom pyramid
r = ( r.faces("<Z").workplane(centerOption="CenterOfMass")
      .rect(width, width)
      .extrude(height, taper=draft_angle)
      .tag("base")
)


# front top
r = add_number(8, 
               r.faces(NearestToPointSelector((0, -1, 1))),
               font_size=font_size
               ) 

# back bottom
r = add_number(1, 
               r.faces(NearestToPointSelector((0, 1, -1))),
               font_size=font_size,
               rotate=180
               )

# left top 
r = add_number(2,
               r.faces(NearestToPointSelector((-1, 0, 1)), tag="base"),
               font_size=font_size
               )

# right bottom
r = add_number(7,
               r.faces(NearestToPointSelector((1, 0, -1)), tag="base"),
               font_size=font_size,
               rotate=180
               )

# front bottom
r = add_number(3,
               r.faces(NearestToPointSelector((0, -1, -1)), tag="base"),
               font_size=font_size,
               rotate=180
               )

# back top
r = add_number("6.",
               r.faces(NearestToPointSelector((0, 1, 1)), tag="base"),
               font_size=font_size
               )

# left bottom
r = add_number(4,
               r.faces(NearestToPointSelector((-1, 0, -1)), tag="base"),
               font_size=font_size,
               rotate=180
               )

# right top
r = add_number(5,
               r.faces(NearestToPointSelector((1, 0, 1)), tag="base"),
               font_size=font_size
               )

show_object(r)