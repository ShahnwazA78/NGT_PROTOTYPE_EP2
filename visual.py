import ast
import cv2
import numpy as np
import pandas as pd

def draw_red_border(img, x1, y1, x2, y2, car_number):
    cv2.rectangle(img, (int(x1), int(y1)), (int(x2), int(y2)), (0, 0, 255), 12)
    (text_width, text_height), _ = cv2.getTextSize(car_number, cv2.FONT_HERSHEY_SIMPLEX, 4.3, 17)
    cv2.putText(img, car_number, (int((x2 + x1 - text_width) / 2), int(y1 - 250 + (text_height / 2)), cv2.FONT_HERSHEY_SIMPLEX, 4.3, (0, 0, 0), 17)
    return img

results = pd.read_csv('./test_interpolated.csv')

# Load video
video_path = 'sample.mp4'
cap = cv2.VideoCapture(video_path)

fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Specify the codec
fps = cap.get(cv2.CAP_PROP_FPS)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
out = cv2.VideoWriter('./out.mp4', fourcc, fps, (width, height)

license_plate = {}
for car_id in np.unique(results['car_id']):
    max_score = np.amax(results[results['car_id'] == car_id]['license_number_score'])
    license_plate[car_id] = {
        'license_plate_bbox': ast.literal_eval(
            results[(results['car_id'] == car_id) & (results['license_number_score'] == max_score)]['license_plate_bbox'].iloc[0]
        ),
        'car_number': results[(results['car_id'] == car_id) & (results['license_number_score'] == max_score)]['license_number'].iloc[0]
    }
    cap.set(cv2.CAP_PROP_POS_FRAMES, results[(results['car_id'] == car_id) & (results['license_number_score'] == max_score)]['frame_nmr'].iloc[0])
    ret, frame = cap.read()

    x1, y1, x2, y2 = license_plate[car_id]['license_plate_bbox']

    license_plate[car_id]['license_crop'] = frame[int(y1):int(y2), int(x1):int(x2), :]

frame_nmr = -1

cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

# Read frames
ret = True
while ret:
    ret, frame = cap.read()
    frame_nmr += 1
    if ret:
        df_ = results[results['frame_nmr'] == frame_nmr]
        for row_indx in range(len(df_)):
            car_number = license_plate[df_.iloc[row_indx]['car_id']]['car_number']
            x1, y1, x2, y2 = license_plate[df_.iloc[row_indx]['car_id']]['license_plate_bbox']
            frame = draw_red_border(frame, x1, y1, x2, y2, car_number)
        
        out.write(frame)
        frame = cv2.resize(frame, (1280, 720))

out.release()
cap.release()
