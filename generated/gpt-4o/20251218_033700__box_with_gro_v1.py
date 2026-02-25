# model used: openai/gpt-4o
import cadquery as cq

# Step 1: Create the base rectangular prism
step1 = cq.Workplane("XY").box(80, 60, 20)

# Step 2: Create the central circular cutout
step2 = step1.faces(">Z").workplane().circle(10).cutThruAll()

# Step 3: Create the horizontal rectangular cutout
step3 = step2.faces(">Z").workplane().rect(40, 10).cutThruAll()

# Assign final result
result = step3
