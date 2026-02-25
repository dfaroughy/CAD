# model used: meta-llama/llama-4-maverick
import cadquery as cq

# Define the dimensions
outer_diameter = 30.0
height = 20.0
inner_diameter = 20.0  # inferred from the drawing

# Step 1: Create the outer cylinder
step1 = cq.Workplane("XY").circle(outer_diameter/2).extrude(height)

# Step 2: Create the inner cylinder
step2 = cq.Workplane("XY").circle(inner_diameter/2).extrude(height)

# Step 3: Subtract the inner cylinder from the outer cylinder
step3 = step1.cut(step2)

# Step 4: Create a single keyway
keyway_width = 5.0  # inferred from the drawing
keyway_depth = 2.0  # inferred from the drawing
step4 = cq.Workplane("XY").rect(keyway_width, keyway_depth).extrude(height)

# Step 5: Create the keyways around the inner cylinder
step5 = step3.cut(step4.translate((inner_diameter/2, 0, 0)))
for i in range(1, 6):
    angle = i * 60  # 6 keyways, 60 degrees apart
    step5 = step5.cut(step4.rotate((0, 0, 1), (0, 0, 0), angle).translate((inner_diameter/2, 0, 0)))

# Step 6: Create the central boss
boss_diameter = 10.0  # inferred from the drawing
boss_height = 10.0  # inferred from the drawing
step6 = step5.cut(cq.Workplane("XY").circle(boss_diameter/2).extrude(boss_height).translate((0, 0, height - boss_height)))

# Step 7: Create the small cutouts at the bottom
cutout_width = 2.0  # inferred from the drawing
cutout_depth = 2.0  # inferred from the drawing
step7 = step6.cut(cq.Workplane("XY").rect(cutout_width, cutout_depth).extrude(height).translate(((outer_diameter - cutout_width)/2, (outer_diameter - cutout_depth)/4, 0)))
step7 = step7.cut(cq.Workplane("XY").rect(cutout_width, cutout_depth).extrude(height).translate(((outer_diameter - cutout_width)/2, -(outer_diameter - cutout_depth)/4, 0)))
step7 = step7.cut(cq.Workplane("XY").rect(cutout_width, cutout_depth).extrude(height).translate((-(outer_diameter - cutout_width)/2, (outer_diameter - cutout_depth)/4, 0)))
step7 = step7.cut(cq.Workplane("XY").rect(cutout_width, cutout_depth).extrude(height).translate((-(outer_diameter - cutout_width)/2, -(outer_diameter - cutout_depth)/4, 0)))

result = step7
