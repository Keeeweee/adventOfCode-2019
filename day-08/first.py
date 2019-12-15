with open('data/data.txt') as data:
    image = data.readline()

width = 25
height = 6
pixelsPerImage = width * height

layers = [image[i:i + pixelsPerImage] for i in range(0, len(image), pixelsPerImage)]

count = layers[0].count('0')
chosen = layers[0]

for layer in layers:
    zeroCount = layer.count('0')
    if zeroCount < count:
        count = zeroCount
        chosen = layer

print(chosen.count('1') * chosen.count('2'))