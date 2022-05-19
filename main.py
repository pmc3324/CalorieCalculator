def cal_calc():
    user_input = input(
        "Hello, and welcome to Paul's Calorie Calculator! Type 'y' to proceed: ")
    user_input = user_input.lower()
    if user_input == 'y':
        while True:
            weight_pound = input("What is your weight in pounds: ")
            weight = float(weight_pound) * .454
            height_inch = float(input("What is your height in inches: "))
            height = height_inch * 2.54
            age = float(input("What is your age in years: "))
            mf = input(
                "Are you male or female? Type 'm' for male and 'f' for female: ")
            mf = mf.lower()
            if mf == 'm':
                bmr = 10 * weight + 6.25 * height - 5 * age + 5
                print(f"Your bmr is {bmr}")
                life_style = input(
                    "What is your activity level? You can choose from sedentary, lightly active, moderately active, very active, and extra active. Would you like to know more about activity level? If you don't know, type 'idk' for more info: ")
                life_style = life_style.lower()
                if life_style == 'idk':
                    new_input = input(
                        "sedentary is little to no exercise, lightly active is light exercise/sports 1-3 days/week, moderately active is moderate exercise/sports 3-5 days/week, very actice is hard exercise/sports 6-7 days a week, and extra active is very hard exercise/sports & a physical job. What is your activity level: ")
                    print(new_input)
                    if new_input == 'sedentary':
                        sbmr = bmr * 1.2
                        return f"You need to eat {sbmr} calories a day. Thanks for participating!"
                    elif new_input == 'lightly active':
                        lbmr = bmr * 1.375
                        return f"You need to eat {lbmr} calories a day. Thanks for participating!"
                    elif new_input == 'moderately active':
                        mbmr = bmr * 1.55
                        return f"You need to eat {mbmr} calories a day. Thanks for participating!"
                    elif new_input == 'very active':
                        vbmr = bmr * 1.725
                        return f"You need to eat {vbmr} calories a day. Thanks for participating!"
                    elif new_input == 'extra active':
                        ebmr = bmr * 1.9
                        return f"You need to eat {ebmr} calories a day. Thanks for participating!"
                    else:
                        print("We didn't catch that, let's start from the top.")
                elif life_style == 'sedentary':
                    sbmr = bmr * 1.2
                    return f"You need to eat {sbmr} calories a day. Thanks for participating!"
                elif life_style == 'lightly active':
                    lbmr = bmr * 1.375
                    return f"You need to eat {lbmr} calories a day. Thanks for participating!"
                elif life_style == 'moderately active':
                    mbmr = bmr * 1.55
                    return f"You need to eat {mbmr} calories a day. Thanks for participating!"
                elif life_style == 'very active':
                    vbmr = bmr * 1.725
                    return f"You need to eat {vbmr} calories a day. Thanks for participating!"
                elif life_style == 'extra active':
                    ebmr = bmr * 1.9
                    return f"You need to eat {ebmr} calories a day. Thanks for participating!"
                else:
                    print("We didn't catch that, let's start from the top.")
            elif mf == 'f':
                bmr = 10 * weight + 6.25 * height - 5 * age - 161
                print(f"Your bmr is {bmr}")
                life_style = input(
                    "What is your activity level? You can choose from sedentary, lightly active, moderately active, very active, and extra active. Would you like to know more about activity level? If you don't know, type 'idk' for more info: ")
                life_style = life_style.lower()
                if life_style == 'idk':
                    new_input = input("sedentary is little to no exercise, lightly active is light exercise/sports 1-3 days/week, moderately active is moderate exercise/sports 3-5 days/week, very actice is hard exercise/sports 6-7 days a week, and extra active is very hard exercise/sports & a physical job. What is your activity level: ")
                    if new_input == 'sedentary':
                        sbmr = bmr * 1.2
                        return f"You need to eat {sbmr} calories a day. Thanks for participating!"
                    elif new_input == 'lightly active':
                        lbmr = bmr * 1.375
                        return f"You need to eat {lbmr} calories a day. Thanks for participating!"
                    elif new_input == 'moderately active':
                        mbmr = bmr * 1.55
                        return f"You need to eat {mbmr} calories a day. Thanks for participating!"
                    elif new_input == 'very active':
                        vbmr = bmr * 1.725
                        return f"You need to eat {vbmr} calories a day. Thanks for participating!"
                    elif new_input == 'extra active':
                        ebmr = bmr * 1.9
                        return f"You need to eat {ebmr} calories a day. Thanks for participating!"
                    else:
                        print("We didn't catch that, let's start from the top.")
                elif life_style == 'sedentary':
                    sbmr = bmr * 1.2
                    return f"You need to eat {sbmr} calories a day. Thanks for participating!"
                elif life_style == 'lightly active':
                    lbmr = bmr * 1.375
                    return f"You need to eat {lbmr} calories a day. Thanks for participating!"
                elif life_style == 'moderately active':
                    mbmr = bmr * 1.55
                    return f"You need to eat {mbmr} calories a day. Thanks for participating!"
                elif life_style == 'very active':
                    vbmr = bmr * 1.725
                    return f"You need to eat {vbmr} calories a day. Thanks for participating!"
                elif life_style == 'extra active':
                    ebmr = bmr * 1.9
                    return f"You need to eat {ebmr} calories a day. Thanks for participating!"
                else:
                    print("We didn't catch that, let's start from the top.")
            else:
                print("Invalid response. Let's start from the top again.")
    else:
        return "Not a valid input, Goodbye!"


print(cal_calc())
