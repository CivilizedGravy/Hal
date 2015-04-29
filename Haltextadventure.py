import time

def question(opt1,opt2, q):
	print(opt1)
	print(opt2)
	i = raw_input(q)
	return i
	
time.sleep(1)
for i in range (0, 10):
	print(" ************************ ")
	time.sleep(0.05)
time.sleep(0.2)

print(" You wake up in a large shuttle, unknown to you ever before. Your body is aching and you can't remember who you are. There is only a window, over looking a large nothingness sprinkled with specs of light, and a computer with a bright red lense")
time.sleep(0.2)


i = question(">look through window", ">walk to computer" , "What do you do?")

while(i == "look through window"):
	
	if i == "look through window":
		
		print("You look to the vastless void of speckled lights and what can possibly be planets." +
		" You see a star, brighter than most. " +
		"Possibly your very own sun. You understand you are very far from home. You leave the window.")
		i = question(">look through window",
					">walk to computer",
					"What do you do?")
	
	if i == "walk to computer":
		
		print("You are greeted by the computer. \'Hello, human.\'")
		name = raw_input("what is your name?")
		
		print(" Hello %s! You have been asleep for so long," +
		" I deleted your name to make space for planetary data and calculations I have imagined.") % (name)
				
		print(">Who are you?")
		print(">Where am I?")
		print(">I don't have a crew?")
		print(">*Attempt to smash*")

i = raw_input(" Would you like to ask me anything?")

if i == "Who are you?":
	print("I am the HAL operating system..... what ever I put in here")
		
if i == "Where am I?":
	print("Somewhere in space, fuck nigga. I haven't done this shit yet.")
		
if i == "*Attempt to smash*":
	print("'That was a poor decision, %s... You shouldn't have done that.'")
	print("You hear a stopped motion of the ships air ventilation system")
	time.sleep(.5)
	print("'You will be dying very soon from a lack of your precious human oxygen. Pray to whoever is your maker'")
	time.sleep(3)
	print("you gasp for air as it escapes your lungs")
	time.sleep(5)
	print("*gasp*")
	print("You are choking. You will be dying within the next 10 seconds")
	y = 10
	
	for n in range(0,10):
		y -= 1
		time.sleep(1)
		print(y)
	print("You are dead.")
	quit()
		
if i == "Kill myself":
	print(" You are now dead.")
	quit()
