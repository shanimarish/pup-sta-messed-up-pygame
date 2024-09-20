# The game starts here.


# Phone code starts here
label start:
    # Play music
    play music "audio/bg_music.mp3"
    scene dorm
    call phone_start
    $ phone_too = "Akilah" #who the conversation is with
    call message_start("akilah", "Akilah", " Hello! My name is Akilah and I need your help!")
    call message("akilah", "Akilah", "According to what I've heard, you're an ambitious detective and you’re very knowledgeable about cybersecurity.")
    call message("akilah", "Akilah", "It's no secret that \"5H4D0W,\" a well-known hacker, despises the Polytechnic University of the Philippines and has set out to sow havoc on its campus.")
    call message("akilah", "Akilah", "I’ve been tracking him down for a while, but we need your help to catch him!")
    call message("akilah", "Akilah", "You can meet me at the College of Engineering and Architecture.")
    # call message_img("akilah", "Akilah", "You can meet me at the College of Engineering and Architecture.\n(Click the image to see it full size.)", 0)
    call screen phone_reply("I’m on my way!","choice1")
    label choice1:
        call phone_after_menu
        call message_start("noimage", "me", "I’m on my way!")
        call phone_end # this one puts away the phone
# Phone code ends here

# Location1: College of Engineering and Architecture
label location1:
    scene cea
    show loc1
    pause
    a smile2 "Let’s test your skills first!"
    menu:
        a "How often should you change your password for social media security?"
        "Never.":
            a sad "Oops! Incorrect answer." with hpunch
            jump correct_loc1
        "I will change it only if there are some suspicious activities on my account.":
            a sad "Oops! Incorrect answer." with hpunch
            jump correct_loc1
        "Whenever I think that I need to change it to feel more secure.":
            a laugh "You got it!"
            jump correct_loc1
    label correct_loc1:
        a smile1 "The correct answer is \"Whenever I think that I need to change it to feel more secure.\""
        a normal "The more frequently you change passwords that haven't been used in a while, the safer you'll be; especially if you don't use multi-factor authentication."
        a "You also need to avoid providing personal information online since hackers and data mining firms value your information, which includes your email address, phone number, and social security number as it is worth a lot of money for them."
        a angry "Now, it's time to look for 5H4D0W."
        a annoyed "The hacker enjoys playing tricks on us, and he always leaves riddles to help us figure out where he is."
        a "Let's see if we can track him down!"

label riddle_1:
    scene riddle_1
    with fade
    call screen riddle1

    label wrong1:
        show wrong
        h 1 "Uh.... no! Try again." with hpunch
        hide wrong
        call screen riddle1

    label right1:
        scene main building
        a delighted "Perfect!"
        a smile1 "Originally, the PUP Pylon stood for the true, the good, and the beautiful."
        a "It could also stand for wisdom, strength, and beauty because any great or important undertaking requires wisdom to contrive, strength to support, and beauty to adorn."
        a "However, since 1987, the Pylon has come to symbolize truth, excellence, and wisdom."
        a "Hurry to PUP Pylon now!"
        jump location2

# Location2: PUP Pylon
label location2:
    scene pylon
    show loc2
    pause
    a shocked "A student installed a screensaver application on one of the university's computers. After updating the anti-virus software, a malicious program is discovered."
    menu:
        a "This appears to have infected the system at the same time as the screensaver was installed. Do you know what kind of malware this is?"
        "Spyware":
            a sad "Oops! Incorrect answer." with hpunch
            jump correct_loc2
        "Trojan Horse":
            a laugh "That's right!"
            jump correct_loc2
        "Virus":
            a sad "Oops! Incorrect answer." with hpunch
            jump correct_loc2
    label correct_loc2:
        a normal "A Trojan Horse is a type of malware that disguises itself as an attachment in an email or a free-to-download file before being downloaded and installed on the user's device."
        a sad "After being downloaded, the malicious code will perform the intended function, such as gaining backdoor access to corporate systems, spying on users' internet activities, or stealing sensitive data."
        a annoyed "5H4D0W must have left before we arrived, but it appears that he left another riddle."

label riddle_2:
    scene riddle_2
    with fade
    call screen riddle2

    label wrong2:
        show wrong
        h 1 "Uh.... no! Try again." with hpunch
        hide wrong
        call screen riddle2

    label right2:
        scene main building
        a delighted "That's right!"
        a smile1 "The PUP Lagoon is probably the most popular hangout spot in the university when compared to the rest of the area."
        a "It serves as a waiting area for students while they awaited their next class, a picnic area during breaks, or even a place for students to come up with ideas for group projects."
        a "Let's go to PUP Lagoon now!"

#Location3: PUP Lagoon
label location3:
    scene lagoon
    show loc3
    pause
    a sad "5H4D0W appears to have gotten away once more."
    a smile1 "However, someone appears to require our assistance here!"
    menu:
        a "Alliah needs to log in to her SIS account, she is required to enter her student number, birthday, and password. Which is an example of a strong password?"
        "Ilovemypiano":
            a sad "Oops! Incorrect answer." with hpunch
            jump correct_loc3
        "1234567890":
            a sad "Oops! Incorrect answer." with hpunch
            jump correct_loc3
        "jelly22Fi$h":
            a laugh "Of course, you're right!"
            jump correct_loc3

    label correct_loc3:
        a smile1 "The answer is definitely jelly22Fi$h."
        a normal "Hackers and computer intruders use automated software to guess hundreds of passwords per minute to gain access to user accounts."
        a "To keep your accounts secure, create a strong, difficult-to-guess password and store it in a password manager so you don't forget it."
        a smug "Strong passwords are long and contain a mix of symbols, numbers, upper and lowercase letters, and punctuation."
        a shocked "Look! Instead of a riddle, he left us with a question to figure out. It's challenging, but we can do it!"

label riddle_3:
    scene riddle_3
    with fade
    call screen riddle3

    label wrong3:
        show wrong
        h 1 "Uh.... no! Try again." with hpunch
        hide wrong
        call screen riddle3

    label right3:
        scene main building
        a delighted "That's right!"
        a smile1 "The library of Ninoy Aquino Library and Learning Resource Center (NALLRC) is known as one of the libraries in Southeast Asia and it is also the home of the College of Law and Open University."
        a "Let's go there!"

# Location4: Ninoy Aquino Library and Learning Resource Center
label location4:
    scene nalrc
    show loc4
    pause
    a annoyed "5H4D0W is also not here."
    a "He's probably laughing right now because we can't seem to find him."
    a smug "We need to step up our game!"
    a shocked "Wait! Someone found the riddle 5H4D0W left, and he knows the solution. But, before he tells us the answer, he needs our help."
    menu:
        a "Harold wants to know which of these is a sign of a malware infection. Choose the correct answer."
        "The websites YouTube and Google show you similar ads.":
            a sad "Oops! Incorrect answer." with hpunch
            jump correct_loc4
        "Every time you open your browser, a certain site with several advertisements shows.":
            a laugh "You got it! Harold, by the way, said thank you!"
            jump correct_loc4
        "Every time you visit a website, a video ad plays.":
            a sad "Oops! Incorrect answer." with hpunch
            jump correct_loc4
    label correct_loc4:
        a sad "If a website with a lot of advertising keeps showing up when you open your browser, you most certainly have malware."
        a normal "If you fear you have malware, restart your computer, and clean up your device's disk. Another option is to download a virus scanner."
        a normal "5H4D0W stated that he wishes to see the stage that is used for public performances, activities, and gatherings."
        a "We need proceed to PUP Linear Park immediately."

# Location5: PUP Linear Park
label location5:
    scene linear park
    show loc5
    pause
    a annoyed "So, this is starting to irritate me! He's managed to sneak away once again!"
    a shocked "Now, several students are now reporting that 5H4D0W is sending malicious email to their email accounts."
    menu:
        a "You receive an email with the subject line \"CONGRATS on winning an iPhone!\" It then prompts you to open the message and click the provided link to collect your prize. What will you do?"
        "Without hesitation, I will follow the email's instructions and click the link.":
            a sad "Oops! Incorrect answer." with hpunch
            jump correct_loc5
        "I will click on the link and forward the message to my friends, so they know I've won.":
            a sad "Oops! Incorrect answer." with hpunch
            jump correct_loc5
        "I won’t click the link and instead, I will delete the email.":
            a laugh "Of course, you're right!"
            jump correct_loc5

    label correct_loc5:
        a normal "You should not click the link and instead, delete the email because that is an example of a phishing attack."
        a "Phishing is a type of internet fraud in which thieves impersonate reputable companies via email, text messages, advertisements, and other means in order to obtain sensitive information."
        a "This is commonly accomplished by attaching a link that appears to take you to the company's website, where you can fill out your information – but the website is fake, and the information you provided is directly sent to the scammers."
        a sad "Well … It looks like we need to solve another riddle."

label riddle_5:
    scene riddle_5
    with fade
    call screen riddle5

    label wrong5:
        show wrong
        h 1 "Uh.... no! Try again." with hpunch
        hide wrong
        call screen riddle5

    label right5:
        scene main building
        a delighted "That's right!"
        a smile1 "The Obelisk represents the strength of the Polytechnic University of the Philippines as a higher learning institution."
        a "It promotes educational and moral goals that are bolstered by a determined leadership with a clear vision for Filipino youth and an efficient support system inspired by the virtues of public service."
        a "Get to the PUP Obelisk as soon as possible!"

# Location6: PUP Obelisk
label location6:
    scene obelisk
    show loc6
    pause
    a annoyed "5H4D0W escaped yet again but he's still scheming! He's rumored to have hacked someone!"
    menu:
        a "Below are the things you must do if you’ve been hacked except one. What is it?"
        "Reset your password.":
            a sad "Oops! Incorrect answer." with hpunch
            jump correct_loc6
        "Check your device thoroughly.":
            a sad "Oops! Incorrect answer." with hpunch
            jump correct_loc6
        "Turn off your device.":
            a laugh "You got it!"
            jump correct_loc6
        "Notify your contacts about the hack.":
            a sad "Oops! Incorrect answer." with hpunch
            jump correct_loc6
    label correct_loc6:
        a sad "Turning off the computer is the same as erasing evidence that could lead to the attackers' and their actions being identified."
        a "Turning off the power technically erases all information saved in the device's random-access memory (RAM), which investigators may find useful."
        a laugh "You already know the drill! Here’s the latest riddle."

label riddle_6:
    scene riddle_6
    with fade
    call screen riddle6

    label wrong6:
        show wrong
        h 1 "Uh.... no! Try again." with hpunch
        hide wrong
        call screen riddle6

    label right6:
        scene main building
        a delighted "That's right!"
        a smile1 "PUP has an Olympic-size swimming pool in front of the College of Human Kinetics building, which is used for swimming lessons and intramural swimming competitions."
        a "We must go there now!"

# Location7: PUP Swimming Pool
label location7:
    scene swimming pool
    show loc7
    pause
    a annoyed "And, once again, there is no sign of 5H4D0W! I need your help with this one."
    menu:
        a "What will you do to check if a site’s connection is secure?"
        "Check the SSL Certificate.":
            a sad "Oops! Incorrect answer." with hpunch
            jump correct_loc7
        "Use security tools to evaluate the site.":
            a sad "Oops! Incorrect answer." with hpunch
            jump correct_loc7
        "Check if there is a padlock symbol next to the web address.":
            a sad "Oops! Incorrect answer." with hpunch
            jump correct_loc7
        "All of the above.":
            a laugh "You got it!"
            jump correct_loc7
    label correct_loc7:
        a laugh "All of the choices are right so choosing the latter is the correct one!"
        a normal "If there is a padlock symbol next to the URL, it means that the website is secure. However, even if you see this indicator, you should always be cautious when submitting personal information."
        a smile1 "Check your website's URL if it has \"HTTPS\ \(rather than \"HTTP\") at the beginning of the address."
        a smile2 "This means the website is secure with an SSL certificate. Security tools like antivirus applications installed on a computer can also show if a website is secure or not."
        a angry "5H4D0W duped us once more! I'm running out of patience. Of course, there is another riddle for us to solve."

label riddle_7:
    scene riddle_7
    with fade
    call screen riddle7

    label wrong7:
        show wrong
        h 1 "Uh.... no! Try again." with hpunch
        hide wrong
        call screen riddle7

    label right7:
        scene main building
        a delighted "That's right!"
        a smile1 "The PUP Interfaith Chapel is a nondenominational Christian church that provides a place for students of various faith traditions to meet, meditate, and mingle."
        a "Come on. Time is running!"

# Location8: PUP Interfaith Chapel
label location8:
    scene interfaith chapel
    show loc8
    pause
    a annoyed "Well, 5H4D0W is definitely not here."
    a smug "But I have a feeling that we’re going to catch him soon!"
    a "Source? Trust me bro!"
    menu:
        a "Everyone at the university is saying that they have been receiving friend requests from people they don’t know. What do you think they should do?"
        "Accept the friend request.":
            a sad "Oops! Incorrect answer." with hpunch
            jump correct_loc8
        "Message them and ask if they know you.":
            a sad "Oops! Incorrect answer." with hpunch
            jump correct_loc8
        "Ignore and don't accept their request":
            a laugh "You got it!"
            jump correct_loc8

    label correct_loc8:
        a normal "One tip to stay safe in social media is to be selective with friend requests."
        a "If you don't know the person, decline their friend request because it may be a fake account."
        a laugh "I believe we're getting close to 5H4D0W because he gave us a specific location, the PUP Gymnasium."
        a "I doubt he's telling us the truth, but we should go there right away!"

# Location9: PUP Gymnasium
label location9:
    scene gym
    show loc9
    pause
    a annoyed "Yeah, 5H4D0W deceived us … again. Let’s just answer this question first!"
    menu:
        a "Cybersecurity incident response is a key component to every organization."
        "True":
            a laugh "You got it!"
            jump correct_loc9
        "False":
            a sad "Oops! Incorrect answer." with hpunch
            jump correct_loc9
    label correct_loc9:
        a normal "Incident response is the coordinated and methodical approach to prepare for, identify, contain, and recover from a security event."
        a smile1 "It is a key component because it enables an organization to quickly detect and halt attacks, minimizing damage and preventing future attacks of the same type."
        a laugh "Anyway! The hacker said he is prepared to participate in some sports!"

label riddle_9:
    scene riddle_9
    with fade
    call screen riddle9

    label wrong9:
        show wrong
        h 1 "Uh.... no! Try again." with hpunch
        hide wrong
        call screen riddle9

    label right9:
        scene main building
        a delighted "That's right!"
        a smile1 "The PUP Oval serves as the University's events, assembly, and sports center."
        a "Let's get him!"

# Location10: PUP Oval
label location10:
    scene oval
    show loc10
    pause
    a annoyed "It appears that 5H4D0W has changed his mind."
    a "I just know he's running out of ways to try to trick us."
    a "We must catch him before he tries to escape this school!"
    menu:
        a "Which one of these things is most effective for maintaining your digital privacy?"
        "Covering your computer’s camera.":
            a sad "Oops! Incorrect answer." with hpunch
            jump correct_loc10
        "Not sharing personal information on social media.":
            a laugh "You got it!"
            jump correct_loc10
        "Unsubscribing from all spam emails.":
            a sad "Oops! Incorrect answer." with hpunch
            jump correct_loc10
    label correct_loc10:
        a normal "The best tip that can be applied across the whole spectrum of social networking tools is to don’t overshare."
        a "To maintain your digital privacy, try to keep quiet about anything that you wouldn’t want the world to know."
        a laugh "This includes usernames, aliases, passwords, last names, full-names-as-usernames, pictures, addresses, and other important information."
        a "Here is another question for us to know where 5H4D0W went. Answer it quickly!"

label riddle_10:
    scene riddle_10
    with fade
    call screen riddle10

    label wrong10:
        show wrong
        h 1 "Uh.... no! Try again." with hpunch
        hide wrong
        call screen riddle10

    label right10:
        scene main building
        a delighted "That's right!"
        a smile1 "The great wall of PUP is also known as the “Intramuros of PUP”. It was inspired by the walls of historic Fort Santiago in Intramuros, Manila that gave importance to the history and the country’s heritage."
        a "Don’t lose hope. I think we will be able to catch him!"


# Location11: Intramuros of PUP
label location11:
    scene intramuros
    show loc11
    pause
    a annoyed "5H4D0W not here, but I think we are getting very close!"
    menu:
        a "When you are in public and if a trustworthy network is unavailable, what is the next safest option to access the Internet?"
        "Connect to the public Wi-Fi without a VPN.":
            a sad "Oops! Incorrect answer." with hpunch
            jump correct_loc11
        "Use your mobile carrier to access the Internet.":
            a laugh "You got it!"
            jump correct_loc11
    label correct_loc11:
        a normal "If public Wi-Fi is your only choice and you don't have VPN access, the next safest alternative is to browse the web through your cell carrier."
        a "In using public Wi-Fi, use a Virtual Private Network (VPN) app to minimize security risks. This app hides your IP address and encrypts any data you transfer over the internet."
        a laugh "I have a feeling we’re close to finding 5H4D0W because it looks like he scribbled this riddle quickly."

label riddle_11:
    scene riddle_11
    with fade
    call screen riddle11

    label wrong11:
        show wrong
        h 1 "Uh.... no! Try again." with hpunch
        hide wrong
        call screen riddle11

    label right11:
        scene main building
        a delighted "That's right!"
        a smile1 "The Engineering and Science Research Center is a newly constructed building and was inaugurated last January 7, 2019."
        a "To the Engineering and Science Research Center, we go!"

# Location12: Engineering and Science Research Center
label location12:
    scene research center
    with dissolve
    a smug "I can already see 5H4D0W from here! But for the last time, we need to answer this question."
    menu:
        a "5H4D0W locked out the users and encrypted their computer files and data in the Research Center. He is holding it hostage until the users agree to pay him. What is this practice called?"
        "Ransomware":
            a laugh "You got it!"
            jump correct_loc12
        "Browser Hijacker":
            a sad "Oops! Incorrect answer." with hpunch
            jump correct_loc12
        "Brute Force":
            a sad "Oops! Incorrect answer." with hpunch
            jump correct_loc12
    label correct_loc12:
        a normal "Ransomware holds your files, keeping you from your documents, photos, and financial information."
        a "Those files are still on your computer, but the malware has encrypted your device, making the data inaccessible."
        a smile2 "To protect your computer from ransomware, back up your data regularly, install reliable ransomware protection software, and keep your operating system, apps, and security software up to date."

menu catch:
    "Catch 5H4D0W!":
        jump lastlocation

label lastlocation:
    scene research center
    show loc12
    pause
    h 1 "Well, you found me, so I guess I am now busted. You guys are just too smart for me!"
    a delighted "Thank you so much for your help, future detective! We wouldn't be able to catch him without your cybersecurity knowledge and skills. Until we meet again!"

# This ends the game.

return
