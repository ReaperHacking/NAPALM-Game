# NAPALM GAME!

# INTRO

print("It's the year 2023, you are a person, the president's, choose the right decisions to not go to war and die\n")

first_decision = input(
    "You're at the meeting with all the presidents, when one of them ask you your opinion on nuclear firepower, do you, (1)Tell him you love it and say we should nuke everybody, or (2) We should prevent nuclear war and keep firepower to a minimum at all costs, what do you choose (1/2):\n ")

# first pathway a user can choose in the story

def first_path(first_decision):
    second_decision = None
    third_decision = None
    if first_decision == "1":
        second_decision = input(
            "They say, WHAT THE HELL IS WRONG WITH YOU, DO YOU WANNA TEST ME? You can either (1) choose to say that he is a dick and loser and you don't care if he bombs the nation, or (2) Say, sorry sir, my bad :/ : \n")

    # first ending
    if second_decision == "1":
        print("""
     _.-^^---....,,--       
 _--                  --_  
<                        >)
|                         | 
 \._                   _./  
    ```--. . , ; .--'''       
          | |   |             
       .-=||  | |=-.   
       `-=#$%&%$#=-'   
          | ;  :|     
 _____.,-#%&$@%#&#~,._____

 GAME OVER! (Nuclear Ending (Worst Ending)) :/


  """)
    elif second_decision == "2":
        third_decision = None
        third_decision = input(
            "Ok then, let's proceed, like I was saying before this damn neanderthal interrupted with their useless nonsense, what should we do about the ongoing civil war in our nations? (1) We should beat the civilians and gas them with tear gas, (2) Fund programs to help the civilians (1/2): ")
      # second ending
    if third_decision == "1":
        print("""
      ____________
  |____________|_
   ||--------|| | _________
   ||- _     || |(HA ha ha!)
   ||    - _ || | ---------
   ||       -|| |     //
   ||        || O\    __
   ||        ||  \\  (..)
   ||        ||   \\_|V |_
   ||        ||    \  \/  )
   ||        ||     :    :|
   ||        ||     :    :|
   ||  RIP   ||     :====:O
   ||        ||     (    )
   ||__@@@@__||     | `' |
   || @|..|@ ||     | || |
   ||O@`=='@O||     | || |
   ||_@\/\/@_||     |_||_|
 ----------------   '_'`_`
/________________\----------\
|   GUILLOTINE   |-----------|
|                            |
|____________________________|
DOWN WITH THE HEAD OF THE PRESIDENT!!! 

GAME OVER (Revolution Ending(Neutral Ending)) :/

You stopped the nuclear war, but unfortunately your choice in the treatment of your citizens
caused them to revolt, capture you, and chop your head off :/ TRY AGAIN :/
    """)
      # third ending
    elif third_decision == "2":
        print("""
                _  _   _     _    _        _        _   _
               |_)|_  /\ /` |_   / \|\ |   |_  /\ |_) | |_|
               |  |_ /""\\_,|_   \_/| \|   |_ /""\| \ | | |

                               ..eeeee..
                             e8"   8   "8e
                            d8     8     8b
                            8!   .dWb.   !8
                            Y8 .e* 8 *e. 8P
                             *8*   8   *8*
                               **ee8ee**

                Congratulations! (BEST Ending)

                Awesome Job on getting this ending! 
                Great job, you stopped nuclear war and any public outrage! You get re-elected
                and run another great sucessful term.

                I hope you enjoyed the game! Check out more projects on my github!

    """)

# function for second path, just in case user chooses the (2) second option

def second_path(first_decision):
    if first_decision == "2":
        fourth_decision = None
        fourth_decision = input(
            "Okay good, but what about [c0rRUptTEd]? You look at him with a puzzled look on your face.. (1)What?.. (2)Huh..?: ")
        if fourth_decision == "2":
          # fourth ending
            print("""

⢱⣄⠀⠀⠀⠀⠀⠀⠀⠀⣀⠠⠤⠤⣤⠤⠤⠄⣀⠀⣀        ⡀⡼
⠀⠛⢯⣿⣟⣯⡗⣶⠲⡁⢀⡀⠤⠬⠏⠥⠤⠀⡀⡩⢒⣎⢽⣿⣻⠯⠞⠁
⠀⠀⠀⠀⢉⠝⠓⢻⣤⡸⠣⡀⠀⠀⠀⠀⠀⠠⠚⣴⡾⡟⠉⠣⡀⠀⠀⠀
⠀⠀⠀⣠⣳⣆⠔⠉⠏⣿⡄⢱⣤⢄⣀⢤⣴⡇⣰⡟⢩⠁⠠⡴⡿⡄⠀⠀
⠀⠀⢠⠁⢀⠎⠀⠀⠘⣼⡿⠻⠙⣍⣀⠼⠹⡟⣿⣄⣃⠀⠀⠘⡄⠈⡄⠀
⠀⠀⠇⢀⣬⣶⣬⡫⢋⡼⢷⡗⢀⢗⠉⠧⡀⣊⢸⣧⣑⣴⣭⣴⣴⡄⠸⠀
⠀⢸⠀⠈⠉⠛⠷⣾⣿⣇⣯⣧⣋⢉⡽⠍⢙⣽⣎⣿⣿⠧⠟⠋⠁⡆⠀⡄
⠀⢸⢀⡀⠀⢀⡠⠘⢉⡿⣿⣿⣿⡖⠁⢰⣿⣿⣿⣿⡈⠑⠢⣀⠀⣧⡀⡇
⠀⠘⡎⠏⠖⠓⠒⠒⠺⣿⡈⢷⢃⠁⠀⠎⠼⡾⣉⣿⠇⠀⠀⠈⢁⠉⢫⠀
⠀⠀⢡⠀⠐⡀⠀⠀⠀⠹⣿⣮⠢⡇⠀⢸⠐⣵⢿⠋⠀⠀⠀⠀⠆⠀⡌⠀
⠀⠀⠀⢣⠀⠈⢄⠀⠀⠀⠈⠙⡇⡆⠐⢸⢸⠋⠁⠀⠀⠀⠀⠊⠀⡜⠀⠀
⠀⠀⠀⠀⠑⣄⠀⠑⢄⡀⠀⠀⣿⣦⣤⣴⣾⠀⠀⠀⡀⠐⠁⣠⠊⠀⠀⠀
⠀⠀⠀⠀⠀⠈⠒⢤⡿⠈⠐⠀⠴⢭⣿⣭⠮⠀⠒⠩⣾⡤⠚⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⠐⠀⠤⠀⢈⣶⡘⠀⠤⠔⠂⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠀⠀⠀⠀⠀⠀⠀⠀⠀
          ?1?!#@4$^*9)7 Ending (Secret Cursed Ending)

          Ħɇłłø, mȺꝁɇ sᵾɍɇ ŧø łøȼꝁ ɏøᵾɍ đøøɍs Ⱥnđ wɨnđøws ŧønɨǥħŧ Ⱥnđ ŧø NØŦ łøøꝁ øᵾŧsɨđɇ ɏøᵾɍ            ħøᵾsɇ, wħȺŧɇvɇɍ ɏøᵾ đø, mȺꝁɇ sᵾɍɇ ɨŧ đøɇsn'ŧ sɇɇ ɏøᵾ.. :)

          𝔾𝕆𝕆𝔻 𝕃𝕌ℂ𝕂 :)

      """)
          # fifth and final ending
        elif fourth_decision == "1":
            print("""

⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠈⠋⢝⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⢸⣿⣿⣿⡆⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⢸⣿⣿⣿⡇⠀⡟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⢸⣿⣿⣿⡇⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⠀⢸⣿⣿⣿⡇⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⢸⣿⣿⣿⡇⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡁⠀⢸⣿⣿⣿⡇⠀⢼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⢸⣿⣿⣿⡇⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠀⠀⢸⣿⣿⣿⡇⠀⢞⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠀⣀⣀⣀⣀⣸⣿⣿⣿⣇⣀⣀⣀⣉⠸⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣮⣠⠈⠀⠁⠈⠀⡴⠘⣆⠈⠀⠁⠈⠀⣀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡖⠀⢀⡼⠁⠄⠘⢦⠀⠀⣲⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠀⢀⡞⠀⠠⢈⠐⠈⢧⠀⠐⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⢠⠞⠀⠠⢁⠀⠂⡁⠈⢳⡀⠐⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⢠⢍⠀⠈⢀⠂⠈⠐⠀⠁⠠⠱⡀⠀⠽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠀⢰⠃⠈⠀⠉⠉⢀⣤⠉⠁⠀⠈⠣⡡⠄⠀⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀⡰⠃⠳⣄⠀⠀⠀⢸⣿⠀⠀⠀⠀⣠⠃⠘⣆⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠁⠀⡼⠁⠐⡀⠈⠕⠒⠤⠤⡥⠤⠄⠒⠋⠀⠠⢀⠘⣆⠀⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⡿⠋⠈⠙⢝⢿⣿⣿⣿⣿⣿⣿⣿⠟⠀⢀⡞⠀⠄⡁⢀⠂⠄⠂⠄⡀⠃⠀⠄⠂⡐⠈⠠⠀⢂⠈⢧⠀⠘⢻⣿⣿⣿⣿⣿⣿⣿⡿⠋⠉⠉⠿⣿⣿⣿⣿⣿
⣿⣿⠿⠿⠃⠀⠘⣧⠀⠉⣿⣿⣿⣿⣿⣿⠋⠀⢀⠞⠀⡐⠠⠐⢀⠐⠠⢈⠠⠐⢀⠁⠂⡁⠠⠈⠄⠁⠄⠂⠈⢣⡀⠐⠽⣿⣿⣿⣿⣿⡿⠁⠀⡾⠁⠀⠽⠿⢿⣿⣿
⠟⠉⠀⠀⠀⠀⢀⡿⠀⠐⢝⢿⣿⣿⠟⠉⠀⢀⡞⠀⠀⠁⠀⠀⠈⠀⠀⠈⠀⠀⠈⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠈⢧⡀⠀⠹⡻⢿⣿⡿⠃⠀⠀⣧⠀⠀⠀⠀⠘⠩⢻
⡆⠀⠛⠳⠶⠚⣿⡟⢦⣄⣀⠀⠀⠀⣀⣠⠴⠏⢀⠐⠠⢈⠀⠠⢁⠈⠀⠀⠁⠈⠄⠁⠈⠀⠀⢈⠐⠀⠀⠌⠠⠁⠈⢻⣦⣄⡀⠀⠁⠀⣀⣠⠶⢹⢏⠓⠶⠞⠋⠀⣸
⣿⣆⠀⠘⠒⢛⡸⠁⠀⠀⠉⠉⠉⠉⠁⢠⠏⠀⡀⠈⠀⢀⠀⡀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⢀⠀⠁⠈⠀⠀⢳⡀⠉⠉⠉⠉⠁⠀⠀⠘⣎⠛⠒⠂⠀⣼⣿
⣿⣿⣷⣤⣀⠈⠁⣀⣴⣾⣷⡦⠀⠀⣰⠃⢀⠂⠄⠁⠀⠂⠄⠐⡀⠌⠀⠀⡀⠄⠀⠠⠀⠀⠀⠠⠁⠌⠀⠄⠀⠠⠁⠌⠀⠹⡄⠀⠄⣶⣿⣷⣧⣠⠈⢀⣀⣤⣾⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀⡰⠁⠀⠂⢀⠈⠀⠀⠁⠈⠀⠀⠐⠀⠁⠀⠂⠀⠀⠁⠈⠀⠁⠂⠈⠐⠈⠀⠀⠁⠂⠈⠀⠙⣄⠈⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠁⠀⡼⠁⠠⠁⠌⠀⠄⠂⢀⠂⠄⢁⠂⠀⠐⡀⢂⠐⢀⠂⡐⢀⠂⠀⠐⡀⠂⠄⠀⠄⠂⠠⠐⢀⠠⠘⢆⠀⠚⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠺⠴⠖⠳⠲⠞⠲⠒⠖⠢⠔⢢⡆⠶⠖⠆⠶⠦⠖⠶⠶⠰⠲⠖⠲⠰⢤⡶⠴⠖⠒⠶⠒⠖⠢⠖⠲⠾⠆⠘⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣆⣄⣠⣀⣤⣠⣄⣠⣀⠀⠀⣼⠁⠀⢀⣤⣤⣄⣤⣠⣄⣴⣠⣄⣀⠀⢸⡇⠀⠀⣀⣤⣤⣤⣤⣤⣤⣄⣤⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⣿⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⢸⡇⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⣿⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀⢸⡇⠀⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⢿⡀⠀⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⠧⠀⢸⡇⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠘⣧⡀⠀⠹⠿⣿⣿⣿⣿⣿⠟⠏⠀⢀⡾⠁⢀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠄⠈⠻⢦⣄⡀⠑⢙⠿⠋⠀⢀⣠⡶⠋⠁⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣧⡀⠀⠈⣽⡇⠀⠀⠀⢺⡏⠁⢀⢀⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⣿⠃⠀⠀⠀⢸⡇⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⡿⠀⠠⣄⠀⠈⡇⠀⢴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⣀⣠⣾⣿⣮⣀⣀⣪⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿    


          You saw too much...(C0rRuPt eNdinG :/)

          You unfortunately were mistakened and heard too much, as a result, they had to
          shut you up :/

      """)


while True: # While loop and try-except error handling blocks so the user can restart and the program can take error handling
    try:
        first_path(first_decision)

    except ValueError:
        print("Error, didn't choose 1 or 2, TRY AGAIN :/")

    try:
        second_path(first_decision)

    except ValueError:
        print("Error, didn't choose 1 or 2, TRY AGAIN :/")

    play_again = input("Would you like to play again? (Y/N): ").upper()

    if play_again == "N":
        break
    elif play_again == "Y":
        continue
    else:
        print("ERROR, not Y or N, try again :/")
        break


# I HOPE YOU ENJOYED GUYS! THIS TOOK ME ALMOST 3 HOURS TO MAKE AND I HAD TROUBLE WITH THE TRY-EXCEPT BLOCKS LOL.
# ENJOY AND CHECK OUT MORE STUFF ON MY GITHUB!
# ART used from asciiart.edu and emojicombos.com
# FONTS used from tools.picsart.com
