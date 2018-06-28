import matplotlib.pyplot as plt

class PlotUtils(object):

    @staticmethod
    def plot_2d_array(data):
        assert len(data.shape) == 2, "Only 2d images"

        fig, ax = plt.subplots()
        cax = ax.imshow(data, interpolation=None, cmap='inferno')
        cbar = fig.colorbar(cax, orientation='vertical')
        plt.show()

    @staticmethod
    def plot_3d_array(data):
        assert len(data.shape) == 3, "Only 3d images"

        fig = plt.figure()
        fig.add_subplot(1, 3, 1)
        plt.imshow(data[0])
        plt.colorbar()
        fig.add_subplot(1, 3, 2)
        plt.imshow(data[1])
        plt.colorbar()
        fig.add_subplot(1, 3, 3)
        plt.imshow(data[2])
        plt.colorbar()

        plt.show()