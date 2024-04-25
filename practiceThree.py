def check_speed(speed):
    penalty_points = (speed - 70) // 5
    if speed <= 70:
        return "good"
    else:
        if penalty_points > 12:
            print("گواهینامه شما باطل شد")
        return penalty_points

speed = int(input("سرعت خودرو را وارد کنید: "))
penalty = check_speed(speed)
if penalty:
    print("امتیاز منفی:", penalty)
