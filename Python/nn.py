import math
import numpy as np

def sigmoid(x):
  return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x+(1-x)


class neuron():
    def __init__(self,inputWeight,outputWeight,nInput,nOutput):
        self.inputWeight = inputWeight
        self.outputWeight = outputWeight
        self.input=nInput
        self.output = nOutput
    def process(self):
        pass




def main():
    training_inputs = np.array([
        [0,0,1],
        [1,1,1],
        [1,0,1],
        [0,1,1]]
    )
    training_outputs = np.array([[0,1,1,0]]).T
    np.random.seed(1)
    synaptic_weights = 2*np.random.random((3,1))-1

    print("random starting synaptic weights: \n",synaptic_weights)

    for i in range(20000):
        input_layer = training_inputs

        outputs = sigmoid(np.dot(input_layer,synaptic_weights))

        error=training_outputs - outputs
        
        adjustments = error * sigmoid_derivative(outputs)

        synaptic_weights += np.dot(input_layer.T, adjustments )
    print("synaptic weights after training: \n", synaptic_weights)
    print("outputs after training: \n", outputs)

    error=training_outputs-outputs
    adjustments = error*sigmoid_derivative(outputs)



if __name__ == "__main__":
    main()