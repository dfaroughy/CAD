# model used: meta-llama/llama-4-maverick
import cadquery as cq

# Define the dimensions
width = 12
height = 12
depth = 11.699

# Step 1: Create the base box
step1 = cq.Workplane("XY").box(width, width, height/2, centered=(True, True, False))

# Step 2: Create the top pyramid frustum
step2 = cq.Workplane("XY").polygon(8, width).workplane(offset=height/2).polygon(8, 7.5).loft(combine=False)

# Step 3: Fuse the base box and the top pyramid frustum
step3 = step1.union(step2)

# Step 4: Create the inner cavity
step4 = cq.Workplane("XY").circle(4).extrude(height + 0.1, combine=False)

# Step 5: Cut the inner cavity from the fused shape
step5 = step3.cut(step4)

# Step 6: Fillet the edges
step6 = step5.edges("|Z").fillet(0.5)

# Assign the final geometry to result
result = step6
