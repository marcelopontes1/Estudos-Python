trab_lab = input('Insira aqui a nota do laboratório: ')
aval_sem = input('Insira aqui a nota da avaliação semestral: ')
exam_final = input('Insira aqui a nota do exame final: ')

trab_lab_convert = float(trab_lab)
aval_sem_convert = float(aval_sem)
exam_final_convert = float(exam_final)

media_ponderada = ((trab_lab_convert * 2) + (aval_sem_convert * 3) + (exam_final_convert * 5))/10

print(media_ponderada)

if media_ponderada >= 0 and media_ponderada <= 2.9:
    print('Reprovado')
elif media_ponderada >= 3 and media_ponderada <= 4.9:
    print('Recuperação')
else:
    print('Aprovado')
