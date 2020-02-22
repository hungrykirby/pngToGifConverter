from PIL import Image
import glob

files = sorted(glob.glob('./images/frames/*.png'))
# print(files)
images = list(map(lambda file: Image.open(file), files))

images[0].save('./images/output/out.gif', save_all=True, append_images=images[1:], duration=20, loop=0)