# model used: anthropic/claude-3.5-sonnet
import cadquery as cq

# Base dimensions
width = 40.0
height = 40.0
thickness = 15.0

# Create base box
step1 = cq.Workplane("XY").box(width, height, thickness)

# Create outer circular groove
step2 = step1.faces(">Z").workplane()\
    .circle(15)\
    .circle(13)\
    .cutBlind(-2)

# Create inner circular groove 
step3 = step2.faces(">Z").workplane()\
    .circle(8)\
    .circle(6)\
    .cutBlind(-2)

# Create curved slots
def make_slot(workplane, radius, angle):
    return workplane.transformed(rotate=(0,0,angle))\
        .moveTo(radius, 0)\
        .arc((-radius*2, 0), (-radius, 0))\
        .arc((radius*2, 0), (radius, 0))\
        .cutBlind(-2)

step4 = step3
for angle in [0, 120, 240]:
    step4 = make_slot(step4.faces(">Z").workplane(), 11, angle)

result = step4
