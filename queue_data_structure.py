


import queue
import random 

class Queue:
    def __init__(self):
        self.queue = []

    def first_element(self):
        return self.queue[-1]
    
    def last_element(self):
        return self.queue[0]

    def enqueue(self, person):
        queue = self.queue 
        queue.insert(0, person)
    
    def dequeue(self):
        return self.queue.pop()
    
    def size(self):
        return len(self.queue)

class Roller_Coaster_Queue:
    def add_friends():
        friend_list = []
        cont = True
        while cont == True:
            friend = input("What is your friend's name?")
            friend_list.append(friend)
            answer = input("Have any more friends? y or n")
            if answer != "y":
                break
                
            else: 
                continue



        return friend_list

    def disasters():
        disaster_list = ["They dropped their phone at the top of the mountain", "They puked on their new shirt!", "When the picture was taken, their eyes were closed", 
        "They won't stop talking about how much fun they had", "They complained that this was the most boring ride they've been on ", "They want to go again, but theres no time if you want to ride all the rides"]
        return random.choice(disaster_list)
        
        

    def run():
        queue = Queue()
        print("Welcome to Disney World!")
        print('I see you brought some friends with you, what are their names?')
        friends = Roller_Coaster_Queue.add_friends()
        print(friends)
        for each_friend in friends:
            queue.enqueue(each_friend)


        name = input("and what is your name?")
        queue.enqueue(name)

        print("Your friends want to ride on the Mickey Railway. This is a one person ride and you will each have to take a turn.")
        print("You decide to let your friends go first cause you are afraid. That puts you in " + str(queue.size()) + "th place")
        # input("Press enter to continue")
        # print(queue.dequeue() + " goes first!" + Roller_Coaster_Queue.disasters())
        # print("You are now in " + str(queue.size()) + "th place")
        
        while 2 <= queue.size():
            input("Press enter to continue")
            print(queue.dequeue() + " has now taken their turn!" + Roller_Coaster_Queue.disasters())
            print("You are now in " + str(queue.size()) + "th place")
        print("It is now your turn!")
        queue.dequeue()
        print("It was funner than you imagined and you are now off to enjoy more of the magical kingdom!")

        

Roller_Coaster_Queue.run()