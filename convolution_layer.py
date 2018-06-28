from enum import Enum

import numpy as np

class ConvolutionLayerOptions(Enum):
        FEATURE_SHAPE = 1,
        STRIDE = 2

class ConvolutionLayer(object):

    DEFAULT_NUMBER_OF_FEATURES = 12
    DEFAULT_FEATURE_WIDTH = 3
    DEFAULT_FEATURE_HEIGHT = 3
    DEFAULT_FEATURE_DEPTH = 1
    DEFAULT_STRIDE = 1

    def __init__(self, options):
        super(ConvolutionLayer, self).__init__()
        self.options = options

        #this includes as first axis, the ammount of features
        self.features_shape = self.options.get(
            ConvolutionLayerOptions.FEATURE_SHAPE,
            (
                self.DEFAULT_NUMBER_OF_FEATURES,
                self.DEFAULT_FEATURE_WIDTH,
                self.DEFAULT_FEATURE_HEIGHT,
                self.DEFAULT_FEATURE_DEPTH
            )
        )

        self.stride = self.options.get(ConvolutionLayerOptions.STRIDE, self.DEFAULT_STRIDE)

        #randomize features
        self.features = np.random.uniform(
            low=-1,
            high=1,
            size=self.features_shape
        )

    def forward(self, image):
        assert len(image.shape) == 3, "As input is expected a single image, which are (MxNx3)"

        #calculate the space for the output of the convolution
        image_count = images.shape[0]
        out_cols = int(np.ceil((images.shape[1] - self.features_shape[1] + 1)/self.stride))
        out_rows = int(np.ceil((images.shape[2] - self.features_shape[2] + 1)/self.stride))
        features_count = self.features_shape[1]

        #reserve space for output
        output = np.zeros((image_count, features_count, out_cols, out_rows))

        for i in range(out_cols):
            for j in range(out_rows):
                col_start = i * self.stride
                col_end = col_start + self.features_shape[1]
                row_start = j * self.stride
                row_end = row_start + self.features_shape[2]

                w_x = images[:, col_start:col_end, row_start:row_end, :] * self.features
                print('w_x')
                print(w_x)
                print('w_x.shape')
                print(w_x.shape)
                break
                output[:, i, j, :] = np.sum(
                    w_x,
                    axis=(3,4)
                )
            break
        #at this point we have the 3-dimensional output, let's flatten it
        return np.sum(output, axis=(3))

if __name__ == '__main__':
    main()