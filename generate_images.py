from PIL import Image


def generate(width, height, rgb_color=None, save=False, name=None, format='png'):
    width = 300 if not width else width
    height = height if height else 300
    rgb_color = (250, 0, 0) if not rgb_color else rgb_color
    img = Image.new("RGB", (width, height), rgb_color)  # 产生一张图片
    img.format = format
    if save:
        name = f'demo.{format}' if not name else name
        img.save(name)
    return img


def gen_many():
    pass


if __name__ == '__main__':
    t = generate(100, 100)
    print(t.format)

    # generate(100, 100, (0, 0, 0), save=True)  # black
    # generate(100, 100, (255, 0, 0), save=True)  # red
    # generate(100, 100, (0, 255, 0), save=True)  # green
    # generate(100, 100, (0, 0, 255), save=True)  # blue
    # generate(100, 100, (255, 255, 0), save=True)  # yellow
    # generate(100, 100, (255, 0, 255), save=True)  # pink
    # generate(100, 100, (0, 255, 255), save=True)  # green_blue
    # generate(100, 100, (255, 255, 255), save=True)  # white
