import numpy as np

def increase_grid(size: int, changing_grid: np.ndarray, dtype=np.float64) -> np.ndarray:
    new_grid = np.zeros((size, size), dtype=dtype)
    new_grid[1:size -1, 1: size-1] = changing_grid
    return new_grid

if __name__ == '__main__':
    print(increase_grid(5, 1))