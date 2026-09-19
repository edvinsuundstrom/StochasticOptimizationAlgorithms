import math
import matplotlib.pyplot as plt

# ==============================
# compute_gradient function:
# ==============================


def compute_gradient(x, mu):
    x1, x2 = x[0], x[1]
    g = x1**2 + x2**2 - 1

    if g <= 0:
      grad_1 = 2 * (x1 - 1)
      grad_2 = 4 * (x2 - 2)
    else:
      grad_1 = 2 * (x1 - 1) + 4 * mu * x1 * g
      grad_2 = 4 * (x2 - 2) + 4 * mu * x2 * g

    return [grad_1, grad_2]


# ==============================
# run_gradient_descent function:
# ==============================


def run_gradient_descent(x_start, mu, eta, gradient_tolerance):
    x = list(x_start)

    while True:
      grad = compute_gradient(x, mu)
      grad_norm = math.sqrt(grad[0] ** 2 + grad[1] ** 2)

      if grad_norm < gradient_tolerance:
        return x

      x[0] -= eta * grad[0]
      x[1] -= eta * grad[1]


# ==============================
# Main program:
# ==============================

mu_values = [1, 10, 100, 1000]
eta = 0.0001
x_start = [1.0, 2.0]
gradient_tolerance = 1e-6

results_x1 = []
results_x2 = []

for mu in mu_values:
    x_start = run_gradient_descent(x_start, mu, eta, gradient_tolerance)
    results_x1.append(x_start[0])
    results_x2.append(x_start[1])
    print(f"x = ({x_start[0]:.4f}, {x_start[1]:.4f}), mu = {mu:.1f}")

# Simple plot:

plt.plot(mu_values, results_x1, label="x1")
plt.plot(mu_values, results_x2, label="x2")
plt.xscale("log")
plt.xlabel("mu")
plt.ylabel("x values")
plt.legend()
plt.show()