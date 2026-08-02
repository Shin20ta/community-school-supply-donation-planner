# Program Title

print("COMMUNITY SCHOOL SUPPLY DONATION PLANNER")
print("The purpose of this program is to help a donor with planning a school-supply donation.")

# Donation Information

donation_project_name = input("What is the name of the donation project? ")
amount_of_students = int(input("How many students would you like to help? "))
if amount_of_students <= 0:
    print("The number of students must be greater than zero.")
else:
    total_donation_budget = int(input("What is your total donation budget? "))
    
    # Packages
    
    packages = int(input("What donation package do you want? 1 for Basic, 2 for Standard, and 3 for Expanded "))
    if packages == 1:
    
        # Supply Prices

        notebook = 3
        pack_of_pencils = 2
        folder = 1

        # Basic Supply Package

        number_of_notebooks = 1
        number_of_pencils = 1
        number_of_folders = 1
        notebook_cost = number_of_notebooks * notebook
        pack_of_pencils_cost = number_of_pencils * pack_of_pencils
        folder_cost = number_of_folders * folder

        # Total Donation Cost

        basic_total_cost = amount_of_students *(
            notebook_cost +
            pack_of_pencils_cost +
            folder_cost
        )
        money_remaining = total_donation_budget - basic_total_cost
    
        # Budget Decision
    
        if total_donation_budget > basic_total_cost:
            print("The donation is fully funded.")
            print("There will be",money_remaining,"dollars remaining.")
        elif total_donation_budget == basic_total_cost:
            print("The donation is fully funded with no money remaining.")
        else:
            print("The current budget is not enough.")
            print(abs(total_donation_budget - basic_total_cost),"more dollars are needed to fully fund the donation.")

        # Donation Size Evaluation

        if amount_of_students >= 50:
            print("This is a large community donation.")
        elif amount_of_students >= 25:
            print("This is a strong community donation.")
        elif amount_of_students >=10:
            print("This is a helpful community donation.")
        elif amount_of_students >= 1:
            print("Every student helped matters.")

        # Budget Quality Evaluation

        basic_cost_per_student = basic_total_cost / amount_of_students
        budget_per_student = total_donation_budget / amount_of_students
        if budget_per_student >= basic_cost_per_student:
            print("The budget fully covers the cost per student.")
        elif budget_per_student >= basic_cost_per_student * 0.75:
            print("The budget covers most of the cost per student.")
        elif budget_per_student >= basic_cost_per_student * 0.50:
            print("The budget partially covers the cost per student.")
        else:
            print("Significantly more funding is needed per student.")
    
        # Donation Report

        print("DONATION REPORT")
        print("Project Name: ",donation_project_name)
        print("Students Helped: ",amount_of_students)
        print("Budget Per Student: ",budget_per_student)
        print("Cost Per Student: ",basic_cost_per_student)
        print("Total Donation Cost: ",basic_total_cost)
        if money_remaining >= 0:
            print("Money Remaining:", money_remaining)
        else:
            print("Additional Money Needed:", abs(money_remaining))
    elif packages == 2:
    
        # Supply Prices

        notebook = 3
        pack_of_pencils = 2
        folder = 1
        backpack = 15

        # Standard Supply Package

        number_of_notebooks = 2
        number_of_pencils = 1
        number_of_folders = 2
        number_of_backpacks = 1
        notebook_cost = number_of_notebooks * notebook
        pack_of_pencils_cost = number_of_pencils * pack_of_pencils
        folder_cost = number_of_folders * folder
        backpack_cost = number_of_backpacks * backpack

        # Total Donation Cost

        standard_total_cost = amount_of_students * (
            notebook_cost +
            pack_of_pencils_cost +
            folder_cost +
            backpack_cost
        )
        money_remaining = total_donation_budget - standard_total_cost
    
        # Budget Decision
    
        if total_donation_budget > standard_total_cost:
            print("The donation is fully funded.")
            print("There will be",money_remaining,"dollars remaining.")
        elif total_donation_budget == standard_total_cost:
            print("The donation is fully funded with no money remaining.")
        else:
            print("The current budget is not enough.")
            print(abs(total_donation_budget - standard_total_cost),
            "more dollars are needed to fully fund the donation."
            )

        # Donation Size Evaluation

        if amount_of_students >= 50:
            print("This is a large community donation.")
        elif amount_of_students >= 25:
            print("This is a strong community donation.")
        elif amount_of_students >=10:
            print("This is a helpful community donation.")
        elif amount_of_students >= 1:
            print("Every student helped matters.")

        # Budget Quality Evaluation

        standard_cost_per_student = standard_total_cost / amount_of_students
        budget_per_student = total_donation_budget / amount_of_students
        if budget_per_student >= standard_cost_per_student:
            print("The budget fully covers the cost per student.")
        elif budget_per_student >= standard_cost_per_student * 0.75:
            print("The budget covers most of the cost per student.")
        elif budget_per_student >= standard_cost_per_student * 0.50:
            print("The budget partially covers the cost per student.")
        else:
            print("Significantly more funding is needed per student.")
    
        # Donation Report

        print("DONATION REPORT")
        print("Project Name: ",donation_project_name)
        print("Students Helped: ",amount_of_students)
        print("Budget Per Student: ",budget_per_student)
        print("Cost Per Student: ",standard_cost_per_student)
        print("Total Donation Cost: ",standard_total_cost)
        if money_remaining >= 0:
            print("Money Remaining:", money_remaining)
        else:
            print("Additional Money Needed:", abs(money_remaining))
    elif packages == 3:
        
        # Supply Prices
    
        notebook = 3
        pack_of_pencils = 2
        folder = 1
        backpack = 15
        calculator = 10
    
        # Expanded Supply Package
    
        number_of_notebooks = 3
        number_of_pencils = 2
        number_of_folders = 3
        number_of_backpacks = 1
        number_of_calculators = 1
        
        notebook_cost = number_of_notebooks * notebook
        pack_of_pencils_cost = number_of_pencils * pack_of_pencils
        folder_cost = number_of_folders * folder
        backpack_cost = number_of_backpacks * backpack
        calc_cost = number_of_calculators * calculator
    
        # Total Donation Cost
    
        expanded_total_cost =amount_of_students * (
            notebook_cost +
            pack_of_pencils_cost +
            folder_cost +
            backpack_cost +
            calc_cost
        )
        money_remaining = total_donation_budget - expanded_total_cost
        
        # Budget Decision
        
        if total_donation_budget > expanded_total_cost:
            print("The donation is fully funded.")
            print("There will be",money_remaining,"dollars remaining.")
        elif total_donation_budget == expanded_total_cost:
            print("The donation is fully funded with no money remaining.")
        else:
            print("The current budget is not enough.")
            print(abs(total_donation_budget - expanded_total_cost),
            "more dollars are needed to fully fund the donation."
            )
        # Donation Size Evaluation
    
        if amount_of_students >= 50:
            print("This is a large community donation.")
        elif amount_of_students >= 25:
            print("This is a strong community donation.")
        elif amount_of_students >=10:
            print("This is a helpful community donation.")
        elif amount_of_students >= 1:
            print("Every student helped matters.")
    
        # Budget Quality Evaluation
        expanded_cost_per_student = expanded_total_cost / amount_of_students
        budget_per_student = total_donation_budget / amount_of_students
        if budget_per_student >= expanded_cost_per_student:
            print("The budget fully covers the cost per student.")
        elif budget_per_student >= expanded_cost_per_student * 0.75:
            print("The budget covers most of the cost per student.")
        elif budget_per_student >= expanded_cost_per_student * 0.50:
            print("The budget partially covers the cost per student.")
        else:
            print("Significantly more funding is needed per student.")
        
        # Donation Report
    
        print("DONATION REPORT")
        print("Project Name: ",donation_project_name)
        print("Students Helped: ",amount_of_students)
        print("Budget Per Student: ",budget_per_student)
        print("Cost Per Student: ",expanded_cost_per_student)
        print("Total Donation Cost: ",expanded_total_cost)
        if money_remaining >= 0:
            print("Money Remaining:", money_remaining)
        else:
            print("Additional Money Needed:", abs(money_remaining))
    else:
        print("Invalid package selection.")
