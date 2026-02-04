def add_number(number, face, font_size=16, number_depth=1.5, rotate=0):
    return face.workplane(centerOption="CenterOfMass").transformed(
        rotate=(0, 0, rotate)).text(
        str(number), 
        fontsize=font_size, 
        distance=-number_depth,
        font="Impact"
        # fontPath="/System/Library/Fonts/MarkerFelt.ttc"
    )