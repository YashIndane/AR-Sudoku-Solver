from webcam_process import capture_save 
from model_testing import generate_grid
from sudoku3 import solve
from motion_digits2 import fill_digits_motion
import time


coordinates = capture_save()

GRID , empty_idx = generate_grid()

print(GRID)

time1 = time.time()

num_array = solve(GRID)

time2 = time.time()

fill_digits_motion(num_array , coordinates , empty_idx , 'Solved in ' + '{:.3f}'.format(time2 - time1) + ' secs' )
