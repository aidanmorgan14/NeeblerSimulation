import random
import os
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

os.system('clear')

def run_simulation():
    
    small_neeblers = 5
    big_neeblers = 5
    generation = 0

    
    while True:
        if big_neeblers == 0 or small_neeblers == 0 or generation > 100:
            break
        else:
            initial_small_neeblers = small_neeblers
            initial_big_neeblers = big_neeblers
            
            
            for neebler in range(initial_small_neeblers):
                if random.randint(0, 4) > 2:  
                    small_neeblers -= 1
            
            
            baby_small_neeblers = 0
            for neebler in range(initial_small_neeblers):
                baby_small_neeblers += random.randint(0, 1)  
            
            
            for neebler in range(initial_big_neeblers):
                if random.randint(0, 6) > 3:  
                    big_neeblers -= 1
            
            
            baby_big_neeblers = 0
            for neebler in range(initial_big_neeblers):
                baby_big_neeblers += random.randint(0, 1)  

            
            small_neeblers += baby_small_neeblers
            big_neeblers += baby_big_neeblers

            
            generation += 1

    
    return {
        'generations': generation,
        'final_small_neeblers': small_neeblers,
        'final_big_neeblers': big_neeblers
    }


results = []
num_runs = 20

for _ in range(num_runs):
    result = run_simulation()
    results.append(result)

df = pd.DataFrame(results)


fig, ax = plt.subplots(1, 3, figsize=(24, 8))  


sns.scatterplot(ax=ax[0], data=df, x='generations', y='final_small_neeblers', hue='final_big_neeblers', palette='viridis', size='final_big_neeblers', sizes=(20, 200))
ax[0].set_title('Generation vs Small Neeblers Population')
ax[0].set_xlabel('Generations')
ax[0].set_ylabel('Final Small Neeblers Population')


sns.scatterplot(ax=ax[1], data=df, x='generations', y='final_big_neeblers', hue='final_small_neeblers', palette='viridis', size='final_small_neeblers', sizes=(20, 200))
ax[1].set_title('Generation vs Big Neeblers Population')
ax[1].set_xlabel('Generations')
ax[1].set_ylabel('Final Big Neeblers Population')


the_table = ax[2].table(cellText=df.values, colLabels=df.columns, cellLoc = 'center', loc='center')
the_table.auto_set_font_size(False)
the_table.set_fontsize(10)
the_table.scale(1.2, 1.2)
ax[2].axis('off')  
ax[2].set_title('Simulation Results')

plt.tight_layout()
plt.show()