from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import numpy as np

class Var2FunctionClass:
    def __init__(self, func: callable):
        self.func = func

        self.X = np.array([])
        self.Y = np.array([])
        self.Z = np.array([])

    def compute(self, a: float = 1, b: float = 100, step: float = 1):
        start = a
        end = b
        if a > b:
            start = b
            end = a

        # create x, y plane
        self.X = np.arange(start, end, step)
        self.Y = np.arange(start, end, step)
        self.X, self.Y = np.meshgrid(self.X, self.Y)

        # calculate
        self.Z = self.func(self.X, self.Y)

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
        ax3d.plot3D(self.X, self.Y, self.Z)
    



def test():
    print(np.arange(1, 100+1, 1))

def two_var(x, y):
    return x * y

def main():
    # defining plot
    fig = plt.figure()
    ax3d = plt.axes(projection = "3d")
    # ax2d = plt.axes()

    # 2 var function
    TestFunc = Var2FunctionClass(two_var)
    TestFunc.compute(a = 1, b = 100, step=0.1)
    TestFunc.plot3D(ax3d)

    # contour plot
    # ax2d.plot([1, 2, 3], [4, 5, 6])

    plt.show()

# test()
main()