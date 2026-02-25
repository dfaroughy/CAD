# model used: meta-llama/llama-4-maverick
python
import cadquery as cq

# Dimensions from the drawing
length = 60.0
width = 40.0
thickness = 8.0
corner_hole_diameter = 6.0  # inferred from the drawing

# Step 1: Create the base plate
step1 = cq.Workplane("XY").box(length, width, thickness)

# Step 2: Create the corner holes
step2 = step1.faces(">Z").workplane().pushPoints([
    (-length/2 + corner_hole_diameter/2, -width/2 + corner_hole_diameter/2),
    (length/2 - corner_hole_diameter/2, -width/2 + corner_hole_diameter/2),
    (-length/2 + corner_hole_diameter/2, width/2 - corner_hole_diameter/2),
    (length/2 - corner_hole_diameter/2, width/2 - corner_hole_diameter/2)
]).hole(corner_hole_diameter)

# Step 3: Create the inner pocket
inner_pocket_length = length - 2 * corner_hole_diameter
inner_pocket_width = width - 2 * corner_hole_diameter
step3 = step2.faces(">Z").workplane().rect(inner_pocket_length, inner_pocket_width).cutBlind(-thickness + 2)

# Assign the final geometry to result
result = step3
```
