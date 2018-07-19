sequence = ["1. mountain pose", "2. foward fold", "3. plank"]

for poses in sequence:
    print(poses)


addedPose = input("Choose a pose number or enter q to quit")

while addedPose != "q":
    sequence = ["mountain pose", "foward fold", "plank"]

    if addedPose == "1":
        print(sequence[0])
    elif addedPose == "2":
        print(sequence[1])
    elif addedPose == "3":
        print(sequence[2])
    else:
        print(addedPose)

    addedPose = input("Choose a pose number or enter q to quit")
    print(addedPose)






