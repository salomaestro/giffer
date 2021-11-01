import imageio as im
import numpy as np
from os.path import join
from os import getcwd, listdir

class Converter:
    def __init__(self, folder_path):
        self.folder_path = folder_path
        self.filenames = self._fix_order(listdir(folder_path))
    
    def _fix_order(self, filenames):
        res = []

        for i, filename in enumerate(filenames):
            str1, str2 = filename.split("(")
            image_index, str22 = str2.split(")")

            res.append(int(image_index))
        
        numpy_filenames = np.asarray(filenames)
        sorted_result = numpy_filenames[np.argsort(res)]
        return sorted_result

    def covert(self, save_as):
        images = []
        for filename in self.filenames:
            images.append(im.imread(filename))
        im.mimsave(save_as, images)

    def _is_string(self, string):
        pass

def main():
    path = join(getcwd(), "test_img")
    ins = Converter(path)

if __name__ == "__main__":
    main()