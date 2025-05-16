## Git Stuff

Figure out gitignore stuff and paste here when you do:
You kinda just put the name of the file in the gitignore file and Git takes care of the rest . You can use basic regex to make this more efficient. Common thing is doing something like *.log to get rid of all log files or something

HOWEVER, if the file already was tracked before, you need to remove it manually. If you want it to still be in your directory, you can use the cache version of the command. Do this:

`git rm --cached duck.ai_2025-05-14_21-24-29.txt`

## Some Emacs reminders:
- C-w deletes stuff (a line?)
- C-a -> start of line
- C-e -> end of line
- M-b -> back a word
- M-f -> forward a word


## Some Markdown reminders:  
- Backticks can distinguish code in Markdown 
- Apparently to get one line to be on the line after the first one you need two spaces on the first line lol. THEN press enter.

## Cron Jobs
Cron Tab Task Scheduler for UNIX systems: [Guide](https://medium.com/@justin_ng/how-to-run-your-script-on-a-schedule-using-crontab-on-macos-a-step-by-step-guide-a7ba539acf76)  

Cron Tab Expression Generator: [Link](http://www.cronmaker.com/;jsessionid=node01efv6yyj1wa3s10wger6hjr2tv398869.node0?0)  

Example:  
5:59 every Thursday is --> 0 59 5 ? * THU *  


## Misc Stuff
- Absolute paths start with a slash