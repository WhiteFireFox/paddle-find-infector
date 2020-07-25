import paddlehub as hub
import cv2
import glob

def Detection(sign=4):
    pedestrian_detector = hub.Module(name="yolov3_darknet53_pedestrian")
    font = cv2.FONT_HERSHEY_SIMPLEX
    result = pedestrian_detector.object_detection(images=[cv2.imread('/home/aistudio/pic/0.jpg')])
    SignalPerson = result[0]['data'][sign]
    temp = 1e8
    for j in range(len(glob.glob(pathname='/home/aistudio/pic/*.jpg'))):
        img = cv2.imread('/home/aistudio/pic/'+str(j)+'.jpg')
        point1 = GetPoint(SignalPerson)
        #获取已感染人的位置
        for i in range(len(result[0]['data'])):
            point2 = GetPoint(result[0]['data'][i])
            if GetDistance(point1, point2) <= temp:
                sign = i
                temp = GetDistance(point1, point2)
        #标记
        for i in range(len(result[0]['data'])):
            if i == sign :
                cv2.rectangle(img, (int(result[0]['data'][i]['left']), int(result[0]['data'][i]['top'])), (int(result[0]['data'][i]['right']), int(result[0]['data'][i]['bottom'])), (0, 0, 255), thickness=1) 
                cv2.putText(img, 'Infector', (int(result[0]['data'][i]['left']), int(result[0]['data'][i]['top'])), font, 0.55, (0, 0, 255), 2)
            elif GetDistance(point1, GetPoint(result[0]['data'][i])) < Distance:
                cv2.rectangle(img, (int(result[0]['data'][i]['left']), int(result[0]['data'][i]['top'])), (int(result[0]['data'][i]['right']), int(result[0]['data'][i]['bottom'])), (0, 0, 255), thickness=1) 
                cv2.putText(img, 'Potential infector', (int(result[0]['data'][i]['left']), int(result[0]['data'][i]['top'])), font, 0.55, (0, 0, 255), 2)
            else:
                cv2.rectangle(img, (int(result[0]['data'][i]['left']), int(result[0]['data'][i]['top'])), (int(result[0]['data'][i]['right']), int(result[0]['data'][i]['bottom'])), (0, 255, 0), thickness=1) 
        SignalPerson = result[0]['data'][sign]
        result = pedestrian_detector.object_detection(images=[cv2.imread('/home/aistudio/pic/'+str(j)+'.jpg')])
        cv2.imwrite('/home/aistudio/img/'+str(j)+'.jpg', img)
        temp = 1e8

# 开始预测
Detection(InfectorNum)
