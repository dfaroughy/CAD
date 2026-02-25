# model used: openai/gpt-4o
import cadquery as cq

# Step 1: Create the base box
step1 = cq.Workplane("XY").box(60, 40, 20)

# Step 2: Create the central hole
step2 = step1.faces(">Z").workplane().hole(10)

# Step 3: Create the four corner holes
step3 = step2.faces(">Z").workplane().rect(50, 30, forConstruction=True).vertices().hole(5)

# Step 4: Chamfer the top edges
result = step3.edges("|Z").chamfer(2)
