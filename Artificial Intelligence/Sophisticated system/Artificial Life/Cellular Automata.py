import numpy as np
import matplotlib.pyplot as plt

def sync_update(grid):
    # Synchronous update
    new_grid = np.zeros_like(grid)
    for i in range(1, grid.shape[0] - 1):
        for j in range(1, grid.shape[1] - 1):
            # Update cell state based on Conway's Game of Life rules
            # Here, simplified rules are used; modify as needed for specific requirements
            new_grid[i, j] = update_rule(grid, i, j)
    return new_grid

def random_order_update(grid):
    # Random order update
    indices = np.random.permutation(grid.size)
    n = len(indices) // 2
    new_grid = grid.copy().flatten()
    for idx in indices[:n]:
        i, j = np.unravel_index(idx, grid.shape)
        new_grid[idx] = update_rule(grid, i, j)
    return new_grid.reshape(grid.shape)

def partial_sync_alpha_update(grid, step, alpha):
    # Partial synchronous update and partial alpha asynchronous update in regions
    new_grid = np.zeros_like(grid)
    for i in range(1, grid.shape[0] - 1):
        for j in range(1, grid.shape[1] - 1):
            # Update based on cyclic order
            idx = (i * grid.shape[1] + j + step) % (grid.size - 1) + 1
            m, n = np.unravel_index(idx, grid.shape)

            # Partial synchronous update in a specific region
            if i < grid.shape[0] // 2 and j < grid.shape[1] // 2:
                new_grid[i, j] = sync_update(grid)[i, j]
            # Partial alpha asynchronous update in another region
            else:
                if np.random.rand() < alpha:
                    new_grid[i, j] = update_rule(grid, m, n)
                else:
                    new_grid[i, j] = grid[i, j]
    return new_grid

def alpha_async_update(grid, alpha):
    # Alpha asynchronous update
    new_grid = grid.copy()
    for i in range(1, grid.shape[0] - 1):
        for j in range(1, grid.shape[1] - 1):
            # Update based on probability alpha
            if np.random.rand() < alpha:
                new_grid[i, j] = update_rule(grid, i, j)
    return new_grid

def update_rule(grid, i, j):
    # Obtain cell and its neighbors' states
    current_state = grid[i, j]
    neighbor_sum = np.sum(grid[i-1:i+2, j-1:j+2]) - current_state

    # Conway's Game of Life rules
    if current_state == 1 and (neighbor_sum < 2 or neighbor_sum > 3):
        return 0  # Living cell dies
    elif current_state == 0 and neighbor_sum == 3:
        return 1  # Dead cell comes to life
    else:
        return current_state  # Maintain current state

# Initialize the initial state of the cellular automaton
initial_state = np.random.randint(0, 2, size=(50, 50))

# Define subplot layout
fig, axs = plt.subplots(4, 5, figsize=(20, 16))

# Display the initial state
axs[0, 0].imshow(initial_state, cmap='binary')
axs[0, 0].set_title('Initial State')
axs[0, 0].axis('off')

# Synchronous update, random order update, partial sync-alpha update, alpha asynchronous update for steps 0-4
for step in range(1, 5):
    sync_updated_state = sync_update(initial_state)
    random_updated_state = random_order_update(initial_state)
    partial_updated_state = partial_sync_alpha_update(initial_state, step, alpha=0.5)
    alpha_updated_state = alpha_async_update(initial_state, alpha=0.5)

    # Use the updated state as the initial state for the next step
    initial_state[:] = sync_updated_state

    axs[0, step].imshow(sync_updated_state, cmap='binary')
    axs[1, step].imshow(random_updated_state, cmap='binary')
    axs[2, step].imshow(partial_updated_state, cmap='binary')
    axs[3, step].imshow(alpha_updated_state, cmap='binary')

    axs[0, step].set_title(f'Sync Step {step}')
    axs[1, step].set_title(f'Random Step {step}')
    axs[2, step].set_title(f'Partial Step {step}')
    axs[3, step].set_title(f'Alpha Step {step}')

    for ax in axs.flat:
        ax.axis('off')

plt.show()


