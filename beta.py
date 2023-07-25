import pandas as pd
import json
import os
import datetime as dt
import csv
from tabulate import tabulate

os.system('cls')

table = [["Nomer", "Nama Tanaman"],
        ["1", "Padi"],
        ["2", "Jagung"],
        ["3", "Kedelai"],
        ["4", "Tebu"],
        ["5", "Cabai"],
        ["6", "Tomat"],
        ["7", "Kembali ke main menu"],
]

def validasiLogin(nama, password):
    dict = {}
    kondisi = False
    with open("users.json", "r") as data:
        reader = json.load(data)

    for i in reader:     
        if nama == i["nama"]:
            dict["nama"] = i["nama"]
            dict["pw"] = i["pw"]
            dict["isAdmin"] = i["isAdmin"]
    if dict == {}:
        return kondisi
    else:
        if password != dict["pw"]:
            return kondisi
        else:
            kondisi = True
    return [kondisi, dict["isAdmin"]]

def menuperencanaan():
    os.system("cls")
    print(tabulate(table, headers = "firstrow", tablefmt = "fancy_grid", stralign = "center", numalign = "center"))
    inputan1 = int(input("Pilih nomer : "))
    if inputan1 == 1:
        os.system("cls")
        bibitPadi = float(input("Masukkan jumlah bibit padi dalam kg : "))
        luas1 = bibitPadi/60
        pupukurea1 = luas1*300
        pupuksp361 = luas1*100
        pupukkcl1 = luas1*100
        pupuk1 = pupukurea1 + pupuksp361 + pupukkcl1
        print(f"Luas lahan yang diperlukan = {luas1:.2f} hektar")
        print(f"Jumlah pupuk yang diperlukan = {pupuk1:.2f} kg")
    elif inputan1 == 2:
        os.system("cls")
        bibitJagung = float(input("Masukkan jumlah bibit jagung dalam kg : "))
        luas2 = bibitJagung/25
        pupukurea2 = luas2*200
        pupuknpk2 = luas2*300
        pupuk2 = pupukurea2 + pupuknpk2
        print(f"Luas lahan yang dibutuhkan = {luas2:.2f} hektar")
        print(f"Jumlah pupuk yang diperlukan = {pupuk2:.2f} kg")
    elif inputan1 == 3:
        os.system("cls")
        bibitKedelai = float(input("Masukkan jumlah bibit kedelai dalam kg : "))
        luas3 = bibitKedelai/40
        pupuksp363 = luas3*125
        print(f"Luas lahan yang dibutuhkan = {luas3:.2f} hektar")
        print(f"Jumlah pupuk yang diperlukan = {pupuksp363:.2f} kg")
    elif inputan1 == 4:
        os.system("cls")
        bibitTebu = float(input("Masukkan jumlah batang tebu : "))
        luas4 = bibitTebu/12000
        pupukurea4 = luas4*244
        pupuktsp4 = luas4*283
        pupukkcl4 = luas4*567
        pupuk4 = pupukurea4 + pupuktsp4 + pupukkcl4
        print(f"Luas lahan yang dibutuhkan = {luas4:.2f} hektar")
        print(f"Jumlah pupuk yang diperlukan = {pupuk4:.2f} kg")
    elif inputan1 == 5:
        os.system("cls")
        bibitCabai = float(input("Masukkan jumlah bibit cabai dalam gram : "))
        luas5 = bibitCabai/300
        pupukkandang5 = luas5*10000
        pupukurea5 = luas5*200
        pupuksp365 = luas5*200
        pupukkcl5 = luas5*150
        pupuk5 = pupukkandang5 + pupukurea5 + pupuksp365 + pupukkcl5
        print(f"Luas lahan yang dibutuhkan = {luas5:.2f} hektar")
        print(f"Jumlah pupuk yang diperlukan = {pupuk5:.2f} kg")
    elif inputan1 == 6:
        os.system("cls")
        bibitTomat = float(input("Masukkan jumlah bibit tomat dalam gram : "))
        luas6 = bibitTomat/150
        pupukurea6 = luas6*125
        print(f"Luas lahan yang dibutuhkan = {luas6:.2f} hektar")
        print(f"Jumlah pupuk yang diperlukan = {pupukurea6:.2f} kg")
    elif inputan1 == 7:
        os.system('cls')
        mainMenu()
    else:
        input("Masukkan data yang benar!\nUntuk lanjut tekan enter")
        menuperencanaan()

    inputan3 = int(input("[1] Kembali ke Main Menu\n[2] Akhiri Program\n"))
    if inputan3 == 1:
        os.system("cls")
        mainMenu()
    elif inputan3 == 2:
        outro()

def buatjadwal () :
    os.system("cls")
    Lahanbaru = input("Masukkan Nama Lahan Baru : ")
    pilihjenis = int(input("Pilih Jenis Tanaman\n[1] Padi\n[2] Jagung\n[3] Kedelai\n[4] Tebu\n[5] Cabai\n[6] Tomat\nSilahkan Pilih Jenis Tanaman : "))
    datatanaman = pd.read_csv('datatanaman.csv')
    listdatatanaman = pd.read_csv('data.csv')
    datasementara = [len(listdatatanaman)+1,f"{Lahanbaru}"]

    if pilihjenis == 1 :
        bacadata = datatanaman.iloc[0,0:]
        for i in bacadata :
            datasementara.append(f"{i}")
            
        filejadwalbaru = open("data.csv", "a", newline='')
        writer = csv.writer(filejadwalbaru)
        writer.writerows([datasementara])
        filejadwalbaru.close()
        os.system('cls')
        menupenjadwalan()    
    elif pilihjenis == 2 :
        bacadata = datatanaman.iloc[1,0:]
        for i in bacadata :
            datasementara.append(f"{i}")
            
        filejadwalbaru = open("data.csv", "a", newline='')
        writer = csv.writer(filejadwalbaru)
        writer.writerows([datasementara])
        filejadwalbaru.close()
        os.system('cls')
        menupenjadwalan()    
    elif pilihjenis == 3 :
        bacadata = datatanaman.iloc[2,0:]
        for i in bacadata :
            datasementara.append(f"{i}")
            
        filejadwalbaru = open("data.csv", "a", newline='')
        writer = csv.writer(filejadwalbaru)
        writer.writerows([datasementara])
        filejadwalbaru.close()
        os.system('cls')
        menupenjadwalan()    
    elif pilihjenis == 4 :
        bacadata = datatanaman.iloc[3,0:]
        for i in bacadata :
            datasementara.append(f"{i}")
            
        filejadwalbaru = open("data.csv", "a", newline='')
        writer = csv.writer(filejadwalbaru)
        writer.writerows([datasementara])
        filejadwalbaru.close()
        os.system('cls')
        menupenjadwalan()    
    elif pilihjenis == 5 :
        bacadata = datatanaman.iloc[4,0:]
        for i in bacadata :
            datasementara.append(f"{i}")
            
        filejadwalbaru = open("data.csv", "a", newline='')
        writer = csv.writer(filejadwalbaru)
        writer.writerows([datasementara])
        filejadwalbaru.close()
        os.system('cls')
        menupenjadwalan()    
    elif pilihjenis == 6 :
        bacadata = datatanaman.iloc[5,0:]
        for i in bacadata :
            datasementara.append(f"{i}")
            
        filejadwalbaru = open("data.csv", "a", newline='')
        writer = csv.writer(filejadwalbaru)
        writer.writerows([datasementara])
        filejadwalbaru.close()
        os.system('cls')
        menupenjadwalan()    
    else :
        os.system("cls")
        print("Pilihan Salah, Masukkan Jenis Tanaman yang Benar")
        buatjadwal()

def macamlahan():
    print("Lahan yang ada :")
    listlahan = pd.read_csv('data.csv')
    nilaikosong = 0
    for x in range(len(listlahan)):
        if nilaikosong < len(listlahan) :
            print(f"[{listlahan.iloc[nilaikosong,0]}]" , f"{listlahan.iloc[nilaikosong,1]}")
            nilaikosong += 1
        else :
            break
    banyaklahan()

def banyaklahan() :
    lanjut = int(input("[0] Kembali\nMasukkan Pilihan anda : "))
    listlahan2 = pd.read_csv('data.csv')
    listkosong = []
    listkosongcolumn = []
    for y in listlahan2.iloc[lanjut - 1 , :] :
        listkosong.append([f"{y}"])

    for z in listlahan2 :
        listkosongcolumn.append(f"{z}")

    dictkosong = {}
    arraykosong = 0
    for r in range(len(listkosong)) :
        dictkosong[f'{listkosongcolumn[arraykosong]}'] = listkosong[arraykosong]
        arraykosong += 1
    df = pd.DataFrame(dictkosong)
    os.system("cls")
    if lanjut == 0 :
        menupenjadwalan()
    else :
        df.iloc[0,3] = f"{df.iloc[0,3]} Hari"
        if df.iloc[0,4] != 'nan' :
            df.iloc[0,4] = f"Hari ke-{df.iloc[0,4]}"
        if df.iloc[0,5] != 'nan' :      
            df.iloc[0,5] = f"Hari ke-{df.iloc[0,5]}"
        if df.iloc[0,6] != 'nan' :      
            df.iloc[0,6] = f"Hari ke-{df.iloc[0,6]}"
        if df.iloc[0,7] != 'nan' :      
            df.iloc[0,7] = f"Hari ke-{df.iloc[0,7]}"

        if df.iloc[0,4] == 'nan' :
            df.iloc[0,4] = "-"
        if df.iloc[0,5] == 'nan' :      
            df.iloc[0,5] = "-"
        if df.iloc[0,6] == 'nan' :      
            df.iloc[0,6] = "-"
        if df.iloc[0,7] == 'nan' :      
            df.iloc[0,7] = "-"
        
        print(df.iloc[0,1],"\n")
        print(df)
    inputan3 = int(input("[1] Kembali ke Main Menu\n[2] Akhiri Program\n"))
    if inputan3 == 1:
        os.system("cls")
        mainMenu()
    elif inputan3 == 2:
        outro()

def hapuslahan() :
    buka = pd.read_csv('data.csv')
    print("Pilih Lahan Yang Ingin Anda Hapus")
    nilaikosong = 0
    for x in range(len(buka)):
        if nilaikosong < len(buka) :
            print(f"[{buka.iloc[nilaikosong,0]}]" , f"{buka.iloc[nilaikosong,1]}")
            nilaikosong += 1
        else :
            break   
    pilihan = int(input("[0] Kembali \nMasukkan Pilihan Anda : "))
    if pilihan == 0 :
        menupenjadwalan()
    else :

        columnskosong = []
        row = []
        for i in buka :
            columnskosong.append(i)  

        for j in range (len(buka)) :
            
            row.append([buka.iloc[j,0],buka.iloc[j,1],buka.iloc[j,2],buka.iloc[j,3],buka.iloc[j,4],buka.iloc[j,5],buka.iloc[j,6],buka.iloc[j,7]])
        df = pd.DataFrame(row , columns=columnskosong)
        indexkosong = []
        for k in range(len(df)-1) :
            indexkosong.append(k)

        df = df.drop(pilihan-1)
        df.index = [indexkosong]

        for x in range(len(df)) :
            df.iloc[x,0] = x + 1

        df.to_csv('data.csv',index=False)
        inputan3 = int(input("[1] Kembali ke Main Menu\n[2] Akhiri Program\n"))
        if inputan3 == 1:
            os.system("cls")
            mainMenu()
        elif inputan3 == 2:
            outro()

def menupenjadwalan():   
    os.system("cls") 
    pilihan = int(input("Menu Penjadwalan\n[1] Jadwal Yang Sudah Ada\n[2] Buat Jadwal Baru\n[3] Hapus Lahan\nSilahkan Pilih Menu : "))
    if pilihan == 1 :
        os.system("cls")
        macamlahan()
                
    elif pilihan == 2 :
        os.system("cls")
        print("Buat Jadwal Baru")
        buatjadwal()
    elif pilihan == 3 :
        os.system("cls")
        print("Hapus Lahan")
        hapuslahan()

    else :
        os.system("cls")
        print("Maaf jawaban anda tidak ada di pilihan")
        menupenjadwalan()

def menuperhitungan():
    hargaurea = 20000
    hargasp36 = 9000
    hargakcl = 20000
    harganpk = 215000
    hargatsp = 16000
    hargakandang = 11500
    os.system("cls")
    print(tabulate(table, headers = "firstrow", tablefmt = "fancy_grid", stralign = "center", numalign = "center"))
    inputan2 = int(input("Pilih Nomer : "))
    if inputan2 == 1:
        os.system("cls")
        bibitPadi = float(input("Masukkan jumlah bibit padi dalam kg : "))
        luas1 = bibitPadi/60
        biayaSewa = luas1 * 10000000
        pupukurea1 = luas1*300
        pupuksp361 = luas1*100
        pupukkcl1 = luas1*100
        biayaPupuk = (pupukurea1 * hargaurea) + (pupuksp361 * hargasp36) + (pupukkcl1 * hargakcl)
        print(f"Biaya sewa lahan yg diperlukan adalah Rp {biayaSewa:.2f}")
        print(f"Biaya pupuk yang diperlukan adalah Rp {biayaPupuk:.2f}")
    elif inputan2 == 2:
        os.system("cls")
        bibitJagung = float(input("Masukkan jumlah bibit jagung dalam kg : "))
        luas2 = bibitJagung/25
        biayaSewa = luas2 * 1000000
        pupukurea2 = luas2*200
        pupuknpk2 = luas2*300
        biayaPupuk = (pupukurea2 * hargaurea) + (pupuknpk2 * harganpk)
        print(f"Biaya sewa lahan yg diperlukan adalah Rp {biayaSewa:.2f}")
        print(f"Biaya pupuk yang diperlukan adalah Rp {biayaPupuk:.2f}")
    elif inputan2 == 3:
        os.system("cls")
        bibitKedelai = float(input("Masukkan jumlah bibit kedelai dalam kg : "))
        luas3 = bibitKedelai/40
        biayaSewa = luas3 * 1000000
        pupuksp363 = luas3*125
        biayaPupuk = (pupuksp363 * hargasp36)
        print(f"Biaya sewa lahan yg diperlukan adalah Rp {biayaSewa:.2f}")
        print(f"Biaya pupuk yang diperlukan adalah Rp {biayaPupuk:.2f}")
    elif inputan2 == 4:
        os.system("cls")
        bibitTebu = float(input("Masukkan jumlah batang tebu : "))
        luas4 = bibitTebu/12000
        biayaSewa = luas4 * 1000000
        pupukurea4 = luas4*244
        pupuktsp4 = luas4*283
        pupukkcl4 = luas4*567
        biayaPupuk = (pupukurea4 * hargaurea) + (pupuktsp4 * hargatsp) + (pupukkcl4 * hargakcl)
        print(f"Biaya sewa lahan yg diperlukan adalah Rp {biayaSewa:.2f}")
        print(f"Biaya pupuk yang diperlukan adalah Rp {biayaPupuk:.2f}")
    elif inputan2 == 5:
        os.system("cls")
        bibitCabai = float(input("Masukkan jumlah bibit cabai dalam gram : "))
        luas5 = bibitCabai/300
        biayaSewa = luas5 * 1000000
        pupukkandang5 = luas5*10000
        pupukurea5 = luas5*200
        pupuksp365 = luas5*200
        pupukkcl5 = luas5*150
        biayaPupuk = (pupukkandang5 * hargakandang) + (pupukurea5 * hargaurea) + (pupuksp365 * hargasp36) + (pupukkcl5 * hargatsp)
        print(f"Biaya sewa lahan yg diperlukan adalah Rp {biayaSewa:.2f}")
        print(f"Biaya pupuk yang diperlukan adalah Rp {biayaPupuk:.2f}")
    elif inputan2 == 6:
        os.system("cls")
        bibitTomat = float(input("Masukkan jumlah bibit tomat dalam gram : "))
        luas6 = bibitTomat/150
        biayaSewa = luas6 * 1000000
        pupukurea6 = luas6*125
        biayaPupuk = (pupukurea6 * hargaurea)
        print(f"Biaya sewa lahan yg diperlukan adalah Rp {biayaSewa:.2f}")
        print(f"Biaya pupuk yang diperlukan adalah Rp {biayaPupuk:.2f}")
    elif inputan2 == 7:
        os.system('cls')
        mainMenu()
    else:
        input("Masukkan data yang benar!\nUntuk lanjut tekan enter")
        menuperhitungan()
    
    inputan3 = int(input("[1] Kembali ke Main Menu\n[2] Akhiri Program\n"))
    if inputan3 == 1:
        os.system("cls")
        mainMenu()
    elif inputan3 == 2:
        outro()

def rekomendasiPenanaman():
    os.system("cls")
    print("Rekomendasi Penanaman".center(80, "="))
    print("""Pilih jenis tanaman yang anda cari
    1. Padi
    2. Jagung
    3. Kedelai
    4. Tebu
    5. Cabai
    6. Tomat
    """)
    
    jenis_tanaman = int(input("Silahkan pilih : "))
    if jenis_tanaman == 1:
        os.system("cls")
        print("Rekomendasi Penanaman".center(50, "="))
        print("P A D I".center(50, "="))
        bulan_padi = ["Januari", "Februari", "Maret", "November", "Desember"]
        bulan = input(f"Masukkan Bulan yang anda inginkan : ")
        if bulan.capitalize() in bulan_padi:
            print("Cocok Menanam Padi")
        else:
            print("Tidak Cocok Menanam Padi")
        
    elif jenis_tanaman == 2:
        os.system("cls")
        print("Rekomendasi Penanaman".center(50, "="))
        print("J A G U N G".center(50, "="))
        bulan_jagung = ["Mei", "Juni", "Juli"]
        bulan = input(f"Masukkan Bulan yang anda inginkan : ")
        if bulan.capitalize() in bulan_jagung:
            print("Cocok Menanam Jagung")
        else:
            print("Tidak Cocok Menanam Jagung")
        
    elif jenis_tanaman == 3:
        os.system("cls")
        print("Rekomendasi Penanaman".center(50, "="))
        print("K E D E L A I".center(50, "="))
        bulan_kedelai = ["April", "Mei", "Juni", "Juli"]
        bulan = input(f"Masukkan Bulan yang anda inginkan : ")
        if bulan.capitalize() in bulan_kedelai:
            print("Cocok Menanam Kedela")
        else:
            print("Tidak Cocok Menanam Kedelai")
        
    elif jenis_tanaman == 4:
        os.system("cls")
        print("Rekomendasi Penanaman".center(50, "="))
        print("T E B U".center(50, "="))
        bulan_tebu = ["Desember", "Januari"]
        bulan = input(f"Masukkan Bulan yang anda inginkan : ")
        if bulan.capitalize() in bulan_tebu:
            print("Cocok Menanam Tebu")
        else:
            print("Tidak Cocok Menanam Tebu")
        
    elif jenis_tanaman == 5:
        os.system("cls")
        print("Rekomendasi Penanaman".center(50, "="))
        print("C A B A I".center(50, "="))
        bulan_cabai = ["Maret", "April", "Mei", "Juni"]
        bulan = input(f"Masukkan Bulan yang anda inginkan : ")
        if bulan.capitalize() in bulan_cabai:
            print("Cocok Menanam Cabai")
        else:
            print("Tidak Cocok Menanam Cabai")
        
    elif jenis_tanaman == 6:
        os.system("cls")
        print("Rekomendasi Penanaman".center(50, "="))
        print("T O M A T".center(50, "="))
        bulan_tomat = ["Maret", "April"]
        bulan = input(f"Masukkan Bulan yang anda inginkan : ")
        if bulan.capitalize() in bulan_tomat:
            print("Cocok Menanam Tomat")
        else:
            print("Tidak Cocok Menanam Tomat")
    else :
        input("Masukkan data yang benar!\nUntuk lanjut tekan enter")
        rekomendasiPenanaman()

    inputan3 = int(input("[1] Kembali ke Main Menu\n[2] Akhiri Program\n"))
    if inputan3 == 1:
        os.system("cls")
        mainMenu()
    elif inputan3 == 2:
        outro()

def pemupukan():
    os.system("cls")
    print("Melalui Akar Tanaman".center(80,"="),"\n")
    print("1. Pemupukan dengan cara disebar (broadcasting)\n2. Pemupukan dengan cara ditempatkan di antara larikan/barisan\n3. Pemupukan dengan cara ditempatkan dalam lubang")
    akar = int(input("Pilih metode pemupukan : "))
    if akar == 1:
        os.system("cls")
        print("Pemupukan dengan cara disebar (broadcasting)\n")
        print("Pemupukan dilakukan dengan cara meyebar pupuk secara merata pada tanah\n-tanah di sekitar pertanaman atau pada waktu pembajakan/penggaruan\nterakhir. Dilakakuna sehari sebelum tanam, kemudian diinjak-injak\nagar pupuk masuk ke dalam tanah. Beberapa pertimbangan untuk menggunakan\ncara ini adalah:\n\n1. Tanaman ditanam pada jarak tanam yang rapat, baik teratur dalam\nbarisan maupun tidak teratur dalam barisan,\n2. Tanaman mempunyai akar yang dangkal atau berada dekat dengan permukaan\ntanah,\n3. Tanah mempunyai kesuburan yang relatif baik,\n4. Pupuk yang dipakai cukup banyak atau dosis permukaan tinggi,\n5. Daya larut pupuk besar, karena bila daya larutnya rendah maka\nyang terserap tanaman sedikit,\n6. Cara pemupukan ini biasanya digunakan untuk memupuk tanaman padi,\nkacang-kacangan, dan lain-lain yang mempunyai jarak tanam rapat. Kerugian\ncara ini ialah merangsang pertumbuhan rumput pengganggu/gulma dan\nkemungkinan pengikatan unsur hara tertentu oleh tanah lebih tinggi.\n")
    elif akar == 2:
        os.system("cls")
        print("Pemupukan dengan cara ditempatkan di antara larikan/barisan\n")
        print("Pemupukan dilakukan dengan cara menaburkan pupuk di antara larikan\ntanaman dan kemudian ditutup kembali dengan tanah. Untuk tanaman tahunan,\nditaburkan melingkari tanaman dengan jarak tegak lurus dengan daun terjauh\n(tajuk daun) dan kemudian ditutup kembali dengan tanah.\nCara ini dilakukan dengan pertimbangan-pertimbangan sebagai berikut:\n\n1. Pupuk yang digunakan relatif sedikit,\n2. Jarak tanam antar tanaman yang dipupuk cukup jarang dan jarak antara\nbarisan pertanaman cukup jarang,\n3. Kesuburan tanah rendah,\n4. Tanaman dengan perkembangan akar yang sedikit,\n5. Untuk tanah tegalan atau darat.\n")
    elif akar == 3:
        os.system("cls")
        print("Pemupukan dengan cara ditempatkan dalam lubang\n")
        print("Pemupukan dilakukan dengan cara pupuk dibenamkan ke dalam lubang di\nsamping batang sedalam kurang lebih 10 cm dan ditutup dengan tanah.\nUntuk tanaman tahunan, pupuk dibenamkan ke dalam lubang pupuk yang\nmelingkari tanaman dengan jarak tegak lurus dengan daun terjauh (tajuk\ndaun) dan ditutup kembali dengan tanah. Cara ini dilakukan dengan\npertimbangan sama dengan pemupukan cara larikan/barisan.\n")
    else:
        input("Masukkan data yang benar!\nUntuk lanjut tekan enter")
        TipsTrick()

def penyemprotan():
            os.system("cls")
            print("PEMUPUKAN MELALUI PENYEMPROTAN DAUN TANAMAN (Spraying)\n")
            print("Pemupukan dengan cara pemyemprotan menggunakan pupuk yang dilarutkan\ndalam air dengan konsentrasi sangat rendah kemudian disemprotkan langsung\nkepada daun dengan alat penyemprot biasa (hand sprayer). Pada lahan\nyang luas dapat menggunakan pesawat terbang.\nSebelum melakukan penyemprotan, ada beberapa hal yang harus diketahui\ndulu, yaitu:\n\n1. Konsentrasi larutan pupuk yang dibuat harus sangat rendah atau mengikuti\npetunjuk dalam kemasan pupuk. Jangan berlebihan! Lebih baik kurang\ndaripada berlebihan. Kalau konsentrasinya lebih rendah dari anjuran maka\nuntuk mengimbanginya frekuensi pemupukan bisa diperbanyak, misalnya\ndianjurkan 10 hari bisa dipercepat jadi seminggu sekali.\n2. Pupuk daun disemprotkan ke bagian daun yang menghadap ke bawah karena\nmulut daun (stomata) umumnya menghadap ke bawah atau bagain punggung daun.\n3. Pupuk hendaknya disemprotkan ketika matahari tidak sedang terik-teriknya.\nPaling ideal dilakukan sore atau pagi hari persis ketika matahari belum\nbegitu menyengat. Kalau dipaksakan juga menyemprot ketika panas, pupuk\ndaun itu banyak menguap daripada diserap oleh daun.\n4. Penyemprotan pupuk daun jangan dilaksanakan menjelang musim hujan.\nKarena beresiko pupuk daun akan habis tercuci oleh air hujan. Terlebih\nlagi pada saat hujan seperti itu stomata sedang menutup.\n5. Biasakanlah untuk membaca keterangan yang ada pada kemasan pupuk.\n")

def TipsTrick():
    os.system("cls")
    print("Menu Tips & Trick".center(80,"="))
    print("[1] Metode Pemupukan\n[2] Rekomendasi Penanaman Sesuai Bulan")
    pilihan = int(input("Pilihlah :"))
    if pilihan == 1:
        os.system("cls")
        print("METODE PEMUPUKAN YANG BAIK\n")
        print("Pemupukan merupakan salah satu proses penting dalam budidaya tanaman.\nKenapa menjadi prosesi penting? Karena proses pemupukan akan sangat\nmenentukan keberhasilan produksi tanaman tersebut. Selain harus mengetahui\njenis-jenis pupuk dan proses penyerapan pupuk, kita juga harus tahu\nbagaimana cara mengaplikasikan pupuk pada tanaman yang dibudidayakan\nsehingga proses tersebut menjadi lebih efektif dan efisien.")
        print("\nCara Pemupukan")
        print("1. Melalui Akar Tanaman\n2. Penyemprotan Daun Tanaman (Spraying)\n")
        metode = int(input("Pilihlah : "))
        if metode == 1:
            pemupukan()
        elif metode == 2:
            penyemprotan()
        else:
            input("Masukkan data yang benar!\nUntuk lanjut tekan enter")
            TipsTrick()
        inputan3 = int(input("[1] Kembali ke Main Menu\n[2] Akhiri Program\n"))
        if inputan3 == 1:
            os.system("cls")
            mainMenu()
        elif inputan3 == 2:
            outro()
    elif pilihan == 2:
        rekomendasiPenanaman()
    else:
        input("Masukkan data yang benar!\nUntuk lanjut tekan enter")
        TipsTrick()
    
def mainMenu() :
    os.system("cls")
    print("="*80)
    print("Selamat datang di Program Potray".center(80))
    print("="*80)
    milihMenu = int(input("Silahkan pilih nomer fitur yang anda inginkan\n[1] Perencanaan\n[2] Penjadwalan\n[3] Perhitungan\n[4] Tips & Trick\n[5] Log Out\n[6] Kembali ke HomePage\n[7] Keluar dari program\nPilihan : "))
    if milihMenu == 1:
        menuperencanaan()
    elif milihMenu == 2:
        menupenjadwalan()
    elif milihMenu == 3:
        menuperhitungan()
    elif milihMenu == 4:
        TipsTrick()
    elif milihMenu == 5:
        masuk()
    elif milihMenu == 6:
        awal()
    elif milihMenu == 7:
        outro()
    else:
        input("Masukkan data yang benar!\nUntuk lanjut tekan enter")
        mainMenu()

def databaseKami():
    os.system("cls")
    print("Pilih Database yang anda inginkan\n[1] data.csv\n[2] datatanaman.csv")
    milihDb = int(input("\nPilihan anda : "))
    if milihDb == 1:
        os.system("cls")    
        db1 = pd.read_csv("data.csv")
        print(db1)
    elif milihDb == 2:
        os.system("cls")    
        db2 = pd.read_csv("datatanaman.csv")
        print(db2)
    inputan3 = int(input("[1] Kembali ke Main Menu Admin\n[2] Akhiri Program\n"))
    if inputan3 == 1:
        os.system("cls")
        mainmenuAdmin()
    elif inputan3 == 2:
        outro()
    
def ubahdataPenjadwalan():
    os.system("cls")
    print("Pilih Database yang ingin anda rubah\n[1] datatanaman.csv")
    ubahdb = int(input("\nPilihan anda :"))
    if ubahdb == 1 :
        os.system("cls")
        db1 = pd.read_csv('datatanaman.csv',index_col=0)
        pilihubah1 = int(input("Pilih Data Yang Ingin Anda Rubah\n[1] Lama Panen\n[2] Pupuk 1\n[3] Pupuk 2\n[4] Pupuk 3\nMasukkan Pilihan Anda : "))
        os.system("cls")
        tanaman = int(input ("Pilih Jenis Tanaman \n[1] Padi\n[2] Jagung\n[3] Kedelai\n[4] Tebu\n[5] Cabai\n[6] Tomat\n Masukkan Pilihan Anda : "))
        os.system("cls")
        yangdiubah = input("Masukkan data terbaru : ")
        db1.iloc[tanaman-1 , pilihubah1-1] = yangdiubah
        db1.to_csv('datatanaman.csv')
    else :
        print("Pilihan anda salah")
        ubahdataPenjadwalan() 

    print(db1)       
    inputan3 = int(input("[1] Kembali ke Main Menu Admin\n[2] Kembali ke menu sebelumnya \n[3] Akhiri Program\n"))
    if inputan3 == 1:
        os.system("cls")
        mainmenuAdmin()
    elif inputan3 == 2:
        ubahdataPenjadwalan()
    elif inputan3 == 3:
        outro() 

def hapusakun():
    os.system("cls")
    with open ("users.json","r") as ndaftar:
        userData = json.load(ndaftar)
    print("Hapus Akun\n")
    for idx,i in enumerate(userData):
        print(f"[{idx+1}]",i["nama"])
    index = int(input("Masukkan index akun yang ingin anda hapus atau [99] untuk kembali : "))
    if index == 99:
        mainmenuAdmin()
    userData.pop(index-1)

    with open("users.json", "w") as data:
        json.dump(userData, data, indent=4)

    inputan3 = int(input("[1] Kembali ke Main Menu Admin\n[2] Akhiri Program\n"))
    if inputan3 == 1:
        os.system("cls")
        mainmenuAdmin()
    elif inputan3 == 2:
        outro()

def mainmenuAdmin() :
    os.system("cls")
    print("="*80)
    print("Selamat datang di Menu Admin program Potray".center(80))
    print("="*80)
    milihmenuAdmin = int(input("Silahkan pilih nomer fitur yang anda inginkan\n[1] Database kami\n[2] Ubah Data Penjadwalan\n[3] Hapus akun\n[4] Log Out\n[5] Kembali ke HomePage\n[6] Keluar dari program\nPilihan : "))
    if milihmenuAdmin == 1:
        databaseKami()
    elif milihmenuAdmin == 2:
        ubahdataPenjadwalan()
    elif milihmenuAdmin == 3:
        hapusakun()
    elif milihmenuAdmin == 4:
        masuk()
    elif milihmenuAdmin == 5:
        awal()
    elif milihmenuAdmin == 6:
        outro()
    else:
        input("Masukkan data yang benar!\nUntuk lanjut tekan enter")
        mainMenu()

def intro():
    print("="*80 ) 
    print("Silahkan login".center(80))
    print("="*80 ) 

def outro(): 
    os.system("cls")
    print("="*80) 
    print("Terimakasih telah menggunakan program Potray".center(80))
    print("="*80)

def masuk():
    while True:
        os.system("cls")
        intro()
        name = input("Masukkan nama : ")
        pword = input("Masukkan password : ")
        if validasiLogin(name, pword):
            os.system("cls")
            if validasiLogin(name, pword)[1]:
                mainmenuAdmin()
            else:
                mainMenu()
            break
        else:
            input("Masukkan data yang benar!\nUntuk lanjut tekan enter")
            continue

def daftar():
    os.system("cls")
    namadaftar = input("Masukkan nama : ")
    isAdmin = False
    with open ("users.json","r") as ndaftar:
        userData = json.load(ndaftar)
    masukin = {}
    masukin["nama"] = namadaftar
    for i in userData:
        if masukin["nama"] == i["nama"]:
            print("Akun Sudah Tersedia")
            input("Untuk lanjut tekan enter")
            awal()
    pwdaftar = input("Masukkan password : ")
    masukin["pw"] = pwdaftar
    masukin["isAdmin"] = isAdmin
    userData.append(masukin)
    isAdmin = False
    with open ("users.json","w") as ndaftarin:
        json.dump(userData,ndaftarin,indent=4)
    masuk()

def awal():
    os.system("cls")
    print("="*80)
    print("Selamat Datang Di HomePage POTRAY".center(80))
    print("="*80)
    print("\n[1] Register\n[2] Login")
    awal1 = int(input("Pilihan : "))
    if awal1 == 1:
        os.system("cls")
        daftar()
    elif awal1 == 2:
        os.system("cls")
        masuk()
    else:
        input("Masukkan pilihan yang ada\nUntuk lanjut tekan enter")
        awal()

awal()

































