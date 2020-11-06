def bmr_cal():
    weightInLbs = int(input("Weight: "))
    heightIninches = int(input("height in inches: "))
    age= int(input("Age: "))
    gender= input("Are you a male or female? m/f: ").lower()

    weightInKgs=  weightInLbs / 2.2
    heightInCentimeters = heightIninches * 2.54
    if gender == "m":
        bmr = int((10 * weightInKgs) 
        + (6.25 * heightInCentimeters ) - (5 * age ) + 5)
    elif gender =="f":
        bmr = int((10 * weightInKgs) 
        + (6.25 * heightInCentimeters ) - (5 * age ) - 161)

    #protein and carbs should 40% of calories and fat should be 20%
    print("Your Estimated Basal Metabolic Rate is " + str(bmr) + ".")
    return bmr
    
def daily_caloric_need(bmr):
    print(
        '''Activity Level: 
        1 = Somewhat Active
        2 = Exercise 1 - 3 times a week
        3 = Exercise 4 - 5 times a week
        4 = Daily Exercise or intense exercise 3 - 4 times a week
        5 = Intense Exercise 6 times a week
        ''' 
       )
       
       
    activityLevel = int(input("Select your activity level: "))
    
    if activityLevel == 1:
        activityLevelIndex = 1.2
    elif activityLevel == 2:
        print("")
        activityLevelIndex = 1.375
    elif activityLevel == 3:
        activityLevelIndex = 1.46
    elif activityLevel == 4:
        activityLevelIndex = 1.725
    elif activityLevel == 5:
        activityLevelIndex = 1.9
    
    print(bmr)    
    dailyCaloriesNeeded = int(bmr * activityLevelIndex)
    print("Based on the BMR to maintain your current weight you need: " + str(dailyCaloriesNeeded) + " calories a day ")
    return dailyCaloriesNeeded
    
    
def calculate_macro(calories):

  calories_from_protein = int(.4 * calories)
  calories_in_protein = int(calories_from_protein / 4)
  calories_from_carbs = int(.4 * calories)
  calories_in_carbs = int(calories_from_carbs / 4)
  calories_from_fat = int(.2 * calories)
  calories_in_fat =int(calories_from_fat / 9)
    
  print("Calories from Protein: " + str(calories_from_protein))
  print("Grams of Protein: " + str(calories_in_protein))
  print("Calories from Carbs: " + str(calories_from_carbs))
  print("Grams of Carbs: " + str(calories_in_carbs))
  print("Calories from Fat: " + str(calories_from_fat))
  print("Grams of Fat: " + str(calories_in_fat))
    
    

  #calculate fat loss / gain
  # 1 lb pf fat has 3500 calories to lose .5 lbs a week, divide 3,500 in half and then divide by 7
  halfAPoundaWeek_calories =int(calories - int((3500 / 2) / 7 ))
  print("\n")
  print("To lose .5 lb of fat a week your daily calories needs to drop to:  " + str(halfAPoundaWeek_calories) + ". ")

  calories_from_protein = int(.4 * halfAPoundaWeek_calories)
  calories_in_protein = int(calories_from_protein / 4)
  calories_from_carbs = int(.4 * halfAPoundaWeek_calories)
  calories_in_carbs = int(calories_from_carbs / 4)
  calories_from_fat = int(.2 * halfAPoundaWeek_calories)
  calories_in_fat =int(calories_from_fat / 9)

  print("Calories from Protein: " + str(calories_from_protein))
  print("Grams of Protein: " + str(calories_in_protein))
  print("Calories from Carbs: " + str(calories_from_carbs))
  print("Grams of Carbs: " + str(calories_in_carbs))
  print("Calories from Fat: " + str(calories_from_fat))
  print("Grams of Fat: " + str(calories_in_fat))


bmr_rate = bmr_cal()
dailycaloriesneed= daily_caloric_need(bmr_rate)
calculate_macro(dailycaloriesneed)


