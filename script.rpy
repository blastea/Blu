label main_menu:
return
image picture_1 = "namelanguage.png"
image picture_2 = "walkinghome.png"
image picture_3 = "blumeet.png"
image picture_4 = "bluwrong.png"
image picture_5 = "room.png"
image picture_6 = "deathonly.png"
image picture_7 = "cityscene.png"
image picture_8 = "bluhelp.png"
image picture_9 = "sky.png"
image picture_10 = "deathscene.png"
image picture_11 = "end1.png"
image picture_12 = "end2.png"
image picture_13 = "scenebed.png"
image picture_14 = "scenedie.png"
image picture_15 = "daylight.png"
image picture_16 = "space.png"
image picture_17 = "space2.png"
image picture_18 = "space3.png"
image picture_19 = "space4.png"
image picture_20 = "space5.png"


define b = Character("Blu", color="#0012d8")
define m = Character("Mortis", color="#000f24")

label start:
    
    scene picture_1

    $ player_name = renpy.input("What is your name?")

    $ player_name = player_name.strip()

# The phrase in the brackets is the text that the game will display to prompt 
# the player to enter the name they've chosen.
# The .strip() instruction removes any extra spaces the player 
# may have typed by accident.

    scene picture_2

    play sound "lightrain.wav" fadein 2.5 volume 0.2

    b "Another rainy night."
    
    "*She walks down the streets near my apartment, they seem different tonight. The lights dimmer, the sky darker with rain clouds*"

    b "It's been days since I left my room, I almost forgot what it was like in the world."

    b "I like to walk along the streets when the city is asleep to find peace of mind."

    b "Especially on a lonely night like this. The rain gives me a sense of calm, almost like a friend." 

    b "Otherwise I feel alone."

    b "Tonight the air is cold."

    scene picture_3

#question 1 & dialogue --------------------------------------------------------------------------------------------------

    b "Do you ever feel alone, %(player_name)s?"

#choice 1

    menu: 
        "Yes.":
            jump Yes1
        "No, you are alone.":
            jump No1
        "Remain silent":
            jump Silent1

label Yes1:

    show picture_2

#path 1------------------------------------------------------------------------------------------------------------------

    b "Hmm."

    stop sound fadeout 2.5

    b "I'm glad I'm not alone then."

#rain sounds stop, still path 1

    b "The rain has settled."

    b "It's time to go home."

    jump path1

#choice 1.2 for q1------------------------------------------------------------------------------------------------------

label No1:
    
    show picture_4

    b "Oh, okay. I guess that's just me then."

    b "Sorry for asking dumb questions."
    
    "*She takes a deep breath and pulls out her phone. the time reads 12:03."

    stop sound fadeout 2.5

    b "It's getting late, time to go home."

    jump path1

#choice 1.3 -------------------------------------------------------------------------------------------------------------

label Silent1:

    show picture_4

    b "Don't worry, you don't have to pretent like you understand."

    b "Sometimes I don't even understand what I'm feeling."

    b "At least you're here."

    b "*She takes a deep breath and pulls out her phone. the time reads 12:03.*"

    stop sound fadeout 2.5

    b "It's getting late, time to go home."

    jump path1

#-----------------------------------------------------------------------------------------------------------------------
#next scene should be room
label path1:
    play music "horrorloop2.wav" fadein 2.5 volume 0.1
   
    show picture_5

    b "Home again. The only place I feel safe, where I can be me."

    b "Tonight feels different."

    b "Tonight feels eerie. Like something is wrong but I don't know what"

    b "That doesn't matter now though... I am tired."

    b "But I have felt so tired so often, a void that cannot be filled no matter how long I lie down and let myself fade through the night alone, like a spirit comdemned to one place."

    b "Hours have turned to days that I lie alone."

    b "Deep down, I want to change."

    b "Would you stay and keep me company for a while tonight, %(player_name)s?"

    b "It would mean more than you could know."

    menu:
        "Yes, I wouldn't want you to be in the blues all night.":
            jump Yes2
        "Not this time, sorry.":
            jump No2
        "Remain Silent":
            jump Silent2

#choice 2.1-------------------------------------------------------------------------------------------------------------------

label Yes2:

    b "Thank you."

    b "I want to take you somewhere."

    "*She walks out of her apartment door, and up the stairs to the roof.*"

    show picture_7

    b "Hmm."

    b "The air is crisp tonight."

    "The normal sounds of cars honking and the sirens of police are absent tonight. It is only the sound of silence and the emptiness of solitude."

    b "It's nice to have company now and then, though."

    jump pathcontinue

#choice 2.2-------------------------------------------------------------------------------------------------------------------

label No2:

    b "I see."

    b "Another night alone then. Can't hurt."

    b "It was nice meeting you at least."

    b "Goodbye, %(player_name)s."

    show picture_10

    m "Time isn't a friend."

    stop music fadeout 2.5
    
    play sound "death2.wav" volume .2
    
    queue sound "death.wav" volume .2
    
    m "And you have run out."

#death sound

    jump end2
#choice 2.3-------------------------------------------------------------------------------------------------------------------

label Silent2:

    show picture_6

    m "Silence will only get you so far."

    m "Silence can be a weapon."

    stop music fadeout 2.5

    
    play sound "death2.wav" volume .2
  
    queue sound "death.wav" volume .2

    m "Your silence is their end."

#death sound and death scene

    jump end2

#------------------------------------------------------------------------------------------------------------------------------
label pathcontinue:

    b "I just feel like I'm running out of time."

    b "Do you ever wonder how your life will end?"

    b "We're told theres so much to do in such little time."

    b "And that the only thing that stops us is ourselves."

    b "I don't feel like I am enough. Often I don't feel like I am anything."

    b "Something feels wrong when nothing is."

    b "Nothing feels right when everything is."

    b "I live every night looking at this city, feeling like I contribute nothing to the concrete jungle."

    b "We are told to look at the little things, the trees, the parks, the ponds."

    b "The vibrant birds, the cool air going through your hair."

    b "The little things."

    b "The little things are what makes life, but in the end, what have I done?"

    b "I work, eat, and I sleep. I do it over and over and I look and I see an absence of happiness."

    b "Is that all that there is? Friends come and go, love is gained and lost, and I am left riding a never ceasing wave in the ocean going up and down."

    b "And it seems I am alone."

    show picture_9

    b "Every night I take a deep breath and look to the sky."

    b "Stars in the night sky."

    b "Theres so much to the universe that makes us so little. Life, so small."

    b "I wonder if somewhere, far away, there is someone looking to the sky thinking these same thoughts, living my same life."

    b "I don't want to feel this way anymore."

    b "*She catches herself rambling, and stares blankly at you.*"

    b "I'm sorry."

    b "Anyways, time to get settled for the night."

    "*She walks back down the stairs, into the small room she calls home.*"

    show picture_5

    b "Thank you again for staying."

    b "It's easy to feel alone sometimes."

    show picture_13

    b "I don't really do much to keep myself distracted. Games usually keep me feeling happy for a litte while I guess."

    b "I can only really afford cable though, not much to watch."

    "*She picks up the remote and fidgets with the buttons, looking intently at the remote.*"

    b "I should probably do more with myself. It's just hard sometimes."

    show picture_5

    "*She puts it back down, her tone seemingly changed as she looks around her room.*"

    stop music fadeout 2.5

    b "What would you do, if you were me?"

    menu:
        "Keep going.":
            jump yes3
        "Give up.":
            jump no3
    
#choice 3.1---------------------------------------------------------------------------------------------------------------------
label yes3:

    play music "scifitrack.wav" fadein 2.5 volume 0.1

    b "Hmm."

    b "Theres always something to live for, I suppose. Even the little things."

    b "Tomorrow is a new day."

    b "A fresh start."

    b "Thank you, %(player_name)s."

    b "Goodnight."

    show picture_15

    stop music fadeout 2.5

    "Life doesn't last forever."

    jump end1
#choice 3.2---------------------------------------------------------------------------------------------------------------------
label no3:

    "Enter Blu's head..."

    play sound "horrorambient.wav" fadein 1.5 volume 0.2

    show picture_16

    b "Everything is going to be okay."

    show picture_17

    b "Everything is going to be okay."

    show picture_18

    b "Everything is going to be okay."

    show picture_19

    b "Everything is going to be okay."

    show picture_20

    b "..."

    b "Sometimes life just deals you a bad hand."

    b "..."

    b "Sometimes you're just unlucky."

    b "..."

    b "Sometimes you won't understand yourself."

    b "..."

    b "Sometimes it isn't fair."

    b "..."

    b "Sometimes things just come to an end."

    b "..."

    "Back to reality..."

    stop sound fadeout 2.5

    show picture_14

    b "I thought so."

    b "Maybe its not worth it."

    b "Maybe this is the end."

    b "*She looks around her room, one last time. With a blank expression, she walks to the roof of her apartment.*"
    
    show picture_8

    b "Everyone sees their last day someday."

    "*She looks down, and you take your final leave.*"
    
    b "Goodbye, %(player_name)s."

    show picture_10

    play sound "death2.wav" volume .2
 
    queue sound "death.wav" volume .2

    m "OMNES VIAS FINIS"

#death sound and end

    jump end2

#end script

label end1:

    play music "goodend.wav" fadein 2.5 volume 0.1

    show picture_11

    "The End."

    show picture_1

    "Thank you for playing."

    "I appreciate your time, and look forward to seeing you again soon."

    "Made by JW."

    stop music fadeout 2.5

return

#----------------------------------------------------------------------------------------------------------------------------------

label end2:

    show picture_12

    play sound "lightrain.wav" fadein 3.5 volume 0.1

    "The End."

    show picture_1

    "Thank you for playing."

    "I appreciate your time, and look forward to seeing you again soon."

    "Made by JW."

    return