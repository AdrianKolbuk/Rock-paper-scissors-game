import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def updatePt1(p_t1, counter):
  for n, row in enumerate(counter):
    for m, col in enumerate(row):
      p_t1[n][m] = counter[n][m]/np.sum(row)


def startGame(p_t1, counter, rolls, p_start, allChars, n):
  compRoll = np.random.choice(rolls, replace = True, p = p_start)
  reward = 0
  rewardList = [0]
    
  for i in range(n):
    print("Please type r for rock, p for paper, s for scissors or q to exit")
    roll = input()

    while(roll not in allChars):
      print("Unkown command")
      print("Please type r for rock, p for paper, s for scissors or q to exit")
      roll = input()
            
    if roll == 'q':
      print("End of the game")
      break
    else:
      print("You choose: ", roll)
      print("Computer choose: ", compRoll)
         
    if roll == 'r' and compRoll == 'r':
      print('_its a tie_')
      counter[0][1] += 1    
      updatePt1(p_t1, counter)        
      compRoll = np.random.choice(rolls, p = p_t1[0])

    elif roll == 'p' and compRoll == 'p':
      print('_its a tie_')
      counter[1][2] += 1     
      updatePt1(p_t1, counter)       
      compRoll = np.random.choice(rolls, p = p_t1[1])

    elif roll == 's' and compRoll == 's':
      print('_its a tie_')
      counter[2][0] += 1     
      updatePt1(p_t1, counter) 
      compRoll = np.random.choice(rolls, p = p_t1[2])

    elif roll == 'p' and compRoll == 'r':
      print('_you win_')
      reward += 1            
      counter[1][2] += 1            
      updatePt1(p_t1, counter)
      compRoll = np.random.choice(rolls, p = p_t1[1])

    elif roll == 's' and compRoll == 'r':
      print('_you lose_')
      reward -= 1
      compRoll = np.random.choice(rolls, p = p_t1[2])

    elif roll == 'r' and compRoll == 'p':
      print('_you lose_')
      reward -= 1
      compRoll = np.random.choice(rolls, p = p_t1[0])  

    elif roll == 's' and compRoll == 'p':
      print('_you win_')
      reward += 1  
      counter[2][0] += 1      
      updatePt1(p_t1, counter)
      compRoll = np.random.choice(rolls, p = p_t1[2])

    elif roll == 'r' and compRoll == 's':
      print('_you win_')
      reward += 1
      counter[0][1] += 1            
      updatePt1(p_t1, counter)
      compRoll = np.random.choice(rolls, p = p_t1[0])

    elif roll == 'p' and compRoll == 's':
      print('_you lose_')
      reward -= 1
      compRoll = np.random.choice(rolls, p = p_t1[1])

    rewardList.append(reward)
            
  return rewardList


p_start = [1/3, 1/3, 1/3]
allChars = ['r', 'p', 's', 'q']
rolls = ['r', 'p', 's']
p_t1 = [[1/3, 1/3, 1/3],
        [1/3, 1/3, 1/3],
        [1/3, 1/3, 1/3]]
        
counter = [[1, 1, 1],
           [1, 1, 1],
           [1, 1, 1]]

rewardList = startGame(p_t1, counter, rolls, p_start, allChars, 8)
print("Your reward history = ", rewardList)

df = pd.DataFrame(rewardList, columns = ['reward'])
print(df)
fig = df['reward'].plot(marker = 'o')
fig.set_xlabel('round')
fig.set_ylabel('reward')
plt.show();