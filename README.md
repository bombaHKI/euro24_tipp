
# Euro 24 tippjáték oldal
## Leírás

A projekt a 2024-es UEFA Európabajnokságra készült. A játék lényege eltalálni a meccsek pontos végkimenetelét és a jó tippekért pontokat gyűjteni.
A meccsekre kapott pontok függnek a meccs végkimenetelének előzetes esélyeitől, valamint a lőtt gólok számától.

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
- **Frontend**: Plain JavaScript, Jinja (HTML), CSS
- **Backend**: Python Flask
- **Adatbázis**: SQLAlchemy with MySQL

## Elérhető
Az oldal az alábbi linken érhető el: <https://hkadus.pythonanywhere.com>.

### Feltételek
- Python 3.x
- MySQL
