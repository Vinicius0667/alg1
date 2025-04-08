n1, n2, n3, n4 = map(float, input().split())

media = (n1 * 2 + n2 * 3 + n3 * 4 + n4) / 10

print(f'Media: {media:.1f}')

if media >= 7:
    print('Aluno aprovado.')
elif media >= 5 and media <= 6.9:
    rec = float(input())
    print(f'Aluno em exame.\nNota do exame: {rec:.1f}')
    media_rec = (media + rec) / 2
    if media_rec >= 5:
        print(f'Aluno aprovado.\nMedia final: {media_rec}')
else:
    print('Aluno reprovado.')