# model used: openai/gpt-4o
import cadquery as cq

# Step 1: Create the main cylinder
step1 = cq.Workplane("XY").circle(10).extrude(95)

# Step 2: Create the inner cylinder cut
step2 = step1.faces(">Z").workplane().circle(5).cutBlind(-95)

# Step 3: Create the outer ring
step3 = step2.faces(">Z").workplane().circle(7.5).extrude(20)

# Step 4: Create the inner ring cut
step4 = step3.faces(">Z").workplane().circle(2.5).cutBlind(-20)

# Assign final result
result = step4
