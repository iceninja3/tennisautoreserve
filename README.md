Windows: Use Windows Task Scheduler
Linux/Mac: Use (CronJob)[https://kubernetes.io/docs/concepts/workloads/controllers/cron-jobs/#:~:text=CronJob%20is%20meant%20for%20performing,CronJobs%20have%20limitations%20and%20idiosyncrasies.]

Probably use Selenium to access the (website)[https://secure.recreation.ucla.edu/booking] and select the buttons (the easy part)
- Log in (or if cookies are usable just skip this step)
- Select tennis courts
- Iterate through courts, if unavailable -> move onto the next one (there's 6 courts total?). Send an email to specified user confirming/denying that reservation was made with script

Ideas to bypass 2FA:
- Save the cookies and load a new browser window to avoid manually logging in again?
- Send the code to an email address/SMS and automate reading/inputting that into the website?
- Generate the code yourself with the secret key (although you'd put yourself at significant security risk by doing this lol)
