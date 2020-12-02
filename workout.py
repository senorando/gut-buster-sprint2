import requests, json, os
from os.path import join, dirname, split
from dotenv import load_dotenv

import workout_db

exercises = workout_db.exercises

def retrieve_workout_plan(ID):
    workout_plan = {}
    
    return workout_plan
    
def create_workout_plan(level, split):
    workout_plan = {}

    if split == 'Bro Split':
        workout_plan = bro_split(level)
    elif split == 'Full Body':
        workout_plan = full_body(level)
    elif split == 'Push/Pull/Legs':
        workout_plan = push_pull_legs(level)
    elif split == 'Upper/Lower':
        workout_plan = upper_lower(level)

    return workout_plan

#---Different Types of Splits---#
# 4 - 5 days
def bro_split(level):
    bro_split = {
        'num days': 4,
        'days': {
            'Chest/Triceps': (get_chest(level, 'bro') + get_triceps(level, 'bro')),
            'Back/Biceps': (get_back(level, 'bro') + get_biceps(level, 'bro')),
            'Shoulders': get_shoulder(level, 'bro'),
            'Legs/Abs': (get_legs(level, 'bro') + get_abs(level, 'bro')),
        }

    }

    return bro_split

# 2 - 3 days
def full_body(level):
    full_body = {
        'num days': [2, 3],
        'days': {
            'Day 1': (get_chest(level, 'full') + get_back(level, 'full') + get_legs(level, 'full') + get_triceps(level, 'full') + get_biceps(level, 'full')),
            'Day 2': (get_chest(level, 'full') + get_back(level, 'full') + get_legs(level, 'full') + get_triceps(level, 'full') + get_biceps(level, 'full')),
            'Day 3': (get_chest(level, 'full') + get_back(level, 'full') + get_legs(level, 'full') + get_triceps(level, 'full') + get_biceps(level, 'full')),
        },
    }

    return full_body

# 3 or 6 days
def push_pull_legs(level):
    push_pull = {
        'num days': [3, 6],
        'days': {
            'Push 1': (get_chest(level, 'push/pull/legs') + get_shoulder(level, 'push/pull/legs') + get_triceps(level, 'push/pull/legs')),
            'Pull 1': (get_back(level, 'push/pull/legs') + get_biceps(level, 'push/pull/legs') + get_abs(level, 'push/pull/legs')),
            'Legs 1': (get_legs(level, 'push/pull/legs')),
            'Push 2': (get_chest(level, 'push/pull/legs') + get_shoulder(level, 'push/pull/legs') + get_triceps(level, 'push/pull/legs')),
            'Pull 2': (get_back(level, 'push/pull/legs') + get_biceps(level, 'push/pull/legs') + get_abs(level, 'push/pull/legs')),
            'Legs 2': (get_legs(level, 'push/pull/legs')),
        },
    }

    return push_pull

# 2, 4, or 6 days
def upper_lower(level):
    upper_lower = {
        'num days': [2, 4, 6],
        'days': {
            'Upper 1': (get_chest(level, 'upper/lower') + get_back(level, 'upper/lower') + get_shoulder(level, 'upper/lower') + get_biceps(level, 'upper/lower') + get_triceps(level, 'upper/lower')),
            'Lower 1': (get_legs(level, 'upper/lower') + get_abs(level, 'upper/lower')),
            'Upper 2': (get_chest(level, 'upper/lower') + get_back(level, 'upper/lower') + get_shoulder(level, 'upper/lower') + get_biceps(level, 'upper/lower') + get_triceps(level, 'upper/lower')),
            'Lower 2': (get_legs(level, 'upper/lower') + get_abs(level, 'upper/lower')),
            'Upper 3': (get_chest(level, 'upper/lower') + get_back(level, 'upper/lower') + get_shoulder(level, 'upper/lower') + get_biceps(level, 'upper/lower') + get_triceps(level, 'upper/lower')),
            'Lower 3': (get_legs(level, 'upper/lower') + get_abs(level, 'upper/lower')),
        },
    }

    return upper_lower

#---Main Muscle Groups---#
def get_chest(level, split):
    chest_workout = []

    if split == 'bro':
        num_middle = 2
        num_lower = 1
        num_upper = 1
    elif split == 'full':
        num_middle = 2
        num_lower = 0
        num_upper = 0
    elif split == 'push/pull/legs':
        num_middle = 3
        num_lower = 0
        num_upper = 1
    elif split == 'upper/lower':
        num_middle = 2
        num_lower = 0
        num_upper = 1
    else: 
        num_middle = 0
        num_lower = 0
        num_upper = 0
    
    for muscle in exercises['Chest']:
        if muscle not in chest_workout:
            for workout in exercises['Chest'][muscle]:
                if level >= workout['difficulty']:
                    if workout['name'] in chest_workout:
                        continue
                    elif muscle == 'Pectoralis Major':
                        if num_middle == 0:
                            continue
                        else:
                            chest_workout.append(workout)
                            num_middle -= 1
                    elif muscle == 'Clavicular Head':
                        if num_upper == 0:
                            continue
                        else:
                            chest_workout.append(workout)
                            num_upper -= 1
                    elif muscle == 'Lower Pectoralis Major':
                        if num_lower == 0:
                            continue
                        else:
                            chest_workout.append(workout)
                            num_lower -= 1

    return chest_workout

def get_back(level, split):
    back_workout = []
    
    if split == 'bro':
        num_lat = 2
        num_rear_delt = 1
        num_trap = 1
    elif split == 'full':
        num_lat = 1
        num_rear_delt = 1
        num_trap = 0
    elif split == 'push/pull/legs':
        num_lat = 3
        num_rear_delt = 1
        num_trap = 1
    elif split == 'upper/lower':
        num_lat = 2
        num_rear_delt = 0
        num_trap = 1
    else: 
        num_lat = 0
        num_rear_delt = 0
        num_trap = 0

    for muscle in exercises['Back']:
        if muscle not in back_workout:
            for workout in exercises['Back'][muscle]:
                if level >= workout['difficulty']:
                    if workout['name'] in back_workout:
                        continue
                    elif muscle == 'Latissimus Dorsi':
                        if num_lat == 0:
                            continue
                        else:
                            back_workout.append(workout)
                            num_lat -= 1
                    elif muscle == 'Rhomboids':
                        if num_rear_delt == 0:
                            continue
                        else:
                            back_workout.append(workout)
                            num_rear_delt -= 1
                    elif muscle == 'Trapezius':
                        if num_trap == 0:
                            continue
                        else:
                            back_workout.append(workout)
                            num_trap -= 1

    return back_workout

def get_shoulder(level, split):
    shoulder_workout = []

    if split == 'bro':
        num_ant = 1
        num_lat = 3
        num_post = 1
    elif split == 'full':
        num_ant = 1
        num_lat = 1
        num_post = 0
    elif split == 'push/pull/legs':
        num_ant = 1
        num_lat = 2
        num_post = 0
    elif split == 'upper/lower':
        num_ant = 0
        num_lat = 2
        num_post = 0
    else: 
        num_ant = 0
        num_lat = 0
        num_post = 0

    for muscle in exercises['Shoulders']:
            if muscle not in shoulder_workout:
                for workout in exercises['Shoulders'][muscle]:
                    if level >= workout['difficulty']:
                        if workout['name'] in shoulder_workout:
                            continue
                        elif muscle == 'Anterior Deltoid':
                            if num_ant == 0:
                                continue
                            else:
                                shoulder_workout.append(workout)
                                num_ant -= 1
                        elif muscle == 'Lateral Deltoid':
                            if num_lat == 0:
                                continue
                            else:
                                shoulder_workout.append(workout)
                                num_lat -= 1
                        elif muscle == 'Posterior Deltoid':
                            if num_post == 0:
                                continue
                            else:
                                shoulder_workout.append(workout)
                                num_post -= 1

    return shoulder_workout

def get_triceps(level, split):
    triceps_workout = []
    
    if split == 'bro':
        num_long = 2
        num_lat = 1
        num_med = 0
    elif split == 'full':
        num_long = 1
        num_lat = 1
        num_med = 0
    elif split == 'push/pull/legs':
        num_long = 3
        num_lat = 0
        num_med = 0
    elif split == 'upper/lower':
        num_long = 2
        num_lat = 0
        num_med = 0
    else: 
        num_lat = 0
        num_rear_delt = 0
        num_trap = 0

    for muscle in exercises['Triceps']:
        if muscle not in triceps_workout:
            for workout in exercises['Triceps'][muscle]:
                if level >= workout['difficulty']:
                    if workout['name'] in triceps_workout:
                        continue
                    elif muscle == 'Long Head':
                        if num_long == 0:
                            continue
                        else:
                            triceps_workout.append(workout)
                            num_long -= 1
                    elif muscle == 'Lateral Head':
                        if num_lat == 0:
                            continue
                        else:
                            triceps_workout.append(workout)
                            num_lat -= 1
                    elif muscle == 'Medial Head':
                        if num_med == 0:
                            continue
                        else:
                            triceps_workout.append(workout)
                            num_med -= 1

    return triceps_workout

def get_biceps(level, split):
    biceps_workout = []
    
    if split == 'bro':
        num_long = 2
        num_short = 1
    elif split == 'full':
        num_long = 1
        num_short = 1
    elif split == 'push/pull/lower':
        num_long = 2
        num_short = 0
    elif split == 'upper/lower':
        num_long = 1
        num_short = 0   
    else: 
        num_long = 0
        num_short = 0

    for muscle in exercises['Biceps']:
        if muscle not in biceps_workout:
            for workout in exercises['Biceps'][muscle]:
                if level >= workout['difficulty']:
                    if workout['name'] in biceps_workout:
                        continue
                    elif muscle == 'Long Head':
                        if num_long == 0:
                            continue
                        else:
                            biceps_workout.append(workout)
                            num_long -= 1
                    elif muscle == 'Short Head':
                        if num_short == 0:
                            continue
                        else:
                            biceps_workout.append(workout)
                            num_short -= 1

    return biceps_workout

def get_legs(level, split):
    legs_workout = []
    
    if split == 'bro':
        num_quad = 2
        num_ham = 1
        num_glute = 2
    elif split == 'full':
        num_quad = 1
        num_ham = 1
        num_glute = 0
    elif split == 'push/pull/legs':
        num_quad = 2
        num_ham = 2
        num_glute = 2
    elif split == 'upper/lower':
        num_quad = 2
        num_ham = 1
        num_glute = 2
    else: 
        num_quad = 0
        num_ham = 0
        num_glute = 0

    for muscle in exercises['Legs']:
        if muscle not in legs_workout:
            for workout in exercises['Legs'][muscle]:
                if level >= workout['difficulty']:
                    if workout['name'] in legs_workout:
                        continue
                    elif muscle == 'Quadriceps':
                        if num_quad == 0:
                            continue
                        else:
                            legs_workout.append(workout)
                            num_quad -= 1
                    elif muscle == 'Hamstrings':
                        if num_ham == 0:
                            continue
                        else:
                            legs_workout.append(workout)
                            num_ham -= 1
                    elif muscle == 'Glutes':
                        if num_glute == 0:
                            continue
                        else:
                            legs_workout.append(workout)
                            num_glute -= 1

    return legs_workout

def get_abs(level, split):
    abs_workout = []

    return abs_workout

# level = -1

# while level != 0:
#     print('\nEnter your level: ')
#     level = input()
    
#     print('Enter a split\n<Bro Split> <Full Body> <Push/Pull/Legs> <Upper/Lower>')
#     split = input()
    
#     print(create_workout_plan(int(level), split))