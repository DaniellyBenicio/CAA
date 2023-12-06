'''
sum = 0;   É executado em tempo constante O(1)
for ( int i =0; i < n ; i ++) {     Itera N vezes, então O(n)
for ( int j =1; j <= n ; j ++) {    Itera N vezes, então O(n)
sum ++;      É executado em tempo constante O(1)
} 
}


Logo, o custo do laço será  O(n) x O(n) = O(n²) 
significando que o tempo aumenta quadraticamente com o tamanho da entrada n.
'''


'''
sum = 0;      É executado em tempo constante O(1)
for ( int i =1; i < n ; i *=2) {    O loop itera log(n) porque o i está sendo dobrado exponencialmente 
a cada iteração, logo, o tempo de complexidade é O(logn).
for ( int j =1; j <= n ; j ++) {    Itera N vezes, então O(n)
sum ++;      É executado em tempo constante O(1)
}
}


A complexidade de tempo desse algoritmo então vai ser O(log n) x O(n) = O(n log n). '''

'''
sum = 0;      É executado em tempo constante O(1)
for ( int i =0; i < n ; i *=2) {    O i sempre será zero, pois qualquer que seja o número multiplicado por zero
é zero. Dessa forma, esse loop nunca encerrará, ficará um loop infinito.
for ( int j =1; j <= n ; j += i ) { Nesse loop o j sempre será incrementado + i e ele sempre será 0, então
j sempre será menor que o n.
sum ++;      É executado em tempo constante O(1)
}
}


Desse modo, não tem como avaliar a complexidade de tempo, do custo dos laços nesse algoritmo, visto que
ele retorna um loop infinito.
'''