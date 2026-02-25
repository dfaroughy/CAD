# model used: meta-llama/llama-4-maverick
import cadquery as cq

# Base dimensions
base_length = 50
base_width = 20
base_height = 5

# Column dimensions
column_length = 50
column_width = 20
column_height = 55 - base_height

# Hole dimensions
hole_diameter = 10
hole_depth = 10
hole_distance = 15

step1 = cq.Workplane("XY").box(base_length, base_width, base_height)
step2 = cq.Workplane("XY").workplane(offset=base_height).box(column_length, column_width, column_height)
step3 = step1.union(step2)

step4 = (
    step3.faces(">Z")
    .workplane()
    .pushPoints([(column_length / 2 - hole_distance / 2, column_width / 2), (column_length / 2 + hole_distance / 2, column_width / 2)])
    .circle(hole_diameter / 2)
    .cutThruAll()
)

result = step4
