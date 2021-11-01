import os

from giffer import make_gif

path = os.path.dirname(__file__)
img_folder = os.path.join(path, "test_images")

save_as = os.path.join(path, "giftest.gif")

make_gif(img_folder, save_as)