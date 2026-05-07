from ultralytics import YOLO

model = YOLO('yolov26_custom.pt')

model.predict(source='D:/2026/Developing/ml_projects/object-detection-yollo11/test/1.png',
               show=False,
               save=True, 
               conf =0.5, 
               line_width=2, 
               show_labels=True,
               show_conf=True, 
               save_txt=False,
               classes=[0, 1])


model.predict(source='D:/2026/Developing/ml_projects/object-detection-yollo11/test/1.mp4',
               save=True, 
               conf =0.5, 
               line_width=2, 
               show_labels=True,
               show_conf=True, 
               save_txt=False,
               classes=[0, 1])


# show=True to display the image with detections in a window
# save=True to save the image with detections to the 'runs/detect/predict' directory
# conf=0.5 to set the confidence threshold for displaying detections (default is 0.25)
# line_width=2 to set the thickness of the bounding box lines (default is 3)
# show_labels=True to hide the class labels in the saved image
# show_conf=True to hide the confidence scores in the saved image
# add save_txt to save the detection results in a text file (annotations format)
# add save_crops to save the detected objects as separate images
# classes=[0, 1] to specify which classes to detect (0 for greenlight, 1 for redlight in this case)

# source = "0" to use the webcam as the source for predictions,
#  or you can specify a video file path instead of an image path.

# to export this model to ONNX format, you can use the following code:
# model.export(format='onnx', imgsz=640, device=0)
# to export this model to TensorRT format, you can use the following code:
# model.export(format='tensorrt', imgsz=640, device=0)
# to export this model to saved_model format, you can use the following code:
# model.export(format='saved_model', imgsz=640, device=0)

# instead of writing the code to predict on a single image, you can also use the command line interface (CLI) to run predictions on a folder of images or a video file. For example, you can run the following command in the terminal:
# yolo predict model=yolov26_custom.pt source=1.jpg 
