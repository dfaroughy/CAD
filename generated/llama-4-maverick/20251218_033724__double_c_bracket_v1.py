# model used: meta-llama/llama-4-maverick
import cadquery as cq

# Create the base plate
step1 = cq.Workplane("XY").box(120, 40, 10)

# Create the pocket sketch
pocket_sketch = (
    cq.Sketch()
    .push([(30, 0), (-30, 0)])
    .rect(40, 20)
    .reset()
    .vertices()
    .fillet(5)
)

# Cut the pockets
step2 = step1.faces(">Z").workplane().placeSketch(pocket_sketch).cutBlind(-5)

# Create the side cutout sketch
side_cutout_sketch = cq.Sketch().rect(40, 10)

# Cut the sides
step3 = (
    step2.faces(">Y")
    .workplane(centerOption="CenterOfMass")
    .placeSketch(side_cutout_sketch)
    .cutBlind(-60)
    .faces("<Y")
    .workplane(centerOption="CenterOfMass")
    .placeSketch(side_cutout_sketch)
    .cutBlind(-60)
)

result = step3
