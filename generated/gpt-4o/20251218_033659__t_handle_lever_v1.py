# model used: openai/gpt-4o
import cadquery as cq

# Step 1: Create the main cylindrical body
step1 = cq.Workplane("XY").circle(20).extrude(90)

# Step 2: Create the top flange
step2 = step1.faces(">Z").workplane().circle(30).extrude(10)

# Step 3: Create the cutout on the side
step3 = step2.faces("<Y").workplane(centerOption="CenterOfBoundBox").rect(30, 20).cutBlind(-40)

# Step 4: Create the rounded end
step4 = step3.faces(">Z").workplane().circle(20).extrude(10)

# Step 5: Create the grooves
step5 = step4.faces("<Y").workplane(centerOption="CenterOfBoundBox").rarray(10, 1, 4, 1).circle(2).cutBlind(-90)

# Assign final geometry to result
result = step5
