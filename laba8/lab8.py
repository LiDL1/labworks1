from PIL import Image, ImageDraw, ImageFont


def zd18():
    p = Image.open('6.JPG')
    p2 = p.crop((20, 20, 440, 440))
    p2.show()
    p2.save('p2.JPG')
zd18()


def zd28():
    otkr = {
        '8 марта': '7.JPG',
        '23 февраля': '8.JPG',
        'новый год': '9.JPG',
        '14 февраля': '10.JPG',
        'день рождения': '11.JPG'
    }
    o = []
    prazd = input('Введите название праздника:')
    if prazd in otkr:
        card = Image.open(otkr[prazd])
        card.show()
    else:
        print('Открытки к данному празднику нет')
zd28()


def zd38():
    name = input('Как зовут того, кого вы хотите поздравить?') + ' ,поздравляю!'
    p = Image.open('6.JPG')
    p2 = p.crop((20, 20, 440, 440))
    draw = ImageDraw.Draw(p2)
    font = ImageFont.truetype('arial.ttf', 36)
    draw.text((50, 50), name, font=font, fill=(255, 0, 0))
    p2.save('p3.PNG')
    p2.show()


zd38()

