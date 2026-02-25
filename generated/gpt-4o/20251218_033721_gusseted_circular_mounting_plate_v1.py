# model used: openai/gpt-4o
import cadquery as cq

# Step 1: Create the base cylinder
step1 = cq.Workplane("XY").circle(50).extrude(10)

# Step 2: Create the central hole
step2 = step1.faces(">Z").workplane().circle(10).cutThruAll()

# Step 3: Create the first small hole
step3 = step2.faces(">Z").workplane().center(-30, 30).circle(5).cutThruAll()

# Step 4: Create the second small hole
step4 = step3.faces(">Z").workplane().center(30, 30).circle(5).cutThruAll()

# Step 5: Create the third small hole
step5 = step4.faces(">Z").workplane().center(-30, -30).circle(5).cutThruAll()

# Final result
result = step5
