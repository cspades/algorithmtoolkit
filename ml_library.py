import sys
import torch
from torch.nn import *
from torch.optim import AdamW
from torch.utils.data import Dataset, DataLoader
import numpy as np
from typing import Union

class MatrixFactorize(Module):
    """
    Matrix Factorization Model for Numerical Factorization and Recommender Systems
    """

    def __init__(self, M: Union[torch.Tensor, np.ndarray], dim, mask: Union[torch.Tensor, np.ndarray] = None, bias=True, seed=None):
        """
        Instantiate variables for matrix factorization, i.e. M = A * B + C.
        :param M <torch.Tensor|numpy.ndarray>:      Input 2-D matrix to factorize into A and B (with bias C).
        :param dim <int>:                           Hidden / latent dimension of matrix factorization.
        :param mask <torch.Tensor|numpy.ndarray>:   Mask matrix with shape equivalent to M. 
                                                    Non-zero implies True, while zero implies False.
        :param bias <bool>:                         Utilize bias in factorization. Set to False to exclude affine bias C.
        :param seed <int>:                          Random seed fixture for reproducibility.
        """
        super().__init__()

        # Validate matrix.
        if len(M.shape) != 2 or dim <= 0:
            print(
                f"[MatrixInputError] MatrixFactorize() only supports 2-D matrices. " +
                f"Moreover, the hidden dimension is necessarily > 0.",
                file=sys.stderr, flush=True
            )
            return None

        # Class Parameters
        self.M = torch.Tensor(M)
        self.x, self.y = self.M.shape
        self.dim = dim
        self.bias = bias
        self.mask = torch.ones(self.M.shape)
        if mask is not None and mask.shape == self.M.shape:
            # Construct Boolean mask Tensor.
            self.mask = torch.where(torch.Tensor(mask) != 0, 1, 0)

        # Fix random seed.
        if seed is not None:
            torch_gen = torch.manual_seed(seed)

        # Matrix Factors + Affine Bias
        self.A = Parameter(torch.empty((self.x, self.dim)), requires_grad=True)
        self.B = Parameter(torch.empty((self.dim, self.y)), requires_grad=True)
        self.C = Parameter(torch.empty((self.x, self.y)), requires_grad=True)
        init.xavier_uniform_(self.A)
        init.xavier_uniform_(self.B)
        init.xavier_uniform_(self.C)

        # Track training loss.
        self.loss = float('inf')

    def __repr__(self):
        """
        Output matrix factorization and approximation matrix of M.
        """

        # Avoid scientific notation.
        np.set_printoptions(suppress=True)

        # Collect information.
        output_buffer = f"\nMatrix Factorization Output (M = A * B + C)\n"
        output_buffer += f"\nTarget Matrix:\n\n{self.M.numpy()}\n"
        output_buffer += f"\nMask Matrix:\n\n{self.mask.numpy()}\n"
        output_buffer += f"\nApprox. Matrix:\n\n{self().detach().numpy().round(2)}\n"
        output_buffer += f"\nMatrix A:\n\n{self.A.detach().numpy().round(2)}\n"
        output_buffer += f"\nMatrix B:\n\n{self.B.detach().numpy().round(2)}\n"
        output_buffer += f"\nMatrix C:\n\n{self.C.detach().numpy().round(2)}\n"
        output_buffer += f"\nRegression Loss: {self.loss}\n"

        # Reset notation.
        np.set_printoptions(suppress=False)

        return output_buffer

    def forward(self):
        """
        Compute element of matrix from factorization.
        """
        
        # Compute product matrix or recommendation.
        output = torch.matmul(self.A, self.B)
        if self.bias:
            # Include affine bias.
            output += self.C
        return output

    def fit(self, cycles=1000, lr=8e-4, regularize=0.0001, patience=3, verbose=False):
        """
        Train the factorization.
        :param cycles <int>:        Number of gradient descent cycles.
        :param lr <float>:          Learning rate. Re-calibrated to order of values in matrix M.
        :param regularize <float>:  Regularization lambda for regression fit.
        :param patience <int>:      Number of cycles of convergence before termination.
        :param verbose <bool>:      Output training progress information.
        """

        # Instantiate optimizer. Tune learning rate to order of magnitude of matrix M.
        lr_calibrate = lr * self.M.sum() / torch.numel(self.M)
        optimizer = AdamW(
            self.parameters(),
            lr=lr_calibrate
        )

        # Train factorization.
        factor_opt = self.state_dict()
        timer = 0
        for i in range(cycles):

            # Clear gradients in optimizer.
            self.zero_grad()

            # Compute loss of matrix factorization.
            loss = torch.linalg.norm(
                (self() - self.M) * self.mask
            ) ** 2
            if regularize != 0:
                weight_vector = [self.A, self.B]
                if self.bias: weight_vector.append(self.C)
                for weight in weight_vector:
                    loss += regularize * torch.linalg.norm(weight) ** 2

            # Validate training.
            if i % 100 == 0 and verbose:
                print(
                    f"Training Cycle: {i+1} / {cycles} | Factorization Loss: {loss.item()}",
                    file=sys.stdout, flush=True
                )
            if loss.item() < self.loss:
                # Update optimal factorization.
                factor_opt = self.state_dict()
                # Update optimal loss.
                self.loss = loss.item()
                # Reset patience timer.
                timer = 0
            else:
                # Increment patience timer.
                timer += 1
                if timer > patience:
                    # Model convergence. Revert to optimal factorization. Terminate training.
                    self.load_state_dict(factor_opt)
                    break

            # Back-propagate.
            loss.backward()

            # Apply gradients.
            optimizer.step()


class AutoRec(Module):
    """
    Auto-Encoding Recommendation Neural Network
    """

    def __init__(self) -> None:
        """
        Instantiate class attributes for AutoRec.
        """
        super().__init__()