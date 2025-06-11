import time
from multiprocessing import Process
from datetime import datetime

def make_burger(student_id):
    start = time.time()
    print(f"[{datetime.now().strftime('%H:%M:%S')}] เริ่มทำเบอร์เกอร์ให้นักเรียนคนที่ {student_id}")
    
    print(f"[{datetime.now().strftime('%H:%M:%S')}] 1. ทอดเบอร์เกอร์...\n")
    time.sleep(5)

    print(f"[{datetime.now().strftime('%H:%M:%S')}] 2. ทอดไก่...\n")
    time.sleep(5)

    print(f"[{datetime.now().strftime('%H:%M:%S')}] 3. ใส่ผักและชีส...\n")
    time.sleep(5)

    print(f"[{datetime.now().strftime('%H:%M:%S')}] 4. ห่อเบอร์เกอร์...\n")
    time.sleep(5)

    end = time.time()  # บันทึกเวลาสิ้นสุด

    print(f"[{datetime.now().strftime('%H:%M:%S')}] เสร็จแล้ว! เบอร์เกอร์ของนักเรียนคนที่ {student_id} ใช้เวลา {end - start:.2f} วินาที\n")

def main():
    start = time.time()
    
    processes = []
    for i in range(1, 6):
        p = Process(target=make_burger, args=(i,))
        processes.append(p)
        p.start()
    
    for p in processes:
        p.join()
    
    end = time.time()
    print(f"[{datetime.now().strftime('%H:%M:%S')}] รวมเวลาทั้งหมด: {end - start:.2f} วินาที")

if __name__ == "__main__":
    main()
