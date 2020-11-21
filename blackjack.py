
############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
import random
import replit
import art
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def start():
 return input("Do you want to play the game of blackjack.Type 'y' or 'n' : ")

while start() == "y" :
  replit.clear()
  print(art.logo)
  end_game=False
  blackjack =False
  user_cards=[cards[random.randint(0,len(cards)-1)],cards[random.randint(0,len(cards)-1)]]
  current_score=user_cards[0]+user_cards[1]
  computer_card=[cards[random.randint(0,len(cards)-1)],cards[random.randint(0,len(cards)-1)]]
  computer_current_score=computer_card[0]+computer_card[1]
  print(f"  Your cards: [{user_cards}],current score:{current_score}")
  print(f"  Computer first card: {computer_card[0]}")
  
  if current_score == 21 and computer_current_score == 21:
    print(f"  Your final hand :{user_cards},final score: {current_score}")
    print(f"  Computer final hand: {computer_card},final score: {computer_current_score}")
    print("Both Blackjack")
    end_game= True
    blackjack=True
  elif current_score == 21:
    print(f"  Your final hand :{user_cards},final score: {current_score}")
    print(f"  Computer final hand: {computer_card},final score: {computer_current_score}")
    print("You Blackjack")
    blackjack=True

    end_game=True
  
  elif computer_current_score == 21:
    print(f"  Your final hand :{user_cards},final score: {current_score}")
    print(f"  Computer final hand: {computer_card},final score: {computer_current_score}")
    print("Computer Blackjack")
    end_game=True
    blackjack=True

  

  while current_score < 21 and end_game != True:
    ask=input("Type 'y' to get another card,type 'n' to pass : ")
    if ask == "y":
      user_cards.append(cards[random.randint(0,len(cards)-1)])
      
      for single_card in user_cards:
        if single_card == 11:
          if current_score + 11 > 21:
            position=user_cards.index(single_card) 
            user_cards[position]=1
      current_score=0
      for single_card in user_cards:
        current_score+=single_card


    

      print(f"  Your cards: [{user_cards}],current score:{current_score}")
      print(f"  Computer first card: {computer_card[0]}")


    elif ask =='n':
      print(f"  Your final hand :{user_cards},final score: {current_score}")

   
      random_choice=random.randint(0,1)
      if computer_current_score < 17:
           random_choice = 1
       

      while random_choice == 1 and computer_current_score < 21:
        
        computer_card.append(cards[random.randint(0,len(cards)-1)])
        
        for single_card in computer_card:
          if single_card == 11:
            if computer_current_score + 11 > 21:
              position=computer_card.index(single_card) 
              computer_card[position]=1
        computer_current_score=0
        for single_card in computer_card:
          computer_current_score+=single_card
        if computer_current_score == 21:
          random_choice = 0
        else:
      
          random_choice=random.randint(0,1)
          if computer_current_score < 17:
            random_choice = 1

      print(f"  Computer final hand: {computer_card},final score: {computer_current_score}")
      if computer_current_score > 21:
        print("Opponent went Over.You win")
        end_game= True
       
      elif computer_current_score > current_score:
        print("You lose")
        end_game=True
    
      elif computer_current_score < current_score:
        print("You win")
        end_game=True
      elif computer_current_score == current_score:
        print("Draw")
        end_game=True
      

  if current_score > 21:
    print(f"  Your final hand :{user_cards},final score: {current_score}")
    random_choice=random.randint(0,1)
    if computer_current_score < 17:
      random_choice = 1
    
    while random_choice == 1 and computer_current_score < 21:
      
      computer_card.append(cards[random.randint(0,len(cards)-1)])
      
      for single_card in computer_card:
        if single_card == 11:
          if computer_current_score + 11 > 21:
            position=computer_card.index(single_card) 
            computer_card[position]=1
      computer_current_score=0
      for single_card in computer_card:
        computer_current_score+=single_card
      if computer_current_score == 21:
        random_choice = 0
      else:
        random_choice=random.randint(0,1)
        if computer_current_score < 17:
           random_choice = 1

    print(f"  Computer final hand: {computer_card},final score: {computer_current_score}")
    print("You went over.")
    if computer_current_score > 21:
      print("Opponent went over too.Draw")
    
  elif current_score == 21 and blackjack == False:
    print(f"  Your final hand :{user_cards},final score: {current_score}")
    random_choice=random.randint(0,1)
    if computer_current_score < 17:
      random_choice = 1
    
    while random_choice == 1 and computer_current_score < 21:
      
      computer_card.append(cards[random.randint(0,len(cards)-1)])
      
      for single_card in computer_card:
        if single_card == 11:
          if computer_current_score + 11 > 21:
            position=computer_card.index(single_card) 
            computer_card[position]=1
      computer_current_score=0
      for single_card in computer_card:
        computer_current_score+=single_card
      if computer_current_score == 21:
        random_choice = 0
      else:
        random_choice=random.randint(0,1)
        if computer_current_score < 17:

           random_choice = 1

    print(f"  Computer final hand: {computer_card},final score: {computer_current_score}")
    if computer_current_score == 21:
      print("Draw")
    else:
      print("You win")





############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
import random
import replit
import art
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def start():
 return input("Do you want to play the game of blackjack.Type 'y' or 'n' : ")

while start() == "y" :
  replit.clear()
  print(art.logo)
  end_game=False
  blackjack =False
  user_cards=[cards[random.randint(0,len(cards)-1)],cards[random.randint(0,len(cards)-1)]]
  current_score=user_cards[0]+user_cards[1]
  computer_card=[cards[random.randint(0,len(cards)-1)],cards[random.randint(0,len(cards)-1)]]
  computer_current_score=computer_card[0]+computer_card[1]
  print(f"  Your cards: [{user_cards}],current score:{current_score}")
  print(f"  Computer first card: {computer_card[0]}")
  
  if current_score == 21 and computer_current_score == 21:
    print(f"  Your final hand :{user_cards},final score: {current_score}")
    print(f"  Computer final hand: {computer_card},final score: {computer_current_score}")
    print("Both Blackjack")
    end_game= True
    blackjack=True
  elif current_score == 21:
    print(f"  Your final hand :{user_cards},final score: {current_score}")
    print(f"  Computer final hand: {computer_card},final score: {computer_current_score}")
    print("You Blackjack")
    blackjack=True

    end_game=True
  
  elif computer_current_score == 21:
    print(f"  Your final hand :{user_cards},final score: {current_score}")
    print(f"  Computer final hand: {computer_card},final score: {computer_current_score}")
    print("Computer Blackjack")
    end_game=True
    blackjack=True

  

  while current_score < 21 and end_game != True:
    ask=input("Type 'y' to get another card,type 'n' to pass : ")
    if ask == "y":
      user_cards.append(cards[random.randint(0,len(cards)-1)])
      
      for single_card in user_cards:
        if single_card == 11:
          if current_score + 11 > 21:
            position=user_cards.index(single_card) 
            user_cards[position]=1
      current_score=0
      for single_card in user_cards:
        current_score+=single_card


    

      print(f"  Your cards: [{user_cards}],current score:{current_score}")
      print(f"  Computer first card: {computer_card[0]}")


    elif ask =='n':
      print(f"  Your final hand :{user_cards},final score: {current_score}")

   
      random_choice=random.randint(0,1)
      if computer_current_score < 17:
           random_choice = 1
       

      while random_choice == 1 and computer_current_score < 21:
        
        computer_card.append(cards[random.randint(0,len(cards)-1)])
        
        for single_card in computer_card:
          if single_card == 11:
            if computer_current_score + 11 > 21:
              position=computer_card.index(single_card) 
              computer_card[position]=1
        computer_current_score=0
        for single_card in computer_card:
          computer_current_score+=single_card
        if computer_current_score == 21:
          random_choice = 0
        else:
      
          random_choice=random.randint(0,1)
          if computer_current_score < 17:
            random_choice = 1

      print(f"  Computer final hand: {computer_card},final score: {computer_current_score}")
      if computer_current_score > 21:
        print("Opponent went Over.You win")
        end_game= True
       
      elif computer_current_score > current_score:
        print("You lose")
        end_game=True
    
      elif computer_current_score < current_score:
        print("You win")
        end_game=True
      elif computer_current_score == current_score:
        print("Draw")
        end_game=True
      

  if current_score > 21:
    print(f"  Your final hand :{user_cards},final score: {current_score}")
    random_choice=random.randint(0,1)
    if computer_current_score < 17:
      random_choice = 1
    
    while random_choice == 1 and computer_current_score < 21:
      
      computer_card.append(cards[random.randint(0,len(cards)-1)])
      
      for single_card in computer_card:
        if single_card == 11:
          if computer_current_score + 11 > 21:
            position=computer_card.index(single_card) 
            computer_card[position]=1
      computer_current_score=0
      for single_card in computer_card:
        computer_current_score+=single_card
      if computer_current_score == 21:
        random_choice = 0
      else:
        random_choice=random.randint(0,1)
        if computer_current_score < 17:
           random_choice = 1

    print(f"  Computer final hand: {computer_card},final score: {computer_current_score}")
    print("You went over.")
    if computer_current_score > 21:
      print("Opponent went over too.Draw")
    
  elif current_score == 21 and blackjack == False:
    print(f"  Your final hand :{user_cards},final score: {current_score}")
    random_choice=random.randint(0,1)
    if computer_current_score < 17:
      random_choice = 1
    
    while random_choice == 1 and computer_current_score < 21:
      
      computer_card.append(cards[random.randint(0,len(cards)-1)])
      
      for single_card in computer_card:
        if single_card == 11:
          if computer_current_score + 11 > 21:
            position=computer_card.index(single_card) 
            computer_card[position]=1
      computer_current_score=0
      for single_card in computer_card:
        computer_current_score+=single_card
      if computer_current_score == 21:
        random_choice = 0
      else:
        random_choice=random.randint(0,1)
        if computer_current_score < 17:

           random_choice = 1

    print(f"  Computer final hand: {computer_card},final score: {computer_current_score}")
    if computer_current_score == 21:
      print("Draw")
    else:
      print("You win")






