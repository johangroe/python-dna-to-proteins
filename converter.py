import os
import time


richtung = None
wrong_input = False
dna_in = None
missing_dna = []
sec_dna_strang = None
rna = []
met_found = False
as_sequenz = []
carry_list = []
no_met = False
no_stop = False
sequenz_liste = []
rna_printer = None
sequenz_printer = None



def richtung_festlegen():

    global richtung, os, wrong_input
    
    os.system('cls')
    print()
    if wrong_input ==True:
        print("Falsche Eingabe, bitte '3' oder '5' eingeben")
        print()
    print("Bitte DNA-Richtung festlegen (der gleich von ihnen folgenden Eingabe):")
    print("(von [3]' nach 5' ODER von [5]' nach 3')")

    richtung = input("Richtung: ")
    
    if richtung == "3":
        wrong_input = False
        input_dna()

    elif richtung == "5":
        wrong_input = False
        input_dna()

    elif richtung_festlegen != "3" or richtung !="5":
        print("falsche eingabe")
        wrong_input = True
        richtung_festlegen()
    
def input_dna():
    
    global richtung, wrong_input, dna_in, no_stop, no_met

    os.system('cls')
    print()
    if wrong_input == True:
        print("Falsche Eingabe (mehr als 6 Nucleotide eingeben, nur A, C, T, G)")
    if no_met == True:
        print("Kein Methionin gefunden!")
    if no_stop == True:
        print("Kein Stopp-Codon gefunden!")

    dna_in = input("DNA:").upper()
    
    if dna_in == "":
        wrong_input = True
        input_dna()

    if len(dna_in) < 6:
        wrong_input = True
        input_dna()    

    elif dna_in != "":
        os.system('cls')
        print()
        print("DNA:",dna_in)
        right = input("RICHTIG? [j] [n]: ")
        if right == "j":
            dna_vervollstaeindigen()
        elif right == "n":
            input_dna()


def dna_vervollstaeindigen():

    global dna_in, missing_dna, sec_dna_strang, wrong_input, dna_3_5, dna_5_3

    list_dna = list(dna_in)

    while len(list_dna) != 0:
        carry = list_dna.pop(0)
        if carry == "A":
            missing_dna.append("T")

        if carry == "T":
            missing_dna.append("A")

        if carry == "C":
            missing_dna.append("G")

        if carry == "G":
            missing_dna.append("C")

        if carry not in ["A","T","C","G"]:
            missing_dna.append("?")

    if "?" in missing_dna:
        wrong_input = True
        input_dna()

    sec_dna_strang = "".join(missing_dna)

    

    rna_schreiben()



def rna_schreiben():

    global richtung, dna_in, sec_dna_strang, rna, rna_printer

    if richtung == "3":
        rna_vorlage = list(dna_in)
    elif richtung == "5":
        rna_vorlage = list(sec_dna_strang)

    while len(rna_vorlage) != 0:
        carry = rna_vorlage.pop(0)
        if carry == "A":
            rna.append("U")

        if carry == "T":
            rna.append("A")

        if carry == "C":
            rna.append("G")

        if carry == "G":
            rna.append("C")

        if carry == "?":
            rna.append("?")
    
    rna_printer = "".join(rna)

    proteine()

def proteine():
    global met_found, no_met, no_stop, rna, sequenz_liste, sequenz_printer

    print(rna)

    nuclist = []

    nuc1 = rna.pop(0)
    nuclist.append(nuc1)

    nuc2 = rna.pop(0)
    nuclist.append(nuc2)

    nuc3 = rna.pop(0)
    nuclist.append(nuc3)

    nucs = "".join(nuclist)

    ### methionin finden ###

    while nucs != "AUG":
        print("while")

        nuclist.clear()
        nucs = "".join(nuclist)

        if len(rna) >= 3:
            nuc1 = nuc2
            nuc2 = nuc3
            nuc3 = rna.pop(0)
            nuclist.append(nuc1)
            nuclist.append(nuc2)
            nuclist.append(nuc3)
            nucs = "".join(nuclist)

        if len(rna) < 2:

            no_met = True
            #print("rna end")
            break
        
        if nucs == "":
            no_met = True
            break



    if nucs != "AUG":
        no_met = True
        input_dna()
        
    
    if nucs == "AUG":

        print("met gefunden!")
        '''
        nucs = ""

        nuclist.clear()
        nuclist.append(rna.pop(0))
        nuclist.append(rna.pop(0))
        nuclist.append(rna.pop(0))
        nucs = "".join(nuclist)

        print(nucs)
        '''
        sequenz_liste.append("Met")
        
        
        while nucs not in ["UAA","UAG","UGA"]:
            
            if len(rna) >= 3:
                nucs = ""
                nuclist.clear()
                nuclist.append(rna.pop(0))
                nuclist.append(rna.pop(0))
                nuclist.append(rna.pop(0))
                nucs = "".join(nuclist)
                

                
                if nucs in ["ACU","ACC","ACA","ACG"]:
                    sequenz_liste.append("Thr")
                
                if nucs in ["AAU","AAC"]:
                    sequenz_liste.append("Asn")
                
                if nucs in ["AAA","AAG"]:
                    sequenz_liste.append("Lys")
                
                if nucs in ["AGU","AGC","UCU","UCC","UCA","UCG"]:
                    sequenz_liste.append("Ser")
                
                if nucs in ["AGA","AGG","CGU","CGC","CGA","CGG"]:
                    sequenz_liste.append("Arg")

                if nucs in ["GUU","GUC","GUA","GUG"]:
                    sequenz_liste.append("Val")
                
                if nucs in ["GCU","GCC","GCA","GCG"]:
                    sequenz_liste.append("Ala")
                
                if nucs in ["GAU","GAC"]:
                    sequenz_liste.append("Asp")
                
                if nucs in ["GAA","GAG"]:
                    sequenz_liste.append("Glu")
                
                if nucs in ["GGU","GGC","GGA","GGG"]:
                    sequenz_liste.append("Gly")
                
                if nucs in ["UUU","UUC"]:
                    sequenz_liste.append("Phy")
                
                if nucs in ["UUA","UUG","CUU","CUC","CUA","CUG"]:
                    sequenz_liste.append("Leu")
                
                if nucs in ["UAU","UAC"]:
                    sequenz_liste.append("Tyr")

                if nucs in ["UGU","UGC"]:
                    sequenz_liste.append("Cys")
                
                if nucs in ["UGG"]:
                    sequenz_liste.append("Trp")
                
                if nucs in ["CCU","CCC","CCA","CCG"]:
                    sequenz_liste.append("Pro")
                
                if nucs in ["CAU","CAC"]:
                    sequenz_liste.append("His")

                if nucs in ["CAA","CAG"]:
                    sequenz_liste.append("Gln")
                
                if nucs in ["AUU","AUC","AUA"]:
                    sequenz_liste.append("Ile")
                
                
                
                
                
                
                
            if nucs in ["UAA","UAG","UGA"]:
                no_stop = False
                sequenz_printer = " ".join(sequenz_liste)
                printer()
                break

            if len(rna) <3:
                no_stop = True

                os.system('cls')
                print()
                print("Kein Stopp-Codon vorhanden! Trotzdem anzeigen?")
                
                zeigen = input("[j]a oder [n]ein ")
                if zeigen == "j":
                    sequenz_printer = " ".join(sequenz_liste)
                    printer()
                elif zeigen == "n":
                    input_dna()
                break

                
    

def printer():
    global richtung
    global wrong_input
    global dna_in
    global missing_dna
    global sec_dna_strang
    global rna
    global met_found
    global as_sequenz
    global carry_list
    global no_met
    global no_stop
    global sequenz_liste 
    global dna_3_5
    global dna_5_3
    global rna_printer
    global sequenz_printer

    

    if richtung == "3":
        dna_3_5 = dna_in
        dna_5_3 = sec_dna_strang
    
    elif richtung == "5":
        dna_3_5 = sec_dna_strang
        dna_5_3 = dna_in

    os.system('cls')

    print()
    print("-----------------      -----------------")
    print("DNA 3'-5':",dna_3_5)
    print("DNA 5'-3':",dna_5_3)
    print("RNA 5'-3':",rna_printer)
    print()
    print("Sequenz:")
    print(sequenz_printer)
    print("-----------------      -----------------")
    print()
    



richtung_festlegen()