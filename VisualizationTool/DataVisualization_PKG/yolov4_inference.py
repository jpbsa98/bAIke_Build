import cv2
import numpy as np
#from yolov4.common.media import draw_bboxes
from yolov4.tf import YOLOv4

# https://github.com/qwertyquerty/collision
from collision import Vector, Poly, collide

ATUALIZAR_CAIXAS = 20

X = 640
Y = 480
CENTER_X=int(640/2)

DCAY_1_M_Y=67
DCAY_1_M_X=110
ONE_METER_RIGTH=[CENTER_X-DCAY_1_M_X,Y]
ONE_METER_LEFT=[CENTER_X+DCAY_1_M_X,Y]


DCAY_2_M_Y=67
DCAY_2_M_X=77
TWO_METERS_LEFT=[CENTER_X -DCAY_2_M_X , Y-DCAY_2_M_Y]
TWO_METERS_RIGTH=[CENTER_X +DCAY_2_M_X , Y-DCAY_2_M_Y]

DCAY_3_M_Y=DCAY_2_M_Y+50
DCAY_3_M_X=50
TREE_METERS_LEFT=[CENTER_X-DCAY_3_M_X , Y-DCAY_3_M_Y]
TREE_METERS_RIGTH=[CENTER_X+DCAY_3_M_X , Y-DCAY_3_M_Y]

# Adições

TOP_X = CENTER_X
TOP_Y = Y-220

LEFT_LINE_X = CENTER_X - 110
LEFT_LINE_Y = 640

RIGHT_LINE_X = CENTER_X + 110
RIGHT_LINE_Y = 640    

LEFT_MIDDLE = ((LEFT_LINE_X + TOP_X)  / 2, (LEFT_LINE_Y + TOP_Y)/2)
LEFT_MIDDLE = (320 + 110, 260 )
RIGHT_MIDDLE = ((RIGHT_LINE_X + TOP_X)/2, (RIGHT_LINE_Y + TOP_Y)/2)

#print(f"TOP X {CENTER_X} Y {TOP_Y} | LEFT X {LEFT_LINE_X} Y {LEFT_LINE_Y} \
#        MID {LEFT_MIDDLE} | RIGHT X {RIGHT_LINE_X} Y {RIGHT_LINE_Y} MID \
#            {RIGHT_MIDDLE}")

LEFT_LINE_POLY = Poly(Vector(LEFT_MIDDLE[0], LEFT_MIDDLE[1]), [Vector(TOP_X, TOP_Y), Vector(LEFT_LINE_X, LEFT_LINE_Y)])
RIGHT_LINE_POLY = Poly(Vector(RIGHT_MIDDLE[0], RIGHT_MIDDLE[1]), [Vector(TOP_X, TOP_Y), Vector(RIGHT_LINE_X, RIGHT_LINE_Y)])


thickness = 1
isClosed = True
# Blue color in BGR 
color = (255, 0, 0) 
# Create some points


ppt = np.array([ 
                
                TWO_METERS_LEFT , TWO_METERS_RIGTH,

                TREE_METERS_RIGTH , TREE_METERS_LEFT
                
                ], np.int32)


ppt2 = np.array([          
                TWO_METERS_LEFT , TWO_METERS_RIGTH,

                ONE_METER_LEFT, ONE_METER_RIGTH  
                
                ], np.int32)


LEFT_LINE = np.array([[CENTER_X-110 , Y], [CENTER_X-6 , Y-220+11]], np.int32)

RIGTH_LINE = np.array([[CENTER_X+110 , Y], [CENTER_X+6 , Y-220+11]], np.int32)


M2M=(CENTER_X+64 +20,Y-66)
M3M=(CENTER_X+41 +20,Y-50-66)
M4M=(CENTER_X+22+20,Y-39-50-66)
M5M=(CENTER_X+10  +20,Y-30-39-50-66)
M6M=(CENTER_X+2 +20,Y-24-30-39-50-66)


ONE_METER_LINE=np.array([[CENTER_X-64 , Y-66], [CENTER_X+64 , Y-66]], np.int32) #64
TWO_METER_LINE=np.array([[CENTER_X-41 , Y-50-66], [CENTER_X+41 , Y-50-66]], np.int32) #50
THRE_METER_LINE=np.array([[CENTER_X-22 , Y-39-50-66], [CENTER_X+22 , Y-39-50-66]], np.int32) #39
FOUR_METER_LINE=np.array([[CENTER_X-10 , Y-30-39-50-66], [CENTER_X+10 , Y-30-39-50-66]], np.int32) #30
FIVE_METER_LINE=np.array([[CENTER_X-2 , Y-24-30-39-50-66], [CENTER_X+2 , Y-24-30-39-50-66]], np.int32) #30


ONE_METER_LINE = ONE_METER_LINE.reshape((-1, 1, 2))
TWO_METER_LINE = TWO_METER_LINE.reshape((-1, 1, 2))
THRE_METER_LINE = THRE_METER_LINE.reshape((-1, 1, 2))
FOUR_METER_LINE = FOUR_METER_LINE.reshape((-1, 1, 2))
FIVE_METER_LINE = FIVE_METER_LINE.reshape((-1, 1, 2))

LEFT_LINE = LEFT_LINE.reshape((-1, 1, 2))
RIGTH_LINE=RIGTH_LINE.reshape((-1, 1, 2))

LEFT_LINE = LEFT_LINE.reshape((-1, 1, 2))
RIGTH_LINE=RIGTH_LINE.reshape((-1, 1, 2))


ppt2 = ppt2.reshape((-1, 1, 2))

def check_colisions(box):
    collided = False

    #  1 # # # # 2
    #  #         #
    #  #         #
    #  #         #
    #  3 # # # # 4

    x = box[0] * X
    y = box[1] * Y
    w = box[2] * X
    h = box[3] * Y

    center_x = int(x + (w / 2))
    center_y = int(y + (h / 2))

    pt1 = Vector(center_x - w, center_y - h) 
    pt2 = Vector(center_x - w, center_y + h)
    pt3 = Vector(center_x + w, center_y - h)
    pt4 = Vector(center_x + w, center_y + h)

    box_poly = Poly(Vector(center_x, center_y), [pt1, pt2, pt3, pt4])
    
    #print(box, box_poly, end="\n")
    if collide(box_poly, LEFT_LINE_POLY) or collide(box_poly, RIGHT_LINE_POLY):
        collided = True
    
    return collided

def main():
    cap = cv2.VideoCapture("joinedVideo.mp4")

    color_txt = (0, 255, 0)
    var = 0
    boxes = np.array([])
    while (True):
        text_alert="Free to go" 
        ret, frame = cap.read()

        if frame is None:
            print("Entro")
            break

        frame = cv2.rotate(frame, cv2.ROTATE_90_COUNTERCLOCKWISE)
        #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #frame = np.expand_dims(frame, -1)

        if var % ATUALIZAR_CAIXAS == 0:
            boxes = yolo.predict(frame)
            #@return pred_bboxes == Dim(-1, (x, y, w, h, class_id, probability))
        
        frame = yolo.draw_bboxes(frame, boxes)
        
        if sum([sum(x) for x in boxes]) != 0:
            for box in boxes:
                if check_colisions(box):
                    color_txt = (0, 0, 255)
                    text_alert="Danger detected"
                    print(var, "Sim")

        frame = cv2.putText(frame, text_alert, (10, 30), cv2.FONT_HERSHEY_COMPLEX, 1, color_txt, 2, cv2.LINE_AA)

        font = cv2.FONT_HERSHEY_SIMPLEX
        fontScale_meters_info=0.4
        cv2.putText(frame,'2M', M2M, font, fontScale_meters_info, (0, 0, 255), 1, cv2.LINE_AA)
        cv2.putText(frame,'3M', M3M, font, fontScale_meters_info, (0, 0, 255), 1, cv2.LINE_AA)
        cv2.putText(frame,'4M', M4M, font, fontScale_meters_info, (0, 128, 255), 1, cv2.LINE_AA)
        cv2.putText(frame,'5M', M5M, font, fontScale_meters_info, color, 1, cv2.LINE_AA)
        cv2.putText(frame,'6M', M6M, font, fontScale_meters_info, color, 1, cv2.LINE_AA)
        

        cv2.polylines(frame, [FOUR_METER_LINE,FIVE_METER_LINE], isClosed,color,2)
        cv2.polylines(frame, [LEFT_LINE,RIGTH_LINE], isClosed,(0, 255, 255),3)
        cv2.polylines(frame, [ONE_METER_LINE,TWO_METER_LINE],isClosed ,(0, 0, 255),2)
        cv2.polylines(frame, [THRE_METER_LINE], isClosed,(0, 128, 255),2)
        cv2.imshow('Video',frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        var += 1
        color_txt = (0, 255, 0)

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":

    #help(YOLOv4)

    #yolo = YOLOv4()
    yolo = YOLOv4(tiny=True)
    yolo.classes = "coco.names"
    yolo.input_size = (640, 480)
    
    yolo.make_model()
    yolo.load_weights("yolov4-tiny.weights", weights_type="yolo")
    #yolo.load_weights("yolov4.weights", weights_type="yolo")

    main()