import numpy as np

def increase_grid(size: int, changing_grid: np.ndarray, dtype=np.float64) -> np.ndarray:
    new_grid = np.zeros((size, size), dtype=dtype)
    new_grid[1:size -1, 1: size-1] = changing_grid
    return new_grid

def calculate_validity(arr: np.ndarray, cur_idx: int, sign: int, target=5) -> bool:
    points = 0
    idx = cur_idx
    while idx < len(arr) and arr[idx] == sign:
        points += 1
        idx += 1
    idx = cur_idx - 1
    while idx >= 0 and arr[idx] == sign:
        points += 1
        idx -= 1
    if points >= target: print(arr, cur_idx, sign, target)
    return points >= target

if __name__ == '__main__':
    print(increase_grid(5, 1))
    test_grid = np.random.randint(1, 10, (7, 7))
    print(test_grid)
    print(calculate_validity(np.array([1, 1, 1]), 2, 1, 4))