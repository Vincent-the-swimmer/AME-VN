# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define cole = Character("Cole")
define ame = Character("Ame")
define hina = Character("Hina")

# The game starts here.

label start:

    play music "audio/battle_theme.mp3"

    "I knew something strange was happening. It was impossible not to notice."

    "Nobody ever talked about it, but everybody felt it. The strange feeling that something awful was coursing through our home."

    "Nobody knew what it was… but now I do."

    "Because the sight I’m seeing outside my window… THAT is definitely not normal."

    play sound "audio/bang.mp3"
    play sound "audio/rumble.mp3"
    show bg neighborhood with vpunch

    show hina nervous at left

    "Hina" "“How?! Kai, how did he get so strong? I thought we kept him in check this time!”"

    # "[Kai, adjusting his glasses, appears]"
    show kai normal at right

    "Kai" "“I tracked all of his movements ever since we arrived here. There is no justification.”"

    # "[VFX" "{i}shaking{/i}]
    # {i}rumbling{/i}]
    # {i}Cole descending{/i}]"

    with vpunch
    play sound "audio/rumble.mp3"
    show cole1 normal at center with dissolve
    "Cole" "“...”"

    # "[VFX" "{i}Bright ball of fire coming down from sky (use drop shadow to darken the background around the area of the blast).{/i} {i}Zoom in on one of the houses.{/i}]
    # Ame Universe – Indoors]
    # {i}big bang{/i}]
    # {i}fade Ame’s destroyed house with Ame (scared expression, right side of screen), Hina (angry expression, left side of screen), and Kai (nervous expression, next to Hina){/i}]"

    show bg indoors with fade

    show ame scared at right
    show hina angry at left
    show kai nervous at center

    
    "Ame" "Heh…? Uh… Uh… oh god…" 
    "Ame scared nervous" "You guys couldn’t keep this outside?"
    # "[VFX" "{i}Cole moves in from the left, Hina and Kai come in front of Ame on the right side of the screen. Switch Hina to a nervous expression.{/i}]"

    "Cole" "“You two refuse to die… such a pitiful struggle.”"

    "Ame nervous angry" "“Die?! Huh? If you want to kill each other, get out of my house first!”"

    "Cole" "“Oh well… time to finish up.”"

    "Hina angry" "“Screw you!”"

    "Ame angry" "“Oi! I’m not a piece of furniture! Stop ignoring me!”"

    # "[VFX" "{i}shaking{/i}]
    # {i}rumbling{/i}]"

    "Kai" "I’m sorry you got caught in the crossfire like this, young one…"

    "Ame" "“I don’t care about your apology, just get out of my house. God, my insurance rate is gonna go crazy…”"

    "Cole blue flames, angry" "..."

    # "[VFX" "{i}shaking intensifies{/i}]"

    "Hina" "“I’m sorry, kid… I didn’t mean to drag you and your home into this mess. I’m so, so sorry… I hope the next life is kind to you.”"

    "Ame scared" "“Wait, the next life? No… please…”"

    # "[VFX" "{i}light fills the screen{/i}]
    # {i}music stops{/i}]"

    # "[Scene 3" "Spirit Realm]"

    # "[VFX" "Light recedes, Spirit Realm background, Hina (angry) and Kai (neutral)]"

    "Hina" "“Another world… gone… AHHHHH! We keep losing! Why? Why? Why?!!!!!”"

    "Kai" "“Not much we can do now… we’re stuck here for a while.”"

    "Hina eyes watering" "“Kai!!! You should be mad too! That kid just died because we couldn’t beat Cole!”"

    "Kai" "“I am! But– wait a minute…”"

    # "[VFX" "{i}fade to CG1 – Hina and Kai looking at Ame, laying unconscious on the floor{/i}]
    # Building Grandeur Theme]"

    "Kai" "“They’re here… but that’s impossible. I’ve never seen anything like this before.”"

    "Hina" "“That doesn’t matter! We need to help them!”"

    "Kai" "“I can wake them up.”"

    # "[VFX" "Low, pulsing glow]
    # [Spirit Realm Background with Hina (nervous), Kai (calm), and Ame (confused)]"

    "Ame" "“Where… where am I? I was at my house… and the wall broke, and… and… there were three people… what happened? Didn’t I… didn’t I die? Is this Heaven?”"

    # "[Stop Music]"

    "Kai" "“This isn’t Heaven. It’s the Spirit Realm. Hina and I live here while building up power. It’s a waiting room, essentially. As for what happened…”"

    # "[VFX" "quickly expand and reduce Hina’s size to give the illusion of jumping]"

    "Hina excited" "“YOU’RE ALIVE!”"

    # "[Music" "Quirky Theme]"

    "Ame" "“I’m alive? Thank god… after that guy told me it wasn’t Heaven, I was afraid it was the other place.”"

    "Kai adjusting glasses" "“Well, we did all die, kind of, but not actually because we get resurrected when we end up here by our divine energy. I gave some of that to you. What’s your name?”"

    "Ame" "“I’m Ame… you two are… Hina and Kai, right?”"

    "Hina excited expression" "“Bingo! Good job paying attention! You’re Ame, huh? What an interesting name.”"

    "Ame" "“Thank you for reviving me. So… what exactly are you two? You aren’t normal, right? With all this divine energy and whatnot?”"

    "Hina puffy cheeks" "“I’m perfectly normal, thank you very much!”"

    "Kai normal" "“We’re gods. We went down to your world to protect it from… I guess you could call it a plague that was trying to infect your world.”"

    "Hina angry" "“That’s because he’s pulled a fast one to get way too strong now! He’s impossible to stop!”"

    "Kai annoyed" "“That’s quite enough, Hina.”"

    "Hina nervous" "“Uh oh, he’s mad.”"

    # "[Music" "Sad Theme]"

    "Ame scared" "“Wait, so… what’s happened to my world? To my friends? My family? Are they… dead? Did the plague kill them?”"

    "Hina dreary" "“Something like that… pretty close.”"

    "Ame" "“Pretty close… meaning they’re not dead. Could you send me back? You’re gods, right? You were able to bring me back to life. Can you put me back in my world?”"

    "Kai" "“That’s… that’s not possible. I’m really sorry, Ame, but even if we could send you back… you wouldn’t want to see it.”"

    "Ame sad" "“I need to know. I can’t… I can’t just not know what happened to them.”"

    "Hina" "“I understand…”"

    # "[VFX" "Move Hina closer to Ame]
    # General Conversation]"

    "Kai" "“What are you doing, Hina? Don’t tell me you’re actually going to show them…?”"

    "Hina" "“They deserve to know. It’s the least we can do considering we’re the reason why they can’t be amongst the people they care about.”"

    "Kai" "“I’m not sure you should do this… but I suppose you could form a mind link with Ame.”"

    "Ame" "“A mind link?”"

    "Kai" "“She’ll have access to your mind and vice versa. I mean, it sounds kind of scary, but like… Hina won’t do anything bad to your mind! Well… I guess she is kind of rash, but her heart’s usually in the right place! But I guess…”"

    "Hina " "“Kai, shut up!”"

    "Hina" "“Ahem… The mind link will let me show you what happens to dimensions taken over by that plague. It can also do other things, but I won’t abuse it. You have my word.”"

    "Ame" "“...you’ll have unrestricted access to my mind? I’m not sure I like the idea of that.”"

    "Hina" "“It’s the only way I can show you what you want to see. It’s either this, or you don’t see it.”"

    "Ame hesitant" "“Alright...I need to know. I consent to the mind link. How does this work?”"

    "Hina" "“Well…”"

    # "[VFX" "Insert CG 2 (Hina and Ame holding hands)]"

    "Ame" "“Heh?!”"

    "Hina" "“I need to focus.”"

    "Ame" "“It’s a little warm…”"

    "Hina" "“Well, I am the God of the Sun… now quiet down.”"

    "Ame" "“...”"

    # "[VFX" "Slowly fade to black, and then do a quick flash of white and bring back the visuals with a little shaking effect.]
    # Sad Theme]"

    "Ame terrified" "“That’s… that’s what you’re saying happened to the people I care about?”
    “No… no… I don’t… I don’t want to believe you…”"

    "Hina slightly sad" "“But you do believe me. Because you know it’s true. We can’t send you back there.”"

    "Ame sad" "“I see… that damn plague.”"

    "Ame curious" "“So the two of you… you just go around worlds chasing this plague? Fighting it?”"

    "Kai normal" "“There’s a method by which we can see which world it’s beginning to go to, so we build enough energy to open a gate that allows us to enter. Unfortunately, that takes a lot of time. Lately, by the time we arrive… there’s not much we can do.”"

    "Hina frustrated" "“Cole’s too strong, and he gets into worlds faster than we can. It takes too long for us to build enough energy to construct a dimensional gate capable of handling our power."

    "Hina sad" "“I seriously wish we could’ve saved your world, Ame. I’m so sorry.”"

    # "[Music" "Building Grandeur Theme]"

    "Kai" "“Anyway, this war is our responsibility, Ame. You don’t need to worry about it. What would you like to do?”"

    "Hina thinking" "“You can’t go back to your world, but we could theoretically send you to a new one. Give you an opportunity to start a new life separated from all this chaos.”"

    "Hina" "“You shouldn’t stay here, at the very least. There’s no point. I recommend going to a new world and living out whatever dreams you had.”"

    "Ame" "“...I can’t. I can’t restart my life and turn a blind eye to what happened in my world.”"

    "Kai" "“Huh? Ok… well… what are you going to do then? Staying here won’t do anything.”"

    "Ame" "“Well… is there anything I {i}can{/i} do to help?”"

    # "[Music Stop]"

    "Kai" "“No.”"

    "Hina smirking" "“Yeah, there is.”"

    "Kai angry" "“We are NOT sending them in there alone!”"

    "Hina winking" "“They won’t be alone, they have my mind link.”"

    "Ame frustrated" "“You two are talking like I’m not here again.”"

    "Kai flustered" "“Oh, uh… sorry.”"

    # "[Music" "Building Grandeur Theme]"

    "Hina smirking" "“Ame, you want to help fight the war, right? How do you feel about giving us a little head start?”"

    "Ame curious" "“A head start?”"

    "Hina" "“We know what world Cole is hitting next. We may not be able to go ourselves, but you… you can make the trip quite easily.”"

    "Kai" "“We know literally nothing about the world that we’d be sending you into.”"

    "Hina" "“But we can learn via your mind link contract with me! It’ll allow us to communicate, even across dimensions! If we have intel and somebody working on countering the plague before we arrive, we’ll be far more equipped to take care of Cole in this world!”"

    # "[Music" "Stop]"

    "{i}This is like watching two kids fight over who gets to play with a toy… but why am I the toy???{/i}"

    # "[Music" "Continue]"

    "Hina" "“Anyway, the more time we waste, the less time you have to make a change. Decide, Ame. Hurry up now.”"

    "Ame" "“...ok, I’ll–”"

    "Hina" "“Alright!”"

    "Kai" "“Wait!--”"

    # "[aggressively flick the background and quickly have Ame fly toward a portal that appears.]"

    "Hina" "“Stay in touch! Talk to you soon!”"
return
