# model used: openai/gpt-4o
import cadquery as cq

# Step 1: Create the outer cylinder
outer_radius = 20 / 2
height = 10
step1 = cq.Workplane("XY").circle(outer_radius).extrude(height)

# Step 2: Create the inner cylinder for the hole
inner_radius = 10 / 2
step2 = cq.Workplane("XY").circle(inner_radius).extrude(height)

# Step 3: Subtract the inner cylinder from the outer cylinder
result = step1.cut(step2)
