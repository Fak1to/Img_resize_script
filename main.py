from PIL import Image
import glob, os

os.mkdir('Converted_imgs')

for all_img in glob.glob("*.jpg"):
    file, ext = os.path.splitext(all_img)
    with Image.open(all_img) as img:
        (width, height) = (img.width // 2, img.height // 2)
        img_resized = img.resize((width, height))
        img_resized.save('Converted_imgs/' + file + '.jpg', 'JPEG')