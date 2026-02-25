# model used: openai/gpt-4o
import cadquery as cq

# Step 1: Create the base box
step1 = cq.Workplane("XY").box(60, 40, 20)

# Step 2: Chamfer the edges
step2 = step1.edges("|Z").chamfer(5)

# Step 3: Create the central hole
step3 = step2.faces(">Z").workplane().hole(10)

# Step 4: Create the counterbore
step4 = step3.faces(">Z").workplane().cboreHole(5, 15, 5)

# Assign final result
result = step4
