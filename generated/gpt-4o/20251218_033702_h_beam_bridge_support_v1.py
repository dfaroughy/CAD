# model used: openai/gpt-4o
import cadquery as cq

# Step 1: Create the base block
step1 = cq.Workplane("XY").box(80, 10, 10)

# Step 2: Create the top block
step2 = step1.faces(">Z").workplane().box(80, 10, 10)

# Step 3: Create the middle connecting block
step3 = step2.faces(">Z").workplane(offset=-10).box(30, 10, 10)

# Step 4: Create the cutouts on the top and bottom blocks
step4 = step3.faces("<Z").workplane(offset=5).rarray(20, 1, 4, 1).circle(5).cutThruAll()

# Step 5: Create the cutouts on the middle block
step5 = step4.faces(">Z").workplane(offset=-5).rarray(20, 1, 2, 1).circle(5).cutThruAll()

# Step 6: Create the holes on the ends
step6 = step5.faces(">Y").workplane().rarray(80, 1, 2, 1).circle(5).cutThruAll()

# Assign final geometry to result
result = step6
