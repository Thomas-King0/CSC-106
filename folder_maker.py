import os

for weeknum in range(1,17):
    weekfolder = os.path.join(os.curdir, f"Week {str(weeknum).zfill(2)}")
    
    os.mkdir(weekfolder)
    for day in ["Monday", "Wednesday", "Friday"]:
        os.mkdir(os.path.join(weekfolder, day))
