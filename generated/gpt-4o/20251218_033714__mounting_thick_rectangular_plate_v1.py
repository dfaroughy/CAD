# model used: openai/gpt-4o
import cadquery as cq

# Step 1: Create the base box
step1 = cq.Workplane("XY").box(120, 80, 25)

# Step 2: Create the holes
# Center hole
step2 = step1.faces(">Z").workplane().hole(20)

# Four corner holes
step3 = step2.faces(">Z").workplane().pushPoints([
    (-40, -25), (40, -25), (-40, 25), (40, 25)
]).hole(10)

# Step 4: Create the counterbores
# Center counterbore
step4 = step3.faces(">Z").workplane().cboreHole(20, 30, 5)

# Four corner counterbores
result = step4.faces(">Z").workplane().pushPoints([
    (-40, -25), (40, -25), (-40, 25), (40, 25)
]).cboreHole(10, 20, 5)
