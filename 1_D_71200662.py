def fungsimakanan():
    global totalmakan
    print('=' * 25,' Menu ', '=' * 25)
    print('1. Telur Bakar           : Rp. 7.000')
    print('2. Lele Tebang           : Rp. 10.000')
    print('3. Es Coklat             : Rp. 5.000')
    print('4. Es Doger              : Rp. 13.000')
    print('=' * 25,' Pesanan ', '=' * 25)
    print()

    menu1 = int(input('Telur Bakar          : '))
    menu2 = int(input('Lele Terbang         : '))
    menu3 = int(input('Es Coklat            : '))
    menu4 = int(input('Es Doger             : '))

    #print('=' * 25, " Total ", '=' * 25)

    if menu1 == menu1 :
        totalmkn = 7000*menu1
        print('Total Telur Bakar x', menu1, ' : Rp ',totalmkn)
    elif menu2 == menu2 :
        totalmkn = 10000*menu2
        print('Total Lele Tebang x', menu2, ' : Rp', totalmkn)
        return
    elif menu3 == menu3 :
        totalmkn = 5000*menu3
        print('Total Es Coklat x',menu3, ' : Rp ', totalmkn)
        return
    elif menu4 == menu4 :
        totalmkn = 13000*menu4
        print('Total Es Doger x', menu4, ' : Rp ', totalmkn)
        return
    else:
        print('Jumlah Yang Harus Dibayar Adalah Rp ', totalmkn)
        fungsimakanan()

fungsimakanan()
