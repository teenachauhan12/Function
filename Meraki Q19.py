
def checkSpeed(speed):
    if speed <= 70:
        return "OK"
    else:
        speed1 = (speed-70)//5
        if speed1 <= 12:
            print(f"Point: {speed1}")
        else:
            print("License suspended")

checkSpeed(int(input("Enter speed: ")))