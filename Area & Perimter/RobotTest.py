Person_Saved = 0
Marker_Found = False
room_one_type = 3#int(input("Enter Room 1 Type 1-3 "))
room_two_type = 3#int(input("Enter Room 2 Type 1-3 "))
room_three_type = 3#int(input("Enter Room 2 Type 1-3 "))
room_four_type  = 3#int(input("Enter Room 2 Type 1-3 "))
import time



def Move_To_Room1():
    # room 1
    print("Move to Room 1")
    print("chassis_ctrl.move_with_distance(0, 5.0)")
    print("chassis_ctrl.move_with_distance(0, 2.5)")
    print("gimbal_ctrl.yaw_ctrl(-90)")
    print("chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)")
    print()


def Return_To_Start_Room1():
    # Code to return to start from Room 1
    print()
    print("Return to Start  from Room 1")
    print("gimbal_ctrl.yaw_ctrl(90)")
    print("chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)")
    print("chassis_ctrl.move_with_distance(0, 5.0)")
    print("chassis_ctrl.move_with_distance(0, 2.5)")
    print()


def Move_To_Room2(Person):

    # Move to Room2 Function
    if Person == 0:
        print("Move To Room 2")
        print("If Person_Saved == False:)")
        print("gimbal_ctrl.yaw_ctrl(90)")
        print("chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)")
        print("chassis_ctrl.move_with_distance(0, 5)")
        print("chassis_ctrl.move_with_distance(0, 1.9)")
        print("gimbal_ctrl.yaw_ctrl(-45)")
        # move end of hall: toyoko drift
        print("chassis_ctrl.move_with_distance(-45, 3)")
        print("gimbal_ctrl.recenter")
        print("chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)")
        print("time.sleep(5)")
        print("chassis_ctrl.move_with_distance(0, 5")
        print("chassis_ctrl.move_with_distance(0, .15)")
        print("gimbal_ctrl.yaw_ctrl(-90)")
        print("chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)")
        print()

    # This code goes from Start to Room 2
    elif Person == 1:
        print("Move To Room 2 from Start")
        print("elif Person_Saved == True:")
        print("chassis_ctrl.move_with_distance(0, 5.0)")
        print("chassis_ctrl.move_with_distance(0, 5)")
        print("chassis_ctrl.move_with_distance(0, 4.4)")
        print("gimbal_ctrl.yaw_ctrl(-45)")
        # move end of hall: toyoko drift
        print("chassis_ctrl.move_with_distance(-45, 3)")
        print("gimbal_ctrl.recenter")
        print("chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)")
        print("time.sleep(5)")
        print("chassis_ctrl.move_with_distance(0, 5)")
        print("chassis_ctrl.move_with_distance(0, .15)")
        print("gimbal_ctrl.yaw_ctrl(-90)")
        print("chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)")
        print()


def Return_To_Start_Room2():
    # Return from Room 2
    print()
    print("Return from Room 2")
    print("chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)")
    print("gimbal_ctrl.yaw_ctrl(-90)")
    print("chassis_ctrl.move_with_distance(0, 5)")
    print("chassis_ctrl.move_with_distance(0, .15)")
    print("chassis_ctrl.move_with_distance(-45, 3)")
    print("gimbal_ctrl.yaw_ctrl(-45)")
    print("gimbal_ctrl.recenter")
    print("chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)")
    print("time.sleep(5)")
    print("chassis_ctrl.move_with_distance(0, 5.0)")
    print("chassis_ctrl.move_with_distance(0, 5)")
    print("chassis_ctrl.move_with_distance(0, 4.4)")
    print()


def Move_To_Room3(Person):
    # Move to Room 3 from Room 2

    if Person == 0:
        print("Move To Room 3")
        print("if Person_Saved == False:")
        print("gimbal_ctrl.yaw_ctrl(90)")
        print("chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)")
        print("chassis_ctrl.move_with_distance(0, 5)")
        print("chassis_ctrl.move_with_distance(0, 3.85)")
        print("gimbal_ctrl.yaw_ctrl(-90)")
        print("chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)")

    # Move to Room 3 from Start
    elif Person == 1:
        print("Move To Room 3 From Start")
        print("""Person_Saved == True)
        chassis_ctrl.move_with_distance(0, 5.0)
        chassis_ctrl.move_with_distance(0, 2.5)
        chassis_ctrl.move_with_distance(0, 5)
        chassis_ctrl.move_with_distance(0, 1.9)
        gimbal_ctrl.yaw_ctrl(-45)
        # move end of hall: toyoko drift
        chassis_ctrl.move_with_distance(-45, 3)
        gimbal_ctrl.recenter
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
        time.sleep(5)
        chassis_ctrl.move_with_distance(0, 5)
        chassis_ctrl.move_with_distance(0, .15)
        chassis_ctrl.move_with_distance(0, 5)
        chassis_ctrl.move_with_distance(0, 3.85)
        gimbal_ctrl.yaw_ctrl(-90)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)""")
        print()


def Return_To_Start_Room3():
    print()
    print("Return To Start Room 3")
    # return start from Room 3
    print("""chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
    gimbal_ctrl.yaw_ctrl(-90)
    chassis_ctrl.move_with_distance(0, 5)
    chassis_ctrl.move_with_distance(0, 5)
    chassis_ctrl.move_with_distance(0, 4)
    chassis_ctrl.move_with_distance(-45, 3)
    gimbal_ctrl.yaw_ctrl(-45)
    gimbal_ctrl.recenter
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
    time.sleep(5)
    chassis_ctrl.move_with_distance(0, 5.0)
    chassis_ctrl.move_with_distance(0, 2.5)
    chassis_ctrl.move_with_distance(0, 5)
    chassis_ctrl.move_with_distance(0, 1.9)""")
    print()


def Move_To_Room4(Person):
    # Move to Room 4 from Room 3

    if Person == 0:
        print("Move to Room 4")
        print("""If Person_Saved == False
        gimbal_ctrl.yaw_ctrl(90)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
        chassis_ctrl.move_with_distance(0, 5)
        chassis_ctrl.move_with_distance(0, 5)
        chassis_ctrl.move_with_distance(0, 0.4)
        gimbal_ctrl.yaw_ctrl(-90)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)""")
        print()

    elif Person == 1:
        print("Move to Room 4 From Start")
        print(""" If Person Saved == True:)
        # from Start To Room 4
        chassis_ctrl.move_with_distance(0, 5.0)
        chassis_ctrl.move_with_distance(0, 5.0)
        chassis_ctrl.move_with_distance(0, 4.4)
        gimbal_ctrl.yaw_ctrl(-45)
        # move end of hall: toyoko drift
        chassis_ctrl.move_with_distance(-45, 3)
        gimbal_ctrl.recenter
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
        time.sleep(5)
        chassis_ctrl.move_with_distance(0, 5)
        chassis_ctrl.move_with_distance(0, 5)
        chassis_ctrl.move_with_distance(0, 5)
        chassis_ctrl.move_with_distance(0, 5)
        chassis_ctrl.move_with_distance(0, 4.4)
        gimbal_ctrl.yaw_ctrl(-90)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)""")
        print()


def Return_To_Start_Room4():
    print()
    print("Return to Start Room 4")
    # Returns from Room 4
    print("""gimbal_ctrl.yaw_ctrl(-90)
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
    chassis_ctrl.move_with_distance(0, 5)
    chassis_ctrl.move_with_distance(0, 5)
    chassis_ctrl.move_with_distance(0, 5)
    chassis_ctrl.move_with_distance(0, 5)
    chassis_ctrl.move_with_distance(0, 4.32)
    gimbal_ctrl.yaw_ctrl(45)
    chassis_ctrl.move_with_distance(45, 3)
    # after turn
    gimbal_ctrl.recenter
    chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
    time.sleep(5)
    chassis_ctrl.move_with_distance(0, 5)
    chassis_ctrl.move_with_distance(0, 5)
    chassis_ctrl.move_with_distance(0, 4.8)""")


def Scanner():
    # Rotates the Gimbal and looks for person or fire
    print()
    print("Scanner")
    print("""while marker_found == False:
        gimbal_ctrl.yaw_ctrl(90)
        gimbal_ctrl.yaw_ctrl(-90)""")
    print("Target Found")
    print()



def vision_recognized_marker_letter_F():
    # Scan for F Marker Function
    print("""global marker_found
    vision_ctrl.detect_marker_and_aim(rm_define.marker_letter_F)
    vision_ctrl.disable_detection(rm_define.vision_detection_marker)
    gun_ctrl.fire_once()
    marker_found = True""")
    print("Marker Found")
    Marker_Found == True


def scan_for_fire():
    # Scan for Fire Function
    print()
    print("Scan for Fire")
    print("""global marker_not_found
    vision_ctrl.enable_detection(rm_define.vision_detection_marker)
    marker_found = False""")
    Scanner()


def vision_recognized_people(msg):
    # Recognized People Function
    print("""global person_found
    vision_ctrl.disable_detection(rm_define.vision_detection_people)
    media_ctrl.play_sound(rm_define.media_sound_attacked)
    person_found = True""")
    print("Person Found")
    Marker_Found == True


def scan_for_person_and_play_sound():
    # Scan for Person Function
    print("Scan for Person")
    print()
    print("""global person_found
    vision_ctrl.disable_detection(rm_define.vision_detection_people)
    person_found = False""")
    Scanner()
    Person_Saved = 1
    return Person_Saved


def Room1_Enter():
    # Enter Room 1
    print("""Enter Room 1")
    chassis_ctrl.move_with_distance(0, 3.96)
    gimbal_ctrl.recenter""")
    print()


def Room1_Exit():
    print("""Exit Room 1
    # Return to Exit
    gimbal_ctrl.yaw_ctrl(-180)
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 180)
    chassis_ctrl.move_with_distance(0, 3.75)""")


def Room2_Enter():
    print("Enter Room2")


# insert room 2 commands

def Room2_Exit():
    print("Exit Room2")


# insert room exit commands

def Room3_Enter():
    print("Enter room 3")


# Insert room 3 enter commands

def Room3_Exit():
    print("Exit Room 3")


# insert room 3 exit commands

def Room4_Enter():
    print("Enter Room 4")


# enter room 4 enter commands

def Room4_Exit():
    print("Exit Room 4")


# Enter Room4 Exit Commands


def start():
    Person_Saved = 0
    import time
    # Type 1 is fire
    # Type 2 is Gas
    # Type 3 is Person
    # Sets what type of room it is
    # eventually we want to scan this

    #room_one_type = 1
    #room_two_type = 2
    #room_three_type = 1
    #room_four_type = 4

    print("""robot_ctrl.set_mode(rm_define.robot_mode_free)
    chassis_ctrl.set_trans_speed(0.75)
    chassis_ctrl.set_rotate_speed(30)
    gimbal_ctrl.recenter""")
    print()
    Move_To_Room1()
    print()

    # Fire
    if room_one_type == 1:
        Room1_Enter()
        scan_for_fire()
        Room1_Exit()
    # Gas
    elif room_one_type == 2:
        print("Skip this Room")
    # Person Save
    elif room_one_type == 3:
        Room1_Enter()
        Person_Saved = scan_for_person_and_play_sound()
        Room1_Exit()
        Return_To_Start_Room1()

    print()
    Move_To_Room2(Person_Saved)
    print()
    Person_Saved = 0

    # Fire
    if room_two_type == 1:
        Room2_Enter()
        scan_for_fire()
        Room2_Exit()
    # Gas do nothing
    elif room_two_type == 2:
        print("Skip this room")
    # Person Saved
    elif room_two_type == 3:
        Room2_Enter()
        Person_Saved = scan_for_person_and_play_sound()
        Room2_Exit()
        Return_To_Start_Room2()


    # move to Room 3
    print()
    Move_To_Room3(Person_Saved)
    print()

    Person_Saved = 0
    # Fire
    if room_three_type == 1:
        Room3_Enter()
        scan_for_fire()
        Room3_Exit()
    # Gas
    elif room_three_type == 2:
        print("Skip this room)")
    # Person Save
    elif room_three_type == 3:
        Room3_Enter()
        Person_Saved = scan_for_person_and_play_sound()
        Room3_Exit()
        Return_To_Start_Room3()

    # Move to Room 4
    print()
    Move_To_Room4(Person_Saved)
    print()

    Person_Saved = 0
    # Fire
    if room_four_type == 1:
        Room4_Enter()
        scan_for_fire()
        Room4_Exit()
        Return_To_Start_Room4()
    # Gas
    elif room_four_type == 2:
        Return_To_Start_Room4()
    # Save Person
    elif room_four_type == 3:
        Room4_Enter()
        Person_Saved = scan_for_person_and_play_sound()
        Room4_Exit()
        Return_To_Start_Room4()


start()

