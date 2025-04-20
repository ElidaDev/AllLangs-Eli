import random

# Function to read exercises from a file and return them as a list
def read_exercises(file_name):
    with open(file_name, 'r') as file:
        exercises = file.readlines()
    return [exercise.strip() for exercise in exercises]

# Function to select one random exercise from each category
def select_random_exercises():
    global Muscle
    Muscle = True
    equipmentGroups = {
        "Bands": "BANDS.csv",
        "Barbell": "BARBELL.csv",
        "BattleRopes": "BATTLE ROPES.csv",
        "Bench": "BENCH.csv",
        "Bodyweight": "BODYWEIGHT.csv",
        "Bosu": "BOSU.csv",
        "Box": "BOX.csv",
        "Cables": "CABLES.csv",
        "DipBar": "DIP BAR.csv",
        "DumbBell": "DUMBBELL.csv",
        "EZCURL": "EZ CURL BAR.csv",
        "Hammer": "HAMMER.csv",
        "HexBar": "HEX BAR.csv",
        "KettleBell": "KETTLEBELL.csv",
        "Ladder": "LADDER.csv",
        "LandMine": "LANDMINE.csv",
        "Machine": "MACHINE.csv",
        "MedBall": "MEDBALL.csv",
        "PullUpBar": "PULL-UP BAR.csv",
        "Roller": "ROLLER.csv",
        "TRX": "TRX.csv",
        "YogaBall": "YOGA BALL.csv"
    }
    muscleGroups ={
        # "Calves": "back_calves.csv",
        # "Glutes": "back_glutes.csv",
        # "Hamstrings": "back_hamstrings.csv",
        # "Lats": "back_lats.csv",
        # "LowerBack": "back_lower_back.csv",
        "Abs": "front_abs.csv",
        # "Biceps": "front_biceps.csv",
        # "Chest": "front_chest.csv",
        "Forearms": "front_forearms.csv",
        # "HipAbductors": "front_hip_abductors.csv",
        # "HipAdductors": "front_hip_adductors.csv",
        # "HipFlexors": "front_hip_flexors.csv",
        # "Neck": "front_neck.csv",
        # "Obliques": "front_obliques.csv",
        # "Quads": "front_quads.csv",
        # "Shoulders": "front_shoulders.csv",
        # "Tibialis": "front_tibialis.csv",
        # "Traps": "front_traps.csv",
        "Tricep": "back_tricep.csv"
    }
    # Select one random exercise from each category
    random_exercises = {}

    Equipment = not(Muscle)
    if Muscle:
        for muscle, file_name in muscleGroups.items():
            file_name = "muscle_groups/"+ file_name
            exercises = read_exercises(file_name)
            random_exercises[muscle] = random.choice(exercises)
    if Equipment:
        for equipment, file_name in equipmentGroups.items():
            file_name = "equipment_groups/"+ file_name
            exercises = read_exercises(file_name)
            random_exercises[equipment] = random.choice(exercises)
    return random_exercises



# Print the randomly selected exercises from each category
print()
exercisesAmount = 3
for i in range(exercisesAmount):
    random_exercises = select_random_exercises()
    for category, exercise in random_exercises.items():
        exercise = list(exercise.split(","))
        if Muscle:
            print(f"{category}: https://www.trainwell.net/exercises/{exercise[0]}\nEquipment: {exercise[1]}\nOther Groups: {exercise[2]}\n")
        else:
            print(f"{category}: https://www.trainwell.net/exercises/{exercise[0]}\nMuscles: {exercise[1]}\nOther Groups: {exercise[2]}\n")

