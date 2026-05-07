from ultralytics import YOLO
# Load a model
model = YOLO('yolo26n.pt')  # load a pretrained model (recommended for training)
# Train the model
model.train(data='dataset_custom.yaml', epochs=100, imgsz=640, batch=8, device=0, workers=0)
# device=0 means using the first GPU, you can change it to device=1 for the second GPU, or device='cpu' to use the CPU.

# instead of writing the code to train the model, you can also use the command line interface (CLI) to run training. For example, you can run the following command in the terminal:
# yolo train model=yolo26n.pt data=dataset_custom.yaml epochs=100 imgsz=640 batch=8 device=0 workers=0
