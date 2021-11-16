from GaitAnaylsisToolkit.Session import ViconGaitingTrial
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
from GaitCore.Core import Point, PointArray
import csv
# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    #Change to location of file in your system
    curFile = "/home/nathanielgoldfarb/compareMarkerVsExo/EXODataVisualization/pythonProject/Files/11_12_20_nathaniel_walking_00.csv"
    trial = ViconGaitingTrial.ViconGaitingTrial(vicon_file=curFile)
    markers = trial.vicon.get_markers()
    markers.smart_sort()
    # array of marks
    femur_side = [markers.get_marker("LFemurSide0"), markers.get_marker("LFemurSide1"),
                  markers.get_marker("LFemurSide2"), markers.get_marker("LFemurSide3")]


    femur_center = [markers.get_marker("LFemurFront0"), markers.get_marker("LFemurFront1"),
                    markers.get_marker("LFemurFront2"), markers.get_marker("LFemurFront3"),
                    markers.get_marker("LFemurBack0"), markers.get_marker("LFemurBack1"),
                    markers.get_marker("LFemurBack2"), markers.get_marker("LFemurBack3")]




    tibia_side = [markers.get_marker("LTibiaSide0"), markers.get_marker("LTibiaSide1"),
                  markers.get_marker("LTibiaSide2"), markers.get_marker("LTibiaSide3")]


    tibia_center = [markers.get_marker("LTibiaFront0"), markers.get_marker("LTibiaFront1"),
                markers.get_marker("LTibiaFront2"), markers.get_marker("LTibiaFront3"),
                markers.get_marker("LTibiaBack0"), markers.get_marker("LTibiaBack1"),
                markers.get_marker("LTibiaBack2"), markers.get_marker("LTibiaBack3")]


    trial_range = len(femur_center[0])
    x = np.arange(0, trial_range)

    xav = 0
    yav = 0
    zav = 0
    points = 0
    average_points = []
    average_femur_human = []
    average_femur_side = []

    average_tibia_human = []
    average_tibia_side = []

    for i in range(trial_range):
        human_femur = Point.Point(0, 0, 0)
        exo_femur = Point.Point(0, 0, 0)
        human_tibia = Point.Point(0, 0, 0)
        exo_tibia = Point.Point(0, 0, 0)

        for marker in femur_center:
            human_femur += marker[i]

        for mark in femur_side:
            exo_femur += mark[i]

        for marker in tibia_center:
            human_tibia += marker[i]

        for mark in tibia_side:
            exo_tibia += mark[i]

        human_femur = human_femur / len(femur_center)
        exo_femur = exo_femur / len(femur_side)

        average_femur_human.append(human_femur)
        average_femur_side.append(exo_femur)


        human_tibia = human_tibia / len(tibia_center)
        exo_tibia = exo_tibia / len(tibia_side)

        average_tibia_human.append(human_tibia)
        average_tibia_side.append(exo_tibia)



    average_femur_side = PointArray.PointArray.from_point_array(average_femur_side)
    average_femur_human = PointArray.PointArray.from_point_array(average_femur_human)

    average_tibia_side = PointArray.PointArray.from_point_array(average_tibia_side)
    average_tibia_human = PointArray.PointArray.from_point_array(average_tibia_human)


    x_human = average_femur_human.z
    x_exo = average_femur_side.z
    v_human = np.diff(x_human)/0.01
    v_exo = np.diff(x_exo )/0.01

    d = {}

    d['x_human'] = x_human
    d["x_exo"] = x_exo
    d["v_human"] = v_human
    d["v_exo"] = v_exo

    with open("../matlab/test.csv", "w") as outfile:
        writer = csv.writer(outfile)
        writer.writerow(list(d.keys()))
        writer.writerows(zip(*d.values()))

    t = np.linspace(0, 100, len(average_femur_human))

    fig, ax = plt.subplots(3,2)
    ax[0,0].plot(t, average_femur_human.x, 'b', markersize=1)
    ax[0,0].plot(t, average_femur_side.x, 'r', markersize=1)
    ax[1,0].plot(t, average_femur_human.y, 'b', markersize=1)
    ax[1,0].plot(t, average_femur_side.y, 'r', markersize=1)
    ax[2,0].plot(t, average_femur_human.z, 'b', markersize=1)
    ax[2,0].plot(t, average_femur_side.z, 'r', markersize=1)

    ax[0,1].plot(t, average_tibia_human.x, 'b', markersize=1)
    ax[0,1].plot(t, average_tibia_side.x, 'r', markersize=1)
    ax[1,1].plot(t, average_tibia_human.y, 'b', markersize=1)
    ax[1,1].plot(t, average_tibia_side.y, 'r', markersize=1)
    ax[2,1].plot(t, average_tibia_human.z, 'b', markersize=1)
    ax[2,1].plot(t, average_tibia_side.z, 'r', markersize=1)

    fig.suptitle('Comparison of the human thigh position and the exoskeleton thigh position', fontsize=16)
    ax[0,0].set_title("X Thigh Position", fontsize=16)
    ax[1,0].set_title("Y Thigh Position", fontsize=16)
    ax[2,0].set_title("Z Thigh Position", fontsize=16)

    ax[0,1].set_title("X Shank Position", fontsize=16)
    ax[1,1].set_title("Y Shank Position", fontsize=16)
    ax[2,1].set_title("Z Shank Position", fontsize=16)


    ax[0,0].legend(["Human", "Exoskeleton"])
    ax[0,0].set_ylabel("Position (mm)", fontsize=16)
    ax[1,0].set_ylabel("Position (mm)", fontsize=16)
    ax[2,0].set_ylabel("Position (mm)", fontsize=16)
    ax[2,0].set_xlabel("Trial %", fontsize=16)
    ax[2,1].set_xlabel("Trial %", fontsize=16)


    plt.show()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
