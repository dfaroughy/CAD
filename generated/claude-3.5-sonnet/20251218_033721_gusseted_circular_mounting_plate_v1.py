# model used: anthropic/claude-3.5-sonnet
import cadquery as cq

# Base dimensions
diameter = 100
thickness = 10

# Create base circle
step1 = cq.Workplane("XY").circle(diameter/2).extrude(thickness)

# Create mounting holes
hole_positions = [(35, 0), (0, 35), (-35, 0)]
step2 = step1.faces(">Z").workplane()\
    .pushPoints(hole_positions)\
    .hole(6)

# Create center hole
step3 = step2.faces(">Z").workplane()\
    .hole(20)

# Create curved slot
slot_path = cq.Workplane("XY").moveTo(0, -15)\
    .threePointArc((10, -5), (0, 5))\
    .threePointArc((-10, -5), (0, -15))
    
step4 = step3.faces(">Z").workplane()\
    .plunge(slot_path)\
    .cutThruAll()

result = step4
