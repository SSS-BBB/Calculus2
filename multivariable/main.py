from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import numpy as np
import math

class Var2FunctionClass:
    def __init__(self, func: callable):
        self.func = func

        self.X = np.array([])
        self.Y = np.array([])
        self.Z = np.array([])

        self.start = 0
        self.end = 0
        self.step = 0

    def compute(self, a: float = 1, b: float = 100, step: float = 0.1):
        start = a
        end = b
        if a > b:
            start = b
            end = a

        # create x, y plane
        self.X = np.arange(start, end + step, step)
        self.Y = np.arange(start, end + step, step)
        self.X, self.Y = np.meshgrid(self.X, self.Y)

        # calculate
        self.Z = self.func(self.X, self.Y)

        # set var
        self.start = start
        self.end = end
        self.step = step

        # x_list = []
        # y_list =[]
        # n = int( ((end-start)/step) + 1 )
        # for x in np.arange(start, end + step, step):
        #     x_list += [x] * n
        #     y_list += list(np.arange(start, end + step, step))

        # self.x_container = np.array(x_list)
        # self.y_container = np.array(y_list)

        # calculate with numpy
        # self.z_container = self.func(self.x_container, self.y_container)

        return self.Z
    
    def plot3D(self, ax3d):
        ax3d.plot_surface(self.X, self.Y, self.Z)

    def contour_plot(self, ax2d, K: list, contour_func: callable):
        for k in K:
            X_contour = np.arange(self.start, self.end + self.step, self.step) # x for contour
            Y_contour = contour_func(k, X_contour) # y for contour
            contour_label = "K = " + str(k)
            ax2d.plot(X_contour, Y_contour, label=contour_label)
    



def test():
    print(np.arange(1, 100+1, 1))

def two_var(x, y):
    return (x-3*y) ** 2

def contour(k, x):
    return (x-math.pow(k, 0.5)) / 3

def main():
    # defining plot
    fig = plt.figure()
    ax3d = fig.add_subplot(1, 2, 1, projection="3d")
    ax2d = fig.add_subplot(1, 2, 2)

    # 2 var function
    testFunc = Var2FunctionClass(two_var)
    testFunc.compute()
    testFunc.plot3D(ax3d)

    # contour plot
    testFunc.contour_plot(ax2d, [1, 100, 1000], contour_func=contour)

    plt.legend()
    plt.show()

# test()
main()