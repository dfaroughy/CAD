# model used: openai/gpt-4o
import cadquery as cq

# Step 1: Create the base plate
step1 = cq.Workplane("XY").box(100, 100, 20)

# Step 2: Create the central hole
step2 = step1.faces(">Z").workplane().hole(60)

# Step 3: Create the four corner holes
step3 = step2.faces(">Z").workplane().rect(80, 80, forConstruction=True).vertices().hole(10)

# Step 4: Create the central protrusion
step4 = step3.faces(">Z").workplane().circle(50).extrude(80)

# Assign final geometry to result
result = step4
