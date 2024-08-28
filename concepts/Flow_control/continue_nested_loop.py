for iteration_1 in range(3):
    print("current outer loop iteration_1 value: ",iteration_1)
    for iteration_2 in range(2):
        print("current inner loop iteration_2 value: ",iteration_2)
        if iteration_1==iteration_2:
            print(f"Executing continue as iteration_1 value: {iteration_1} == iteration_2 value :{iteration_2}")
            
            # continue inside inner loop - terminates current iteration of inner loop and executes next iteration
            continue
        
        print(f"current outer loop iteration_1 value: {iteration_1} with its current inner loop iteration_2 value: {iteration_2}")