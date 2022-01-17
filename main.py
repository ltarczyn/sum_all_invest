
import tkinter
import time
import json
from binance import binance
from kraken import kraken
from kursy_walut import get_rates_of_currency
from XTB import xtb
from yfin import akcje_from_yahoo


def sum_dic(x):
    suma_in_usd = 0
    for a, b in x.items():
        suma_in_usd += x[a]
    return suma_in_usd


PASSWORD = '*****************'

real_usd = "login"
real_pln = "login"

cryp_binance = binance()
cryp_kraken = kraken()
"""print(f"binance{cryp_binance}")
print(f"kraken {cryp_kraken}")"""
#cryp_binance = {'LRC': 27.854500027480004}
#cryp_kraken = {'DOGE': 30.804204103999997}

sum_usd_in_binance = round(sum_dic(cryp_binance), 2)

sum_usd_in_kraken = round(sum_dic(cryp_kraken), 2)

kurs = get_rates_of_currency("usd",1)
x = json.loads(kurs)

w = x['rates']
dic_usd_pln = w[0]
usd_pln = round(dic_usd_pln['mid'],2)
suma_krypto = round((sum_usd_in_kraken+sum_usd_in_binance) * usd_pln, 2)
#print(f"Suma inwestycji w krypto: {suma_krypto} Złotych")

akcje_poltreg_ilosc = 15

akcje_poltreg = int(akcje_from_yahoo("PTG.WA") * akcje_poltreg_ilosc)

#print(f"wartość akcji Poltreg w Mbanku to: {akcje_poltreg}")

wynik_xtb_pln = xtb(real_pln, PASSWORD)
time.sleep(1)
wynik_xtb_usd = xtb(real_usd, PASSWORD)
suma_akcje = int(wynik_xtb_pln + (wynik_xtb_usd*usd_pln))
#print(f"suma inwestycji w akcje: {suma_akcje}")

suma_all_invest = round(suma_akcje + suma_krypto + akcje_poltreg, 2)
czas = time.localtime()
time_string = time.strftime("%m/%d/%Y,%H:%M:%S", czas)
dane_do_zapisu = time_string + ":" + str(suma_all_invest) + "\n"

with open("dane.txt", mode="a") as file:
    file.write(dane_do_zapisu)

window = tkinter.Tk()
window.title("Wartość moich inwestycji")
label_kraken = tkinter.Label(text=f"Suma inwestycji na giełdzie kryptowalut Kraken to: {sum_usd_in_kraken * usd_pln} PLN")
label_kraken.pack()
label_binance = tkinter.Label(text=f"Suma inwestycji na giełdzie kryptowalut Binance to: {sum_usd_in_binance * usd_pln} PLN")
label_binance.pack()
label_krypto = tkinter.Label(text=f"Suma inwestycji w kryptowaluty to: {suma_krypto}PLN")
label_krypto.pack()
label_akcje = tkinter.Label(text=f"Suma inwestycji w akcje to : {suma_akcje + akcje_poltreg}PLN")
label_akcje.pack()
label_all = tkinter.Label(text=f"Suma wszystkich inwestycji to: {suma_all_invest}PLN")
label_all.pack()

window.mainloop()

#print(f"suma wszystkich inwesycji: {suma_all_invest}")
