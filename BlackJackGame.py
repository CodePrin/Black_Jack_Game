#Day-11 Project: Black Jack Game

import random
from art import black_jack_ascii

print(black_jack_ascii)

#Users cards
black_jack=True
while black_jack==True:
  cards=[11,2,3,4,5,6,7,8,9,10,10,10]
  user_card1=random.randint(1,12)
  user_card2=random.randint(1,12)
  user_card=[user_card1, user_card2]

  #Users score
  def user_score(user_card):
    user_score=0
    for card in user_card:
      user_score+=cards[card-1]
    return (user_score)


  print("Your cards:",  user_card,"     Your score is:  ",user_score(user_card))

  #COmputers cards
  comp_card1=random.randint(1,12)
  comp_card2=random.randint(1,12)

  comp_card_list=[comp_card1, comp_card2]
  comp_card_shown=random.choice(comp_card_list)
  print("Comp card shown",comp_card_shown)
  comp_card=[comp_card_shown, "_"]
  print("Computer's cards:   ",comp_card)
  print("Computer's first card is:  ",comp_card_shown)

  #Computer_score
  def comp_score(comp_card_list):
    comp_score=0
    for c_card in comp_card_list:
      comp_score+=cards[c_card-1]
    return (comp_score)

  #Asking user to  get another card or pass
  another_card=True
  while another_card==True:

    if user_score(user_card)>21:
      print("Computer cards:   ",comp_card_list,"         Computer score:   ",comp_score(comp_card_list))
      print("You Bust\n")
      another_card=False

    if user_score(user_card)<=21:
      ask_user=input("Type 'y' to get another card and type 'n' to pass.\n").lower()
     
      if ask_user=="y":
        users_next_card=random.randint(1,12)
        user_card.append(users_next_card)
        print("Your cards:",  user_card,"     Your score is:  ",user_score(user_card))
            
      x=len(user_card)  
      comp_next_card=random.randint(1,12)
      comp_card_list.append(comp_next_card)

      if ask_user=="n":
        print("You passed the cards. Now it is computer's turn.")
        print("Computer cards:   ",comp_card_list,"         Computer score:   ",comp_score(comp_card_list))
        
        if comp_score(comp_card_list)>user_score(user_card) and comp_score(comp_card_list)<22:
          print("You Lose\n")
        another_card=False
        if user_score(user_card)>comp_score(comp_card_list) and comp_score(comp_card_list)<22:
          print("You Win\n")
        if user_score(user_card)<comp_score(comp_card_list) and comp_score(comp_card_list)>21:
          print("You Win\n")  
        if user_score(user_card)==comp_score(comp_card_list):
          print("Draw\n")
    
  if user_score(user_card)==comp_score(comp_card_list) and user_score(user_card)>21:
    print("Draw")                

  continue_game=input("If you want to start a new game type 'Start' and if you want to stop the game then type 'Stop'. ").lower()  
  if continue_game=="start":
    print("\nBlack-Jack game is continued")
    black_jack==True
   
  if continue_game=="stop":
    print("Black-Jack game is stopped")
    black_jack==False
    
