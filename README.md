# IMAGE-CLASSIFICATION-MODEL

COMPANY : CODTECH IT SOLUTIONS

NAME : B.Yaswanth Kumar

INTERN ID : CT06DZ363

DOMAIN : MACHINE LEARNING

DURATION : 6 WEEKS

MENTOR : NEELA SANTHOSH

**This task involves implementing a basic Convolutional Neural Network (CNN) from scratch using only core Python, without relying on

any external libraries such as TensorFlow, PyTorch, or NumPy. The primary goal is to understand and simulate how core components of a CNN work under

the hood by using simple constructs like lists, loops, and basic math operations. This educational exercise is particularly useful for beginners and those

looking to strengthen their conceptual understanding of convolutional networks.

CNNs are widely used in image classification, object detection, and other visual recognition tasks due to their ability to capture spatial hierarchies in images.

In real-world scenarios, CNNs are built using advanced libraries that abstract away the mathematical and computational complexity.

However, this task simplifies a CNN into its fundamental parts to help demystify how it works internally.

Dataset: Instead of using a large dataset, this task works with a single, hardcoded 5×5 grayscale image, represented as a 2D list. Each pixel value ranges from 0 to 1, where:

1 indicates the presence of a feature (like an edge or object), and

0 represents the background or no signal.

This small image is manually crafted to simulate a basic pattern that can be detected through convolution.

CNN Architecture Breakdown: The CNN implemented here has the following layers and functions:

Convolution Layer The convolution operation is implemented using nested loops that slide a 2×2 kernel (filter) across the input image. For each position,
the overlapping values of the image and the kernel are multiplied and summed to produce a new feature map. This process helps detect local patterns like edges or corners in the image.

ReLU Activation Function The Rectified Linear Unit (ReLU) is a widely used activation function in CNNs. It introduces non-linearity by setting all negative values to zero and retaining positive values.
This allows the network to learn complex patterns. In this task, ReLU is applied element-wise on the convolution output.

Flattening Layer The 2D feature map resulting from the ReLU layer is converted into a 1D list. This is necessary before feeding the data into a fully connected (dense) layer, as dense layers require vector input.

Fully Connected Layer The flattened output is passed to a dense layer, which applies a weighted sum of inputs plus a bias term.

Here, the weights are simply initialized to a constant value (0.5), and the bias is set to -2.

This layer computes a classification score (logit) that determines the class of the input image.

Logic: After computing the score from the fully connected layer, a basic threshold is applied to make a binary classification:

if the score is greater than 0, the image is predicted as Class A. Otherwise, it's predicted as Class B.

This classification logic, while extremely simplified, mimics the decision boundary of a real classifier trained via gradient descent and backpropagation.

Although this model is not trained using real data and does not generalize beyond the example input, it serves as a foundational exercise to explore the principles of CNNs.

**OUTPUT:**

<img width="1920" height="1020" alt="Image" src="https://github.com/user-attachments/assets/62602091-14a8-4a27-ba8c-6b2f782d23a3" />

