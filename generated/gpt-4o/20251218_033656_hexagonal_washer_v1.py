# model used: openai/gpt-4o
import cadquery as cq

# Step 1: Create a hexagon base
step1 = cq.Workplane("XY").polygon(6, 19.691).extrude(3.0)

# Step 2: Cut the central hole
step2 = step1.faces(">Z").workplane().circle(17.321 / 2).cutThruAll()

# Final result
result = step2
