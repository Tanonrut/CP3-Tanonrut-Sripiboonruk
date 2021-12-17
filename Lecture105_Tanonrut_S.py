# สร้าง Class ที่มีฟังชั่นและตัวแปรที่มีการใช้งานซ้ำกัน
class Vehicle:
    lecenseCode = ""
    serialCode = ""
    def turnOnAirConditioner(self):
        print("Turn On : Air")
# นำ Class ที่มีมีการใช้งานซ้ำกันได้ มาใส่ไว้ใน Class ต่างๆ
class Car(Vehicle):
    pass
class PickUp(Vehicle):
    pass
class Van(Vehicle):
    pass

# การเรียกใช้งาน Class
car001 = Car()
car001.turnOnAirConditioner()

pickUp001 = PickUp()
pickUp001.turnOnAirConditioner()

van001 = Van()
van001.turnOnAirConditioner()