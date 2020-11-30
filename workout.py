import requests, json, os
from os.path import join, dirname, split
from dotenv import load_dotenv

import workout_db

exercises = workout_db.exercises

def create_workout_plan(level, split, custom_split):
    workout_plan = {}
    custom_split = custom_split

    if split == 'Bro Split':
        workout_plan = bro_split(level, custom_split)
    elif split == 'Full Body':
        workout_plan = full_body(level)
    elif split == 'Push/Pull/Legs':
        workout_plan = push_pull_legs(level)
    elif split == 'Upper/Lower':
        workout_plan = upper_lower(level)

    return workout_plan

#---Different Types of Splits---#
# 4 - 5 days
def bro_split(level, custom_split):
    if custom_split == 'none':
        custom_split = [
            ['Chest', 'Triceps'],
            ['Back', 'Biceps'],
            ['Shoulders'],
            ['Legs', 'Abs'],
        ]
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

        },
    }

    return full_body

# 3 or 6 days
def push_pull_legs(level):
    push_pull = {}

    return push_pull

# 2, 4, or 6 days
def upper_lower(level):
    upper_lower = {}

    return upper_lower

#---Main Muscle Groups---#
def get_chest(level, split):
    chest_workout = []
    num_middle = 0
    num_upper = 0
    num_lower = 0

    if split == 'bro':
        for muscle in exercises['Chest']:
            if muscle not in chest_workout:
                for workout in exercises['Chest'][muscle]:
                    if level >= workout['difficulty']:
                        if workout['name'] in chest_workout:
                            continue
                        elif muscle == 'Pectoralis Major':
                            if num_middle == 2:
                                continue
                            else:
                                chest_workout.append(workout)
                                num_middle += 1
                        elif muscle == 'Clavicular Head':
                            if num_upper == 1:
                                continue
                            else:
                                chest_workout.append(workout)
                                num_upper += 1
                        elif muscle == 'Lower Pectoralis Major':
                            if num_lower == 1:
                                continue
                            else:
                                chest_workout.append(workout)
                                num_lower += 1

    return chest_workout

def get_back(level, split):
    back_workout = []
        
    num_lat = 0
    num_rear_delt = 0
    num_trap = 0

    if split == 'bro':
        for muscle in exercises['Back']:
            if muscle not in back_workout:
                for workout in exercises['Back'][muscle]:
                    if level >= workout['difficulty']:
                        if workout['name'] in back_workout:
                            continue
                        elif muscle == 'Latissimus Dorsi':
                            if num_lat == 2:
                                continue
                            else:
                                back_workout.append(workout)
                                num_lat += 1
                        elif muscle == 'Rhomboids':
                            if num_rear_delt == 2:
                                continue
                            else:
                                back_workout.append(workout)
                                num_rear_delt += 1
                        elif muscle == 'Trapezius':
                            if num_trap == 1:
                                continue
                            else:
                                back_workout.append(workout)
                                num_trap += 1

    return back_workout

def get_shoulder(level, split):
    shoulder_workout = []

    num_ant = 0
    num_lat = 0
    num_post = 0

    if split == 'bro':
        for muscle in exercises['Shoulders']:
            if muscle not in shoulder_workout:
                for workout in exercises['Shoulders'][muscle]:
                    if level >= workout['difficulty']:
                        if workout['name'] in shoulder_workout:
                            continue
                        elif muscle == 'Anterior Deltoid':
                            if num_ant == 2:
                                continue
                            else:
                                shoulder_workout.append(workout)
                                num_ant += 1
                        elif muscle == 'Lateral Deltoid':
                            if num_lat == 3:
                                continue
                            else:
                                shoulder_workout.append(workout)
                                num_lat += 1
                        elif muscle == 'Posterior Deltoid':
                            if num_post == 2:
                                continue
                            else:
                                shoulder_workout.append(workout)
                                num_post += 1

    return shoulder_workout

def get_triceps(level, split):
    triceps_workout = []
    
    num_long = 0
    num_lat = 0
    num_med = 0

    if split == 'bro':
        for muscle in exercises['Triceps']:
            if muscle not in triceps_workout:
                for workout in exercises['Triceps'][muscle]:
                    if level >= workout['difficulty']:
                        if workout['name'] in triceps_workout:
                            continue
                        elif muscle == 'Long Head':
                            if num_long == 2:
                                continue
                            else:
                                triceps_workout.append(workout)
                                num_long += 1
                        elif muscle == 'Lateral Head':
                            if num_lat == 1:
                                continue
                            else:
                                triceps_workout.append(workout)
                                num_lat += 1
                        elif muscle == 'Medial Head':
                            if num_med == 0:
                                continue
                            else:
                                triceps_workout.append(workout)
                                num_med += 1

    return triceps_workout

def get_biceps(level, split):
    biceps_workout = []

    num_long = 0
    num_short = 0

    if split == 'bro':
        for muscle in exercises['Biceps']:
            if muscle not in biceps_workout:
                for workout in exercises['Biceps'][muscle]:
                    if level >= workout['difficulty']:
                        if workout['name'] in biceps_workout:
                            continue
                        elif muscle == 'Long Head':
                            if num_long == 2:
                                continue
                            else:
                                biceps_workout.append(workout)
                                num_long += 1
                        elif muscle == 'Short Head':
                            if num_short == 1:
                                continue
                            else:
                                biceps_workout.append(workout)
                                num_short += 1

    return biceps_workout

def get_legs(level, split):
    legs_workout = []
    
    num_quad = 0
    num_ham = 0
    num_glute = 0

    if split == 'bro':
        for muscle in exercises['Legs']:
            if muscle not in legs_workout:
                for workout in exercises['Legs'][muscle]:
                    if level >= workout['difficulty']:
                        if workout['name'] in legs_workout:
                            continue
                        elif muscle == 'Quadriceps':
                            if num_quad == 2:
                                continue
                            else:
                                legs_workout.append(workout)
                                num_quad += 1
                        elif muscle == 'Hamstrings':
                            if num_ham == 1:
                                continue
                            else:
                                legs_workout.append(workout)
                                num_ham += 1
                        elif muscle == 'Glutes':
                            if num_glute == 2:
                                continue
                            else:
                                legs_workout.append(workout)
                                num_glute += 1

    return legs_workout

def get_abs(level, split):
    abs_workout = []

    return abs_workout