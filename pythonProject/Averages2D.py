from GaitAnaylsisToolkit.Session import ViconGaitingTrial
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
from GaitCore.Core import Point

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    fig, ax = plt.subplots(3)
    #Change to location of file in your system
    curFile = r"C:\Users\Owner\Documents\GaitAnalysisCSVs\CSVs\11_12_20_nathaniel_walking_00.csv"
    trial = ViconGaitingTrial.ViconGaitingTrial(vicon_file=curFile)
    markers = trial.vicon.get_markers()
    markers.smart_sort()
    # array of marks
    markingSide = [markers.get_marker("LFemurSide0"), markers.get_marker("LFemurSide1"),
                   markers.get_marker("LFemurSide2"), markers.get_marker("LFemurSide3")]
    marking = [markers.get_marker("LFemurFront0"), markers.get_marker("LFemurFront1"),
               markers.get_marker("LFemurFront2"), markers.get_marker("LFemurFront3"),
               markers.get_marker("LFemurBack0"), markers.get_marker("LFemurBack1"),
               markers.get_marker("LFemurBack2"), markers.get_marker("LFemurBack3")]
    trial_range = len(marking[0])
    x = np.arange(0, trial_range)
    ax[0].set_title('Front & Back Y (blue), Side Y (yellow), Over Time')
    ax[1].set_title('Front & Back X (blue), Side X (yellow), Over Time')
    ax[2].set_title('Front & Back Z (blue), Side Z (yellow), Over Time')
    xav = 0
    yav = 0
    zav = 0
    points = 0
    average_points = []

    for i in range(trial_range):
        my_maker = Point.Point(0, 0, 0)
        side_maker = Point.Point(0, 0, 0)
        for marker in marking:
            my_maker += marker[i]

        for mark in markingSide:
            side_maker += mark[i]
        my_maker = my_maker / len(marking)
        side_maker = side_maker / len(markingSide)

        average_points.append(my_maker)
        #Y
        ax[0].plot(i, my_maker.y, 'bo', markersize=1)
        #ax[0].plot(i, my_maker.x, 'bo', markersize=1)
        ax[0].plot(i, side_maker.y, 'yo', markersize=1)

        # X
        #ax[1].plot(i, my_maker.z, 'ro', markersize=1)
        ax[1].plot(i, my_maker.x, 'bo', markersize=1)
        ax[1].plot(i, side_maker.x, 'yo', markersize=1)

        # Z
        #ax[2].plot(i, my_maker.y, 'ro', markersize=1)
        ax[2].plot(i, my_maker.z, 'bo', markersize=1)
        ax[2].plot(i, side_maker.z, 'yo', markersize=1)

        xav = xav + my_maker.x
        yav = yav + my_maker.y
        zav = zav + my_maker.z
        points = points + 1

    xav = xav / points
    yav = yav / points
    zav = zav / points
    plt.show()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
