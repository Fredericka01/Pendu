#Import
import random

#File used
sett = open("PenduData.cfg", "r")
banque = open("PenduData.json", "r")

#Defining value
display_sting = ""
underscore = "_ "
drawn_letter = True


#Dranw letters base value
if drawn_letter != 0:
    drawn_letter_a = False
    drawn_letter_b = False
    drawn_letter_c = False
    drawn_letter_d = False
    drawn_letter_e = False
    drawn_letter_f = False
    drawn_letter_g = False
    drawn_letter_h = False
    drawn_letter_i = False
    drawn_letter_j = False
    drawn_letter_k = False
    drawn_letter_l = False
    drawn_letter_m = False
    drawn_letter_n = False
    drawn_letter_o = False
    drawn_letter_p = False
    drawn_letter_q = False
    drawn_letter_r = False
    drawn_letter_s = False
    drawn_letter_t = False
    drawn_letter_u = False
    drawn_letter_v = False
    drawn_letter_w = False
    drawn_letter_x = False
    drawn_letter_y = False
    drawn_letter_z = False
a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z ="_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_"
fonction3 = 0
final_display = " "


#Setting extraction 
setting1 = sett.readline()
sett_data1 = (setting1.index(":"))
sett_value1 = (int(sett_data1)+1)
prevalue1 = (setting1[sett_value1:])
setting1 = int(prevalue1)

#Ramdom word selection
word_id = (random.randint(1, setting1))
for word in range(word_id):
    word = banque.readline()



#Word to letter list 
raw_word = word
len_p = len(raw_word)
carr1 = 0
list_word = []
factor2 = 0
for carr in range(len_p):
    list_word.append(raw_word[(carr1 + factor2)])
    factor2 = factor2 + 1

#take /n off + re-len
list_word.pop()
len_w = len(list_word)

#Closing file
sett.close()
banque.close()

#Counting letters in word
if len_w !=0:
    wa = (list_word.count("a"))
    wb = (list_word.count("b"))
    wc = (list_word.count("c"))
    wd = (list_word.count("d"))
    we = (list_word.count("e"))
    wf = (list_word.count("f"))
    wg = (list_word.count("g"))
    wh = (list_word.count("h"))
    wi = (list_word.count("i"))
    wj = (list_word.count("j"))
    wk = (list_word.count("k"))
    wl = (list_word.count("l"))
    wm = (list_word.count("m"))   
    wn = (list_word.count("n"))
    wo = (list_word.count("o"))
    wp = (list_word.count("p"))
    wq = (list_word.count("q"))
    wr = (list_word.count("r"))   
    ws = (list_word.count("s"))
    wt = (list_word.count("t"))
    wu = (list_word.count("u"))
    wv = (list_word.count("v"))
    ww = (list_word.count("w"))
    wx = (list_word.count("x"))
    wy = (list_word.count("y"))
    wz = (list_word.count("z"))


#########################(essai)
essai = len_w * 2

#Premiere image
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print("           *@#################:")
print("           ==  :W*           =*")
print("           ==:W*             =*")
print("           =W*               ++")
print("           ==")
print("           ==")
print("           ==")
print("           ==")
print("           ==")
print("           ==")
print("           ==")
print("           ==")
print("           ==")
print("           ==")
print("           ==")
print("-::::::::::=#::::::::::::::::::::::::::")
print()
print()
print()
print()
print()
print()
print()
print()
print()


mistakes = 0

#Drawn letters
for last_letter in range(essai):
    if mistakes <= 6:
        print(" ")
        print(" ")
        last_letter = input("Entrez une lette : ")
        
        if last_letter == "a" and wa == 0:
            mistakes = mistakes + 1
        if last_letter == "b" and wb == 0:
            mistakes = mistakes + 1
        if last_letter =="c" and wc == 0:
            mistakes = mistakes + 1
        if last_letter == "d" and wd == 0:
            mistakes = mistakes + 1
        if last_letter == "e" and we == 0:
            mistakes = mistakes + 1
        if last_letter == "f" and wf == 0:
            mistakes = mistakes + 1
        if last_letter == "g" and wg == 0:
            mistakes = mistakes + 1
        if last_letter == "h" and wh == 0:
            mistakes = mistakes + 1
        if last_letter == "i" and wi == 0:
            mistakes = mistakes + 1
        if last_letter == "j" and wj == 0:
            mistakes = mistakes + 1
        if last_letter == "k" and wk == 0:
            mistakes = mistakes + 1
        if last_letter == "l" and wl == 0:
            mistakes = mistakes + 1
        if last_letter == "m" and wm == 0:
            mistakes = mistakes + 1
        if last_letter == "n" and wn == 0:
            mistakes = mistakes + 1
        if last_letter == "o" and wo == 0:
            mistakes = mistakes + 1
        if last_letter == "p" and wp == 0:
            mistakes = mistakes + 1
        if last_letter == "q" and wq == 0:
            mistakes = mistakes + 1
        if last_letter == "r" and wr == 0:
            mistakes = mistakes + 1
        if last_letter == "s" and ws == 0:
            mistakes = mistakes + 1
        if last_letter == "t" and wt == 0:
            mistakes = mistakes + 1
        if last_letter == "u" and wu == 0:
            mistakes = mistakes + 1
        if last_letter == "v" and wv == 0:
            mistakes = mistakes + 1
        if last_letter == "w" and ww == 0:
            mistakes = mistakes + 1
        if last_letter == "x" and wx == 0:
            mistakes = mistakes + 1
        if last_letter == "y" and wy == 0:
            mistakes = mistakes + 1
        if last_letter == "z" and wz == 0:
            mistakes = mistakes + 1
        
        
        if last_letter !=0:
            if last_letter == "a":
                drawn_letter_a = True
            if last_letter == "b":
                drawn_letter_b = True
            if last_letter == "c":
                drawn_letter_c = True
            if last_letter == "d":
                drawn_letter_d = True
            if last_letter == "e":
                drawn_letter_e = True
            if last_letter == "f":
                drawn_letter_f = True
            if last_letter == "g":
                drawn_letter_g = True
            if last_letter == "h":
                drawn_letter_h = True
            if last_letter == "i":
                drawn_letter_i = True
            if last_letter == "j":
                drawn_letter_j = True
            if last_letter == "k":
                drawn_letter_k = True
            if last_letter == "l":
                drawn_letter_l = True
            if last_letter == "m":
                drawn_letter_m = True
            if last_letter == "n":
                drawn_letter_n = True
            if last_letter == "o":
                drawn_letter_o = True
            if last_letter == "p":
                drawn_letter_p = True
            if last_letter == "q":
                drawn_letter_q = True
            if last_letter == "r":
                drawn_letter_r = True
            if last_letter == "s":
                drawn_letter_s = True
            if last_letter == "t":
                drawn_letter_t = True
            if last_letter == "u":
                drawn_letter_u = True
            if last_letter == "v":
                drawn_letter_v = True
            if last_letter == "w":
                drawn_letter_w = True
            if last_letter == "x":
                drawn_letter_x = True
            if last_letter == "y":
                drawn_letter_y = True
            if last_letter == "z":
                drawn_letter_z = True
        
        
        
        if drawn_letter_a == True:
            a= "A "
        if drawn_letter_b == True:
            b= "B "
        if drawn_letter_c == True:
            c= "C "
        if drawn_letter_d == True:
            d= "D "
        if drawn_letter_e == True:
            e= "E "
        if drawn_letter_f == True:
            f= "F "
        if drawn_letter_g == True:
            g= "G "
        if drawn_letter_h == True:
            h= "H " 
        if drawn_letter_i == True:
            i= "I "
        if drawn_letter_j == True:
            j= "J "
        if drawn_letter_k == True:
            k= "K "
        if drawn_letter_l == True:
            l= "L "
        if drawn_letter_m == True:
            m= "M "
        if drawn_letter_n == True:
            n= "N "
        if drawn_letter_o == True:
            o= "O "
        if drawn_letter_p == True:
            p= "P "
        if drawn_letter_q == True:
            q= "Q "
        if drawn_letter_r == True:
            r= "R "
        if drawn_letter_s == True:
            s= "S "
        if drawn_letter_t == True:
            t= "T "
        if drawn_letter_u == True:
            u= "U "
        if drawn_letter_v == True:
            v= "V "
        if drawn_letter_w == True:
            w= "W "
        if drawn_letter_x == True:
            x= "X "
        if drawn_letter_y == True:
            y= "Y "
        if drawn_letter_y == True:
            z= "Z "


        dictionary = {
            "a": a,
            "b": b,
            "c": c,
            "d": d,
            "e": e,
            "f": f,
            "g": g,
            "h": h,
            "i": i,
            "j": j,
            "k": k,
            "l": l,
            "m": m,
            "n": n,
            "o": o,
            "p": p,
            "q": q,
            "r": r,
            "s": s,
            "t": t,
            "u": u,
            "v": v,
            "w": w,
            "x": x,
            "y": y,
            "z": z,
        }
    

        fonction3 = 0    
        if mistakes == 0:
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print("           *@#################:")
            print("           ==  :W*           =*")
            print("           ==:W*             =*")
            print("           =W*               ++")
            print("           ==")
            print("           ==")
            print("           ==")
            print("           ==")
            print("           ==")
            print("           ==")
            print("           ==")
            print("           ==")
            print("           ==")
            print("           ==")
            print("           ==")
            print("-::::::::::=#::::::::::::::::::::::::::")
            print()
            print()
            print()
            print()
            print()

        if mistakes == 1:
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print("           *******************")
            print("           @+  +W*           @+")
            print("           @++W+             @+")
            print("           @W+             -=W@*-")
            print("           @+             @*----=#")
            print("           @+               @==W ")
            print("           @+")
            print("           @+")
            print("           @+")
            print("           @+                          ")
            print("           @+                          ")
            print("           @+                          ")
            print("           @+                          ")
            print("           @+                          ")
            print(":**********@#**************************")
            print()
            print()
            print()
            print()

        if mistakes == 2:
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print("           -#*****************-        ")
            print("           :@  -@#           #*        ")
            print("           :@-@#             #*        ")
            print("           :W=             -#WW#:      ")
            print("           :@             *@:---=#     ")
            print("           :@              :@WW@+      ")
            print("           :@                *#        ")
            print("           :@                *#        ")
            print("           :@                *#        ")
            print("           :@                *#        ")
            print("           :@                *#        ")
            print("           :@                          ")
            print("           :@                          ")
            print("           :@                          ")
            print("           :@                          ")
            print(" ######################################")
            print()
            print()

        if mistakes == 3:
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print("          -*:::::::::::::::::-         ")
            print("          :W   +W+          :W         ")
            print("          :W +W+            :W         ")
            print("          :WW+              *W+-       ")
            print("          :W              ##:--=W-     ")
            print("          :W             :W:----#*     ")
            print("          :W              *W*:+@#      ")
            print("          :W          W:     W:        ")
            print("          :W           :W=   W:        ")
            print("          :W              +@@W:        ")
            print("          :W                 W:        ")
            print("          :W                 W:        ")
            print("          :W                 W:        ")
            print("          :W                           ")
            print("          :W                           ")
            print("          :W                           ")
            print("          :W                           ")
            print("***************************************")
            print()
            print()

        if mistakes == 4:
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print("          -*:::::::::::::::::-         ")
            print("          :W   +W+          :W         ")
            print("          :W +W+            :W         ")
            print("          :WW+              *W+-       ")
            print("          :W              ##:--=W-     ")
            print("          :W             :W:----#*     ")
            print("          :W              *W*:+@#      ")
            print("          :W          :W     W:    W:  ")
            print("          :W           :W=   W:   W:   ")
            print("          :W              +@@W:@@+     ")
            print("          :W                 W:        ")
            print("          :W                 W:        ")
            print("          :W                 W:        ")
            print("          :W                           ")
            print("          :W                           ")
            print("          :W                           ")
            print("          :W                           ")
            print("***************************************")
            print()
            print()

        if mistakes == 5:
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print("          -*:::::::::::::::::-         ")
            print("          :W   +W+          :W         ")
            print("          :W +W+            :W         ")
            print("          :WW+              *W+-       ")
            print("          :W              ##:--=W-     ")
            print("          :W             :W:----#*     ")
            print("          :W              *W*:+@#      ")
            print("          :W          :W     W:    W:  ")
            print("          :W           :W=   W:   W:   ")
            print("          :W              +@@W:@@+     ")
            print("          -W-                W:        ")
            print("          -W-                W:        ")
            print("          -W-                W:        ")
            print("          -W-               :W:        ")
            print("          -W-             +W*          ")
            print("          -W-           -W+            ")
            print("          -W-         -W*              ")
            print("          -W-                          ")
            print("-::::::::::W+::::::::::::::::::::::::::")
            print()
            print()

        if mistakes == 6:
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print("          -*:::::::::::::::::-         ")
            print("          :W   +W+          :W         ")
            print("          :W +W+            :W         ")
            print("          :WW+              *W+-       ")
            print("          :W              ##:--=W-     ")
            print("          :W             :W:----#*     ")
            print("          :W              *W*:+@#      ")
            print("          :W          :W     W:    W:  ")
            print("          :W           :W=   W:   W:   ")
            print("          :W              +@@W:@@+     ")
            print("          -W-                W:        ")
            print("          -W-                W:        ")
            print("          -W-                W:        ")
            print("          -W-               :W:        ")
            print("          -W-             +W*  *W+     ")
            print("          -W-           -W+     +W-    ")
            print("          -W-         -W*        *W-   ")
            print("          -W-                          ")
            print("-::::::::::W+::::::::::::::::::::::::::")
            print()
            print()

        if mistakes == 7:
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print("             YOU LOST  !!!              ")
            print("                                       ")
            print("                                       ")
            print("             ´?ë©#¶ææ¶#©ë?´            ")
            print("          '±NXí          íXN@'         ")
            print("        '¶@í                í@¶'       ")
            print("       *©/                    /©*      ")
            print("      I¶í    *###©í    §##N»   í¶I     ")
            print("     ,N*     £####/   ?####±    ?N,    ")
            print("     »©       ;*?       *&;      ©»    ")
            print("     /©í           í??í         í©/    ")
            print("     ´æ%        ;@©X  &¶¶»      &æ´    ")
            print("       N?    íXN±í       %N±í  ?N      ")
            print("       ^©o   íí            í  %©^      ")
            print("         &NI                *N&        ")
            print("           íÉ©X»        »X©Éí          ")
            print("               ^*XÑÉÉÉX*^              ")
            print("                                       ")
            print("                                       ")
            print("             YOU LOST  !!!             ")
            print()
            print()




    #Dictionary 1

        dictionary = {
            "a": a,
            "b": b,
            "c": c,
            "d": d,
            "e": e,
            "f": f,
            "g": g,
            "h": h,
            "i": i,
            "j": j,
            "k": k,
            "l": l,
            "m": m,
            "n": n,
            "o": o,
            "p": p,
            "q": q,
            "r": r,
            "s": s,
            "t": t,
            "u": u,
            "v": v,
            "w": w,
            "x": x,
            "y": y,
            "z": z,
        }


        if list_word[0] == "a":
        ###############################
            for word in range(len_w):
                final_display = final_display + str(dictionary.get(list_word[fonction3])) + " "
                fonction3 = fonction3 + 1
            print(final_display)
            final_display = ""

        fonction3 = 0    
    
        if list_word[0] == "b":
        ###############################
            for word in range(len_w):
                final_display = final_display + str(dictionary.get(list_word[fonction3])) + " "
                fonction3 = fonction3 + 1
            print(final_display)
            final_display = ""

        fonction3 = 0

        if list_word[0] == "c":
        ###############################
            for word in range(len_w):
                final_display = final_display + str(dictionary.get(list_word[fonction3])) + " "
                fonction3 = fonction3 + 1
            print(final_display)
            final_display = ""

        fonction3 = 0

        if list_word[0] == "d":
        ###############################
            for word in range(len_w):
                final_display = final_display + str(dictionary.get(list_word[fonction3])) + " "
                fonction3 = fonction3 + 1
            print(final_display)
            final_display = ""
    
        fonction3 = 0

        if list_word[0] == "e":
        ###############################
            for word in range(len_w):
                final_display = final_display + str(dictionary.get(list_word[fonction3])) + " "
                fonction3 = fonction3 + 1
            print(final_display)
            final_display = ""

        fonction3 = 0

        if list_word[0] == "f":
        ###############################
            for word in range(len_w):
                final_display = final_display + str(dictionary.get(list_word[fonction3])) + " "
                fonction3 = fonction3 + 1
            print(final_display)
            final_display = ""

        fonction3 = 0

        if list_word[0] == "g":
        ###############################
            for word in range(len_w):
                final_display = final_display + str(dictionary.get(list_word[fonction3])) + " "
                fonction3 = fonction3 + 1
            print(final_display)
            final_display = ""

        fonction3 = 0

        if list_word[0] == "h":
        ###############################
            for word in range(len_w):
                final_display = final_display + str(dictionary.get(list_word[fonction3])) + " "
                fonction3 = fonction3 + 1
            print(final_display)
            final_display = ""

        fonction3 = 0

        if list_word[0] == "i":
        ###############################
            for word in range(len_w):
                final_display = final_display + str(dictionary.get(list_word[fonction3])) + " "
                fonction3 = fonction3 + 1
            print(final_display)
            final_display = ""

        fonction3 = 0
        if list_word[0] == "j":
        ###############################
            for word in range(len_w):
                final_display = final_display + str(dictionary.get(list_word[fonction3])) + " "
                fonction3 = fonction3 + 1
            print(final_display)
            final_display = ""

        fonction3 = 0

        if list_word[0] == "k":
        ###############################
            for word in range(len_w):
                final_display = final_display + str(dictionary.get(list_word[fonction3])) + " "
                fonction3 = fonction3 + 1
            print(final_display)
            final_display = ""
    
        fonction3 = 0

        if list_word[0] == "l":
        ###############################
            for word in range(len_w):
                final_display = final_display + str(dictionary.get(list_word[fonction3])) + " "
                fonction3 = fonction3 + 1
            print(final_display)
            final_display = ""
    
        fonction3 = 0

        if list_word[0] == "m":
        ###############################
            for word in range(len_w):
                final_display = final_display + str(dictionary.get(list_word[fonction3])) + " "
                fonction3 = fonction3 + 1
            print(final_display)
            final_display = ""

        fonction3 = 0

        if list_word[0] == "n":
        ###############################
            for word in range(len_w):
                final_display = final_display + str(dictionary.get(list_word[fonction3])) + " "
                fonction3 = fonction3 + 1
            print(final_display)
            final_display = ""
    
        fonction3 = 0

        if list_word[0] == "o":
        ###############################
            for word in range(len_w):
                final_display = final_display + str(dictionary.get(list_word[fonction3])) + " "
                fonction3 = fonction3 + 1
            print(final_display)
            final_display = ""

        fonction3 = 0

        if list_word[0] == "p":
        ###############################
            for word in range(len_w):
                final_display = final_display + str(dictionary.get(list_word[fonction3])) + " "
                fonction3 = fonction3 + 1
            print(final_display)
            final_display = ""
    
        fonction3 = 0

        if list_word[0] == "q":
        ###############################
            for word in range(len_w):
                final_display = final_display + str(dictionary.get(list_word[fonction3])) + " "
                fonction3 = fonction3 + 1
            print(final_display)
            final_display = ""
    
        fonction3 = 0

        if list_word[0] == "r":
        ###############################
            for word in range(len_w):
                final_display = final_display + str(dictionary.get(list_word[fonction3])) + " "
                fonction3 = fonction3 + 1
            print(final_display)
            final_display = ""

        fonction3 = 0

        if list_word[0] == "s":
        ###############################
            for word in range(len_w):
                final_display = final_display + str(dictionary.get(list_word[fonction3])) + " "
                fonction3 = fonction3 + 1
            print(final_display)
            final_display = ""
    
        fonction3 = 0

        if list_word[0] == "t":
        ###############################
            for word in range(len_w):
                final_display = final_display + str(dictionary.get(list_word[fonction3])) + " "
                fonction3 = fonction3 + 1
            print(final_display)
            final_display = ""

        fonction3 = 0

        if list_word[0] == "u":
        ###############################
            for word in range(len_w):
                final_display = final_display + str(dictionary.get(list_word[fonction3])) + " "
                fonction3 = fonction3 + 1
            print(final_display)
            final_display = ""

        fonction3 = 0

        if list_word[0] == "v":
        ###############################
            for word in range(len_w):
                final_display = final_display + str(dictionary.get(list_word[fonction3])) + " "
                fonction3 = fonction3 + 1
            print(final_display)
            final_display = ""

        fonction3 = 0

        if list_word[0] == "w":
        ###############################
            for word in range(len_w):
                final_display = final_display + str(dictionary.get(list_word[fonction3])) + " "
                fonction3 = fonction3 + 1
            print(final_display)
            final_display = ""

        fonction3 = 0
    
        if list_word[0] == "x":
        ###############################
            for word in range(len_w):
                final_display = final_display + str(dictionary.get(list_word[fonction3])) + " "
                fonction3 = fonction3 + 1
            print(final_display)
            final_display = ""

        fonction3 = 0

        if list_word[0] == "y":
        ###############################
            for word in range(len_w):
                final_display = final_display + str(dictionary.get(list_word[fonction3])) + " "
                fonction3 = fonction3 + 1
            print(final_display)
            final_display = ""

        fonction3 = 0

        if list_word[0] == "z":
        ###############################
            for word in range(len_w):
                final_display = final_display + str(dictionary.get(list_word[fonction3])) + " "
                fonction3 = fonction3 + 1
            print(final_display)
            final_display = ""