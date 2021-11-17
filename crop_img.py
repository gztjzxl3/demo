from testing.generate_a_image import generate
from PIL import Image
img = Image.open('1.jpg')
# img = generate(300, 1610)


# print(img.format)
# res = img.crop((0, 0, 100, 100))
# res.show()
class CropImage:
    def __init__(self):
        pass

    def check_black(self, img):  # 检测黑屏
        pass

    # def check_bottom(self, img):
    #     print(img.bottom)

    def avr_crop(self, img, copy_count=None):
        """如果没有指定份数，就按照800左右的长度截（如果800能平均截就按800，不能就调整平均）"""
        if not copy_count:
            cut_length = 800  # 按800像素长度截取
        else:
            # 如果指定了份数，
            cut_length = img.height / copy_count  # 取平均长度
        self.crop_img(img, cut_length)

    def crop_img(self, img, length=800, img_name=''):
        img_format = img.format
        img_width = img.width
        start_y = 0
        number = 1
        # img_name = f'test_{number}.{img_format}' if not img_name else img_name
        # try:
        while True:
            if start_y > img.height:
                break
            img_name = f'test_{number}.{img_format}'
            print(number)
            res = img.crop((0, start_y, img_width, start_y + length))
            res.save(img_name)
            start_y += length
            number += 1

        # except Exception as e:
        #     print(e)


if __name__ == '__main__':
    import os
    def clear():
        for i in os.listdir():
            if i.startswith('test_'):
                os.remove(i)
    # clear()
    crop = CropImage()
    # crop.crop_img(img, length=800)
    crop.avr_crop(img)
    # crop.avr_crop(img,copy_count=)
