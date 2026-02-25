# model used: meta-llama/llama-4-maverick
import cadquery as cq

# Define the dimensions
outer_diameter = 50
height = 45
inner_diameter = 30
protrusion_width = 45
protrusion_height = 50
protrusion_thickness = 15
notch_width = 10
notch_height = 10

# Step 1: Create the main cylinder
step1 = cq.Workplane("XY").circle(outer_diameter/2).extrude(height)

# Step 2: Create the inner cylinder
step2 = cq.Workplane("XY").circle(inner_diameter/2).extrude(height)

# Step 3: Subtract the inner cylinder from the main cylinder
step3 = step1 - step2

# Step 4: Create the protrusion
step4 = cq.Workplane("XZ").box(protrusion_width, protrusion_thickness, protrusion_height).translate((0, outer_diameter/2 + protrusion_thickness/2, 0))

# Step 5: Union the protrusion with the main cylinder
step5 = step3.union(step4)

# Step 6: Create the notch
step6 = cq.Workplane("YZ").box(notch_width, protrusion_thickness, notch_height).translate((0, outer_diameter/2 + protrusion_thickness/2, height/2 - notch_height/2))

# Step 7: Subtract the notch from the main body
step7 = step5 - step6

# Step 8: Create the opposite notch
step8 = step7 - step6.rotate((0,0,0), (0,0,1), 180)

result = step8
