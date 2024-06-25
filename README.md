
# Euro 24 tippjáték oldal
## Leírás

A projekt a 2024-es UEFA Európabajnokságra készült. A játék lényege eltalálni a meccsek pontos végkimenetelét és a jó tippekért pontokat gyűjteni.
A meccsekre kapott pontok függnek a meccs végkimenetelének előzetes esélyeitől, valamint a lőtt gólok számától.
Az oldal az alábbi linken érhető el: <https://hkadus.pythonanywhere.com>.

## Funkciók

### Felhasználók
- **Tippelés**: A "Meccsek" oldalon a felhasználók be tudják írni tippjeiket.
- **Állás**: Az összes felhasználó gyűjtött pontjai alapján felállított ranglista.
- **Tippek**: Minden felhasználó tippjeit (és az azokért járó pontokat) meg lehet nézni.
- **Követés**: Lehetséges más felhasználókat követni (egyirányú, a követett nem kap értesítést). Lehetséges csak a követettek tippjeit és ranglistáját megtekinteni.
- **Profil tevékenységek**: Be/Kijelentkezés, adatok módosítása (email, felhasználónév, jelszó).

### Admin
- **Felhasználók kezelése**: A játékra jelentkezőt elfogadása/elutasítása. A felvett jelentkezők automatikus emailt kapnak egy biztonságosan generált jelszóval.
- **Meccsek kezelése**: Meccsek automatikus frissítése (időpontok, új meccsek) egy API hívással.
- **Oddsok**: A meccsekre kapható plusz pontok frissítése valós fogadóirodák által adott oddsok alapján.

## Használt technológiák
- **Frontend**: Plain JavaScript, Jinja (HTML), CSS (külső könyvtárak nélkül)
- **Backend**: Python Flask
- **Adatbázis**: SQLAlchemy with MySQL

   ## Megjegyzés
   Az oldal eredetije megtalálható [Molnár-Sáska Zoltán](https://github.com/mszoli), volt osztálytársam [honlapján](http://molnar-saska.hu/). Az eredeti PHP-ban íródott, én ezt készítettem el teljesen nulláról, átgondolt megjelenéssel és funkciókkal.

## Média
### Login oldal
<img src="media/login.PNG" height="500">
<img src="media/login_filled.PNG" height="500">

### Bejelentkezés után
<img src="media/udv.PNG" height="500">

### Szabályok oldal
<img src="media/szabalyok.PNG" height="500">

### Meccsek oldal
<img src="media/meccsek.PNG" height="500">

### Állás oldal
<img src="media/allas1.PNG" height="500">
<img src="media/allas2.PNG" height="500">
<img src="media/allas3.PNG" height="500">


