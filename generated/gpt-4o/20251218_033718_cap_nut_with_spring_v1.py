# model used: openai/gpt-4o
import cadquery as cq

# Step 1: Create the main hexagonal prism
step1 = cq.Workplane("XY").polygon(6, 12).extrude(12)

# Step 2: Create the cylindrical cutout
step2 = step1.faces(">Z").workplane().circle(6).cutThruAll()

# Step 3: Create the chamfer on the top edges
step3 = step2.edges("|Z").chamfer(1)

# Step 4: Create the fillet on the bottom edges
result = step3.edges("<Z").fillet(1)
