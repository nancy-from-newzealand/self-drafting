# self-drafting

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

