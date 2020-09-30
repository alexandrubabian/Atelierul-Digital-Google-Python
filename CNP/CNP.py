while True:
    cnp=input("Introduceti cnp-ul:")
    if cnp.isdigit() and len(cnp)==13:
        if cnp[0]=='3' or cnp[0]=='4':
            ok=1;
        elif cnp[0]=='0':
            print("CNP-ul este invalid pentru ca prima cifra nu poate sa fie 0\n")
            break
        if (cnp[0]=='5' or cnp[0]=='6') and int(cnp[1:3])>20:
            print("CNP-ul este invalid intrucat nu s-a nascut\n")
            break
        elif int(cnp[3:5])>12 or int(cnp[3:5])==0:
            print("CNP-ul este invalid pentru ca lunile trb sa fie intre 1 si 12\n")
            break
        else:
            #keep on going
            luna=int(cnp[3:5])
            an=int(cnp[1:3])
            if an%4==0 and luna==2 and int(cnp[5:7])>29:
                print("CNP-ul este invalid intrucat ziua trb sa fie mai mica ca 30 in februarie in an bisect\n")
                break
            elif an%4!=0 and luna==2 and int(cnp[5:7])>28:
                print("CNP-ul este invalid intrucat ziua trb sa fie mai mica ca 29 in februarie in an obisnuit\n")
                break
            else:
                nr31=[1, 3, 5, 7, 8, 10,12]
                nr30=(4, 6, 9, 11)
                if (luna in nr31) and int(cnp[5:7])>31:
                    print("CNP-ul este invalitd intrucat luna are peste 31 de zile\n")
                    break
                elif (luna in nr30) and int(cnp[5:7])>30:
                    print("CNP-ul este invalid intrucat este o luna cu 30de zile dar ziua este peste 30\n")
                    break
                else:
                    #keep on going
                    if int(cnp[7:9])>52 or cnp[7:9]=='00':
                        print("CNP-ul este invalid pentru ca nu exista acest cod de judet\n")
                        break
                    else:
                        #keep on going
                        if cnp[9:12] == '000':
                            print("CNP-ul este invalid incat indexul dat de judet nu poate fi 000\n")
                            break
                        else:
                            #keep on checking
                            auxiliar='279146358279'
                            suma=0
                            for i in range(12):
                                suma=suma + int(cnp[i])*int(auxiliar[i])
                            rest=suma%11
                            if (rest == 10 and cnp[12]!='1') or (rest!=int(cnp[12])):
                                print("CNP-ul este invalid pt ca cifra de control nu este corecta\n")
                                break
                            else:
                                print("CNP-ul introdus este valid\n")
    else:
        print("ati introdus un sir de caractere care nu e format doar din cifre sau nu are 13 cifre\n")
        break




