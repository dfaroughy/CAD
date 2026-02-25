# model used: openai/gpt-4o
import cadquery as cq

# Step 1: Create the main cylindrical body
step1 = cq.Workplane("XY").circle(15).extrude(20)

# Step 2: Create the inner cutout
step2 = step1.faces(">Z").workplane().circle(14.9995).cutBlind(-20)

# Step 3: Create the slots
slot_profile = cq.Workplane("XY").rect(3, 5).extrude(20)
step3 = step2.cut(slot_profile.translate((0, 12.5, 0)))
step3 = step3.cut(slot_profile.translate((0, -12.5, 0)))

# Assign final result
result = step3
