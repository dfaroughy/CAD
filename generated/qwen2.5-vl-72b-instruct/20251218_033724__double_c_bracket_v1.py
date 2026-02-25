# model used: qwen/qwen2.5-vl-72b-instruct
import cadquery as cq

step1 = cq.Workplane("XY").box(120, 40, 10)

step2 = step1.faces("<Z").workplane().rect(20, 30).cutThruAll()

step3 = step2.faces("<Z").workplane().center(40, 0).rect(20, 30).cutThruAll()

result = step3
