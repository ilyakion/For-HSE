# ДНК представляет из себя последовательность (строку) из чередований четырёх молекул (букв): аденин (A), цитозин (C), гуанин (G), тимин (T).
# РНК же состоит из чередований аденина (A), цитозина (C), гуанина (G) и урацила (U). При транскрипции ДНК в РНК.
# аденин переходит в урацил
# цитозин - в гуанин,
# гуанин - в цитозин,
# тимин - в аденин.
# Ваша задача написать функцию, которая по последовательности ДНК (например, 'AGCTAT')
# вычисляет последовательность РНК (соответственно 'UCGAUA')

def transcription(dnk):
    rnk=''
    for i in dnk:
        if i=='A':
            rnk+='U'
        elif i=='C':
            rnk+='G'
        elif i=='G':
            rnk+='C'
        elif i=='T':
            rnk+='A'
        else:
            print("eror")
            return
    return rnk
fghdngdn
