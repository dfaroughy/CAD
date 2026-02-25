# model used: openai/gpt-4o
import cadquery as cq

# Step 1: Create the base rectangle
step1 = cq.Workplane("XY").rect(60, 40).extrude(8)

# Step 2: Create the inner cutout rectangle with rounded corners
step2 = step1.faces(">Z").workplane().rect(40, 20, forConstruction=True)\
    .vertices().fillet(5).extrude(-8)

# Step 3: Create the four corner holes
step3 = step2.faces(">Z").workplane().rect(50, 30, forConstruction=True)\
    .vertices().circle(5).cutThruAll()

# Final result
result = step3
