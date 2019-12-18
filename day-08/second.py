with open('data/data.txt') as data:
    image = data.readline()

width = 25
height = 6
pixelsPerImage = width * height

layers = [image[i:i + pixelsPerImage] for i in range(0, len(image), pixelsPerImage)]
renderedImage = ''
for i in range(pixelsPerImage):
    value = '2'
    layerIndex = 0
    while value == '2':
        value = layers[layerIndex][i]
        layerIndex += 1
    renderedImage += value

renderedImage = renderedImage.replace('0', ' ')
renderedImage = renderedImage.replace('1', '#')

for i in range(0, pixelsPerImage, width):
    print(renderedImage[i:i + width])
