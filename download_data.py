import roboflow

rf = roboflow.Roboflow(api_key="E1lW7SfMx7fHWUZKIg2J")
project = rf.workspace("vmadupu2024").project("beebot-marigold-detector")
dataset = project.version(5).download("yolov5")
