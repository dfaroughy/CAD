# model used: openai/gpt-4o
import cadquery as cq

# Step 1: Create the largest base cylinder
step1 = cq.Workplane("XY").circle(25).extrude(10)

# Step 2: Create the second cylinder
step2 = step1.faces(">Z").workplane().circle(20).extrude(5)

# Step 3: Create the third cylinder
step3 = step2.faces(">Z").workplane().circle(15).extrude(5)

# Step 4: Create the fourth cylinder
step4 = step3.faces(">Z").workplane().circle(10).extrude(5)

# Step 5: Create the top cylinder
step5 = step4.faces(">Z").workplane().circle(5).extrude(3)

# Step 6: Create the slot on the largest base
step6 = step5.faces("<Z").workplane().center(0, 0).rect(5, 10).cutBlind(-5)

# Assign final result
result = step6
