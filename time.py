import time
from tqdm import tqdm

seconds = 10

for i in tqdm(range(seconds)):
    time.sleep(1)  # sleep one second in each iteration