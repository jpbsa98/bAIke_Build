from collision import Vector, Poly, test_aabb

def get_route_boxes(pct):

    X = int(640*pct)
    Y = int(480*pct)

    CENTER_X= X//2
    TOP_X = CENTER_X
    TOP_Y = Y-int(220*pct)

    TWO_METERS_MIDDLE_LEFT =  (int(265*pct), Y - int(33*pct)) 
    TWO_METERS_MIDDLE_RIGHT = (int(375*pct), Y - int(33*pct))

    TWO_METERS_P1 = (int(-55*pct), int(-34*pct)) 
    TWO_METERS_P2 = (int(-55*pct), int(34*pct))
    TWO_METERS_P3 = (int(55*pct), int(-34*pct))
    TWO_METERS_P4 = (int(55*pct), int(34*pct))

    THREE_METERS_MIDDLE_LEFT = (int(320*pct) - int(76*pct)//2, Y - int(91*pct))
    THREE_METERS_MIDDLE_RIGHT = (int(320*pct) + int(76*pct)//2, Y - int(91*pct))

    THREE_METERS_P1 = (int(-76*pct)//2, int(-50*pct)//2)
    THREE_METERS_P2 = (int(-76*pct)//2, int(50*pct)//2)
    THREE_METERS_P3 = (int(76*pct)//2, int(-50*pct)//2)
    THREE_METERS_P4 = (int(76*pct)//2, int(50*pct)//2)

    FOUR_METERS_MIDDLE_LEFT = (int(320*pct) - int(52*pct)//2, Y - int(134*pct))
    FOUR_METERS_MIDDLE_RIGHT = (int(320*pct) + int(52*pct)//2, Y - int(134*pct))

    FOUR_METERS_P1 = (int(-52*pct)//2, int(-38*pct)//2)
    FOUR_METERS_P2 = (int(-52*pct)//2, int(38*pct)//2)
    FOUR_METERS_P3 = (int(52*pct)//2, int(-38*pct)//2)
    FOUR_METERS_P4 = (int(52*pct)//2, int(38*pct)//2)

    FIVE_METERS_MIDDLE_LEFT = ( int(320*pct) - int(33*pct)//2, Y - int(170*pct))
    FIVE_METERS_MIDDLE_RIGHT = (int(320*pct) + int(33*pct)//2, Y - int(170*pct))

    FIVE_METERS_P1 = (int(-33*pct)//2, int(-30*pct)//2)
    FIVE_METERS_P2 = (int(-33*pct)//2, int(30*pct)//2)
    FIVE_METERS_P3 = (int(33*pct)//2, int(-30*pct)//2)
    FIVE_METERS_P4 = (int(33*pct)//2, int(30*pct)//2)

    SIX_METERS_MIDDLE_LEFT = (int(311*pct), Y - int(197*pct))
    SIX_METERS_MIDDLE_RIGHT = (int(329*pct), Y - int(197*pct))

    SIX_METERS_P1 = (int(-9*pct), int(-12*pct))
    SIX_METERS_P2 = (int(-9*pct), int(12*pct))
    SIX_METERS_P3 = (int(9*pct), int(-12*pct))
    SIX_METERS_P4 = (int(9*pct), int(12*pct))

    vec_6_l = Vector(SIX_METERS_MIDDLE_LEFT[0], SIX_METERS_MIDDLE_LEFT[-1])
    vec_6_r = Vector(SIX_METERS_MIDDLE_RIGHT[0], SIX_METERS_MIDDLE_RIGHT[-1])

    vec_6_p1 = Vector(SIX_METERS_P1[0], SIX_METERS_P1[-1])
    vec_6_p2 = Vector(SIX_METERS_P2[0], SIX_METERS_P2[-1])
    vec_6_p3 = Vector(SIX_METERS_P3[0], SIX_METERS_P3[-1])
    vec_6_p4 = Vector(SIX_METERS_P4[0], SIX_METERS_P4[-1])

    vec_5_l = Vector(FIVE_METERS_MIDDLE_LEFT[0], FIVE_METERS_MIDDLE_LEFT[-1])
    vec_5_r = Vector(FIVE_METERS_MIDDLE_RIGHT[0], FIVE_METERS_MIDDLE_RIGHT[-1])

    vec_5_p1 = Vector(FIVE_METERS_P1[0], FIVE_METERS_P1[-1])
    vec_5_p2 = Vector(FIVE_METERS_P2[0], FIVE_METERS_P2[-1])
    vec_5_p3 = Vector(FIVE_METERS_P3[0], FIVE_METERS_P3[-1])
    vec_5_p4 = Vector(FIVE_METERS_P4[0], FIVE_METERS_P4[-1])

    vec_4_l = Vector(FOUR_METERS_MIDDLE_LEFT[0], FOUR_METERS_MIDDLE_LEFT[-1])
    vec_4_r = Vector(FOUR_METERS_MIDDLE_RIGHT[0], FOUR_METERS_MIDDLE_RIGHT[-1])

    vec_4_p1 = Vector(FOUR_METERS_P1[0], FOUR_METERS_P1[-1])
    vec_4_p2 = Vector(FOUR_METERS_P2[0], FOUR_METERS_P2[-1])
    vec_4_p3 = Vector(FOUR_METERS_P3[0], FOUR_METERS_P3[-1])
    vec_4_p4 = Vector(FOUR_METERS_P4[0], FOUR_METERS_P4[-1])

    vec_3_l = Vector(THREE_METERS_MIDDLE_LEFT[0], THREE_METERS_MIDDLE_LEFT[-1])
    vec_3_r = Vector(THREE_METERS_MIDDLE_RIGHT[0], THREE_METERS_MIDDLE_RIGHT[-1])

    vec_3_p1 = Vector(THREE_METERS_P1[0], THREE_METERS_P1[-1])
    vec_3_p2 = Vector(THREE_METERS_P2[0], THREE_METERS_P2[-1])
    vec_3_p3 = Vector(THREE_METERS_P3[0], THREE_METERS_P3[-1])
    vec_3_p4 = Vector(THREE_METERS_P4[0], THREE_METERS_P4[-1])

    vec_2_l = Vector(TWO_METERS_MIDDLE_LEFT[0], TWO_METERS_MIDDLE_LEFT[-1])
    vec_2_r = Vector(TWO_METERS_MIDDLE_RIGHT[0], TWO_METERS_MIDDLE_RIGHT[-1])

    vec_2_p1 = Vector(TWO_METERS_P1[0], TWO_METERS_P1[-1])
    vec_2_p2 = Vector(TWO_METERS_P2[0], TWO_METERS_P2[-1])
    vec_2_p3 = Vector(TWO_METERS_P3[0], TWO_METERS_P3[-1])
    vec_2_p4 = Vector(TWO_METERS_P4[0], TWO_METERS_P4[-1])

    box_6l = Poly(vec_6_l, [vec_6_p1, vec_6_p2, vec_6_p3, vec_6_p4])
    box_6r = Poly(vec_6_r, [vec_6_p1, vec_6_p2, vec_6_p3, vec_6_p4])

    box_5l = Poly(vec_5_l, [vec_5_p1, vec_5_p2, vec_5_p3, vec_5_p4])
    box_5r = Poly(vec_5_r, [vec_5_p1, vec_5_p2, vec_5_p3, vec_5_p4])

    box_4l = Poly(vec_4_l, [vec_4_p1, vec_4_p2, vec_4_p3, vec_4_p4])
    box_4r = Poly(vec_4_r, [vec_4_p1, vec_4_p2, vec_4_p3, vec_4_p4])

    box_3l = Poly(vec_3_l, [vec_3_p1, vec_3_p2, vec_3_p3, vec_3_p4])
    box_3r = Poly(vec_3_r, [vec_3_p1, vec_3_p2, vec_3_p3, vec_3_p4])

    box_2l = Poly(vec_2_l, [vec_2_p1, vec_2_p2, vec_2_p3, vec_2_p4])
    box_2r = Poly(vec_2_r, [vec_2_p1, vec_2_p2, vec_2_p3, vec_2_p4])

    boxes_lst = [("2L", box_2l.aabb), ("2R", box_2r.aabb), ("3L", box_3l.aabb), 
                ("3R", box_3r.aabb), ("4L", box_4l.aabb), ("4R", box_4r.aabb),
                ("5L", box_5l.aabb), ("5R", box_5r.aabb), ("6L", box_6l.aabb),
                ("6R", box_6r.aabb)
                ]
    
    return boxes_lst