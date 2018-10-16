import numpy as np
import torch
import torch.nn as nn
from torch.autograd import Variable
from pytorch2keras.converter import pytorch_to_keras


class TestConst(nn.Module):
    """Module for Const conversion testing
    """

    def __init__(self, inp=10, out=16, bias=True):
        super(TestConst, self).__init__()
        self.linear = nn.Linear(inp, out, bias=False)

    def forward(self, x):
        x = self.linear(x) * 2.0
        return x


if __name__ == '__main__':
    max_error = 0
    for i in range(100):
        inp = np.random.randint(1, 100)
        out = np.random.randint(1, 100)
        model = TestConst(inp, out, inp % 2)

        input_np = np.random.uniform(0, 1, (1, inp))
        input_var = Variable(torch.FloatTensor(input_np))

        output = model(input_var)

        k_model = pytorch_to_keras(model, input_var, (inp,), verbose=True)

        pytorch_output = output.data.numpy()
        keras_output = k_model.predict(input_np)

        error = np.max(pytorch_output - keras_output)
        print(error)
        if max_error < error:
            max_error = error

    print('Max error: {0}'.format(max_error))
