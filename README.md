# Prototype of a Vehicle Identification App​

## Team - VehiScan Squad

## Introduction: 
->The Vehicle Number Plate Recognition System is a powerful application prototype designed to tackle the challenge of automating the registration number               
logging process for vehicles entering or leaving a specific location, such as Nagarro building premises. This innovative system is built to recognize, capture, and store vehicle registration numbers from a recorded video stream in a robust and adaptable manner.

## Technologies Used
1->Python: The project is primarily developed using Python, a versatile and widely-used programming language that provides the foundation for the entire 
           system. 
2->YOLOv8: YOLO (You Only Look Once) is a state-of-the-art real-time object detection system. YOLOv8, in particular, is used to identify and locate vehicles    
           and their number plates within the video stream.
3->EasyOCR: EasyOCR is a powerful Optical Character Recognition (OCR) library in Python. It plays a crucial role in recognizing and extracting the 
            registration numbers from the vehicle number plates within the video stream.
4->OpenCV: OpenCV (Open Source Computer Vision Library) is used for image and video processing. It is integral to tasks such as capturing, preprocessing, 
           and annotating frames in the video stream.

## Models: Custom Trained Model


          Trained using YoloV8 with the  provided by the roboflow. 
[Data Set](https://universe.roboflow.com/kongu-engineering-college/number-plate-detection-p94ai/dataset/1)

## Dependencies

The sort module used from [this repository](https://github.com/abewley/sort).

## Steps to Run
1-> Clone the [Repository](https://github.com/ShahnwazA78/NGT_PROTOTYPE_EP2.git)
```bash
git clone https://github.com/ShahnwazA78/NGT_PROTOTYPE_EP2.git
```
2-> Make an environment with python=3.8 using the following command
``` bash
conda create --prefix ./env python==3.8 -y
```
3-> Go to the protect directory NGT_PROTOTYPE_EP2 by following command
```bash
cd /path/to/NGT_PROTOTYPE_EP2/
```
4-> Install the project dependencies using the following command 
```bash
pip install -r requirements.txt
```
5-> Go to sort Directory by following command
```bash
cd sort
```
6-> Install the sort module dependencies using following command
```bash
pip install -r requirements.txt
```
7-> Provide the video in Test-Videos
8-> Run main.py file
9-> Run add_missing_data.py
10-> Run visualize.py 

## Result : Number plate data is stored is test.csv file locally in the folder itself.
           Also processed.mp4 an output video is produced for visualization.
   




