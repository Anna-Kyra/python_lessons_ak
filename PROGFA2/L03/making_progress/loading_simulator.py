from progress_bar import ProgressBar
import random
import time

background = ProgressBar("background", 0)
sound_files = ProgressBar("sound files", 0)
spritesheet = ProgressBar("spritesheet", 0)
user_data = ProgressBar("user data", 0)

files = list()

files.append(background)
files.append(sound_files)
files.append(spritesheet)
files.append(user_data)

for file in files:
    while file.percentage < 100:
        add = random.randint(1, 3)
        add_percentage = add * 10
        sleep_time = random.randint(2, 20) / 10

        if file.percentage + add_percentage >= 100:
            file.percentage = 100
            print(file)
            print(f"--> Finished loading {file.name}")
        else:
            file.percentage += add_percentage
            print(file)
            time.sleep(sleep_time)

print(f"==> all {len(files)} files have been loaded!")
