# PrvHosting
###### Prosta usługa magazynowania plików.

## Cechy
- Upload jednym kliknięciem
- Minimalistyczny interface
- Drag & Drop
- Wparcie dla [Sharex](https://getsharex.com/)
- Konta użytkowników
- Skracanie linków

## Użyte biblioteki
- [flask](https://github.com/pallets/flask)
- [PyMySQL](https://github.com/PyMySQL/PyMySQL)

## Sposób wykonania
 - Pliki są przechowywane na dysku
 - Nazwa pliku i url to losowy string (base64) o długości 5
 - W bazie danych znajduje nazwa pliku, jego oryginalna nazwa, typ i checksum wygenerowany z pliku.
 - Bazując na checksumie, identyczne kopie pliku nie będą oddzielnie zapisywane, a uploadującemu zostanie odesłany link do już istniejącej pliku.
 
