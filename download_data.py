import roboflow

rf = roboflow.Roboflow(api_key="YOUR_API_KEY")
project = rf.workspace("YOUR_WORKSPACE").project("marigold")
dataset = project.version(5).download("yolov5")
