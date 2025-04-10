#populatie = alegem indivizi alleator din intervalul D
#construim o populatie(t+1) din cea anterioara cat timp nu exista conditia de terminare
#selectie = genereaza populatie intermediara selectand din populatia(t) dupa un criteriu de selectie
#crossover/incrucisare = operator de incrucisare pe unii indivizi din prima P intermediara -> P2 intermediara
#operator de mutatie peste populatia intermediata P2 -> urmatoarea populatie / evolutie(t+1)
#dimesiune = nr de cromozomi

#etapele de selectie, incrucisare si mutatie
#metoda de codificare din curs
#incrucisarea cu un singur punct de taietura
#se tine cont de selectia de tip elitist (individul cu fitness maxim din populatia(t) va fi in populatia(t+1))

#output - prezinta detaliat operatiile din prima etapa + rezumat evolutie ptr celalalte etape
#extra - interfata grafica sugestiva care arata evolutia
#output - populatia initiala - ptr fiecare individ
        # - reprezntarea pe biti, nnumarul real, val functiei, prob de selectie
        # - prob cumulate care dau intervalele pentru selectie

#n - dimensiunea populatiei
# a,b,c - coeficientii functiei de maximizat
#precizie - precizia cu care se discretizeaza intervalul
#prob_recombinare - probabilitatea de recombinare
#prob_mutatie - probabilitatea de mutatie
#nr_etape - numarul de etape de evolutie
#domeniu - de definitie a functiei

import math
import random
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import scrolledtext


def data_input(n,a,b,c,precizie,prob_recombinare,prob_mutatie,nr_etape,domeniu):
    file = open("date.in", "r")
    n = int(file.readline().strip())  # citire dimensiune populatie
    c1, c2 = map(float, file.readline().strip().split())  # citire domeniu de definitie
    domeniu = [c1, c2]
    a,b,c = map(int, file.readline().strip().split())  # citire coeficienti
    precizie = int(file.readline().strip())  # citire precizie
    prob_recombinare = float(file.readline().strip())  # citire probabilitate de recombinare
    prob_mutatie = float(file.readline().strip())  # citire probabilitate de mutatie
    nr_etape = int(file.readline().strip())  # citire numar de etape
    if prob_recombinare > 1:
        prob_recombinare /= 100
    if prob_mutatie > 1:
        prob_mutatie /= 100
    return n, a, b, c, precizie, prob_recombinare, prob_mutatie, nr_etape, domeniu

def transf_binar(x, chromosome_length):
    binary = bin(x)[2:].zfill(chromosome_length)
    return binary

def func_max(a, b, c, x):
    return a * x ** 2 + b * x + c

def cautare_binara(x, q_selectie, n):
    st, dr = 0, n - 2
    while st <= dr:
        mij = (st + dr) // 2
        if q_selectie[mij] <= x < q_selectie[mij + 1]:
            return mij
        if x < q_selectie[mij]:
            dr = mij - 1
        else:
            st = mij + 1
    return -1


def main():
    n, a,b,c, precizie, prob_recombinare, prob_mutatie, nr_etape = 0,0, 0, 0, 0, 0, 0, 0
    domeniu = [] 
    n,a,b,c,precizie,prob_recombinare, prob_mutatie, nr_etape, domeniu=data_input(n,a,b,c,precizie,prob_recombinare,prob_mutatie,nr_etape,domeniu)
    chromosome_length = math.ceil(math.log2((domeniu[1] - domeniu[0])*(10**precizie)))
    
    population = [] # lista pentru populatia initiala
    write_file = open("Evolutie.txt", "w")
    write_file.write("Populatia initiala:\n")
    for i in range(n):
        x = random.randint(0, (1 << chromosome_length) - 1) # [0, 2^l-1]
        val_x = (domeniu[1] - domeniu[0]) * x / ((1 << chromosome_length) - 1) + domeniu[0]
        population.append(x) #adaugam cromozomul in populatie
        write_file.write(f"{i+1}: {transf_binar(x,chromosome_length)} | x= {val_x:.6f} | f= {func_max(a, b, c, val_x):.6f}\n") #scriem in fisier

    for etapa in range(nr_etape):
        total_fitness = sum(func_max(a, b, c, (domeniu[1] - domeniu[0]) * x / ((1 << chromosome_length) - 1) + domeniu[0]) for x in population) # performanta totala a populatiei
        prob_selectie = [func_max(a, b, c, (domeniu[1] - domeniu[0]) * x / ((1 << chromosome_length) - 1) + domeniu[0]) / total_fitness for x in population] # probabilitatea de selectie
        q_selectie = [sum(prob_selectie[:i+1]) for i in range(n)]
        q_selectie[0] = 0 #conventie check
        #pastram chromozomul cu fitness maxim / elitist
        elite_chromosome = population[prob_selectie.index(max(prob_selectie))]

        population_selected = [] # lista pentru populatia selectata
        if etapa == 0:
            write_file.write("\nProbabilitati selectie:\n")
            for i in range(n):
                write_file.write(f"Cromozomul {i+1}: {prob_selectie[i]:.9f}\n")
            write_file.write("\nIntervale probabilitati selectie:\n")
            for i in range(n-1):
                write_file.write(f"{i+1}. {q_selectie[i]:.9f} {q_selectie[i+1]:.9f}\n")
            
            write_file.write("\nProcesul de selectie:\n")
        # selectam cromozomii cu prob de selectie
        for i in range(n):
            u = random.random()
            index = index = cautare_binara(u, q_selectie, n) # cautam in intervalul de selectie
            if etapa == 0:
                write_file.write(f"u = {u:.6f} selectam cromozomul {index+1}\n")
            population_selected.append(index)
        # ii alegem pe cei pentru recombinare
        if etapa == 0:
             write_file.write("\nCromozomii care participa la recombinare:\n")
        population_recombination = [] # lista pentru cromozomii care participa la recombinare
        for i in range(n):
            u = random.random()
            if u < prob_recombinare:
                population_recombination.append(population_selected[i])
            if etapa == 0 and u < prob_recombinare:
                write_file.write(f"u = {u:.6f} | cromozomul {population_selected[i]+1} participa la recombinare\n")

       #facem crossover
        population_crossover = []
        for i in range(len(population_recombination)-1):
            for j in range(i+1, len(population_recombination)):
                if population_recombination[i] != population_recombination[j]: #disjuncte
                    if etapa == 0:
                        write_file.write(f"\ncromozomul {population_recombination[i]+1} cu cromozomul {population_recombination[j]+1}:\n")
                    punct_rupere = random.randint(1, chromosome_length - 1)
                    
                    mask = (1 << (chromosome_length-punct_rupere)) - 1
                    
                    population_crossover.append((population[population_recombination[i]] & ~mask) | (population[population_recombination[j]] & mask))
                    population_crossover.append((population[population_recombination[j]] & ~mask) | (population[population_recombination[i]] & mask))
                    if etapa == 0:
                        write_file.write(f"{transf_binar(population[population_recombination[i]], chromosome_length)} | {transf_binar(population[population_recombination[j]], chromosome_length)} -> intre punctul {punct_rupere}\n")
                        write_file.write(f"Rezultat {transf_binar(population_crossover[-1], chromosome_length)} | {transf_binar(population_crossover[-2], chromosome_length)}\n")
        
        if etapa == 0:
            write_file.write("\nPopulatia dupa recombinare:\n")
            for i in range(len(population_crossover)):
                val_x = (domeniu[1] - domeniu[0]) * population_crossover[i] / ((1 << chromosome_length) - 1) + domeniu[0]
                write_file.write(f"{i+1}: {transf_binar(population_crossover[i], chromosome_length)} | x= {val_x:.6f} | f= {func_max(a, b, c, val_x):.6f}\n")
        
        #mutatii
        for i in range(len(population_crossover)):
            u = random.random()
            if u < prob_mutatie: #mutatie rara
                p = random.randint(0, chromosome_length - 1) #pozitie aleatoare
                population_crossover[i] = population_crossover[i] ^ (1 << p) #inversam bitul de la pozitia p

        if etapa == 0:
            write_file.write("\nPopulatia dupa mutatie:\n")
            for i in range(len(population_crossover)):
                val_x = (domeniu[1] - domeniu[0]) * population_crossover[i] / ((1 << chromosome_length) - 1) + domeniu[0]
                write_file.write(f"{i+1}: {transf_binar(population_crossover[i], chromosome_length)} | x= {val_x:.6f} | f= {func_max(a, b, c, val_x):.6f}\n")

        population = population_crossover.copy()
        population.append(elite_chromosome) #adaugam cromozomul elitist in populatia curenta

        if etapa == 0:
            write_file.write("\n\nRestul generatiilor:\n")
        else:
            write_file.write(f"\nGeneratia curenta: {etapa+1}\n")
            write_file.write(f"Max Fitness: {func_max(a, b, c, (domeniu[1] - domeniu[0]) * elite_chromosome / ((1 << chromosome_length) - 1) + domeniu[0]):.6f}\n")
            write_file.write(f"Mean Fitness: {sum(func_max(a, b, c, (domeniu[1] - domeniu[0]) * x / ((1 << chromosome_length) - 1) + domeniu[0]) for x in population) / n:.6f}\n")
    
def evolution_show(): #update la interfata
    text_area.delete(1.0, tk.END)  # sterge continutul anterior
    write_file = open("Evolutie.txt", "r")
    content = write_file.read()
    text_area.insert(tk.END, content)  # afiseaza continutul fisierului in campul de text

def on_start_button_click():
    main()
    evolution_show()
    root.after(1000, evolution_show)
   
root = tk.Tk()
root.title("Evoluție algoritm genetic")

# camp de ttext
text_area = scrolledtext.ScrolledText(root, width=80, height=30, wrap=tk.WORD)
text_area.pack(expand=True,fill="both",side='bottom')

# buton
start_button = tk.Button(root, text="Start", command=on_start_button_click)
start_button.pack()

root.mainloop()