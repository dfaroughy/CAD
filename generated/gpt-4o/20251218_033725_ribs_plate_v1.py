# model used: openai/gpt-4o
import cadquery as cq

# Step 1: Create the main rectangular base
step1 = cq.Workplane("XY").box(120, 97.5, 18.5)

# Step 2: Create the two holes
step2 = step1.faces(">Z").workplane().hole(18.5).move(40, 0).hole(18.5)

# Step 3: Create the top feature
step3 = step2.faces(">Z").workplane(centerOption="CenterOfBoundBox").move(0, 48.75).rect(18.5, 18.5).extrude(18.5)

# Assign final geometry to result
result = step3
