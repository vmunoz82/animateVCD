from animateVCD import TextReplacer, StyleReplacer, compareBitField, convertBinStrToInt
animators = []

# add the animators. The svg_id matches the ID in the SVG file, and the vcd_id is the name of the data in the VCD file
# 1 for the counter
animators.append(
    TextReplacer(svg_id='count', vcd_id='counter', conversion=convertBinStrToInt()))

# 1 for each segment in the display
for bit in range(10):
    animators.append(
        StyleReplacer(svg_id='seg%d' % bit, vcd_id='segs', replace=('fill:none', 'fill:red'), compare=compareBitField(bit)))

# how many frames 
frames = 16

# files
svg_file = "7seg.svg"
vcd_file = "test.vcd"
