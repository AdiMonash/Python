
# Student_ID: 29187990
# Name: Aditya Vinod Rane
# Start Date: 04/08/2018
# Last Modified Date: 24/08/2018

# Creating the Player_1 function to add units to its list
def Player(army ,army_player):
	if (army) > 10:
		print("Cant take more than 10:")
		return
	army_count = 1 #initializing the count for the list
	count = 10 #initialiazing the $ value to 10 and decreasing 1$ per unit taken 
	while(army_count <= army): #just checking if army_count is less than army
		print("1.Archer")
		print("2.Soldier")
		print("3.Knight")
	
		print("Please enter the full choice:")
		choice = input("Enter the choice (Archer/Soldier/Knight):").upper() #making user input as upper as i have taken my choice in upper case

		if choice == 'ARCHER' :
			army_player.append(choice)
			print(army_player)
			count -= 1 #i am decreasing the count of total money to -1
			print("Available Balance is:",count,"$")
			army_count += 1
		
		elif choice == 'SOLDIER':
			army_player.append(choice)
			print(army_player)
			count -= 1 #i am decreasing the count of total money to -1
			print("Available Balance is:",count,"$")
			army_count += 1

		elif choice == 'KNIGHT':
			army_player.append(choice)
			print(army_player)
			count -= 1 #i am decreasing the count of total money to -1
			print("Available Balance is:",count,"$")
			army_count += 1

		else :
			print("Invalid Input")
# Creating the Player_1 function to add units to its list

def Player2(army, army_player2):
	
	if (army) > 10:
		print("Cant take more than 10:")
		return
	army_count = 1 #initializing the count for the list
	count = 10 #initialiazing the $ value to 10 and decreasing 1$ per unit taken
	while(army_count <= army): #just checking if army_count is less than army
		print("1.Archer")
		print("2.Soldier")
		print("3.Knight")
	
		print("Please enter the full choice:")
		choice = input("Enter the choice (Archer/Soldier/Knight):").upper() #making user input as upper as i have taken my choice in upper case
			
		if choice == 'ARCHER' :
		
			army_player2.append(choice)
			print(army_player2)
			count -= 1 #i am decreasing the count of total money to -1
			print("Available Balance is:",count,"$")
			army_count += 1
		
		elif choice == 'SOLDIER':
			army_player2.append(choice)
			print(army_player2)
			count -= 1 #i am decreasing the count of total money to -1
			print("Available Balance is:",count,"$")
			army_count += 1

		elif choice == 'KNIGHT':
			army_player2.append(choice)
			print(army_player2)
			count -= 1 #i am decreasing the count of total money to -1
			print("Available Balance is:",count,"$")
			army_count += 1

		else :
			print("Invalid Input")
		
	
# Defining the function for winning 
def win(army_player, army_player2, Player_1, Player_2):
	points_1 = 0 #Initializing the points for 1st player
	points_2 = 0 #Initializing the points for 2nd player
	i = 0
	j = 0

	#Winning conditions on battlefield
	if ((army_player[i] == 'ARCHER' and army_player2[j] == 'ARCHER') or (army_player[i] == 'SOLDIER' and army_player2[j] == 'SOLDIER') or (army_player[i] == 'KNIGHT' and army_player2[j] == 'KNIGHT')
		) or ((army_player2[j] == 'ARCHER' and army_player[i] == 'ARCHER') or (army_player2[j] == 'SOLDIER' and army_player[i] == 'SOLDIER') or (army_player2[j] == 'KNIGHT' and army_player[i] == 'KNIGHT')):
		print("Result Tie")
		army_player.pop(0) #if player1 and player 2 have same army it will be tie, so i am using pop function to remove the army element
		army_player2.pop(0) #if player1 and player 2 have same army it will be tie, so i am using pop function to remove the army element
		print (army_player)
		print (army_player2)
		points_1 += 1 # if its a tie i am allocating 1 point to player 1 
		points_2 += 1 # if its a tie i am allocating 1 point to player 2
		print("Result",Player_1,"Points are:",points_1)
		print("Result",Player_2,"Points are:",points_2)

	elif (army_player[i] == 'ARCHER' and army_player2[j] == 'SOLDIER'):
		print("Winner is :",army_player[i])
		army_player2.pop(0) #if player1 and player 2 have same army it will be tie, so i am using pop function to remove the army element
		print (army_player)
		print (army_player2)
		points_1 += 2 # if its a win i am allocating 2 point to winning player
		print("Result",Player_1,"Points are:",points_1)
		print("Result",Player_2,"Points are:",points_2)

	elif (army_player2[j] == 'ARCHER' and army_player[i] == 'SOLDIER'):
		print("Winner is :",army_player2[j])
		army_player.pop(0) #if player1 and player 2 have same army it will be tie, so i am using pop function to remove the army element
		print (army_player)
		print (army_player2)
		points_2 += 2 # if its a win i am allocating 2 point to winning player
		print("Result",Player_1,"Points are:",points_1)
		print("Result",Player_2,"Points are:",points_2)

	elif (army_player[i] == 'ARCHER' and army_player2[j] == 'KNIGHT'):
		print("Winner is :",army_player2[j])
		army_player.pop(0) #if player1 and player 2 have same army it will be tie, so i am using pop function to remove the army element
		print (army_player)
		print (army_player2)
		points_2 += 2 # if its a win i am allocating 2 point to winning player
		print("Result",Player_1,"Points are:",points_1)
		print("Result",Player_2,"Points are:",points_2)

	elif (army_player2[j] == 'ARCHER' and army_player[i] == 'KNIGHT'):
		print("Winner is :",army_player[i])
		army_player2.pop(0) #if player1 and player 2 have same army it will be tie, so i am using pop function to remove the army element
		print (army_player)
		print (army_player2)
		points_1 += 2 # if its a win i am allocating 2 point to winning player
		print("Result",Player_1,"Points are:",points_1)
		print("Result",Player_2,"Points are:",points_2)

	elif (army_player[i] == 'SOLDIER' and army_player2[j] == 'ARCHER'):
		print("Winner is :",army_player2[j])
		army_player.pop(0) #if player1 and player 2 have same army it will be tie, so i am using pop function to remove the army element
		print (army_player)
		print (army_player2)
		points_2 += 2 # if its a win i am allocating 2 point to winning player
		print("Result",Player_1,"Points are:",points_1)
		print("Result",Player_2,"Points are:",points_2)

	elif (army_player2[j] == 'SOLDIER' and army_player[i] == 'ARCHER'):
		print("Winner is :",army_player[i])
		army_player2.pop(0) #if player1 and player 2 have same army it will be tie, so i am using pop function to remove the army element
		print (army_player)
		print (army_player2)
		points_1 += 2 # if its a win i am allocating 2 point to winning player
		print("Result",Player_1,"Points are:",points_1)
		print("Result",Player_2,"Points are:",points_2)

	elif (army_player[i] == 'SOLDIER' and army_player2[j] == 'KNIGHT'):
		print("Winner is :",army_player[i])
		army_player2.pop(0) #if player1 and player 2 have same army it will be tie, so i am using pop function to remove the army element
		print (army_player)
		print (army_player2)
		points_1 += 2 # if its a win i am allocating 2 point to winning player
		print("Result",Player_1,"Points are:",points_1)
		print("Result",Player_2,"Points are:",points_2)

	elif (army_player2[j] == 'SOLDIER' and army_player[i] == 'KNIGHT'):
		print("Winner is :",army_player2[j])
		army_player.pop(0) #if player1 and player 2 have same army it will be tie, so i am using pop function to remove the army element
		print (army_player)
		print (army_player2)
		points_2 += 2 # if its a win i am allocating 2 point to winning player
		print("Result",Player_1,"Points are:",points_1)
		print("Result",Player_2,"Points are:",points_2)

	elif (army_player[i] == 'KNIGHT' and army_player2[j] == 'SOLDIER'):
		print("Winner is :",army_player2[j])
		army_player.pop(0) #if player1 and player 2 have same army it will be tie, so i am using pop function to remove the army element
		print (army_player)
		print (army_player2)
		points_2 += 2 # if its a win i am allocating 2 point to winning player
		print("Result",Player_1,"Points are:",points_1)
		print("Result",Player_2,"Points are:",points_2)

	elif (army_player2[j] == 'KNIGHT' and army_player[i] == 'SOLDIER'):
		print("Winner is :",army_player[i])
		army_player2.pop(0) #if player1 and player 2 have same army it will be tie, so i am using pop function to remove the army element
		print (army_player)
		print (army_player2)
		points_1 += 2 # if its a win i am allocating 2 point to winning player
		print("Result",Player_1,"Points are:",points_1)
		print("Result",Player_2,"Points are:",points_2)

	else:
		print("Wrong Input:")
	return points_1 , points_2 # counting the points of each player so we can find out the winnner easily
	

# Defining the function for non empty list
def not_empty(army_player, army_player2, Player_1, Player_2):
	P1 = 0 # initializing the points for player1
	P2 = 0 # initializing the points for player2
	
	while len(army_player)!= 0 and len(army_player2) != 0:
		a1,a2 = win(army_player, army_player2, Player_1, Player_2)
		P1 += a1
		P2 += a2
	print("The total points of player 1:",P1)
	print("The total points of player 2:",P2)
	if P1 > P2:
		print("Your winner is :",Player_1)
	elif P1 == P2:
		print("It's a tie:",P1,P2)
	else:
		print("Your winner is :",Player_2)

def game():
	print("\n\nWelcome to Combat Simulator: Where everything is fair in war:")
	print("\n How to play the game\n\n Each commander will be give $10 to purchase their army.\n\nCommanders may spend minimum $1 to max $10.")
	print("\n Each unit in standard game cost $1 and the fight will be conducted in the order of purchased army")
	print("\n\n *****************************************************************\n\n")

	Player_1 = input("Enter the name of your team maximum of 8 characters or numbers are allowed:")
	print(Player_1.upper()) #taking the input from user and making it upper
	
	while len(Player_1) > 8: #condition for making the length of player name to max of 8 characters
		Player_1 = input("Re-Enter your team name maximum of 8 characters or numbers are allowed:")

	army_player = []
	
	print("CAUTION: cant exceed more than 10")
	army1 = int(input("Enter the number of army you need you:")) #taking the number of armies player1 needs
	Player(army1, army_player)
	
	
	Player_2 = input("Enter the name of your team:")
	print(Player_2.upper()) #taking the input from user and making it upper
	while len(Player_2) > 8: #condition for making the length of player name to max of 8 characters
		Player_2 = input("Re-Enter your team name maximum of 8 characters or numbers are allowed:")

	army_player2 = []

	print("CAUTION: cant exceed more than 10")
	army2 = int(input("Enter the number of army you need you:")) #taking the number of armies player1 needs
	
	while army1 != army2: # checking if the user input for army 1 is same as army 2 
		print("Both the armies should have length same")
		army2 = int(input("Enter the number of army you need you:")) # if no than the player 2 can enter the army size again
	Player2(army2, army_player2)

	print("Army of Player 1 is : ",army_player) # displaying the army of player 1
	print("Army of Player 2 is : ",army_player2) # displaying the army of player 2
	not_empty(army_player, army_player2, Player_1, Player_2)

def main():
	game() #calling the game function
	while True: #checking if they want to play the game again
		answer = input("Do you want to continue playing yes/no?")
		if answer == "yes":
			game() #if user input yes than the game function is called again
		elif answer == "no" :
			print("K Bye......")
			return
	

if __name__ == "__main__":
	main()