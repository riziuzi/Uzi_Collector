# Uzi Collector

Welcome to the Uzi Collector repository! This repository contains the Python script `Uzi_Collector.py` which is used to collect data and create a file structure in your specified directory. This README file will guide you on how to get started with using the script.

## Getting Started

To get started with using the Uzi Collector script, follow these steps:

1. Clone the repository or download the ZIP file and extract it to a directory of your choice.

2. Open the `Uzi_configuration.py` file located in the root of the repository.

3. Set the values of the two variables `root` and `control`.

   - `root`: This variable stores the location of the directory where you want to store the collected data. You can set the location to a local Google Drive directory which can work as your cloud server if you automate the process using a task scheduler.
   
   - `control`: This variable stores the current location of the repository, from where you are launching the program.
   
4. Once you have set both variables, save and close the `Uzi_configuration.py` file.

5. Open the `rizi_spawner.py` file located in the root of the repository.

6. Execute the `rizi_spawner.py` file by double-clicking on it. This will spawn a terminal showing a simple progress bar for 18*3 folders (explained in the `Industry_ticker.xlsx` section). This will create a file structure in your specified `root` location and collect the data (make sure you have internet!).

## Further Explanation

More details on how the Uzi Collector script works will be added soon. 

## Automating the Process

If you want to automate the process of collecting data and creating the file structure, you can use the Windows task scheduler. Follow these steps:

1. Open the Windows Task Scheduler and create a new task.

2. Set the name of the task and select the frequency at which you want the task to run.

3. Under the Actions section, set Program/script: `py`, and Add arguments (optional): `-u "<location of your repo, or simply, control>\rizi_spawner.py"`

4. Set any additional settings and save the task.

Now, the Uzi Collector script will run automatically at the scheduled time and collect the data and create the file structure.
