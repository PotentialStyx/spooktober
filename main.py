from PIL import Image
import numpy
import blend_modes

inp = Image.open("in.png").convert("L").convert("RGBA")
color = Image.new('RGB', (inp.width, inp.height), (77, 25, 0)).convert("RGBA")

new = numpy.uint8(blend_modes.hard_light(numpy.array(inp).astype(float), numpy.array(color).astype(float), 0.91))

Image.fromarray(new).save("out.png")
