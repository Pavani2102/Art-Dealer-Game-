#import libraries
import random

#define variables
level_choose='y'
#card symbols
card_symbols = {"spades":chr(0x2663), "hearts":chr(0x2665), "clubs": chr(0x2660), "diamonds": chr(0x2666)}
symbols=[card_symbols["spades"],card_symbols["hearts"],card_symbols["clubs"],card_symbols["diamonds"]]

#card types
card_nums = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

#card value
card_values = {"A": 11, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10,
               "J":10, "Q":10, "K":10}

heart=card_symbols["hearts"];club=card_symbols["clubs"];spade=card_symbols["spades"];diamond=card_symbols["diamonds"]

#art dealer selected paintings
art_dealer_selection=[]

#start game again
again_play1='y';again_play2='y';again_play3='y'

#game logo
def logo():
    for i in range(1,6):
        for j in range(6,-i):
            print(" " , end = " ")
        for j in range(1,i):
            print(card_symbols["diamonds"], end =" ")
        for j in range(i,0,-1):
            print(card_symbols["hearts"], end= " ")
        for j in range(i,1,-2):
            print(card_symbols["clubs"], end= " ")
        print()

    #print name of the game
    print('\t\t\t'+'Art Dealer Game'+'\n')

    for i in range(8):
        for j in range(i+2):
            print(" " ,end = " ")
        for j in range(1,7-i):
            print(card_symbols["clubs"],end= " " )
        for j in range(5-i,0,-1):
            print(random.randint(0,10),end = " ")
        for j in range(3-i,0,-1):
            print(card_symbols["spades"],end = " ")
        print()

#print the cards
def print_card(num1,num2,num3,num4,symbol1,symbol2,symbol3,symbol4):
    print()
    print('\tOption1\t'+'\t\tOption2\t'+'\t\tOption3\t'+'\t\tOption4\t')
    print()
    print(' '+'-'*17+'\t'+' '+'-'*17+'\t'+' '+'-'*17+'\t'+' '+'-'*17)
    for i in range(13):
        if i==1:
            print('|'+' '+num1+'\t\t'+'  '+'|'+'\t'+'|'+' '+num2+'\t\t'+'  '+'|'+'\t'+'|'+' '+num3+'\t\t'+'  '+'|'+'\t'+'|'+' '+num4+'\t\t'+'  '+'|')
        elif i==6:
            print('|'+'\t'+' '+symbol1+'\t'+'  '+'|'+'\t'+'|'+'\t'+' '+symbol2+'\t'+'  '+'|'+'\t'+'|'+'\t'+' '+symbol3+'\t'+'  '+'|'+'\t'+'|'+'\t'+' '+symbol4+'\t'+'  '+'|')
        elif i==11:
            print('|'+' '+'\t\t'+num1+' '+'|'+'\t'+'|'+' '+'\t\t'+num2+' '+'|'+'\t'+'|'+' '+'\t\t'+num3+' '+'|'+'\t'+'|'+' '+'\t\t'+num4+' '+'|')
        else:
            print('|'+'\t\t'+'  '+'|'+'\t'+'|'+'\t\t'+'  '+'|'+'\t'+'|'+'\t\t'+'  '+'|'+'\t'+'|'+'\t\t'+'  '+'|')
    print(' '+'-'*17+'\t'+' '+'-'*17+'\t'+' '+'-'*17+'\t'+' '+'-'*17)


#choose random cards
def choose_card():
    deck=dict()
    selected_numbers=[]
    selected_symbols=[]
    selection=[]
    for i in range(1,5):
        num=random.choice(card_nums)
        symbol=random.choice(symbols)
        sel_val=deck.values()
        
        if str(num+symbol)in sel_val:
            while True:
                num=random.choice(card_nums)
                symbol=random.choice(symbols)
                
        deck['Option'+str(i)]=num+symbol
        selected_numbers.append(num)
        selected_symbols.append(symbol)
                    
    return deck,selected_numbers,selected_symbols

#blowing balls for winners
def blow_balloons():
    print('\nYes, you have selected correct painting for me! Thank you!')
    print()
    print('\U0001F388'+'\U0001F3C6'+'\U0001F388'+'\U0001F388'+'\U0001F388')
    print('\t'+'\U0001F388'+'\U0001F388'+'\U0001F3C6'+'\U0001F3C6'+'\U0001F388'+'\U0001F388')
    print('\t\t'+'='*10)
    print('\t\t'+'YOU ARE THE WINNER!!!')
    print('\t\t'+'='*10)
    print('\t\t\t'+'\U0001F388'+'\U0001F388'+'\U0001F3C6'+'\U0001F3C6'+'\U0001F388'+'\U0001F388')
    print('\t\t\t\t '+'\U0001F388'+'\U0001F388'+'\U0001F388'+'\U0001F3C6'+'\U0001F388')

def pattern_1_n_3(symbol1,symbol2,symbol3,owner_selection_symbol):
    #pattern 1,3:all cards symbols are red or (all cards symbol is diamond or heart)
    if symbol1 in [heart,diamond] and symbol2 in [heart,diamond] and symbol3 in [heart,diamond]:
        if owner_selection_symbol in [heart,diamond]:
            #print('pattern1 or 3')
            return True
        else:
            return False

def pattern_2_n_3(symbol1,symbol2,symbol3,owner_selection_symbol):
    #pattern 2,3:all cards symbols are black or (all cards symbol is spade or club)
    if symbol1 in [spade,club] and symbol2 in [spade,club] and symbol3 in [spade,club]:
        if owner_selection_symbol in [spade,club]:
            #print('pattern2 or 3')
            return True
        else:
            return False

def game_winning_patterns_l1(owner_selection_num,owner_selection_symbol):
    data=[]
    for i in range(3):
        if '10' in art_dealer_selection[i]:
            num,symbol='10',art_dealer_selection[i][-1]
        else:
            num,symbol=art_dealer_selection[i]
        data.append(num)
        data.append(symbol)
    print('data:',data)
        
    num1,symbol1,num2,symbol2,num3,symbol3=data

    return pattern_1_n_3(symbol1,symbol2,symbol3,owner_selection_symbol),pattern_2_n_3(symbol1,symbol2,symbol3,owner_selection_symbol),data

def game_winning_patterns_l3(owner_selection_num,owner_selection_symbol):
    data=[]
    for i in range(3):
        if '10' in art_dealer_selection[i]:
            num,symbol='10',art_dealer_selection[i][-1]
        else:
            num,symbol=art_dealer_selection[i]
        data.append(num)
        data.append(symbol)
    #print('data:',data)
        
    num1,symbol1,num2,symbol2,num3,symbol3=data
##    print(num1,num2,num3)
##    print(data)
##    print(num1[0],num2[0],num3[0])
##    print(card_values[num1],card_values[num2],card_values[num3],card_values[owner_selection_num])
##    

    #heart=card_symbols["hearts"];club=card_symbols["clubs"];spade=card_symbols["spades"];diamond=card_symbols["diamonds"]

    #pattern 1,3:all cards symbols are red or (all cards symbol is diamond or heart)
    if symbol1 in [heart,diamond] and symbol2 in [heart,diamond] and symbol3 in [heart,diamond]:
        if owner_selection_symbol in [heart,diamond]:
            #print('pattern1 or 3')
            blow_balloons()
        else:
            print('\n'+'\U0001F641'+'Sorry, you have selected wrong painting for me!'+'\U0001F641')
        
    #pattern 2,3:all cards symbols are black or (all cards symbol is spade or club)
    elif symbol1 in [spade,club] and symbol2 in [spade,club] and symbol3 in [spade,club]:
        if owner_selection_symbol in [spade,club]:
            #print('pattern2 or 3')
            blow_balloons()
        else:
            print('\n'+'\U0001F641'+'Sorry, you have selected wrong painting for me!'+'\U0001F641')
    else:
        #print('different symbols')
        #pattern-4: all cards have same number but different symbol---check from here
        if num1 == num2 and num2 == num3:
            if num1 == owner_selection_num and num2 == owner_selection_num and num3 == owner_selection_num:
                #print('pattern4')
                blow_balloons()
            else:
                print('\n'+'\U0001F641'+'Sorry, you have selected wrong painting for me!'+'\U0001F641')
                    
        #pattern-5: single digit prime number 2,3,5,7 with different symbol
        elif num1[0] in ["2","3","5","7"] and num2[0] in ["2","3","5","7"] and num3[0] in ["2","3","5","7"] and owner_selection_num in ["2","3","5","7"]:
            if num1[0] is not num2[0] and num1[0] is not num3[0] and num2[0] is not num3[0]:
                if owner_selection_num is not num1[0] and owner_selection_num is not num2[0] and owner_selection_num is not num3[0]:
                    #print('pattern5')
                    blow_balloons()
                else:
                    print('\n'+'\U0001F641'+'Sorry, you have selected wrong painting for me!'+'\U0001F641')
        #pattern-6:all cards symbol different but number is even number
        elif int(card_values[num1])%2==0 and int(card_values[num2])%2==0 and int(card_values[num3])%2==0:
            if int(card_values[owner_selection_num])%2==0:
                #print('pattern6')
                blow_balloons()
            else:
                print('\n'+'\U0001F641'+'Sorry, you have selected wrong painting for me!'+'\U0001F641')

        #pattern-7: all number addition is 21 with different symbol
        elif int(card_values[num1])+int(card_values[num2])+int(card_values[num3])+int(card_values[owner_selection_num])==21:
            print('pattern7 as 21')
            blow_balloons()
        elif int(card_values[num1])+int(card_values[num2])+int(card_values[num3])+int(card_values[owner_selection_num])!=21:
            print('pattern7 as not 21')
            print('\n'+'\U0001F641'+'Sorry, you have selected wrong painting for me!'+'\U0001F641')
        
        else:
            print('\n'+'\U0001F641'+'Sorry, This is not an our pattern of selection!'+'\U0001F641')


#main program
logo()

print("There are 3 levels.\n1)Level 1(K2)\n2)Level 2(G 3-5)\n3)Level 3(G 6-8)")

while level_choose=='y':
    level_option=input('\nWhich level do you want to play (1/2/3)?.Please enter level number:')

    if level_option=='1':
          print('\nHello, I am Gallery Owner.'+'Please choose any three my best art gallery paintings.')
          while again_play1=='y':
              for i in range(3):
                  deck,card_num,card_symbol=choose_card()
                  print_card(card_num[0],card_num[1],card_num[2],card_num[3],card_symbol[0],card_symbol[1],card_symbol[2],card_symbol[3])
                  option=random.choice(list(deck.keys()))
                  art_dealer_selection.append(deck[option])
              print('\nYour selected paintings are as below.')
              print('-'*40)
              print('1)'+art_dealer_selection[0]+'\n2)'+art_dealer_selection[1]+'\n3)'+art_dealer_selection[2])

              print('\nCard Options:')
              print('-'*14)
              print('Card Numbers:',"A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")
              print('Card Symbols:','Spades'+chr(0x2663)+',Hearts'+chr(0x2665)+',Clubs'+chr(0x2660)+',Diamonds'+chr(0x2666))
              num=0
              while num<3:
                  while True:
                      gallery_owner_choice=input('\nHello Buyer,I will select next painting for you from above options. ')
                      if ' ' in gallery_owner_choice:
                          split_selection=gallery_owner_choice.split()
                          owner_selection_num=split_selection[0]
                          symbol=split_selection[1].lower()
                          if owner_selection_num in card_nums:
                              if symbol.lower() in ['spades','diamonds','clubs','hearts']:
                                  owner_selection_symbol=card_symbols[symbol]
                                  break
                              else:
                                  print('\nInvalid card selection.')
                          else:
                              print('\nInvalid card selection.')
                      else:
                        print('\nInvalid card selection.')

                  print('It is ',owner_selection_num+owner_selection_symbol)

                  red,black,data=game_winning_patterns_l1(owner_selection_num,owner_selection_symbol)
                  if red==True:
                      blow_balloons()
                      break
                  elif black==True:
                      blow_balloons()
                      break
                  elif red==False:
                      print('\n'+'\U0001F641'+'Sorry, you have selected wrong painting for me!'+'\U0001F641')
                      num=num+1
                  elif black==False:
                      print('\n'+'\U0001F641'+'Sorry, you have selected wrong painting for me!'+'\U0001F641')
                      num=num+1
                  else:
                      print('\n'+'\U0001F641'+'Sorry, This is not an our pattern of selection for level 1!'+'\U0001F641')
                      break
                    
              again=input('\nDo you want to play again? ')
              if again_play1==again[0].lower():
                  art_dealer_selection=[]
              else:
                  print('\nThanks for playing Level 1!!!')
                  level_choose='n'
                  break
              print()
              break
                      
    elif level_option=='2':
          print('\nHello, I am Gallery Owner.'+'Please choose any three my best art gallery paintings.')
          while again_play1=='y':
              for i in range(3):
                  deck,card_num,card_symbol=choose_card()
                  print_card(card_num[0],card_num[1],card_num[2],card_num[3],card_symbol[0],card_symbol[1],card_symbol[2],card_symbol[3])
                  option=random.choice(list(deck.keys()))
                  art_dealer_selection.append(deck[option])
              print('\nYour selected paintings are as below.')
              print('-'*40)
              print('1)'+art_dealer_selection[0]+'\n2)'+art_dealer_selection[1]+'\n3)'+art_dealer_selection[2])

              print('\nCard Options:')
              print('-'*14)
              print('Card Numbers:',"A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")
              print('Card Symbols:','Spades'+chr(0x2663)+',Hearts'+chr(0x2665)+',Clubs'+chr(0x2660)+',Diamonds'+chr(0x2666))
              num=0
              while num<3:
                  while True:
                      gallery_owner_choice=input('\nHello Buyer,I will select next painting for you from above options. ')
                      if ' ' in gallery_owner_choice:
                          split_selection=gallery_owner_choice.split()
                          owner_selection_num=split_selection[0]
                          symbol=split_selection[1].lower()
                          if owner_selection_num in card_nums:
                              if symbol.lower() in ['spades','diamonds','clubs','hearts']:
                                  owner_selection_symbol=card_symbols[symbol]
                                  break
                              else:
                                  print('\nInvalid card selection.')
                          else:
                              print('\nInvalid card selection.')
                      else:
                        print('\nInvalid card selection.')

                  print('It is ',owner_selection_num+owner_selection_symbol)

                  red,black,data=game_winning_patterns_l1(owner_selection_num,owner_selection_symbol)
                  num1,symbol1,num2,symbol2,num3,symbol3=data
                  if red==True:
                      blow_balloons()
                      break
                  elif black==True:
                      blow_balloons()
                      break
                  elif red==False:
                      print('\n'+'\U0001F641'+'Sorry, you have selected wrong painting for me!'+'\U0001F641')
                      num=num+1
                  elif black==False:
                      print('\n'+'\U0001F641'+'Sorry, you have selected wrong painting for me!'+'\U0001F641')
                      num=num+1
                  else:
                      #print('different symbols')
                      #pattern-4: all cards have same number but different symbol---check from here
                      if num1 == num2 and num2 == num3:
                          if num1 == owner_selection_num and num2 == owner_selection_num and num3 == owner_selection_num:
                              #print('pattern4')
                              blow_balloons()
                              break
                          else:
                              print('\n'+'\U0001F641'+'Sorry, you have selected wrong painting for me!'+'\U0001F641')
                              num=num+1
                                    
                      #pattern-5: single digit prime number 2,3,5,7 with different symbol
                      elif num1[0] in ["2","3","5","7"] and num2[0] in ["2","3","5","7"] and num3[0] in ["2","3","5","7"] and owner_selection_num in ["2","3","5","7"]:
                          if num1[0] is not num2[0] and num1[0] is not num3[0] and num2[0] is not num3[0]:
                              if owner_selection_num is not num1[0] and owner_selection_num is not num2[0] and owner_selection_num is not num3[0]:
                                  #print('pattern5')
                                  blow_balloons()
                                  break
                              else:
                                  print('\n'+'\U0001F641'+'Sorry, you have selected wrong painting for me!'+'\U0001F641')
                                  num=num+1
                                  
                      #pattern-7: all number addition is 21 with different symbol
                      elif int(card_values[num1])+int(card_values[num2])+int(card_values[num3])+int(card_values[owner_selection_num])==21:
                          #print('pattern7 as 21')
                          blow_balloons()
                          break
                      elif int(card_values[num1])+int(card_values[num2])+int(card_values[num3])+int(card_values[owner_selection_num])!=21:
                          #print('pattern7 as not 21')
                          print('\n'+'\U0001F641'+'Sorry, you have selected wrong painting for me!'+'\U0001F641')
                          num=num+1
                      else:
                          print('\n'+'\U0001F641'+'Sorry, This is not an our pattern of selection for level 1!'+'\U0001F641')
                          break
                    
              again=input('\nDo you want to play again? ')
              if again_play1==again[0].lower():
                  art_dealer_selection=[]
              else:
                  print('\nThanks for playing Level 2!!!')
                  level_choose='n'
                  break
              print()
              break
                  
    elif level_option=='3':
          #define player's name---------------------------------------------
          art_dealer = input("\nEnter a name for art_dealer: ").strip()
          art_seller = input("\nEnter a name for art_seller: ").strip()
          print('\nGame is being played between ' + art_dealer + ' and ' + art_seller)
          print('*'*50)
          print('\nHello, I am Gallery Owner.'+'These are my best art gallery paintings.')
          while again_play3 in ['y','Y']:
            for i in range(3):
                deck,card_num,card_symbol=choose_card()
                print_card(card_num[0],card_num[1],card_num[2],card_num[3],card_symbol[0],card_symbol[1],card_symbol[2],card_symbol[3])
                while True:
                    art_dealer=input('Please tell me, which painting do you want to choose?')
                    if art_dealer.lower()=='option1':
                        print('Thanks for selecting option1.')
                        art_dealer_selection.append(deck['Option1'])
                        break
                    elif art_dealer.lower()=='option2':
                        print('Thanks for selecting option2.')
                        art_dealer_selection.append(deck['Option2'])
                        break
                    elif art_dealer.lower()=='option3':
                        print('Thanks for selecting option3.')
                        art_dealer_selection.append(deck['Option3'])
                        break
                    elif art_dealer.lower()=='option4':
                        print('Thanks for selecting option4.')
                        art_dealer_selection.append(deck['Option4'])
                        break
                    else:
                        print('\nInvalid option selection!Please retry!!\n')
            print('\nYour selected paintings are as below.')
            print('-'*40)
            print('1)'+art_dealer_selection[0]+'\n2)'+art_dealer_selection[1]+'\n3)'+art_dealer_selection[2])

            print('\nCard Options:')
            print('-'*14)
            print('Card Numbers:',"A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")
            print('Card Symbols:','Spades'+chr(0x2663)+',Hearts'+chr(0x2665)+',Clubs'+chr(0x2660)+',Diamonds'+chr(0x2666))

            while True:
                gallery_owner_choice=input('\nHello Buyer,I will select next painting for you from above options. ')
                if ' ' in gallery_owner_choice:                 
                    split_selection=gallery_owner_choice.split()
                    owner_selection_num=split_selection[0]
                    symbol=split_selection[1].lower()
                    if owner_selection_num in card_nums:
                        if symbol.lower() in ['spades','diamonds','clubs','hearts']:   
                            owner_selection_symbol=card_symbols[symbol]
                            break              
                        else:
                            print('\nInvalid card selection.')
                    else:
                        print('\nInvalid card selection.')
                else:
                    print('\nInvalid card selection.')
            
            print('It is ',owner_selection_num+owner_selection_symbol)

            game_winning_patterns_l3(owner_selection_num,owner_selection_symbol)
                    
            again3=input('\nDo you want to play again? ')
            
            if again_play3==again3[0].lower():
                art_dealer_selection=[]                
            else:
                print('\nThanks for playing Level 3!!!')
                level_choose='n'
                break
            print()
            break
            
    else:
        print('\nInvalid option selection')
        level_choose='y'
