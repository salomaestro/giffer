import imageio
import os

def make_gif(folder_name, save_as):

    filenames = ["img (" + str(i) + ").png" for i, _ in enumerate(os.listdir(os.path.join(cwd, folder_name)))]
    images = []
    for filename in filenames:
        images.append(imageio.imread(os.path.join(folder_name, filename)))

    imageio.mimsave(os.path.join(cwd, save_as), images)

if __name__ == "__main__":
    cwd = os.getcwd()

    save_as = "new_gif.gif"
