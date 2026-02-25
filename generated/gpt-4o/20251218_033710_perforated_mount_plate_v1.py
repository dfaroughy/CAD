# model used: openai/gpt-4o
import cadquery as cq

# Step 1: Create the base plate
step1 = cq.Workplane("XY").box(120, 80, 5)

# Step 2: Create the holes
# Hole positions based on the drawing
hole_positions = [
    (-40, 20),  # Top left
    (0, 20),    # Top center
    (40, 20),   # Top right
    (-40, -20), # Bottom left
    (40, -20)   # Bottom right
]

# Step 3: Drill the holes
step2 = step1.faces(">Z").workplane().pushPoints(hole_positions).hole(10)

# Final result
result = step2
