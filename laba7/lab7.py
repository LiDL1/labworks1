from PIL import Image, ImageFilter
def f1():

    a = "1.jpg"
    with Image.open(a) as img:
        img.load()
    img.show()
    w, h = img.size
    format = img.format
    mode = img.mode
    print('Ширина: ', w)
    print('Высота: ', h)
    print('Формат: ', format)
    print('Цветовая мода: ', mode)


def f2():

    b = '1.jpg'
    with Image.open(b) as img:
        img.load()
    img2 = img.resize((img.width // 3, img.height // 3))
    img2.save('12.jpg')


def f3():

    for i in range(1, 6):
        i = str(i)
        img = Image.open(i + '.jpg')
        img = img.filter(ImageFilter.EMBOSS)
        img.save("C:\Windows\pics" + i + ".jpg")


def f4():

    img = Image.open('6.jpg')
    wm = Image.open('4.png')
    img.paste(wm, (300, 230), wm)
    img.save('imgwm.jpg')


f3()

