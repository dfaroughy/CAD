# model used: meta-llama/llama-4-maverick
python
import cadquery as cq

# Create the base plate
step1 = cq.Workplane("XY").box(50, 50, 5)

# Create the large center hole
step2 = step1.faces(">Z").workplane().circle(12.5).cutThruAll()

# Create the four smaller holes
step3 = (
    step2.faces(">Z")
    .workplane()
    .pushPoints([(15, 15), (-15, 15), (-15, -15), (15, -15)])
    .circle(5)
    .cutThruAll()
)

# Create the four corner holes
step4 = (
    step3.faces(">Z")
    .workplane()
    .pushPoints([(15, 15), (-15, 15), (-15, -15), (15, -15)])
    .circle(7.5)
    .cutThruAll()
)

# Assign the final geometry to result
result = step4
```
