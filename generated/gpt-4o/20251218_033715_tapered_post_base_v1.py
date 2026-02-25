# model used: openai/gpt-4o
import cadquery as cq

# Step 1: Create the base square
step1 = cq.Workplane("XY").box(70, 70, 10)

# Step 2: Create the tapered section
step2 = step1.faces(">Z").workplane().rect(70, 70).loft(
    cq.Workplane("XY").rect(50, 50).workplane(offset=80)
)

# Step 3: Create the top flange
step3 = step2.faces(">Z").workplane().rect(70, 70).extrude(10)

# Step 4: Create the central hole
step4 = step3.faces(">Z").workplane().circle(30).cutThruAll()

# Step 5: Create the corner holes
step5 = step4.faces(">Z").workplane().pushPoints([
    (30, 30), (-30, 30), (30, -30), (-30, -30)
]).circle(5).cutThruAll()

# Assign final geometry to result
result = step5
