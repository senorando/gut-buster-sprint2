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
                'name': 'Machine-assisted Chest Dip',
                'difficulty': 1,
                'accessory_muscles': 'Pectoralis Major, Triceps, Rhomboids, Teres Major',
                'utility': 'Basic',
                'equipment': 'Chest Dip Machine',
            }, 
            {
                'name': 'Barbell Bench Press',
                'difficulty': 2,
                'accessory_muscles': 'Clavicular Head, Triceps, Anterior Delt, Forearms',
                'utility': 'Basic',
                'equipment': 'Barbell, Bench',
            }, 
            {
                'name': 'Dumbbell Bench Press',
                'difficulty': 1,
                'accessory_muscles': 'Triceps, Shoulders',
                'utility': 'Basic',
                'equipment': 'Dumbbells, Bench',
            }, 
            {
                'name': 'Cable Chest Press',
                'difficulty': 1,
                'accessory_muscles': 'Triceps, Biceps, Deltoid, Pectoralis Major',
                'utility': 'Basic',
                'equipment': 'Chest Bench Press, Cable',
            }, 
            {
                'name': 'Push Ups',
                'difficulty': 1,
                'accessory_muscles': 'Triceps, Shoulders',
                'utility': 'Basic or Auxilary',
                'equipment': 'N/A',
            },
            {
                'name': 'Seated Cable Chest Flyes',
                'difficulty': 2,
                'accessory_muscles': 'Triceps, Biceps, Deltoid, Pectoralis Major',
                'utility': 'Auxilary',
                'equipment': 'Cables, Bench, Chest fly Machine',
            },
            {
                'name': 'Cable Lying Fly',
                'difficulty': 2,
                'accessory_muscles': 'Biceps, Triceps, Deltoid, Wrist Flexors ',
                'utility': 'Auxilary',
                'equipment': 'Cables, Bench, Chest fly Machine',
            },
        ],
        'Clavicular Head': [
            {
                'name': 'Incline Barbell Bench Press',
                'difficulty': 2,
                'accessory_muscles': 'Triceps, Shoulders, Forearms',
                'utility': 'Basic',
                'equipment': 'Barbell, Bench',
            }, 
            {
                'name': 'Incline Dumbell Bench Press',
                'difficulty': 1,
                'accessory_muscles': 'Triceps, Shoulders',
                'utility': 'Basic',
                'equipment': 'Dumbells, Bench',
            },
            {
                'name': 'Incline Cabel Bench Press',
                'difficulty': 2,
                'accessory_muscles': 'Triceps, Shoulders, Biceps, Pectoralis Major',
                'utility': 'Basic',
                'equipment': 'Bench Press Machine, Bench',
            }, 
            {
                'name': 'Incline Dumbell Bench Press',
                'difficulty': 1,
                'accessory_muscles': 'Triceps, Shoulders',
                'utility': 'Basic',
                'equipment': 'Dumbells, Bench',
            }, 
             {
                'name': 'Incline Cable Chest Flyes',
                'difficulty': 2,
                'accessory_muscles': 'Shoulders',
                'utility': 'Basic',
                'equipment': 'Cables, Bench',
            },
            {
                'name': 'Decline Push Ups',
                'difficulty': 1,
                'accessory_muscles': 'Triceps, Shoulders, Biceps',
                'utility': 'Basic',
                'equipment': 'Bench',
            }, 
             {
                'name': 'Pike Push Ups',
                'difficulty': 3,
                'accessory_muscles': 'Triceps, Shoulders, Biceps',
                'utility': 'Basic',
                'equipment': 'Bench',
            },
           
        ],
        'Lower Pectoralis Major': [
            {
                'name': 'Decline Barbell Bench Press',
                'difficulty': 2,
                'accessory_muscles': 'Triceps, Shoulders, Forearms',
                'utility': 'Basic',
                'equipment': 'Barbell, Bench',
            },
            {
                'name': 'Decline Dumbell Bench Press',
                'difficulty': 2,
                'accessory_muscles': 'Triceps, Shoulders',
                'utility': 'Basic',
                'equipment': 'Dumbells, Bench',
            }, 
            {
                'name': 'Incline Push Ups',
                'difficulty': 1,
                'accessory_muscles': 'Triceps, Shoulders',
                'utility': 'Auxilary',
                'equipment': 'N/A',
            },
            {
                'name': 'Clap Push Ups',
                'difficulty': 3,
                'accessory_muscles': 'Triceps, Shoulders',
                'utility': 'Auxilary',
                'equipment': 'N/A',
            },
            {
                'name': 'Decline Cable Chest Flyes',
                'difficulty': 3,
                'accessory_muscles': 'Shoulders',
                'utility': 'Auxilary',
                'equipment': 'Cables',
            },
        ],        
    },
    'Back': {
        'Latissimus Dorsi ': [
            {
                'name': 'Seated Row',
                'difficulty': 1,
                'accessory_muscles': 'Rhomboids, Biceps',
                'utility': 'Basic',
                'equipment': 'Bench + Cable',
            }, 
            {
                'name': 'One Arm Bent Over Row',
                'difficulty': 1,
                'accessory_muscles': 'Rhomboids, Biceps',
                'utility': 'Basic',
                'equipment': 'Dumbell',
            }, 
         
            
        ],
        'Rhomboids': [
              {
                'name': 'Machine-assisted Chin-up',
                'difficulty': 1,
                'accessory_muscles': 'Latissimus Dorsi, Teres Major, Rhomboids',
                'utility': 'Basic',
                'equipment': 'Chin-up Machine',
            },
            {
                'name': 'Barbell Pullover',
                'difficulty': 3,
                'accessory_muscles': 'Latissimus Dorsi, Teres Major, Rhomboids, Wrist Flexors',
                'utility': 'Auxilary',
                'equipment': 'Bench, Barbell',
            },
            {
                'name': 'Cable Close Grip Pulldown',
                'difficulty': 1,
                'accessory_muscles': 'Latissimus Dorsi, Teres Major, Rhomboids, Brachialis',
                'utility': 'Basic',
                'equipment': 'Back Pulldown Machine',
            },
        ],
        'Trapezius': [
            {
                'name': 'Dumbbell Shrugs',
                'difficulty': 1,
                'accessory_muscles': 'Forearms',
                'utility': 'Basic',
                'equipment': 'Dumbbell, Bench (optional)',
            },
            {
                'name': 'Barbell Shrugs',
                'difficulty': 1,
                'accessory_muscles': 'Forearms',
                'utility': 'Basic',
                'equipment': 'Barbell',
            }, 
            {
                'name': 'Trap Bar Shrug',
                'difficulty': 1,
                'accessory_muscles': 'Trapezius, Levator Scapulae, Erector Spinae',
                'utility': 'Basic',
                'equipment': 'Barbell',
            },
            {
                'name': 'Cable Shrug (with stirrups)',
                'difficulty': 2,
                'accessory_muscles': 'Upper Trapezius, Levator Scapulae, Erector Spinae',
                'utility': 'Basic or Auxilary',
                'equipment': 'Cable, Shrug Machine',
            },
        ],        
    },
    'Triceps': {
        'Long Head': [
            {
                'name': 'Incline Dumbbell Triceps Kickbacks',
                'difficulty': 2,
                'accessory_muscles': 'Triceps Branchii, Lower Arm, elbow',
                'utility': 'Basic',
                'equipment': 'Bench, Dumbbell',
            }, 
            {
                'name': 'One-Arm Overhead Cable Extensions',
                'difficulty': 2,
                'accessory_muscles': 'Triceps Branchii, Long head, elbow',
                'utility': 'Basic',
                'equipment': 'Cable',
            }, 
            {
                'name': 'Two-Arm Overhead Dumbbell Extensions',
                'difficulty': 2,
                'accessory_muscles': 'Triceps Branchii, Long head,Arms',
                'utility': 'Auxilary',
                'equipment': 'Dumbbell,Bench',
            },
            {
                'name': 'French Presses',
                'difficulty': 3,
                'accessory_muscles': 'Triceps Branchii, Long head, Arms',
                'utility': 'Basic',
                'equipment': 'Curl Bar,Bench'
            },
        ],
        'Lateral Head': [
            {
                'name': 'Triangle Push Ups',
                'difficulty': 2,
                'accessory_muscles': 'Lateral Head, Triceps Branchii',
                'utility': 'Basic',
                'equipment': 'N/A',
            }, 
            {
                'name': 'Triceps kickbacks',
                'difficulty': 1,
                'accessory_muscles': 'Lateral Head, Triceps Branchii',
                'utility': 'Basic',
                'equipment': 'Dumbbell, Bench',
            }, 
            {
                'name': 'Triceps chair dips',
                'difficulty': 1,
                'accessory_muscles': 'Lateral Head, Triceps Branchii',
                'utility': '',
                'equipment': 'Chair',
            },
          
        ],
        'Medial Head': [
            {
                'name': 'Overhead Triceps Press',
                'difficulty': 2,
                'accessory_muscles': 'Medial Head, Triceps Branchii',
                'utility': 'Basic',
                'equipment': 'Dumbbell',
            },
            {
                'name': 'Triceps Push-Downs',
                'difficulty': 1,
                'accessory_muscles': 'Medial Head, Triceps Branchii, Arms',
                'utility': 'Basic',
                'equipment': 'Bar, Cable Machine',
            }, 
            {
                'name': 'Barbell JM Bench Press',
                'difficulty': 3,
                'accessory_muscles': 'Triceps Brachii, Wrist Flexors, Pectoralis Major ',
                'utility': 'Auxilary',
                'equipment': 'Bench, Barbell',
            },
            
        ],    
    },
    'Biceps': {
        'Long Head': [
            {
                'name': 'Narrow Grip Barbell Curls',
                'difficulty': 2,
                'accessory_muscles': 'Biceps Brachii, Trapezius, Wrist Flexors',
                'utility': 'Basic',
                'equipment': 'Barbell',
            }, 
            {
                'name':  'Incline Dumbbell Curls',
                'difficulty': 2,
                'accessory_muscles': 'Biceps Brachii, Trapezius, Wrist Flexors, Levator Scapulae',
                'utility': 'Basic',
                'equipment': 'Bench, Dumbbell',
            }, 
            {
                'name': 'Single-Arm Behind-the-Back Band Curl',
                'difficulty': 1,
                'accessory_muscles': 'Biceps Brachii,Trapezius, Wrist Flexors',
                'utility': 'Auxilary',
                'equipment': 'Band',
            },
            {
                'name': 'Dumbbell Hammer Curls',
                'difficulty': 1,
                'accessory_muscles': 'Arms, Shoulders, Biceps Branchii',
                'utility': 'Basic',
                'equipment': 'Dumbell',
            },
        ],
        'Short Head': [
            {
                'name': 'Barbell curls with wide grip',
                'difficulty': 1,
                'accessory_muscles': 'Biceps Brachii, Trapezius, Wrist Flexors',
                'utility': 'Basic',
                'equipment': 'Barbell',
            }, 
            {
                'name': 'Preacher curl',
                'difficulty': 1,
                'accessory_muscles': 'Biceps Brachii, Trapezius, Wrist Flexors',
                'utility': 'Auxilary',
                'equipment': 'Curl Machine',
            }, 
            {
                'name': 'Concentration curls',
                'difficulty': 1,
                'accessory_muscles': 'Arms, Biceps Brachii, anterior deltoid',
                'utility': 'Auxilary',
                'equipment': 'Bench, Dumbbell',
            },
            {
                'name': 'Spider curls',
                'difficulty': 2,
                'accessory_muscles': 'Arms, Biceps Brachii',
                'utility': 'Basic',
                'equipment': 'Bench, Dumbbell',
            },
        ],
    },
    'Shoulders': {
        'Anterior Deltoid': [
            {
                'name': 'Barbell Behind Neck Press',
                'difficulty': 1,
                'accessory_muscles': 'Deltoid, Lateral, Triceps Brachii, Supraspinatus',
                'utility': 'Basic',
                'equipment': 'Bench, Barbell',
            }, 
            {
                'name': 'Barbell Military Press',
                'difficulty': 2,
                'accessory_muscles': 'Pectoralis Major, Clavicular, Serratus Anterior',
                'utility': 'Basic',
                'equipment': 'Barbell',
            }, 
            {
                'name': 'Dumbbell Shoulder Press',
                'difficulty': 1,
                'accessory_muscles': 'Deltoid, Lateral, Triceps Brachii',
                'utility': 'Basic',
                'equipment': 'Dumbbell, Bench',
            },
            {
                'name': 'Cable Twisting Overhead Press',
                'difficulty': 1,
                'accessory_muscles': 'Deltoid, Anterior, Triceps Brachii',
                'utility': 'Auxilary',
                'equipment': 'Cable',
            },
        ],
        'Lateral Deltoid': [
            {
                'name': 'Barbell Upright Row',
                'difficulty': 2,
                'accessory_muscles': 'Deltoid, Lateral, Supraspinatus, Brachialis',
                'utility': 'Basic',
                'equipment': 'Barbell',
            }, 
            {
                'name': 'Cable Upright Row',
                'difficulty': 1,
                'accessory_muscles': 'Deltoid, Lateral, Supraspinatus, Biceps Brachii',
                'utility': 'Basic',
                'equipment': 'Cable bar',
            }, 
            {
                'name': 'Cable Y Raise',
                'difficulty': 2,
                'accessory_muscles': 'Deltoid, Lateral, Supraspinatus, Back',
                'utility': 'Auxilary',
                'equipment': 'Cable',
            },
            {
                'name': 'Dumbbell Lateral Raise',
                'difficulty': 1,
                'accessory_muscles': 'Deltoid, Lateral, Supraspinatus, Serratus Anterior',
                'utility': 'Auxilary',
                'equipment': 'Dumbbell',
            },
        ],
        'Posterior Deltoid': [
            {
                'name': 'Barbell Rear Delt Raise',
                'difficulty': 1,
                'accessory_muscles': 'Deltoid, Posterior, Biceps Brachii, Levator Scapulae',
                'utility': 'Auxiliary',
                'equipment': 'Barbell',
            },
            {
                'name': 'Cable Reverse Fly',
                'difficulty': 2,
                'accessory_muscles': 'Deltoid, Posterior, Infraspinatus, Rhomboids,',
                'utility': 'Auxiliary',
                'equipment': 'Pulley Cable',
            }, 
            {
                'name': 'Cable Rear Delt Row',
                'difficulty': 1,
                'accessory_muscles': 'Deltoid, Posterior, Infraspinatus, Biceps Brachii',
                'utility': 'Auxiliary',
                'equipment': 'cable bar',
            },
            {
                'name': 'Dumbbell Lying Rear Delt Row',
                'difficulty': 1,
                'accessory_muscles': 'Deltoid, Posterior, Rhomboids, Biceps Brachii',
                'utility': 'Auxiliary',
                'equipment': 'Bench, Dumbbell',
            },
        ],    
    },
    'Legs': {
        'Quadriceps': [
            {
                'name': 'Barbell Lunge',
                'difficulty': 1,
                'accessory_muscles': 'Quadriceps, Hamstrings, Calf',
                'utility': 'Auxiliary',
                'equipment': 'Barbell',
            }, 
            {
                'name': 'Barbell Full Squat',
                'difficulty': 2,
                'accessory_muscles': 'Quadriceps, Hamstrings, Calf, Obliques',
                'utility': 'Basic',
                'equipment': 'Barbell',
            }, 
            {
                'name': 'Barbell Single Leg Split Squat',
                'difficulty': 3,
                'accessory_muscles': 'Quadriceps, Hamstrings, Calf',
                'utility': 'Auxiliary',
                'equipment': 'Barbell',
            },
            {
                'name': 'Lateral Step-up',
                'difficulty': 1,
                'accessory_muscles': 'Quadriceps, Hamstrings, Calf',
                'utility': 'Auxilary',
                'equipment': 'Bench',
            },
        ],
        'Hamstrings': [
            {
                'name': 'Barbell Inverse Leg Curl',
                'difficulty': 2,
                'accessory_muscles': 'Hamstrings',
                'utility': 'Basic',
                'equipment': 'Leg Curl Machine',
            }, 
            {
                'name': 'Barbell Straight Leg Deadlift',
                'difficulty': 1,
                'accessory_muscles': 'Hamstrings, Erector Spinae, Adductor Magnus',
                'utility': 'Basic',
                'equipment': 'Barbell',
            }, 
            {
                'name': 'Trap Bar Straight Leg Deadlift',
                'difficulty': 1,
                'accessory_muscles': 'Hamstrings, Erector Spinae, Adductor Magnus',
                'utility': 'Basic',
                'equipment': 'Barbell',
            },
            {
                'name': 'Lying Leg Curl (plate loaded)',
                'difficulty': 1,
                'accessory_muscles': 'Hamstrings, Sartorius, Gracilis',
                'utility': 'Basic',
                'equipment': 'Leg Curl Machine',
            },
        ],
        'Glutes': [
            {
                'name': 'Cable Hip Adduction',
                'difficulty': 1,
                'accessory_muscles': 'Adductors, Hip, Gluteus Maximus, Lower Fibers',
                'utility': 'Auxilary',
                'equipment': 'Cable',
            },
            {
                'name': 'Seated Hip Adduction (plate loaded)',
                'difficulty': 1,
                'accessory_muscles': 'Adductors, Hip',
                'utility': 'Auxiliary',
                'equipment': 'Hip Adduction Machine',
            },
             {
                'name': 'Seated Hip Adduction',
                'difficulty': 1,
                'accessory_muscles': 'Adductors, Hip, Pectineus, Gracilis',
                'utility': 'Auxiliary',
                'equipment': 'Hip Adduction Machine',
            }
           
        ],        
    },
    'Core': {
        'Rectus Abdominis': [
            {
                'name': 'Lying Leg Raise Crunch',
                'difficulty': 1,
                'accessory_muscles': 'Rectus Abdominis, Obliques',
                'utility': 'Auxiliary',
                'equipment': 'Leg Raise Machine',
            }, 
            
            {
                'name': 'Vertical Leg-Hip Raise',
                'difficulty': 1,
                'accessory_muscles': 'Rectus Abdominis, Obliques, Iliopsoas',
                'utility': 'Auxiliary',
                'equipment': 'N/A',
            }, 
            {
                'name': 'Crunch (arms crossed)',
                'difficulty': 1,
                'accessory_muscles': 'Rectus Abdominis, Obliques, Iliopsoas',
                'utility': 'Basic',
                'equipment': 'N/A',
            }, 
             {
                'name': 'V-up',
                'difficulty': 3,
                'accessory_muscles': 'Rectus Abdominis, Obliques, Iliopsoas',
                'utility': 'Basic',
                'equipment': 'N/A',
            }, 
            
            
        ],
        'Obliques': [
            {
                'name': 'Cable Kneeling Twisting Crunch',
                'difficulty': 1,
                'accessory_muscles': 'Obliques, Rectus Abdominis, Triceps, Long Head',
                'utility': 'Auxiliary',
                'equipment': 'Cable, weights',
            }, 
            {
                'name': 'Dumbbell Russian Twist (on stability ball)',
                'difficulty': 2,
                'accessory_muscles': 'Obliques, Hip External Rotators',
                'utility': 'Auxiliary',
                'equipment': 'Dumbbell, Stability Ball',
            }, 
            {
                'name': 'Kneeling Twist',
                'difficulty': 1,
                'accessory_muscles': 'Obliques, Quadratus lumborum, Iliocastalis lumborum',
                'utility': 'Auxiliary',
                'equipment': 'Kneeling Twist Machine',
            },
            {
                'name': 'Barbell Rollout',
                'difficulty': 1,
                'accessory_muscles': 'Obliques, Triceps, Shoulder',
                'utility': 'Auxiliary',
                'equipment': 'Barbell, Weight Plate',
            },
             {
                'name': 'Plank',
                'difficulty': 1,
                'accessory_muscles': 'Obliques, Triceps, Shoulder, Biceps',
                'utility': 'Basic',
                'equipment': 'N/A',
            },
             {
                'name': 'Mountain Climber',
                'difficulty': 1,
                'accessory_muscles': 'Obliques, Hip, Shoulder',
                'utility': 'Auxiliary',
                'equipment': 'N/A',
            },
        ]
    },
}