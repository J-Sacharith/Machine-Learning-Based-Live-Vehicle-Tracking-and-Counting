# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 23:09:28) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: C:\Users\Dell\OneDrive\Desktop\major project\RealTimeVehicleProject\input_retrieval.py
# Compiled at: 2020-05-29 17:47:14
# Size of source mod 2**32: 1709 bytes
import argparse, os

def parseCommandLineArguments():
    ap = argparse.ArgumentParser()
    ap.add_argument('-i', '--input', required=True, help='path to input video')
    ap.add_argument('-o', '--output', required=True, help='path to output video')
    ap.add_argument('-y', '--yolo', required=True, help='base path to YOLO directory')
    ap.add_argument('-c', '--confidence', type=float, default=0.5, help='minimum probability to filter weak detections')
    ap.add_argument('-t', '--threshold', type=float, default=0.3, help='threshold when applying non-maxima suppression')
    ap.add_argument('-u', '--use-gpu', type=bool, default=False, help='boolean indicating if CUDA GPU should be used')
    args = vars(ap.parse_args())
    labelsPath = os.path.sep.join([args['yolo'], 'coco.names'])
    LABELS = open(labelsPath).read().strip().split('\n')
    weightsPath = os.path.sep.join([args['yolo'], 'yolov3.weights'])
    configPath = os.path.sep.join([args['yolo'], 'yolov3.cfg'])
    inputVideoPath = args['input']
    outputVideoPath = args['output']
    confidence = args['confidence']
    threshold = args['threshold']
    USE_GPU = args['use_gpu']
    return (
     LABELS, weightsPath, configPath, inputVideoPath, outputVideoPath, confidence, threshold, USE_GPU)