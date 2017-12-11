import lavavu

lv = lavavu.Viewer(quality=2)

lv.image('test.png')

#Test base64 image encoding
lvencoded = lv.image('', resolution=(250,150), transparent=False)
lv.image('small.png', resolution=(250,150), transparent=False)
with open('small.png', mode='rb') as file: # b is important -> binary
    fileContent = file.read()
    import base64
    pyencoded = 'data:image/png;base64,' + str(base64.b64encode(fileContent),'utf-8')
    if pyencoded != lvencoded:
        raise ValueError('Base64 encoded images do not match')

lv.image('test0.png', resolution=(1040,480))
lv.image('test0.jpg', resolution=(451,199))

lv.test()

lv.image('test1.jpg', resolution=(350,300))
lv.image('test1.png', resolution=(451,199), transparent=True)

lv.testimages()
