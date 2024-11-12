from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import numpy as np

class Var2FunctionClass:
    def __init__(self, func: callable):
        self.func = func

        self.x_container = np.array([])
        self.y_container = np.array([])
        self.z_container = np.array([])

    def compute(self, a: float = 1, b: float = 100):
        start = a
        end = b
        if a > b:
            start = b
            end = a

        # create x, y plane
        x_list = []
        y_list =[]
        n = end - start + 1
        for x in range(start, end + 1):
            x_list += [x] * n
            y_list += range(start, end + 1)

        self.x_container = np.array(x_list)
        self.y_container = np.array(y_list)

        # calculate with numpy
        self.z_container = self.func(self.x_container, self.y_container)

        return self.z_container
    
    def plot3D(self, ax3d):
        ax3d.plot3D(self.x_container, self.y_container, self.z_container)
    



def two_var(x, y):
    return x * y

# defining plot
fig = plt.figure()
ax3d = plt.axes(projection = "3d")

# 2 var function
TestFunc = Var2FunctionClass(two_var)
TestFunc.compute()
TestFunc.plot3D(ax3d)

plt.show()