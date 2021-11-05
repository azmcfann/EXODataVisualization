from GaitAnaylsisToolkit.Session import ViconGaitingTrial
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
from GaitCore.Core import Point

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    curFile = r"C:\Users\Owner\Documents\GaitAnalysisCSVs\CSVs\11_12_20_nathaniel_walking_00.csv"
    trial = ViconGaitingTrial.ViconGaitingTrial(vicon_file=curFile)
    markers = trial.vicon.get_markers()
    markers.smart_sort()
    # array of marks
    marking = [markers.get_marker("LTHI"), markers.get_marker("RTHI")]
    trial_range = len(marking[0])
    xav = 0
    yav = 0
    zav = 0
    points = 0
    average_points = []
    print(len(marking))
    # LFemurFront0 - 3
    file_output = open(r"C:\Users\Owner\PycharmProjects\pythonProject\Files\MostRecentOutput.txt", "w+")
    average_output = open(r"C:\Users\Owner\PycharmProjects\pythonProject\Files\RecentOutputAvg.txt", "w+")
    file_output.write("   X      Y      Z   \n")
    for i in range(trial_range):
        my_maker = Point.Point(0, 0, 0)

        for marker in marking:
            my_maker += marker[i]
        my_maker = my_maker / len(marking)

        average_points.append(my_maker)
        ax.scatter(my_maker.x, my_maker.y, my_maker.z)
        xav = xav + my_maker.x
        yav = yav + my_maker.y
        zav = zav + my_maker.z
        points = points + 1
        SL = [str(my_maker.x), " ", str(my_maker.y), " ", str(my_maker.z), "\n"]
        file_output.write(str(points))
        file_output.write(":     ")
        file_output.writelines(SL)

    xav = xav/points
    yav = yav/points
    zav = zav/points
    print("Average x value: " + str(xav) + "\n")
    average_output.write("X Avg:  ")
    average_output.write(str(xav))
    average_output.write("\n")
    print("Average y value: " + str(yav) + "\n")
    average_output.write("Y Avg:  ")
    average_output.write(str(yav))
    average_output.write("\n")
    print("Average z value: " + str(zav) + "\n")
    average_output.write("Z Avg:  ")
    average_output.write(str(zav))
    average_output.write("\n")

    # print(toe)
    # my_foot = []
    # print(markers.get_rigid_body("L_Foot"))
    # for i in range(4):
    #     m = "L_Foot" + str(i)
    #     my_foot.append(markers.get_marker(m))
    # print(my_foot)
    average_output.close()
    file_output.close()
    plt.show()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
