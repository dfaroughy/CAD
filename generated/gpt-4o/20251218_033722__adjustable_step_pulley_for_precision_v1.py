# model used: openai/gpt-4o
import cadquery as cq

# Step 1: Create the base cylinder
step1 = cq.Workplane("XY").circle(30).extrude(10)

# Step 2: Create the second tier
step2 = step1.faces(">Z").workplane().circle(25).extrude(10)

# Step 3: Create the third tier
step3 = step2.faces(">Z").workplane().circle(20).extrude(10)

# Step 4: Create the fourth tier
step4 = step3.faces(">Z").workplane().circle(15).extrude(10)

# Step 5: Create the top cylinder
step5 = step4.faces(">Z").workplane().circle(5).extrude(10)

# Step 6: Create the hole
result = step5.faces("<Z").workplane().circle(5).cutThruAll()
