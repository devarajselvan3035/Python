import math
from typing im

class SimpleRNN:
    def __init__(self, input_size, hidden_size):
        # Initialize weights with small random-ish values
        self.w_xh = [[0.1] * hidden_size for _ in range(input_size)]  # Input to Hidden
        self.w_hh = [
            [0.1] * hidden_size for _ in range(hidden_size)
        ]  # Hidden to Hidden
        self.bias = [0] * hidden_size
        self.hidden_size = hidden_size

    def sigmoid(self, x):
        return 1 / (1 + math.exp(-x))

    def forward(self, inputs):
        # Start with a hidden state of zeros (no memory yet)
        h_t = [0] * self.hidden_size

        # Process each item in the sequence
        for x_t in inputs:
            new_h = [0] * self.hidden_size
            for j in range(self.hidden_size):
                # 1. Contribution from current input
                input_part = sum(x_t[i] * self.w_xh[i][j] for i in range(len(x_t)))

                # 2. Contribution from previous hidden state (the memory)
                hidden_part = sum(
                    h_t[i] * self.w_hh[i][j] for i in range(self.hidden_size)
                )

                # 3. Combine and apply activation function
                new_h[j] = self.sigmoid(input_part + hidden_part + self.bias[j])

            h_t = new_h  # Update memory for the next step

        return h_t


# --- Usage Example ---
# Input: A sequence of 3 items, each with 2 features
sequence = [[1, 0], [0, 1], [1, 1]]
rnn = SimpleRNN(input_size=2, hidden_size=3)

output_state = rnn.forward(sequence)
print(f"Final Hidden State (Memory): {output_state}")
