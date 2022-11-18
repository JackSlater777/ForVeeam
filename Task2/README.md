This is a readme file to the second task:

Implement a program that synchronizes two folders: source and replica. The program should maintain a full, identical copy of destination folder at replica folder.

Requirements:

•	Synchronization must be one-way: after the synchronization content of the replica folder should be modified to exactly match content of the source folder;

•	Synchronization should be performed periodically;

•	File creation/copying/removal operations should be logged to a file and to the console output;

•	Folder paths, synchronization interval and log file path should be provided using the command line arguments.


********************************************
To provide main file path, synchronization interval and log file path use the command line arguments.

- first argument is the main file name;
- second argument is the synchronization interval;
- third argument is the log file path.

For example, to run the program, paste into the command line:

cd <path_to_task2_folder>

python main.py 60 logs.txt

where:
- main.py - main file
- 60 - the synchronization interval (in seconds)
- logs.txt - file with the backup history

Also check out the "setting.py" for more possibilities!
