import os

def input_student_data():
    name = input("ป้อนชื่อ-สกุลนักเรียน: ")
    mid_score = input("ป้อนคะแนนกลางภาค: ")
    final_score = input("ป้อนคะแนนปลายภาค: ")
    point_score = input("ป้อนคะแนนเก็บ: ")
    total_score = int(mid_score) + int(final_score) + int(point_score)
    return name, mid_score, final_score, point_score, total_score

def create_subject_file():
    print("สร้างไฟล์วิชาใหม่เพื่อเพิ่มข้อมูล")
    subject_name = input("ป้อนชื่อไฟล์วิชาเพื่อเก็บข้อมูลคะแนน(xxx.txt): ").strip()
    if not ".txt" in subject_name:
        print("ชื่อ-นามสกุลไฟล์ไม่ถูกต้องกรุณาป้อนใหม่")
    else:
        with open(subject_name, "w", encoding="utf-8") as new_file:
            name, mid_score, final_score, point_score, total_score = input_student_data()
            result_status = "ผ่าน" if total_score > 50 else "ไม่ผ่าน"
            new_file.write(f"ชื่อ: {name}\nคะแนนกลางภาค: {mid_score}\nคะแนนปลายภาค: {final_score}\nคะแนนเก็บ: {point_score}\nคะแนนรวม: {total_score}\nผล: {result_status}\n\n")
        print("สร้างไฟล์ใหม่และเพิ่มข้อมูลลงไฟล์เรียบร้อยแล้ว")

def add_data_to_file():
    file_names = [file for file in os.listdir() if file.endswith(".txt")]
    if not file_names:
        print("ไม่มีไฟล์ใดๆอยู่เลย")
    else:
        for file in file_names:
            print(file)
        print("เลือกวิชาและเพิ่มข้อมูลต่อท้ายไฟล์")
        selected_file = input("เลือกไฟล์โดยการป้อนชื่อไฟล์: ").strip()
        if selected_file not in file_names:
            print("คุณพิมพ์ชื่อไฟล์ผิด หรือ นามสกุลไฟล์ผิด")
        else:
            with open(selected_file, "a", encoding="utf-8") as add_file:
                name, mid_score, final_score, point_score, total_score = input_student_data()
                result_status = "ผ่าน" if total_score > 50 else "ไม่ผ่าน"
                add_file.write(f"ชื่อ: {name}\nคะแนนกลางภาค: {mid_score}\nคะแนนปลายภาค: {final_score}\nคะแนนเก็บ: {point_score}\nคะแนนรวม: {total_score}\nผล: {result_status}\n\n")
            print("เพิ่มข้อมูลต่อท้ายไฟล์เรียบร้อยแล้ว")

def read_data_from_file():
    file_names = [file for file in os.listdir() if file.endswith(".txt")]
    if not file_names:
        print("ไม่มีไฟล์ใดๆอยู่เลย")
    else:
        for file in file_names:
            print(file)
        print("อ่านข้อมูลในไฟล์")
        selected_file = input("เลือกไฟล์โดยการป้อนชื่อไฟล์: ").strip()
        if selected_file not in file_names:
            print("คุณพิมพ์ชื่อไฟล์ผิด หรือ นามสกุลไฟล์ผิด")
        else:
            with open(selected_file, "r", encoding="utf-8") as data_file:
                read_data = data_file.read()
                print(read_data)

def remove_data_from_file():
    print("เลือกวิชาและลบไฟล์")
    file_names = [file for file in os.listdir() if file.endswith(".txt")]
    if not file_names:
        print("ไม่มีไฟล์ใดๆอยู่เลย")
    else:
        for file in file_names:
            print(file)
        selected_file = input("เลือกไฟล์โดยการป้อนชื่อไฟล์: ").strip()
        if selected_file not in file_names:
            print("คุณพิมพ์ชื่อไฟล์ผิด หรือ นามสกุลไฟล์ผิด")
        elif selected_file in file_names:
            os.remove(selected_file)
            print("ลบไฟล์เรียบร้อย")

def main_menu():
    while True:
        print("SCHOOL")
        print("1. สร้างไฟล์วิชาใหม่เพื่อเพิ่มข้อมูล")
        print("2. เลือกวิชาและเพิ่มข้อมูลต่อท้ายไฟล์")
        print("3. เลือกวิชาและอ่านข้อมูลจากไฟล์มาแสดงผล")
        print("4. เลือกวิชาและลบไฟล์")
        print("0. จบการทำงาน")
        try:
            user_input = input("เลือกเมนู: ")
            if user_input == "1":
                create_subject_file()
                break
            elif user_input == "2":
                add_data_to_file()
                break
            elif user_input == "3":
                read_data_from_file()
                break
            elif user_input == "4":
                remove_data_from_file()
                break
            elif user_input == "0":
                print("จบการทำงาน")
                break
            else:
                print("กรุณาเลือกเมนู 1, 2, 3, 4 หรือ 0 เท่านั้น")
                break
        except ValueError:
            print("กรุณาป้อนตัวเลขด้วยครับ")
            break

main_menu()
