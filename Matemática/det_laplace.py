def calc_det(mtz):
    if len(mtz) == 2:
        return mtz[0][0]*mtz[1][1] - mtz[0][1]*mtz[1][0]
    
    cofatores = []

    # Percorre pelos elementos utilizados para cofatores 
    for x in range(len(mtz)):
        mtz_interna = [[] for s in range(len(mtz)-1)]

        # Percorre a matriz
        for i in range(len(mtz)):

            for j in range(len(mtz)):    
            
                # Adiciona elemento que não seja da mesma linha e coluna
                if i != 0 and j != x:
                    mtz_interna[i-1].append(mtz[i][j])

        # Calcula o cofator do elemento x
        cof_x = mtz[0][x] * calc_det(mtz_interna) * ((-1) ** (x + 2))

        cofatores.append(cof_x)

    return sum(cofatores)

# Exemplo
mtz = [
    [-5,2,3,-4],
    [0,2,0,0],
    [-5,2,-3,0],
    [-8,2,3,1],
]

print(calc_det(mtz))

