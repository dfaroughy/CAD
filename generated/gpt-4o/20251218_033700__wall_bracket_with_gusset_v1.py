# model used: openai/gpt-4o
import cadquery as cq

# Step 1: Create the main rectangular base
step1 = cq.Workplane("XY").box(80, 70, 25)

# Step 2: Create the top rectangular feature
step2 = step1.faces(">Z").workplane().center(0, 0).rect(80, 25).extrude(25)

# Step 3: Create the triangular support
step3 = step2.faces(">Z").workplane().center(0, 0).polyline([(0, 0), (40, 25), (-40, 25)]).close().extrude(25)

# Step 4: Create the two holes
step4 = step3.faces(">Z").workplane().center(-20, 0).hole(10)
step4 = step4.faces(">Z").workplane().center(40, 0).hole(10)

# Step 5: Create the notch on the top feature
step5 = step4.faces(">Z").workplane().center(0, 0).rect(10, 5).cutBlind(-5)

# Final result
result = step5
