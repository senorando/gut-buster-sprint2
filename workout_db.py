'''
    Difficulty Levels:
        1 - Beginner
        2 - Intermediate
        3 - Advanced
'''

exercises = {
    'Reps/Sets/Rest': {
        'Strength': {
            'rep range': [1, 6],
            'set range': [3, 5],
            'rest': '2-5 minutes',
        },
        'Newbie': {
            'rep range': [8, 8],
            'set range': [3, 3],
            'rest': '90 seconds',
        },
        'Hypertrophy': {
            'rep range': [7, 12],
            'set range': [3, 4],
            'rest': '1-2 minutes',
        },
    },
    'Chest': {
        'Pectoralis Major': [
            {
                'name': 'Barbell Bench Press',
                'difficulty': 2,
                'accessory_muscles': 'Clavicular Head, Triceps, Anterior Delt, Forearms',
                'movement': 'push',
                'equipment': 'Barbell, Bench',
            }, 
            {
                'name': 'Dumbbell Bench Press',
                'difficulty': 1,
                'accessory_muscles': 'Triceps, Shoulders',
                'movement': 'push',
                'equipment': 'Dumbbells, Bench',
            }, 
            {
                'name': 'Push Ups',
                'difficulty': 1,
                'accessory_muscles': 'Triceps, Shoulders',
                'movement': 'push',
                'equipment': 'N/A',
            },
            {
                'name': 'Cable Chest Flyes',
                'difficulty': 2,
                'accessory_muscles': 'Shoulders',
                'movement': 'aduction',
                'equipment': 'Cables, Bench (optional)',
            },
            {
                'name': 'Cable Chest Flyes',
                'difficulty': 2,
                'accessory_muscles': 'Shoulders',
                'movement': 'aduction',
                'equipment': 'Cables, Bench (optional)',
            },
        ],
        'Clavicular Head': [
            {
                'name': 'Incline Barbell Bench Press',
                'difficulty': 2,
                'accessory_muscles': 'Triceps, Shoulders, Forearms',
                'movement': 'push',
                'equipment': 'Barbell, Bench',
            }, 
            {
                'name': 'Incline Dumbell Bench Press',
                'difficulty': 1,
                'accessory_muscles': 'Triceps, Shoulders',
                'movement': 'push',
                'equipment': 'Dumbells, Bench',
            }, 
            {
                'name': 'Decline Push Ups',
                'difficulty': 1,
                'accessory_muscles': 'Triceps, Shoulders',
                'movement': 'push',
                'equipment': 'N/A',
            },
            {
                'name': 'Incline Cable Chest Flyes',
                'difficulty': 2,
                'accessory_muscles': 'Shoulders',
                'movement': 'aduction',
                'equipment': 'Cables, Bench',
            },
        ],
        'Lower Pectoralis Major': [
            {
                'name': 'Decline Barbell Bench Press',
                'difficulty': 2,
                'accessory_muscles': 'Triceps, Shoulders, Forearms',
                'movement': 'push',
                'equipment': 'Barbell, Bench',
            },
            {
                'name': 'Decline Dumbell Bench Press',
                'difficulty': 1,
                'accessory_muscles': 'Triceps, Shoulders',
                'movement': 'push',
                'equipment': 'Dumbells, Bench',
            }, 
            {
                'name': 'Incline Push Ups',
                'difficulty': 1,
                'accessory_muscles': 'Triceps, Shoulders',
                'movement': 'push',
                'equipment': 'N/A',
            },
            {
                'name': 'Decline Cable Chest Flyes',
                'difficulty': 2,
                'accessory_muscles': 'Shoulders',
                'movement': 'aduction',
                'equipment': 'Cables',
            },
        ],        
    },
    'Back': {
        'Latissimus Dorsi': [
            {
                'name': 'Seated Row',
                'difficulty': 1,
                'accessory_muscles': 'Rhomboids, Biceps',
                'movement': 'pull',
                'equipment': 'Bench + Cable',
            }, 
            {
                'name': 'One Arm Bent Over Row',
                'difficulty': 1,
                'accessory_muscles': 'Rhomboids, Biceps',
                'movement': 'pull',
                'equipment': 'Dumbell',
            }, 
            {
                'name': 'Lat 3',
                'difficulty': 1,
                'accessory_muscles': '',
                'movement': 'pull',
                'equipment': '',
            },
            {
                'name': 'Lat 4',
                'difficulty': 1,
                'accessory_muscles': '',
                'movement': 'aduction',
                'equipment': '',
            },
        ],
        'Rhomboids': [
            {
                'name': 'Rhomb 1',
                'difficulty': 2,
                'accessory_muscles': '',
                'movement': 'pull',
                'equipment': '',
            }, 
            {
                'name': 'Rhomb 2',
                'difficulty': 1,
                'accessory_muscles': '',
                'movement': 'pull',
                'equipment': '',
            }, 
            {
                'name': 'Rhomb 3',
                'difficulty': 1,
                'accessory_muscles': '',
                'movement': 'pull',
                'equipment': '',
            },
            {
                'name': 'Rhomb 4',
                'difficulty': 2,
                'accessory_muscles': '',
                'movement': 'aduction',
                'equipment': '',
            },
        ],
        'Trapezius': [
            {
                'name': 'Dumbbell Shrugs',
                'difficulty': 1,
                'accessory_muscles': 'Forearms',
                'movement': 'pull',
                'equipment': 'Dumbbell, Bench (optional)',
            },
            {
                'name': 'Barbell Shrugs',
                'difficulty': 1,
                'accessory_muscles': 'Forearms',
                'movement': 'pull',
                'equipment': 'Barbell',
            }, 
            {
                'name': 'Trap 3',
                'difficulty': 1,
                'accessory_muscles': 'Triceps, Shoulders',
                'movement': '',
                'equipment': '',
            },
            {
                'name': 'Trap 4',
                'difficulty': 1,
                'accessory_muscles': '',
                'movement': '',
                'equipment': '',
            },
        ],        
    },
    'Triceps': {
        'Long Head': [
            {
                'name': 'Long 1',
                'difficulty': 1,
                'accessory_muscles': '',
                'movement': '',
                'equipment': '',
            }, 
            {
                'name': 'Long 2',
                'difficulty': 1,
                'accessory_muscles': '',
                'movement': '',
                'equipment': '',
            }, 
            {
                'name': 'Long 3',
                'difficulty': 1,
                'accessory_muscles': '',
                'movement': 'pull',
                'equipment': '',
            },
            {
                'name': 'Long 4',
                'difficulty': 1,
                'accessory_muscles': '',
                'movement': '',
                'equipment': '',
            },
        ],
        'Lateral Head': [
            {
                'name': 'Lat 1',
                'difficulty': 2,
                'accessory_muscles': '',
                'movement': '',
                'equipment': '',
            }, 
            {
                'name': 'Lat 2',
                'difficulty': 1,
                'accessory_muscles': '',
                'movement': 'pull',
                'equipment': '',
            }, 
            {
                'name': 'Lat 3',
                'difficulty': 1,
                'accessory_muscles': '',
                'movement': '',
                'equipment': '',
            },
            {
                'name': 'Lat 4',
                'difficulty': 2,
                'accessory_muscles': '',
                'movement': '',
                'equipment': '',
            },
        ],
        'Medial Head': [
            {
                'name': 'Med 1',
                'difficulty': 1,
                'accessory_muscles': '',
                'movement': '',
                'equipment': '',
            },
            {
                'name': 'Med 2',
                'difficulty': 1,
                'accessory_muscles': '',
                'movement': '',
                'equipment': '',
            }, 
            {
                'name': 'Med 3',
                'difficulty': 1,
                'accessory_muscles': '',
                'movement': '',
                'equipment': '',
            },
            {
                'name': 'Med 4',
                'difficulty': 1,
                'accessory_muscles': '',
                'movement': '',
                'equipment': '',
            },
        ],    
    },
    'Biceps': {
        'Long Head': [
            {
                'name': 'Long 1',
                'difficulty': 1,
                'accessory_muscles': '',
                'movement': '',
                'equipment': '',
            }, 
            {
                'name': 'Long 2',
                'difficulty': 1,
                'accessory_muscles': '',
                'movement': '',
                'equipment': '',
            }, 
            {
                'name': 'Long 3',
                'difficulty': 1,
                'accessory_muscles': '',
                'movement': 'pull',
                'equipment': '',
            },
            {
                'name': 'Long 4',
                'difficulty': 1,
                'accessory_muscles': '',
                'movement': '',
                'equipment': '',
            },
        ],
        'Short Head': [
            {
                'name': 'Short 1',
                'difficulty': 2,
                'accessory_muscles': '',
                'movement': '',
                'equipment': '',
            }, 
            {
                'name': 'Short 2',
                'difficulty': 1,
                'accessory_muscles': '',
                'movement': 'pull',
                'equipment': '',
            }, 
            {
                'name': 'Short 3',
                'difficulty': 1,
                'accessory_muscles': '',
                'movement': '',
                'equipment': '',
            },
            {
                'name': 'Short 4',
                'difficulty': 2,
                'accessory_muscles': '',
                'movement': '',
                'equipment': '',
            },
        ],
    },
    'Shoulders': {
        'Anterior Deltoid': [
            {
                'name': 'Anterior 1',
                'difficulty': 1,
                'accessory_muscles': '',
                'movement': '',
                'equipment': '',
            }, 
            {
                'name': 'Anterior 2',
                'difficulty': 1,
                'accessory_muscles': '',
                'movement': '',
                'equipment': '',
            }, 
            {
                'name': 'Anterior 3',
                'difficulty': 1,
                'accessory_muscles': '',
                'movement': 'pull',
                'equipment': '',
            },
            {
                'name': 'Anterior 4',
                'difficulty': 1,
                'accessory_muscles': '',
                'movement': '',
                'equipment': '',
            },
        ],
        'Lateral Deltoid': [
            {
                'name': 'Lat 1',
                'difficulty': 2,
                'accessory_muscles': '',
                'movement': '',
                'equipment': '',
            }, 
            {
                'name': 'Lat 2',
                'difficulty': 1,
                'accessory_muscles': '',
                'movement': 'pull',
                'equipment': '',
            }, 
            {
                'name': 'Lat 3',
                'difficulty': 1,
                'accessory_muscles': '',
                'movement': '',
                'equipment': '',
            },
            {
                'name': 'Lat 4',
                'difficulty': 2,
                'accessory_muscles': '',
                'movement': '',
                'equipment': '',
            },
        ],
        'Posterior Deltoid': [
            {
                'name': 'Posterior 1',
                'difficulty': 1,
                'accessory_muscles': '',
                'movement': '',
                'equipment': '',
            },
            {
                'name': 'Posterior 2',
                'difficulty': 1,
                'accessory_muscles': '',
                'movement': '',
                'equipment': '',
            }, 
            {
                'name': 'Posterior 3',
                'difficulty': 1,
                'accessory_muscles': '',
                'movement': '',
                'equipment': '',
            },
            {
                'name': 'Posterior 4',
                'difficulty': 1,
                'accessory_muscles': '',
                'movement': '',
                'equipment': '',
            },
        ],    
    },
    'Legs': {
        'Quadriceps': [
            {
                'name': 'Quads 1',
                'difficulty': 1,
                'accessory_muscles': '',
                'movement': '',
                'equipment': '',
            }, 
            {
                'name': 'Quads 2',
                'difficulty': 1,
                'accessory_muscles': '',
                'movement': '',
                'equipment': '',
            }, 
            {
                'name': 'Quads 3',
                'difficulty': 1,
                'accessory_muscles': '',
                'movement': '',
                'equipment': '',
            },
            {
                'name': 'Quads 4',
                'difficulty': 1,
                'accessory_muscles': '',
                'movement': '',
                'equipment': '',
            },
        ],
        'Hamstrings': [
            {
                'name': 'Hamstrings 1',
                'difficulty': 2,
                'accessory_muscles': '',
                'movement': '',
                'equipment': '',
            }, 
            {
                'name': 'Hamstrings 2',
                'difficulty': 1,
                'accessory_muscles': '',
                'movement': '',
                'equipment': '',
            }, 
            {
                'name': 'Hamstrings 3',
                'difficulty': 1,
                'accessory_muscles': '',
                'movement': '',
                'equipment': '',
            },
            {
                'name': 'Hamstrings 4',
                'difficulty': 2,
                'accessory_muscles': '',
                'movement': '',
                'equipment': '',
            },
        ],
        'Glutes': [
            {
                'name': 'Glutes 1',
                'difficulty': 1,
                'accessory_muscles': '',
                'movement': '',
                'equipment': '',
            },
            {
                'name': 'Glutes 2',
                'difficulty': 1,
                'accessory_muscles': '',
                'movement': '',
                'equipment': '',
            }, 
            {
                'name': 'Glutes 3',
                'difficulty': 1,
                'accessory_muscles': '',
                'movement': '',
                'equipment': '',
            },
            {
                'name': 'Glutes 4',
                'difficulty': 1,
                'accessory_muscles': '',
                'movement': '',
                'equipment': '',
            },
        ],        
    },
    'Abs': {
        '': [
            {
                'name': ' 1',
                'difficulty': 1,
                'accessory_muscles': '',
                'movement': '',
                'equipment': '',
            }, 
            {
                'name': ' 2',
                'difficulty': 1,
                'accessory_muscles': '',
                'movement': '',
                'equipment': '',
            }, 
            {
                'name': ' 3',
                'difficulty': 1,
                'accessory_muscles': '',
                'movement': '',
                'equipment': '',
            },
            {
                'name': ' 4',
                'difficulty': 1,
                'accessory_muscles': '',
                'movement': '',
                'equipment': '',
            },
        ],
        '': [
            {
                'name': ' 1',
                'difficulty': 2,
                'accessory_muscles': '',
                'movement': '',
                'equipment': '',
            }, 
            {
                'name': ' 2',
                'difficulty': 1,
                'accessory_muscles': '',
                'movement': '',
                'equipment': '',
            }, 
            {
                'name': ' 3',
                'difficulty': 1,
                'accessory_muscles': '',
                'movement': '',
                'equipment': '',
            },
            {
                'name': ' 4',
                'difficulty': 2,
                'accessory_muscles': '',
                'movement': '',
                'equipment': '',
            },
        ],
        '': [
            {
                'name': ' 1',
                'difficulty': 1,
                'accessory_muscles': '',
                'movement': '',
                'equipment': '',
            },
            {
                'name': ' 2',
                'difficulty': 1,
                'accessory_muscles': '',
                'movement': '',
                'equipment': '',
            }, 
            {
                'name': ' 3',
                'difficulty': 1,
                'accessory_muscles': '',
                'movement': '',
                'equipment': '',
            },
            {
                'name': ' 4',
                'difficulty': 1,
                'accessory_muscles': '',
                'movement': '',
                'equipment': '',
            },
        ],        
    },
}