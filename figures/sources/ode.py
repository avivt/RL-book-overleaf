# matplotlib.use('macosx')
import numpy as np
import matplotlib.pyplot as plt


# Make R a 2D rotation matrix by pi/4
theta = -np.pi/4
R = np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])

# Define the matrix A and initial vector x0
A0 = np.array([[-0.1, -5], [0.1, -1]])
x0 = np.array([[0], [1]])

# Set A to be R A0 R^{-1}
A = np.dot(np.dot(R, A0), np.linalg.inv(R))
print(A)

B = 0.9 * np.array([[-1, -1], [0, -1]])
print(B)
# Number of iterations
num_iterations = 100

# Time step
dt = 0.2

# Initialize an array to store the iterates
iterates = np.zeros((2, num_iterations+1))
iterates[:, 0] = x0.flatten()

iterates_2 = np.zeros((2, num_iterations+1))
iterates_2[:, 0] = x0.flatten()

# Compute the iterates
for t in range(num_iterations):
    iterates[:, t+1] = iterates[:, t] + dt * np.dot(A, iterates[:, t])
    iterates_2[:, t+1] = iterates_2[:, t] + dt * np.dot(B, iterates_2[:, t])

# Plot the iterates
plt.plot(iterates[0, :], iterates[1, :], 'o-', markersize=3)
plt.plot(iterates_2[0, :], iterates_2[1, :], 'ro-', markersize=3)
plt.legend(['$A_{no-contraction}$', '$A_{contraction}$'])
plt.xlabel('$X_1$')
plt.ylabel('$X_2$')
plt.xlim(-2.5, 2.5)
plt.ylim(-2.5, 2.5)
plt.text(0, 1, r'$X_0$', fontsize=12)
plt.text(0, 0, r'$X^*$', fontsize=12)
# plt.axis('equal')
plt.title('Iterates of $X_{t+1} = A X_{t}$')
plt.grid(True)
plt.savefig('/Users/aviv/Repositories/scripts/ode.png')