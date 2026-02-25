# model used: meta-llama/llama-4-maverick
import cadquery as cq

# Base plate dimensions
length = 80
width = 30
thickness = 10

# Create the base plate
step1 = cq.Workplane("XY").box(length, width, thickness)

# Hole dimensions
hole_diameter = 10
hole_positions = [(10, 15), (30, 15), (50, 15), (70, 15)]

# Create holes in the base plate
step2 = step1.faces(">Z").workplane().pushPoints(hole_positions).hole(hole_diameter)

# U-shaped cutout dimensions
cutout_width = 40
cutout_depth = 20

# Create the U-shaped cutout
step3 = step2.faces(">Z").workplane().rect(cutout_width, cutout_depth).cutBlind(-thickness)

# End tab dimensions
tab_width = 10
tab_length = 10
tab_height = 11

# Create end tabs
step4 = (
    step3.faces(">Z")
    .workplane()
    .center(-length / 2 + tab_width / 2, 0)
    .box(tab_width, tab_length, tab_height)
    .faces(">Z")
    .workplane()
    .center(length / 2 - tab_width / 2, 0)
    .box(tab_width, tab_length, tab_height)
)

# Tab hole dimensions
tab_hole_diameter = 5
tab_hole_positions = [(-length / 2 + tab_width / 2, 0), (length / 2 - tab_width / 2, 0)]

# Create holes in the end tabs
step5 = (
    step4.faces(">Z")
    .workplane()
    .pushPoints(tab_hole_positions)
    .hole(tab_hole_diameter)
)

result = step5
