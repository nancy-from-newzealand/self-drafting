# self-drafting

# Git commands
Some usefull git commands you can from the terminal of your pi:
 - Install git, from the terminal
 ```
    $ sudo apt-get update 
    $ sudo apt-get install git.
 ```

- Switch to another existing branch
          `git checkout <name_of_branch>`
   
- Create new branch
         `git checkout -b <name_of_branch>`
            
            !! NOTE: before creating a new branch, switch to master and pull master
  
 - Pull branch (pull remote changes from remote)
   `git checkout <name_of_branch>`
   `git pull`
   
  - Push changes (push local changes to remote)
    ` git add *`
    ` git commit -m "Commit message"`
     `git push `
  - Check what is on the stage
   ` git status ' 



# Roomba commands

   -   Start Command opcode: 128 Number of data bytes: 0
         Starts the SCI. The Start command must be sent before any other SCI commands. This command puts the SCI in passive mode.
   -  Control Command opcode: 130
         Number of data bytes: 0
         Enables user control of Roomba. This command must be sent after the start command and before any control commands are sent to the SCI. The SCI must be in passive mode to accept this command. This command puts the SCI in safe mode.
   -  A Drive command with a positive velocity and a positive radius will make Roomba drive forward while turning toward the left. A negative      radius will make it turn toward the right. 
   - Serial sequence: [137] [Velocity high byte] [Velocity low byte] [Radius high byte] [Radius low byte]
   - Drive data bytes 1 and 2: Velocity (-500 – 500 mm/s)
      Drive data bytes 3 and 4: Radius (-2000 – 2000 mm) Special cases: 
      Straight = 32768 = hex 8000
      Turn in place clockwise = -1
      Turn in place counter-clockwise = 1
   - Stop: 173 --> /xAD

## Docs
  - [iRobot create ](https://www.irobotweb.com/~/media/MainSite/PDFs/About/STEM/Create/iRobot_Roomba_600_Open_Interface_Spec.pdf)
  - [Roomba](https://www.usna.edu/Users/weaprcon/esposito/_files/roomba.matlab/Roomba_SCI.pdf)
