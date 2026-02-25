# model used: openai/gpt-4o
import cadquery as cq

# Step 1: Create the main vertical bar
step1 = cq.Workplane("XY").box(15, 50, 15)

# Step 2: Create the main horizontal bar
step2 = cq.Workplane("XY").box(50, 15, 15).translate((0, 0, 15/2))

# Step 3: Combine the two bars
step3 = step1.union(step2)

# Step 4: Create the small vertical bar
step4 = cq.Workplane("XY").box(15, 15, 50).translate((0, 0, 15/2))

# Step 5: Combine with the small vertical bar
step5 = step3.union(step4)

# Step 6: Create the small horizontal bar
step6 = cq.Workplane("XY").box(50, 15, 15).translate((0, 0, 15/2))

# Step 7: Combine with the small horizontal bar
step7 = step5.union(step6)

# Step 8: Create the cutout
cutout = cq.Workplane("XY").circle(7.5).extrude(15).translate((0, 0, 15/2))

# Step 9: Subtract the cutout
result = step7.cut(cutout)
