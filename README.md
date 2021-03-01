# PSM-and-LI-chatbot
=======CHATBOT=======

Fundamental step before start chatbot:

1. Install anaconda, create environment with any name.
2. Select the environment created, and run VSCode Software from anaconda.

Follow the step to run the chatbot in localhost:

3. Open terminal in VSCode from anaconda and environment created
4. Type in Terminal(Do not close while running): rasa run actions 
5. Type in Terminal(Do not close while running): rasa run -m models --enable-api --cors "*" --debug

=======WEBSITE=======

Next, download/copy/clone file from the link below into your htdocs
https://github.com/yazwan/PSM-LI-Website Download this in your Htdocs folder, Xampp.

Turn on Apache & MySQL in Xampp software

with Ngrok Software, run two command:
Type (Do not close while running): ngrok http 5005
Type (Do not close while running): ngrok http 80

Once you got URL created after run Ngrok http 5005, copy the URL generated and put inside the website code shown as below:

socketUrl: "https://...ngrok.io" 
Four files need to be inserted with above code, the filename is:
1. oklogin.php
2. home.php
3. manage_user.php
4. view_feedback.php

You are all set! You may explore the website with browser
URL offline: localhost
URL online: https://...ngrok.io (look at Ngrok http 80 you created)

DONE
