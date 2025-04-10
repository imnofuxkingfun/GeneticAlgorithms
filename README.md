# Algoritmi Genetici
Implementați un algoritm genetic pentru determinarea maximului unei funcții pozitive pe un domeniu dat. Funcția va fi un polinom de gradul 2, cu coeficienți dați.
Algoritmul trebuie să cuprindă etapele de selecție, încrucișare (crossover) și mutație.

## Precizări
Se vor folosi metoda de codificare discutată la curs și încrucișarea cu un singur punct de tăietură/de rupere. Se va ține cont și de selecția de tip elitist (individul cu fitness-ul cel mai mare va trece automat în generația următoare).


## Date de intrare
• Dimensiunea populației (numărul de cromozomi)
• Domeniul de definiție al funcției (capetele unui interval închis)
• Parametrii pentru funcția de maximizat (coeficienții polinomului de grad 2)
• Precizia cu care se lucrează (cu care se discretizează intervalul)
• Probabilitatea de recombinare (crossover, încrucișare)
• Probabilitatea de mutație
• Numărul de etape al algoritmului

## Date de ieșire
• Un fișier text sugestiv care prezintă detaliat operațiile efectuate
în prima etapă a algoritmului, iar apoi un rezumat al evoluției
populației pentru celelalte etape.
Un exemplu este fișierul Evolutie.txt, care a fost obținut pentru
funcția −x2 + x + 2, domeniul [−1, 2], dimensiunea populației 20,
precizia 6, probabilitatea de recombinare 25%, probabilitatea de
mutație 1% și 50 de etape.
• Extra: o interfață grafică sugestivă, care afișează evoluția algo-
ritmului.

## Conținut fișier de ieșire
În fișier vor fi incluse cel puțin următoarele informații:
• Populația inițială, cu următoarele date pentru fiecare individ
– reprezentarea pe biți a cromozomului;
– valoarea corespunzătoare cromozomului în domeniul de
definiție al funcției (număr real);
– valoarea cromozomului, adică valoarea funcției în punc-
tul din domeniu care corespunde acestuia.
• Probabilitățile de selecție pentru fiecare cromozom;
• Probabilitățile cumulate care dau intervalele pentru selecție;
• Evidențierea procesului de selecție, care constă în generarea unui număr aleator u uniform pe [0, 1) și determinarea intervalului [qi, qi+1) căruia aparține acest număr; corespunzător acestui interval se va selecta cromozomul i + 1. Procesul se repetă până se selectează numărul dorit de cromozomi. Cerință: căutarea intervalului corespunzător se va face folosind căutarea binară.
• Evidențierea cromozomilor care participă la recombinare.
• Pentru recombinările care au loc se evidențiază perechile de cromozomi care participă la recombinare, punctul de rupere generat aleator precum și cromozomii rezultați în urma recombinării (sau, după caz, se evidențiază tipul de încrucișare ales).
• Populația rezultată după recombinare.
• Populația rezultată după mutațiile aleatoare.
• Pentru restul generațiilor (populațiile din etapele următoare) se va afișa doar valoarea maximă și valoarea mediei a fitnessului (performanței) populației.
