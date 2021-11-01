import imageio
import numpy as np
import matplotlib.pyplot as plt
import os
from os.path import dirname, join
from _util import make_gif

class Gif:
    """
    All inclusive Gif object.

    Parameters:
        path: string
            String which a temporary directory will save frames as .png images before combining to a standalone .gif.
    """
    def __init__(self, path:str):
        self.path = path
        self.tempdir = join(path, "temp_img")
        self.i = 0
        self._make_temp_dir()

    def _make_temp_dir(self):
        """ Creates a temporary image directory """
        try:
            os.makedirs(self.tempdir)
        except OSError as e:
            print("Error: %s : %s" % (self.tempdir, e.strerror))

    def _remove_temp_dir(self):
        """ Destroys the temporary image directory """
        try:
            # remove contents of temp directory then the directory itself
            for elem in os.listdir(self.tempdir):
                os.remove(join(self.tempdir, elem))
            os.rmdir(self.tempdir)
        except OSError as e:
            print("Error: %s : %s" % (self.tempdir, e.strerror))

    def frame(self) -> None:
        """
        Add a frame to the gif! Use this function inside a plot-updating loop.

        Utilizes matplotlib's pyplot.savefig() to temporarily save images from a iterating frame.
        """
        plt.savefig(join(self.tempdir, "img (" + str(self.i) + ").png"))
        self.i += 1

    def save(self, gifname:str) -> None:
        """ 
        Save and combine .png's into a .gif.
        Utilizes this modules make_gif() function.

        Parameters:
            gifname: string
                The final name of the constructed gif-file. Use .gif at the end.
        """
        make_gif(self.tempdir, join(gifname))
        self._remove_temp_dir()