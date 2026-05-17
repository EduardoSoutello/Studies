import numpy as np
import cv2
from time import sleep

VIDEO = "D:/Git/Estudos/Alura/ComputerVision_MovementDetection/Videos/Rua.mp4"
#VIDEO = "D:/Git/Estudos/Alura/ComputerVision_MovementDetection/Videos/Estradas.mp4"
#VIDEO = "D:/Git/Estudos/Alura/ComputerVision_MovementDetection/Videos/Rua.mp4"
#VIDEO = "D:/Git/Estudos/Alura/ComputerVision_MovementDetection/Videos/Arco.mp4"

delay = 10

cap = cv2.VideoCapture(VIDEO)
hasFrame, frame = cap.read()

framesIds = cap.get(cv2.CAP_PROP_FRAME_COUNT) * np.random.uniform(size=72)

frames = []
for fid in framesIds:
    cap.set(cv2.CAP_PROP_POS_FRAMES, fid)
    hasFrame, frame = cap.read()
    frames.append(frame)

medianFrame = np.median(frames, axis=0).astype(dtype=np.uint8)
#print(medianFrame)
#cv2.imshow("Median Frame", medianFrame)
#cv2.waitKey(0)
cv2.imwrite("median_frame.jpg", medianFrame)
cv2.destroyAllWindows()

cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
grayMedianFrame = cv2.cvtColor(medianFrame, cv2.COLOR_BGR2GRAY)
#cv2.imshow("Cinza", grayMedianFrame)
#cv2.waitKey(0)
cv2.imwrite("gray_median_frame.jpg", grayMedianFrame)

while True:
    tempo = float(1/delay)
    sleep(tempo)
    
    hasFrame, frame = cap.read()

    if not hasFrame:
        print("Fim do vídeo")
        break

    grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    dframe = cv2.absdiff(grayFrame, grayMedianFrame)
    th, dframe = cv2.threshold(dframe, 30, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

    #cv2.imshow("Frame em Cinza", grayFrame)
    cv2.imshow("Frame Diferenca", dframe)

    if cv2.waitKey(1) & 0xFF == ord('c'):
        break

cap.release()
cv2.destroyAllWindows()