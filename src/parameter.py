#显示图片
import matplotlib.pyplot as plt
import paddlehub as hub
import cv2

#加载yolov3_darknet53_pedestrian模型
pedestrian_detector = hub.Module(name="yolov3_darknet53_pedestrian")
result = pedestrian_detector.object_detection(images=[cv2.imread('pic/0.jpg')])

img = cv2.imread('/home/aistudio/pic/0.jpg')
font = cv2.FONT_HERSHEY_SIMPLEX

for i in range(len(result[0]['data'])):
    cv2.rectangle(img, (int(result[0]['data'][i]['left']), int(result[0]['data'][i]['top'])), (int(result[0]['data'][i]['right']), int(result[0]['data'][i]['bottom'])), (0, 255, 0), thickness=1) 
    cv2.putText(img, str(i), (int(result[0]['data'][i]['left']), int(result[0]['data'][i]['top'])), font, 0.8, (0, 255, 0), 2)

#保存图片
cv2.imwrite('show.jpg', img)

# 显示图片
img = cv2.imread('show.jpg')
%matplotlib inline
plt.imshow(img)
plt.show()

# 设定“感染者”
InfectorNum = 4

# 设定“安全距离”
# 求距离
def GetPoint(data):
    length = data['right'] - data['left']
    width = data['top'] - data['bottom']
    x = data['left'] + length/2
    y = data['bottom'] + width/2
    return (x, y)

def GetDistance(point1, point2):
    return (point1[0]-point2[0])*(point1[0]-point2[0])+(point1[1]-point2[1])*(point1[1]-point2[1])

# 设置安全距离
PersonPoint1 = GetPoint(result[0]['data'][9])         # 选定9号
PersonPoint2 = GetPoint(result[0]['data'][22])        # 选定22号
Distance = GetDistance(PersonPoint1, PersonPoint2)    # 计算9号与22号之间距离，设定为“安全距离”

print(Distance)
