# model used: meta-llama/llama-4-maverick
import cadquery as cq

# Define the dimensions
plate_size = 120.0
plate_thickness = 8.0
corner_hole_diameter = 8.0
center_hole_diameter = 20.0
corner_hole_offset = 10.0

# Step 1: Create the base plate
step1 = cq.Workplane("XY").box(plate_size, plate_size, plate_thickness)

# Step 2: Create the corner holes
corner_holes = (
    cq.Workplane("XY")
    .pushPoints(
        [
            (-plate_size / 2 + corner_hole_offset, -plate_size / 2 + corner_hole_offset),
            (plate_size / 2 - corner_hole_offset, -plate_size / 2 + corner_hole_offset),
            (plate_size / 2 - corner_hole_offset, plate_size / 2 - corner_hole_offset),
            (-plate_size / 2 + corner_hole_offset, plate_size / 2 - corner_hole_offset),
        ]
    )
    .circle(corner_hole_diameter / 2)
    .extrude(plate_thickness)
)

# Step 3: Create the center hole
center_hole = (
    cq.Workplane("XY")
    .circle(center_hole_diameter / 2)
    .extrude(plate_thickness)
)

# Step 4: Cut the holes from the base plate
step2 = step1.cut(corner_holes).cut(center_hole)

# Assign the final geometry to 'result'
result = step2
