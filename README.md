# Daily-Quote-Automated-Texting-

A program that sends daily quotes at a specified time via the Twilio API. 

- You can specify which time in the day you want the quote to be sent in "run.py". The text will be continued to be sent as long as the program is running in the background. 
- Second "test field" in "run.py" can be used to set the message send time to the current time (set manually) so the message can be sent immediately. 

Installation
--------------
- In the program directory run the folowing Terminal Command:

```
pip install -r requirements.txt

```

Setup
--------
1. Setup a free Twilio account and obtain your account token and account sid. The program will not work without it. 
2. In your "twilio_credentials.py" input this information in the fields. 

- "cellphone" (number you want to send the text to, format as country code followed by phone number (i.e +66, +1, etc).
- "twilio_number" (number that comes with your twilio account)
- twilio_account_sid" (twilio account sid)  *SECRET
- "twilio token" (your twilio account token, which can be found in the account settings.) *SECRET 

3. Setup complete

*They Said So API credentials are not needed, since we are accessing the FREE Public API. 

Running the program
--------------------

- In the program directory run the folowing Terminal Command:

```
python3 run.py 

```