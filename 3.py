import random

# Objective function (maximize this)
def objective_function(x):
    return -x**2 + 5

# Hill Climbing algorithm
def hill_climbing(start_x, step_size, max_iterations):
    current_x = start_x
    current_score = objective_function(current_x)

    for i in range(max_iterations):
        # Try a new solution nearby
        new_x = current_x + random.uniform(-step_size, step_size)
        new_score = objective_function(new_x)

        print(f"Iteration {i+1}: x = {current_x:.4f}, f(x) = {current_score:.4f}")

        # If the new solution is better, move to it
        if new_score > current_score:
            current_x = new_x
            current_score = new_score
        else:
            # No improvement; stop if you want a simple version
            pass

    print("\nFinal Solution:")
    print(f"x = {current_x:.4f}, f(x) = {current_score:.4f}")
    return current_x, current_score

# Run the algorithm
# best_x, best_score = hill_climbing(start_x=random.uniform(-5, 5), step_size=0.1, max_iterations=100)
best_x, best_score = hill_climbing(start_x=0.1, step_size=0.05, max_iterations=5)
