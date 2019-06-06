import random

values = ['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15']
value_dict = [['A','10'],['B','11'],['C','12'],['D','13'],['E','14'],['F','15']]
start = "#"

def contrastcolor(color):
    if color[0] == '#':
        color = color[1:]
    rgb = (color[0:2], color[2:4], color[4:6])
    comp = ['%02X' % (255 - int(a, 16)) for a in rgb]
    return ''.join(comp)

def startcolor():
    color = "#"
    for i in range(6):
        x = values[random.randint(0,len(values)-1)]

        for thing in value_dict:
            if x == thing[1]:
                x = thing[0]
        color = color + x
    return color

base = startcolor()
contrast = start + contrastcolor(base)

print("The colors: {0}".format([base, contrast]))