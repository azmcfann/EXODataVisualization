# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

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
    # array of toe marks
    marking =[ markers.get_marker("LTHI"),markers.get_marker("RTOE")]
    trial_range = len(marking[0])
    xav = 0
    yav = 0
    zav = 0
    points = 0
    average_points = []
    print(len(marking))
    for i in range(trial_range):
        my_maker = Point.Point(0,0,0)
        for marker in marking:
            my_maker += marker[i]
        my_maker = my_maker/len(marking)
        average_points.append(my_maker)
        ax.scatter(my_maker.x, my_maker.y, my_maker.z)

    print("Average x value: " + str(xav) + "\n")
    print("Average y value: " + str(yav) + "\n")
    print("Average z value: " + str(zav) + "\n")
    # print(toe)
    # my_foot = []
    # print(markers.get_rigid_body("L_Foot"))
    # for i in range(4):
    #     m = "L_Foot" + str(i)
    #     my_foot.append(markers.get_marker(m))
    # print(my_foot)
    plt.show();
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
