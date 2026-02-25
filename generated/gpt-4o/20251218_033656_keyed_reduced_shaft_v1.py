# model used: openai/gpt-4o
import cadquery as cq

# Step 1: Create the main cylinder
step1 = cq.Workplane("XY").circle(10).extrude(50)

# Step 2: Create the inner hole
step2 = step1.faces(">Z").workplane().circle(5).cutThruAll()

# Step 3: Create the rectangular protrusion
step3 = step2.faces(">Y").workplane(centerOption="CenterOfBoundBox").rect(4, 8).extrude(2)

# Assign final result
result = step3
