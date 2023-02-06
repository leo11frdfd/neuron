class Neuron():
    def __init__(self):
        self.weight = 0.01
        self.last_error = 1.1
        self.smoothing = 0.001

    def get_last_error(self):
        return self.last_error

    def get_smoothing(self):
        return self.smoothing

    def get_weight(self):
        return self.weight


    def process_input_data(self, input_data):
        return input_data * self.weight

    def train(self, input, expected_result):
        result_now = input * self.weight
        self.last_error = expected_result - result_now
        correction = self.last_error / result_now
        correction = correction * self.smoothing
        self.weight += correction

    def check_training(self):
        if (self.last_error > self.smoothing or self.last_error < -self.smoothing):
            return True
        else:
            return False


 491.41
iteration = 1
while (Neuron.check_training()):
    Neuron.train(input, expected_result)
    #print("Iteration: " + str(iteration) + " weight:|" + str(neuron.get_weight()))
    iteration += 1

print("--Successful training--")
print(Neuron.get_weight())
print(Neuron.get_last_error())
print(Neuron.get_smoothing())