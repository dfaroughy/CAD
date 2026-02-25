# model used: meta-llama/llama-4-maverick
import cadquery as cq

# Define the dimensions
width = 90
depth = 90
height = 90
top_size = 70
thickness = 10
fillet_radius = 5

# Step 1: Create the outer shell
step1 = cq.Workplane("XY").box(width, depth, height)

# Step 2: Create the inner cavity
step2 = step1.faces(">Z").workplane().rect(top_size, top_size).extrude(-height + thickness * 2)

# Step 3: Cut out the inner cavity
step3 = step1.cut(step2)

# Step 4: Create the top and bottom faces with fillets
step4 = step3.faces(">Z").edges().fillet(fillet_radius).faces("<Z").edges().fillet(fillet_radius)

# Step 5: Create the four corner holes
step5 = step4.faces(">Z").workplane().rect(top_size, top_size, forConstruction=True).vertices().circle(5).extrude(-height)

# Step 6: Cut out the four corner holes
step6 = step5.cut(step5)

# Step 7: Create the side cutouts
step7 = step6.faces(">X").workplane(-depth/2 + thickness).rect(20, height - thickness * 2).extrude(-width + thickness * 2, combine=False)
step7 = step7.union(step6.faces("<X").workplane(depth/2 - thickness).rect(20, height - thickness * 2).extrude(width - thickness * 2))

# Step 8: Cut out the side cutouts
step8 = step6.cut(step7)

# Assign the final geometry to result
result = step8
