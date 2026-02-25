# model used: openai/gpt-4o
import cadquery as cq

# Step 1: Create the base rectangle
step1 = cq.Workplane("XY").rect(120, 40).extrude(10)

# Step 2: Create the first rounded rectangle cutout
step2 = step1.faces(">Z").workplane().center(-30, 0).rect(40, 20).vertices().fillet(5).cutThruAll()

# Step 3: Create the second rounded rectangle cutout
step3 = step2.faces(">Z").workplane().center(60, 0).rect(40, 20).vertices().fillet(5).cutThruAll()

# Step 4: Create the circular cutouts
step4 = step3.faces(">Z").workplane().center(-30, 0).rarray(60, 0, 2, 1).circle(5).cutThruAll()

# Assign final result
result = step4
