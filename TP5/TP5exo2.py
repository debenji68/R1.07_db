note = []
coefficient = []
s0= ""
somme_ponderee = 0.0
total_coefficients = 0
note_elim = False
for i in range (1,6):
    s0=((input(f"Veuillez entrer la note du module {i} et le coefficient correspondant : ")))
    values = s0.split()
    note.append(float(values[0]))
    coefficient.append(int(values[1]))
for i in range(len(note)):
    if int(note[i]) < 8:
        note_elim = True
    somme_ponderee += note[i] * coefficient[i]
    total_coefficients += coefficient[i]

moyenne_generale = somme_ponderee / total_coefficients
condition_moyenne = moyenne_generale > 10
condition_note_min = not note_elim

if condition_moyenne and condition_note_min:
    print("\nL'étudiant est ADMIS.")
else:
    print("\nL'étudiant n'est PAS ADMIS.")