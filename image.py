image = [
    [1, 1, 0, 0, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 1, 1, 0],
    [0, 0, 1, 1, 0],
    [0, 0, 0, 0, 1]
]

# Example 2x2 filter (kernel)
filter = [
    [1, 0],
    [0, -1]
]

# Step 1: Convolution (valid padding, stride = 1)
def convolve2d(image, kernel):
    kernel_size = len(kernel)
    output_size = len(image) - kernel_size + 1
    output = []
    for i in range(output_size):
        row = []
        for j in range(output_size):
            val = 0
            for ki in range(kernel_size):
                for kj in range(kernel_size):
                    val += image[i+ki][j+kj] * kernel[ki][kj]
            row.append(val)
        output.append(row)
    return output

# Step 2: ReLU activation
def relu(matrix):
    return [[max(0, x) for x in row] for row in matrix]

# Step 3: Flatten
def flatten(matrix):
    return [x for row in matrix for x in row]

# Step 4: Fully connected layer (1 output neuron, simple weights + bias)
def dense_layer(inputs, weights, bias):
    output = 0
    for i in range(len(inputs)):
        output += inputs[i] * weights[i]
    output += bias
    return output

# Apply the CNN steps
conv_output = convolve2d(image, filter)
relu_output = relu(conv_output)
flat_output = flatten(relu_output)

# Simulated weights and bias for classification
weights = [0.5 for _ in flat_output]  # simple constant weights
bias = -2

# Classification score (logits, could apply softmax manually)
score = dense_layer(flat_output, weights, bias)

# Output result
print("Convolved Feature Map:")
for row in conv_output:
    print(row)

print("\nAfter ReLU Activation:")
for row in relu_output:
    print(row)

print("\nFlattened Vector:", flat_output)
print("\nClassification Score:", score)
print("Prediction:", "Class A" if score > 0 else "Class B")
