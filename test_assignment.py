import assignment

def main():
	assert assignment.problem1 == 17, "Your parameter for problem 1 is incorrect"
	assert assignment.friends == "So no one told you life was gonna be this way", "Incorrect quote"
	assert type(assignment.problem3_parameter) == float, "Your parameter for problem 3 is incorrect"
	assert (assignment.quadratic_formula(-2,-1,3) == -1.5 or assignment.quadratic_formula(-2,-1,3) == 1), "Double check your formula"
	assert (assignment.quadratic_formula(5,6,-8) == .8 or assignment.quadratic_formula(5,6,-8) == -2), "Double check your formula"
	assert assignment.quadratic_formula(3,6,3) == -1, "Double check your formula"
	print ("Congratulations! You are done with the assignment!")

if __name__ == '__main__':
   main()