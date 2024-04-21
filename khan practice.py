import random
import os
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


print(f"{'Run':<5} {'Generations':<12} {'Small Neeblers':<15} {'Big Neeblers':<15}")
for i, res in enumerate(results):
    print(f"{i+1:<5} {res['generations']:<12} {res['final_small_neeblers']:<15} {res['final_big_neeblers']:<15}")
