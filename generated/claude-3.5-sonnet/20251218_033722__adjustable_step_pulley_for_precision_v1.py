# model used: anthropic/claude-3.5-sonnet
import cadquery as cq

# Base dimensions
base_diameter = 60.0
base_height = 40.0
total_height = 40.0

# Create base cylinder
step1 = cq.Workplane("XY").circle(base_diameter/2).extrude(base_height)

# Create stepped sections
step2 = step1.faces(">Z").workplane()\
    .circle(50/2).extrude(8)

step3 = step2.faces(">Z").workplane()\
    .circle(40/2).extrude(6)

step4 = step3.faces(">Z").workplane()\
    .circle(30/2).extrude(4)

step5 = step4.faces(">Z").workplane()\
    .circle(20/2).extrude(4)

step6 = step5.faces(">Z").workplane()\
    .circle(10/2).extrude(3)

# Create center hole
result = step6.faces(">Z").workplane()\
    .hole(5.0, depth=total_height)
