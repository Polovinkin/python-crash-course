responses = {}

#Set a flag indicating that polling is active
polling_active = True

while polling_active:
    #Prompt the person's name and responce
    name = input("\nWhat's your name? ")
    responce = input("\nWhat mountain would you like to climb one day? ")

    #Store the responce in the dictionary
    responses[name] = responce

    #Find out if someone wants to participate in poll too
    repeat = input("\nDoes someone else wants to respond? ")
    if repeat == "no":
        polling_active = False

#Polling is active, show the results
print("\n--- Poll Results ---")
for name, responce in responses.items():
    print(name.title() + ' would like to climb ' + responce.title() + '.')