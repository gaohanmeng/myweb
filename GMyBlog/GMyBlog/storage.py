from io import BytesIO

from django.core.files.storage import FileSystemStorage
from django.core.files.uploadedfile import InMemoryUploadedFile

from PIL import Image, ImageDraw, ImageFont


class WatermarkStorage(FileSystemStorage):
    def save(self, name, content, max_length=None):
        if 'image' in content.content_type:
            image = self.watermark_with_text(content, 'gaohanmeng', 'blue')  # 加水印
            content = self.convert_image_to_file(image, name)

        return super().save(name, content, max_length=max_length)

    def convert_image_to_file(self, image, name):
        temp = BytesIO()
        image.save(temp, format='PNG')
        file_size = temp.tell()
        return InMemoryUploadedFile(temp, None, name, 'image/png', file_size, None)

    def watermark_with_text(self, file_obj, text, color, fontfamily=None):
        image = Image.open(file_obj).convert('RGBA')
        draw = ImageDraw.Draw(image)
        width, height = image.size
        margin = 10
        if fontfamily:  # fontfamily 参数可以自己定义字体样式
            font = ImageFont.truetype(fontfamily, int(height / 20))
        else:
            font = None

        text_width, text_height = draw.textsize(text, font)
        x = (width - text_width - margin) / 2  # 计算横轴位置
        y = height - text_height - margin  # 计算纵轴位置
        draw.text((x, y), text, color, font)
        return image
