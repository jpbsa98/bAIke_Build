import cv2

from yolov4.tf import YOLOv4

from collisions import test_aabb, Vector, Poly
from utils import boxes_lst


scale_percent = 60

yolo = YOLOv4(tiny=True)
yolo.classes = "/opt/ros/melodic/lib/pei2020/coco.names"
yolo.input_size = (384, 288)

yolo.make_model()
yolo.load_weights("/opt/ros/melodic/lib/pei2020/yolov4-tiny.weights", weights_type="yolo")

def get_box(bx):

    c_x = bx[0] * 640
    c_y = bx[1] * 480
    half_w = (bx[2] * 640) // 2
    half_h = (bx[3] * 480) // 2

    pt1 = Vector(c_x - half_w, c_y - half_h) 
    pt2 = Vector(c_x - half_w, c_y + half_h)
    pt3 = Vector(c_x + half_w, c_y - half_h)
    pt4 = Vector(c_x + half_w, c_y + half_h)

    return Poly(Vector(c_x, c_y), [Vector(-half_w, -half_h), Vector(-half_w, half_h), Vector(half_w, -half_h), Vector(half_w, half_h)])

def check_colisions(box):

    collisions = [] 
    box_poly = get_box(box)
    for name, bbox in boxes_lst:
        if test_aabb(box_poly.aabb, bbox):
            collisions.append(name)

    return collisions

def impactDetection(frame):
    
    frame = cv2.rotate(frame, cv2.ROTATE_90_COUNTERCLOCKWISE)
    boxes = yolo.predict(frame)
    lst = []

    if sum([sum(x) for x in boxes]) != 0:
        for box in boxes:
            if check_colisions(box):
                lst = check_colisions(box) 

    return lst
