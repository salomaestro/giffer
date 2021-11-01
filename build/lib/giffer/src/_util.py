import imageio
import os

def make_gif(folder_name: str, save_as: str) -> None:
    """ 
    Makes a gif from a collection of png images in an array where image names are of the form: img (i).png for i = 0, i -> N.

    Parameters:
        folder_name: string
            Name of the folder containing images which are to be converted into a gif.
        save_as: string
            Name of final gif file, with absolute path. Must be of the form: ../my_video.gif
    """

    filenames = ["img (" + str(i) + ").png" for i, _ in enumerate(os.listdir(folder_name))]
    images = []
    for filename in filenames:
        images.append(imageio.imread(os.path.join(folder_name, filename)))

    imageio.mimsave(save_as, images)
