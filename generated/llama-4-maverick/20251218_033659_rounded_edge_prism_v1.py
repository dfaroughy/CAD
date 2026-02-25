# model used: meta-llama/llama-4-maverick
python
import cadquery as cq

step1 = cq.Workplane("XY").box(60, 40, 20).edges("|Z").fillet(5)
step2 = step1.faces(">Z").workplane().rect(40, 20).cutBlind(-10)
step3 = step2.faces(">Z").workplane().circle(5).cutThruAll()
result = step3
```
