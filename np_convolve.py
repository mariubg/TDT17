import numpy as np

def convolve2d(image, kernel, stride=1, padding=0):
    # Add zero padding to the input image
    if padding > 0:
        image = np.pad(image, ((padding, padding), (padding, padding)), mode='constant', constant_values=0)
    
    # Get dimensions of the image and kernel
    image_height, image_width = image.shape
    kernel_height, kernel_width = kernel.shape
    
    # Calculate the dimensions of the output image
    output_height = (image_height - kernel_height) // stride + 1
    output_width = (image_width - kernel_width) // stride + 1
    
    # Initialize the output image
    output = np.zeros((output_height, output_width))
    
    # Apply the convolution operation
    for y in range(0, output_height):
        for x in range(0, output_width):
            # Determine the region of the input image to apply the kernel on
            region = image[y*stride:y*stride+kernel_height, x*stride:x*stride+kernel_width]
            # Perform element-wise multiplication and sum the result
            output[y, x] = np.sum(region * kernel)

    
    return output

def relu(x):
    return max(0, x)
vec_relu = np.vectorize(relu)


# Example usage:
# x = np.array([[2,0,4], [1,-1,0], [-2,3,1]])
# c1 = np.array([[0,-2,1],[2,-3,0],[2,-3,-1]])
# c2 = np.array([[0,-2,1],[2,-3,0],[2,-3,-1]])

# o1 = convolve2d(x, c1, stride=1, padding=1)
# print(o1)
# o1 = vec_relu(o1)
# print(o1)


# y2 = convolve2d(o1, c2, stride=1, padding=1)
# print(y2)

# o2 = vec_relu(y2)
# print(o2)

I = np.array([[1,2,1,0,-1], [-1,0,2,3,4], [0,1,3,-1,2], [2,-1,0,1,-2], [-3,2,1,0,1]])
K = np.array([[1, 0, -1], [-1, 1, 0], [0, -1, 1]])

y = convolve2d(I, K, stride=1, padding=0)
print(y)