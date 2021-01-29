import math
from forEgitim import *
import numpy as np

def sigmoid(x):
    ans = 1 / (1 + math.exp(-x))
    return ans


def araKatmaniGuncelle(hata,w,op,iterasyonBilgisi,guncellemeBilgisi):
    hataBar = []

    for i in range(0,len(w[0])):
        hataBar.append(op[i] * (1 - op[i]) * (w[0][i] * hata[0] + w[1][i] * hata[1]))

    for i in range(0, 10):  # wbar GUNCELLEME
        for j in range(0, 23):
            wBarYeni.append(
                wBar[j][i] + wBarGuncellemeMiktari(hataBar[i], Pgiris[j][iterasyonBilgisi], guncellemeBilgisi, j))
            wbarguncellemeMik[j].pop(guncellemeBilgisi)

    for i in range(0,len(biasBar)):
        biasBarYeni.append(biasBar[i] + biasBarGuncellemeMiktari(hataBar[i],guncellemeBilgisi))
        bbarguncellemeMik.pop(guncellemeBilgisi)


def biasBarGuncellemeMiktari(hataBar,guncellemeBilgisi):
    deltabiasbar = nu*hataBar + alfa*bbarguncellemeMik[guncellemeBilgisi]
    bbarguncellemeMik.append(deltabiasbar)
    return deltabiasbar

def wBarGuncellemeMiktari(hataBar,xp,guncellemeBilgisi,j):
    deltawbar = nu*hataBar*xp+wbarguncellemeMik[j][guncellemeBilgisi]*alfa
    wbarguncellemeMik[j].append(deltawbar)
    return deltawbar


def cikisKatmaniGuncelle(op1, op2, op, target, nu, alfa, w, bias, iterasyonBilgisi, guncellemeBilgisi):
    hata = (target[0]-op1)*op1*(1-op1)
    hata1 = (target[1]-op2)*op2*(1-op2)
    hatalar = [hata, hata1]
    for i in range(0,len(w[0])):   # 1 nolu cikis noronuna giden w lar
        wYeni.append(w[0][i] + wGuncellemeMiktari(op[i], nu, alfa, hata, guncellemeBilgisi, 0))
        wguncellemeMik[0].pop(guncellemeBilgisi)

    for i in range(0, len(w[1])):   # 2 nolu cikis noronuna giden w lar
        wYeni.append(w[1][i] + wGuncellemeMiktari(op[i], nu, alfa, hata1, guncellemeBilgisi, 1))
        wguncellemeMik[1].pop(guncellemeBilgisi)


    for i in range(0,len(bias)):
        biasYeni.append(bias[i]+biasGuncellemeMiktari(nu,hatalar[i],alfa,guncellemeBilgisi))
        bguncellemeMik.pop(guncellemeBilgisi)

    araKatmaniGuncelle(hatalar, w, op, iterasyonBilgisi, guncellemeBilgisi)


def wGuncellemeMiktari(op,nu,alfa,hata,guncellemeBilgisi,i):
    deltaw = nu * hata * op + wguncellemeMik[i][guncellemeBilgisi] * alfa
    wguncellemeMik[i].append(deltaw)
    return deltaw

def biasGuncellemeMiktari(nu,hata,alfa,guncellemeBilgisi):
    deltab = nu*hata+alfa*bguncellemeMik[guncellemeBilgisi]
    bguncellemeMik.append(deltab)
    return deltab

def calculateV(i,op,bi):
    x = 0
    for j in range(0,23):
        x = x + Pgiris[j][i] * wBar[j][op]
    x = x + bi
    return x

if __name__ == '__main__':

    target = Levels
    nu = 0.6 #momentum katsayisi 0.6-0.8
    alfa = 0.5# ogrenme katsayisi 0 - 1
    biasBar = [0.612, 0.553, 0.814, 0.535, 0.745,0.612, 0.553, 0.814, 0.535, 0.745]
    wBar = [[0.39003898 ,0.80438863,0.97274102 ,0.70464998, 0.58293415,0.39003898 ,0.80438863,0.97274102 ,0.70464998, 0.58293415],
             [0.27724255, 0.48599125, 0.64315834, 0.3012671 , 0.39380036,0.78262914 ,0.5679381 , 0.70889579, 0.1667466,  0.95553792],
             [0.58627725 ,0.34312827, 0.15569347, 0.9506881 , 0.6121192 ,0.39003898 ,0.80438863,0.97274102 ,0.70464998, 0.58293415],
             [0.50501318, 0.82751435, 0.31833272, 0.07945444 ,0.63026526,0.78262914 ,0.5679381 , 0.70889579, 0.1667466,  0.95553792],
             [0.60117447, 0.41037528, 0.68990818 ,0.57178124, 0.79435591,0.83717803, 0.72089388, 0.71023595, 0.05875828, 0.02197396],
             [0.27359228 ,0.39987033, 0.59602468, 0.77692921, 0.16585439,0.83717803, 0.72089388, 0.71023595, 0.05875828, 0.02197396],
             [0.14365746, 0.9378136 , 0.57894125, 0.22246333, 0.54928799,0.78262914 ,0.5679381 , 0.70889579, 0.1667466,  0.95553792],
             [0.25643875, 0.15484043, 0.40362156 ,0.14563059, 0.75990885,0.25643875, 0.15484043, 0.40362156 ,0.14563059, 0.75990885],
             [0.66247897, 0.54241767, 0.3981583 , 0.31939565, 0.71873753,0.83717803, 0.72089388, 0.71023595, 0.05875828, 0.02197396],
             [0.22036362 ,0.17917825, 0.9850608 , 0.37409281, 0.91128049,0.39003898 ,0.80438863,0.97274102 ,0.70464998, 0.58293415],
             [0.11629522, 0.84793744, 0.0977005,  0.70334993, 0.24281955,0.39003898 ,0.80438863,0.97274102 ,0.70464998, 0.58293415],
             [0.50202576, 0.66512274, 0.89408569, 0.13007066, 0.76065556,0.78262914 ,0.5679381 , 0.70889579, 0.1667466,  0.95553792],
             [0.75768729, 0.5675139 , 0.08389441 ,0.78492602, 0.5709849 ,0.39003898 ,0.80438863,0.97274102 ,0.70464998, 0.58293415],
             [0.97721548 ,0.89954754 ,0.08544426 ,0.71786267, 0.78479269,0.25643875, 0.15484043, 0.40362156 ,0.14563059, 0.75990885],
             [0.75665249, 0.73390491, 0.61103053, 0.58816452, 0.71678397,0.78262914 ,0.5679381 , 0.70889579, 0.1667466,  0.95553792],
             [0.83717803, 0.72089388, 0.71023595, 0.05875828, 0.02197396,0.25643875, 0.15484043, 0.40362156 ,0.14563059, 0.75990885],
             [0.69085855 ,0.02017029, 0.13948269, 0.64924042, 0.27597445,0.25643875, 0.15484043, 0.40362156 ,0.14563059, 0.75990885],
             [0.64821913, 0.33684823, 0.31781877, 0.88251822, 0.81901155,0.39003898 ,0.80438863,0.97274102 ,0.70464998, 0.58293415],
             [0.6925028,  0.69016818, 0.8127688,  0.15105471, 0.67532981,0.25643875, 0.15484043, 0.40362156 ,0.14563059, 0.75990885],
             [0.59696779, 0.4943355 , 0.84947358 ,0.57711343, 0.23367012,0.83717803, 0.72089388, 0.71023595, 0.05875828, 0.02197396],
             [0.69305722, 0.27939649, 0.72687244 ,0.35535488 ,0.98927133,0.39003898 ,0.80438863,0.97274102 ,0.70464998, 0.58293415],
             [0.99117806, 0.60217756 ,0.63163201, 0.76050322, 0.03820735,0.25643875, 0.15484043, 0.40362156 ,0.14563059, 0.75990885],
             [0.78262914 ,0.5679381 , 0.70889579, 0.1667466,  0.95553792,0.83717803, 0.72089388, 0.71023595, 0.05875828, 0.02197396]]

   # arr = np.random.random((23,5))
    w = [[0.51909, 0.39335, 0.49568, 0.05013, 0.75279,0.05369, 0.23932, 0.45669, 0.36924, 0.58238], [0.05369, 0.23932, 0.45669, 0.36924, 0.58238,0.51909, 0.39335, 0.49568, 0.05013, 0.75279]]
    bias = [0.976, 0.123]
    wbarguncellemeMik = [[0]*10]*23
    bguncellemeMik = [0,0]
    wguncellemeMik = [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]
    bbarguncellemeMik = [0,0,0,0,0,0,0,0,0,0]
    guncellemeBilgisi = 0
    wBarYeni = []
    biasBarYeni = []
    wYeni = []
    biasYeni = []
    araKatman = 2
    epoch = 100000
    itterasyon = 700
    opbar = []
    for k in range(0, epoch):
        iterasyonBilgisi = 0
        for i in range(0, itterasyon):
            V = []
            for j in range(0, 10):
                V.append(calculateV(iterasyonBilgisi, j, biasBar[j]))
            op1bar = sigmoid(V[0])
            op2bar = sigmoid(V[1])
            op3bar = sigmoid(V[2])
            op4bar = sigmoid(V[3])
            op5bar = sigmoid(V[4])
            op6bar = sigmoid(V[5])
            op7bar = sigmoid(V[6])
            op8bar = sigmoid(V[7])
            op9bar = sigmoid(V[8])
            op0bar = sigmoid(V[9])

            op1 = sigmoid(op1bar * w[0][0] + op2bar * w[0][1] + op3bar * w[0][2] + op4bar * w[0][3] + op5bar * w[0][4] + op6bar * w[0][5] + op7bar * w[0][6] + op8bar * w[0][7] + op9bar * w[0][8]+ op0bar * w[0][9]+bias[0])
            op2 = sigmoid(op1bar * w[1][0] + op2bar * w[1][1] + op3bar * w[1][2] + op4bar * w[1][3] + op5bar * w[1][4]  + op6bar * w[1][5] + op7bar * w[1][6] + op8bar * w[1][7] + op9bar * w[1][8]+ op0bar * w[1][9] + bias[1])
            if round(op1, 3) > 0.990:
                op1 = 1
            if round(op2, 3) > 0.990:
                op2 = 1
            if round(op1, 3) < 0.009:
                op1 = 0
            if round(op2, 3) < 0.009:
                op2 = 0
            op = [op1bar, op2bar, op3bar, op4bar, op5bar,op6bar,op7bar,op8bar,op9bar,op0bar]
            if op1 != target[i][0] or op2 != target[i][1]:
                cikisKatmaniGuncelle(op1, op2, op, target[i], nu, alfa, w, bias, iterasyonBilgisi, guncellemeBilgisi)

                sayac = 0
            ## Yeni degerleri ata
                for i in range(0,2):
                    for j in range(0,10):
                        w[i][j] = wYeni[sayac]
                        sayac = sayac + 1
                for i in range(0,len(bias)):
                    bias[i] = biasYeni[i]
                sayac1 = 0
                for i in range(0,10):
                    for j in range(0,23):
                        wBar[j][i] = wBarYeni[sayac1]
                        sayac1 = sayac1 + 1
                for i in range(0,len(biasBar)):
                    biasBar[i] = biasBarYeni[i]
                wYeni.clear()
                biasBarYeni.clear()
                wBarYeni.clear()
                biasYeni.clear()
            iterasyonBilgisi += 1
            if k == epoch-1:
                print(op1)
                print(op2)
                print(w)
                print(bias)
                print(wBar)
                print(biasBar)


