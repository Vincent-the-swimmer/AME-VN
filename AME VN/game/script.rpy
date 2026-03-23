# Declare characters used by this game. The color argument colorizes the
# name of the character.




# declaring animation presets

transform quick_jump:
    yoffset 0
    zoom 1.0
    linear 0.08 yoffset -40 zoom 1.04
    linear 0.08 yoffset 0 zoom 1.0

transform descend_from_top:
    yoffset -500
    alpha 0.0
    linear 0.40 yoffset 0 alpha 1.0

transform tossed_into_portal_right:
    xoffset 0
    yoffset 0
    rotate 0
    zoom 1.0
    alpha 1.0
    linear 0.04 xoffset -20 rotate -4
    linear 0.20 xoffset 900 yoffset -120 rotate 16 zoom 0.85 alpha 0.0

define whiteflash = Fade(0.05, 0.0, 0.20, color="#ffffff")

transform shake_hard:
    xoffset 0
    yoffset 0
    linear 0.02 xoffset -16 yoffset 6
    linear 0.02 xoffset 16 yoffset -6
    linear 0.02 xoffset -12 yoffset 4
    linear 0.02 xoffset 12 yoffset -4
    linear 0.02 xoffset 0 yoffset 0

# Fireball

transform slow_house_zoom:
    zoom 1.0
    xalign 0.5
    yalign 0.5
    linear 0.7 zoom 1.08


transform fireball_trail(
    start_x=0.82,
    start_y=-0.56,
    end_x=-0.06,
    end_y=0.42,
    start_zoom=0.55,
    end_zoom=1.55,
    start_rot=34,
    end_rot=34,
    fade_in=0.03,
    travel_time=0.78
):
    xpos start_x
    ypos start_y
    zoom start_zoom
    rotate start_rot
    alpha 0.0

    parallel:
        linear fade_in alpha 1.0

    parallel:
        easein_quad travel_time xpos end_x ypos end_y zoom end_zoom rotate end_rot


transform bg_darken_in:
    alpha 0.0
    linear 0.20 alpha 0.12
    linear 0.30 alpha 0.24
    linear 0.25 alpha 0.34


screen fireball_darkening():
    zorder 90

    # Main dimming layer: translucent, not opaque.
    add Solid("#000000") at bg_darken_in

    # Very subtle warm tint so it doesn't feel like a plain fade-to-black.
    add Solid("#2a1200") at bg_darken_in


screen fireball():
    zorder 100

    fixed:
        at fireball_trail(
            start_x=0.82,
            start_y=-0.56,
            end_x=-0.06,
            end_y=0.42,
            start_zoom=0.34,
            end_zoom=1.40,
            start_rot=34,
            end_rot=34,
            fade_in=0.03,
            travel_time=0.75
        )

        text "●":
            xpos 150
            ypos -210
            size 150
            color "#ff5a0018"

        text "●":
            xpos 120
            ypos -165
            size 135
            color "#ff6a0022"

        text "●":
            xpos 92
            ypos -126
            size 120
            color "#ff7a0030"

        text "●":
            xpos 68
            ypos -92
            size 108
            color "#ff8a0044"

        text "●":
            xpos 48
            ypos -62
            size 96
            color "#ff980066"

        text "●":
            xpos 30
            ypos -38
            size 84
            color "#ffb02088"

        text "●":
            xpos 14
            ypos -18
            size 94
            color "#ff6a0038"

        text "●":
            xpos 0
            ypos 0
            size 78
            color "#ff9d00dd"

        text "●":
            xpos 6
            ypos 6
            size 58
            color "#ffd15acc"

        text "●":
            xpos 14
            ypos 14
            size 36
            color "#fff4cc"

# Game starts here
label start:
    

    "I knew something strange was happening. It was impossible not to notice."

    "Nobody ever talked about it, but everybody felt it. The strange feeling that something awful was coursing through our home."

    "Nobody knew what it was… but now I do."

    "Because the sight I’m seeing outside my window… THAT is definitely not normal."

    play music "audio/beatdown.mp3"
    play sound "audio/bang.mp3"
    play sound "audio/rumble.mp3"
    show bg neighborhood with vpunch

    show hina1 sweatx at left with dissolve

    h "How?! Kai, how did he get so strong? I thought we kept him in check this time!"

    # "[Kai, adjusting his glasses, appears]"
    show kai1 adjustr behindl at right with dissolve
    k "I tracked all of his movements ever since we arrived here. There is no justification."

    # "[VFX" "{i}shaking{/i}]
    # {i}rumbling{/i}]
    # {i}Cole descending{/i}]"

    with vpunch
    play sound "audio/rumble.mp3"
    show cole1 at center, descend_from_top
    
    c "..."
    hide cole1
    hide hina1
    hide kai1
    scene bg neighborhood at slow_house_zoom
    show screen fireball_darkening
    "{i}Wait, wait, why are they getting closer? Why are they flying toward my house? What am I even supposed to do here?! I can’t run away from this… thing!{/i}"
    show screen fireball
    pause 0.70
    hide screen fireball
    hide screen fireball_darkening
    scene bg neighborhood with Fade(0.03, 0.0, 0.18, color="#ffcc88")
    scene bg indoors with hpunch
    # "[VFX" "{i}Bright ball of fire coming down from sky (use drop shadow to darken the background around the area of the blast).{/i} {i}Zoom in on one of the houses.{/i}]
    # Ame Universe – Indoors]
    # {i}big bang{/i}]
    # {i}fade Ame’s destroyed house with Ame (scared expression, right side of screen), Hina (angry expression, left side of screen), and Kai (nervous expression, next to Hina){/i}]"
    
    scene bg indoors with whiteflash

    show hina1 angry grit angryx pointl at left, descend_from_top
    show kai1 worry adjustr behindl sweatx at center, descend_from_top
    show ame1 sad grit chestr chestl sweatx at right with dissolve:
        xalign 0.8
    
    a "Heh…? Uh… Uh… oh god…" 
    a "You guys couldn’t keep this outside?"
    # "[VFX" "{i}Cole moves in from the left, Hina and Kai come in front of Ame on the right side of the screen. Switch Hina to a nervous expression.{/i}]"

    show hina1 angry grit angryx pointl zorder 3 with MoveTransition(0.25):
        xalign 0.6
    show kai1 worry adjustr behindl sweatx zorder 2 with MoveTransition(0.25):
        xalign 1.0
    show ame1 sad grit chestr chestl sweatx with dissolve:
        xalign 0.8

    show cole1:
        xalign -0.1, descend_from_top

    c "You two refuse to die… such a pitiful struggle."

    a "Die?! Huh? If you want to kill each other, get out of my house first!"

    c "Oh well… time to finish up."

    h "Screw you!"


    "{i}Oi! I’m not a piece of furniture! Stop ignoring me! Why do I have to be here for this?!{/i}"

    # "[VFX" "{i}shaking{/i}]
    with vpunch
    # {i}rumbling{/i}]"

    k "I’m sorry you got caught in the crossfire like this, young one…"

    "{i}I don’t care about your apology, just get out of my house. God, my insurance rate is gonna go crazy if I survive this…{/i}"

    show cole1 blueangry with dissolve
    c "..."

    # "[VFX" "{i}shaking intensifies{/i}]"
    with vpunch 

    h "I’m sorry, kid… I didn’t mean to drag you and your home into this mess. I’m so, so sorry… I hope the next life is kind to you."

    hide hina1 
    hide kai1
    hide cole1
    hide ame1
    show ame1 sad grit chestr chestl at center with dissolve
    a "Wait, the next life? No… please…"
    stop music
    a "...I don't want to die."

    # "[VFX" "{i}light fills the screen{/i}]
    # {i}music stops{/i}]"

    # "[Scene 3" "Spirit Realm]"
    scene bg spirit_realm with fade
    # "[VFX" "Light recedes, Spirit Realm background, Hina (angry) and Kai (neutral)]"

    show hina1 angry grit angryx pointl at left with dissolve

    h "Another world… gone… AHHHHH! We keep losing! Why? Why? Why?!!!!!"

    show kai1 worry frown adjustr behindl sweatx at right with dissolve

    k "Not much we can do now… we’re stuck here for a while."

    play music "audio/grandeur_theme.mp3"

    h "Kai!!! You should be mad too! That kid just died because we couldn’t beat Cole!"

    k "I am! But– wait a minute…"

    # "[VFX" "{i}fade to CG1 – Hina and Kai looking at Ame, laying unconscious on the floor{/i}]
    # Building Grandeur Theme]"
    

    k "They’re here… but that’s impossible. I’ve never seen anything like this before."

    h "That doesn’t matter! We need to help them!"

    k "I can wake them up."

    # "[VFX" "Low, pulsing glow]
    show flash:
        alpha 0.0
        linear 0.75 alpha 1.0  
        linear 0.75 alpha 0.0   
    # [Spirit Realm Background with Hina (nervous), Kai (calm), and Ame (confused)]"
    
    hide hina1
    show hina1 sweatx at left
    show ame1 side open dropsx at center
    "{i}Heh? Where the hell am I? What even happened just now? I was at my house… then those people crashed into my house, and then… I died, didn’t I? I’m dead. So… what is this place?{/i}"

    a "Is this Heaven?"
    # "[Stop Music]"
    stop music

    k "This isn’t Heaven. It’s the Spirit Realm. Hina and I live here while building up power. It’s a waiting room, essentially. As for what happened…"

    # "[VFX" "quickly expand and reduce Hina’s size to give the illusion of jumping]"

    show hina1 smile sparklex at left, quick_jump

    h "YOU’RE ALIVE!"

    # "[Music" "Quirky Theme]"
    play music "audio/quirky_theme.mp3"

    show ame1 smile sparklex

    a "I’m alive? Thank god… after that guy told me it wasn’t Heaven, I was afraid it was the other place."

    show kai1 adjustr at right

    k "Well, we did all die, kind of, but not actually because we get resurrected when we end up here by our divine energy. I gave some of that to you. What’s your name?"

    a "I’m Ame… you two are…"

    h "I’m Hina, and this guy over here is Kai! You’re Ame, yeah? What an interesting name."

    "{i}At the very least, it doesn’t seem like these two want to kill me.{/i}"

    a "Thank you for reviving me. So… what exactly are you two?" 
    a"You aren’t normal, right? With all this divine energy and whatnot?"

    show hina1 tongue sparklex at left

    h "I’m perfectly normal, thank you very much!"

    show kai1 adjustr behindl at right

    k "We’re gods. We went down to your world to protect it from… I guess you could call it a plague that was trying to infect your world."

    k "The other person you saw, Cole, is responsible for spreading it."

    show hina1 angry grit angryx pointl at left

    h "That’s because he’s pulled a fast one to get way too strong now! He’s impossible to stop!"

    show kai1 frown
    k "That’s quite enough, Hina."

    hide hina1
    show hina1 smirk at left
    stop music
    h "Uh oh, he’s mad."

    # "[Music" "Sad Theme]"
    play music "audio/sad_theme.mp3" fadeout 0.5 fadein 0.5

    show hina1 sad frown sweatx at left
    show ame1 sad grit chestr chestl at center

    a "Wait, so… what’s happened to my world? To my friends? My family? Are they… dead? Did the plague kill them?"

    h "Something like that… pretty close."

    a "Pretty close… meaning they’re not dead. Could you send me back? You’re gods, right?" 
    a "You were able to bring me back to life. Can you put me back in my world?"

    k "That’s… that’s not possible. I’m really sorry, Ame, but even if we could send you back… you wouldn’t want to see it."

    a "I need to know. I can’t… I can’t just not know what happened to them."

    h "I understand…"

    # "[VFX" "Move Hina closer to Ame]
    show hina1 sad frown sweatx at left with move:
        xalign 0.1
    # General Conversation]"

    k "What are you doing, Hina? Don’t tell me you’re actually going to show them…?"

    h "They deserve to know. It’s the least we can do considering we’re the reason why they can’t be amongst the people they care about."

    k "I’m not sure you should do this… but I suppose you could form a mind link with Ame."

    stop music

    a "A mind link?"

    play music "audio/quirky_theme.mp3"

    k "She’ll have access to your mind and vice versa. I mean, it sounds kind of scary, but like… Hina won’t do anything bad to your mind!"

    k "Well… I guess she is kind of rash, but her heart’s usually in the right place! But I guess…"

    h "Kai, shut up!"

    h "Ahem… The mind link will let me show you what happens to dimensions taken over by that plague. It can also do other things, but I won’t abuse it. You have my word."

    a "...you’ll have unrestricted access to my mind? I’m not sure I like the idea of that."

    "{i}Listen, it’s not like I have any especially weird thoughts or anything… seriously! I’m a normal person. But still, wouldn’t a normal person hate to have a relative stranger have access to every single thought of theirs? Seriously though, I’m normal. Very normal.{/i}"

    h "It’s the only way I can show you what you want to see. It’s either this, or you don’t see it."

    "{i}I may not like the idea of having a stranger going through my mind, but…{/i}"


    #Ame hesistant, what does she look like?
    play music "audio/grandeur_theme.mp3" fadeout 0.5 fadein 0.5

    a "Alright...I need to know. I consent to the mind link. How does this work?"

    h "Well…"

    # "[VFX" "Insert CG 2 (Hina and Ame holding hands)]"

    scene cg2_hinaame1 with dissolve

    a "Heh?!"

    h "I need to focus."

    scene cg2_hinaame2 with dissolve

    a "It’s a little warm…"

    h "Well, I am the God of the Sun… now quiet down."

    scene cg2_hinaame2 with whiteflash
    scene cg2_hinaame2 with whiteflash

    scene cg2_hinaame3 with whiteflash

    stop music

    a "..."

    # "[VFX" "Slowly fade to black, and then do a quick flash of white and bring back the visuals with a little shaking effect.]
    # Sad Theme]"
    play music "audio/sad_theme.mp3"

    
    a "That’s… that’s what you’re saying happened to the people I care about?" 

    a "No… no… I don’t… I don’t want to believe you…"

    h "But you do believe me. Because you know it’s true. We can’t send you back there."

    "{i}If I wasn’t in front of people I don’t know, I’d be on the ground sobbing. Of all the possibilities I thought of, including the death of every single person in my home…{/i}"
    
    "{i}This is worse.{/i}"
    
    "{i}Just thinking about it makes me want to vomit… but weirdly enough, I’m keeping it together.Maybe it’s because these two gods are standing in front of me… but I’m calm. I’m angry, I’m disgusted… but I’m calm.{/i}"

    scene bg spirit_realm with dissolve

    # "[Music" "Building Grandeur Theme]"
    play music "audio/grandeur_theme.mp3" fadein 0.5

    show ame1 neutral chestr sparklex
    a "So the two of you… you just go around worlds chasing this plague? Fighting it?"

    show kai1 adjustr behindl at right

    k "There’s a method by which we can see which world it’s beginning to go to, so we build enough energy to open a gate that allows us to enter." 
    
    k "Unfortunately, that takes a lot of time. Lately, by the time we arrive… there’s not much we can do."

    show hina1 angry grit angryx at left
    h "Cole’s too strong, and he gets into worlds faster than we can. It takes too long for us to build enough energy to construct a dimensional gate capable of handling our power."

    show hina1 sad frown
    h "I seriously wish we could’ve saved your world, Ame. I’m so sorry."

    a "Don't apologize. It's not because of you."

    "{i}I’m not sure I can even process what’s going through my mind right now, but I do think I can trust these two…{/i}" 
    
    "{i}I’m willing to give them grace and go along with them. They saved my life, after all.{/i}"

    k "Anyway, this war is our responsibility, Ame. You don’t need to worry about it. What would you like to do?"

    show hina1 smile pointl
    h "You can’t go back to your world, but we could theoretically send you to a new one. Give you an opportunity to start a new life separated from all this chaos."

    h "You shouldn’t stay here, at the very least. There’s no point. I recommend going to a new world and living out whatever dreams you had."

    "{i}That’s a pretty good deal I’m being offered. Almost too good to be true. Straight out of a fictional story where I’d get the opportunity to live the way I want.{/i}"

    "{i}I spent so many nights dreaming about a chance to get that kind of life… of course I should take it. I really should. It makes no sense not to! But…{/i}"

    a "...I can’t. I can’t restart my life and turn a blind eye to what happened in my world."

    k "Huh? Ok… well… what are you going to do then? Staying here won’t do anything."

    a "Well… is there anything I {i}can{/i} do to help?"

    # "[Music Stop]"
    stop music

    k "No."

    play music "audio/quirky_theme.mp3"

    show hina1 smirk
    h "Yeah, there is."

    show kai1 angry frown behindl angryx
    k "We are NOT sending them in there alone!"

    show hina1 wink smile
    h "They won’t be alone, they have my mind link."

    show ame1 angry grit angryx
    a "You two are talking like I’m not here again."

    show kai1 worry nervous adjustr behindl dropsx
    k "Oh, uh… sorry."

    # "[Music" "Building Grandeur Theme]"
    play music "audio/grandeur_theme.mp3" fadein 0.5

    show hina1 smirk
    h "Ame, you want to help fight the war, right? How do you feel about giving us a little head start?"
    
    show ame1 neutral chestr sparklex
    a "A head start?"

    h "We know what world Cole is hitting next. We may not be able to go ourselves, but you… you can make the trip quite easily."

    k "We know literally nothing about the world that we’d be sending you into."

    h "But we can learn via your mind link contract with me! It’ll allow us to communicate, even across dimensions!"

    h "If we have intel and somebody working on countering the plague before we arrive, we’ll be far more equipped to take care of Cole in this world!"

    # "[Music" "Stop]"
    stop music

    "{i}This is like watching two kids fight over who gets to play with a toy… but why am I the toy???{/i}"

    # "[Music" "Continue]"
    play music "audio/grandeur_theme.mp3"

    h "Anyway, the more time we waste, the less time you have to make a change. Decide, Ame. Hurry up now."

    "{i}This is all coming so fast, I don’t know what I’m meant to do… let’s just slow this down.{/i}"

    a "...ok, I’ll–"

    h "Alright!"

    scene bg spirit_realm_portal with whiteflash
    show ame1 neutral chestr sparklex at center
    show hina1 smirk at left
    show kai1 worry nervous adjustr behindl dropsx at right
    with whiteflash
    "{i}Heh??????{/i}"

    k "Wait!--"

    # "[aggressively flick the background and quickly have Ame fly toward a portal that appears.]"
    show hina1 smirk at left, quick_jump
    show ame1 side grit chestr dropsx at center, tossed_into_portal_right
    h "Stay in touch! Talk to you soon!"
return
