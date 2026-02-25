# model used: openai/gpt-5.1-codex
import cadquery as cq

step1 = cq.Workplane("XY").circle(6/2).extrude(20)
result = step1
