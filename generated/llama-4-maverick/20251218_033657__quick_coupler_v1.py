# model used: meta-llama/llama-4-maverick
import cadquery as cq

# Base dimensions
width = 20
length = 40
height = 51.252
padlock_height = 20

# Create the base
step1 = cq.Workplane("XY").box(width, length, height - padlock_height)

# Create the padlock
step2 = cq.Workplane("XY").box(width, length, padlock_height).faces(">Z").workplane().circle(20).extrude(2)
step3 = cq.Workplane("XY").box(width, length, padlock_height).faces(">Z").workplane().rect(8, 20).extrude(4)

# Combine the padlock parts
step4 = step2.union(step3)

# Create the shackle
step5 = cq.Workplane("XY").box(2, 20, 10).translate((0, 0, padlock_height))
step6 = cq.Workplane("XY").circle(2).extrude(20).translate((0, 10, padlock_height + 5))

# Combine the shackle parts
step7 = step5.union(step6)

# Combine all parts
step8 = step1.union(step4).union(step7)

# Final result
result = step8
