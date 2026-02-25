# model used: openai/gpt-4o
import cadquery as cq

# Step 1: Create the base rectangle
step1 = cq.Workplane("XY").rect(30, 5).extrude(5)

# Step 2: Create the middle section
step2 = step1.faces(">Z").workplane().rect(20, 5).extrude(32.5)

# Step 3: Create the top section
step3 = step2.faces(">Z").workplane().rect(30, 5).extrude(5)

# Step 4: Fillet the edges
result = step3.edges("|Z").fillet(2.5)
