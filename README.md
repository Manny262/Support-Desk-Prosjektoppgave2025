# Support-Desk-Prosjektoppgave2025

## Beskrivelse:
 - Lage et SupportDesk program der brukere i "organisasjonen" kan legge til saker, og saksbehandlere kan administrere over saker. 
 - I denne oppgaven så vil jeg lage for en IT-avdeling på en skole, der elever og lærere kan sende inn saker til IT-avdelingen.

## Installasjonsveiledning

### Forutsetninger
- Python 3.13.9 installert
- PostgreSQL installert og kjørende
- Git installert

### 1. Clone prosjektet fra GitHub

```bash
git clone https://github.com/[ditt-brukernavn]/Support-Desk-Prosjektoppgave2025.git
cd Support-Desk-Prosjektoppgave2025
```

### 2. Opprett et virtuelt miljø

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

(Noen pc-er tilatter bruk av "py" istedenfor python)

**Mac/Linux:**
```bash
python -m venv venv
source venv\bin\activate
```

### 3. Installer nødvendige pakker

```bash
cd DjangoParentSupportDesk
pip install -r requirements.txt
```

asgiref==3.10.0
Django==5.2.8
django-tables2==2.8.0
psycopg2-binary==2.9.11
python-decouple==3.8
sqlparse==0.5.3
tzdata==2025.2
whitenoise==6.11.0


### 4. Sett opp databasen

#### 4.1 Opprett PostgreSQL database

Åpne PostgreSQL (pgAdmin eller kommandolinje) og opprett en database:

```sql
CREATE DATABASE "ProsjektHøstDatabase";
```

#### 4.2 Konfigurer database tilkobling

Åpne filen `DjangoSupportDesk\.env` og oppdater verdiene til dine egne:

```env
DB_ENGINE=django.db.backends.postgresql 
DB_NAME=ProsjektHøstDatabase
DB_USER=[ditt-postgres-brukernavn]
DB_PASSWORD=[ditt-postgres-passord]
DB_HOST=localhost
DB_PORT=5432
```

#### 4.3 Kjør database migrasjoner

```bash
cd DjangoSupportDesk
python manage.py migrate
```

### 5. Opprett superbruker (Hvis man vil ha tilgang til admin-panelet), 

```bash
python manage.py createsuperuser
```

Følg instruksjonene i terminalen for å opprette en admin-bruker.

### 6. Start utviklingsserveren

```bash
python manage.py runserver
```
Jeg brukte 
```bash
python manage.py runserver 0.0.0.0:8000   
```
for at andre på nettverket skal få tilgang (i utviklermiljøet)


### 7. Tilgang til admin panel

Gå til **http://dinIP:/admin/** og logg inn med superbruker-kontoen du opprettet i steg 5.

### Kobling fra andre enheter

Gå til `DjangoSupportDesk\DjangoProjectSupportDesk\settings.py`.
Finn:
```py
ALLOWED_HOSTS = [
    'localhost', 'din-ip-adresse']
```

Erstatt `'din-ip-adresse'` med din IP-adresse (f.eks. `'192.168.1.100'`). 

For å tillate alle IP-adresser under utvikling (ikke anbefalt i produksjon):
```python
ALLOWED_HOSTS = ['*']
```


#### Finne IP-adresse

**Windows:**
```bash
ipconfig
```
Se etter "IPv4 Address".

**Mac:**
```bash
ifconfig
```
Eller gå til System Preferences → Network og se IP-adressen til din aktive tilkobling.

**Linux:**
```bash
ip a
```

#### docs:
- Jeg brukte github projects (kanban) for oversikt over todo, og completed (pluss backlog)

##### Planleggingsfasen:

Dette er det jeg gjorde i planleggingsfasen:

- Se [Funksjoner.md] for oversikt over funksjonalitet.       

- [ProsjektHøstDatamodellV2Screenshot.png] for datamodell av databasen. 
MERK: `User model` og `Case manager model` har blit til en tabell: `public.auth_user`.
Saksbehandlere kan istedenfor bli merket som Staff i admin-panelet, for å få tilgang til 'CaseManager'-appen. En middelvare er satt opp, så at staff-brukere ikke skal få tilang til admin-panelet. 

- [ProsjektHøstWireframeV1.png]: visuell guide som viser skjelettrammeverket til applikasjonen

- [stack.md] viser hvilke stack jeg tenkte å bruke.

##### Under programmeringen og på avslutten:

- [currentStack.md] for hvilke stack jeg endte opp med.

- [SystemArktitektur.md] : viser mappestruktur til prosjektet.

- [Testbrukere.md] : Oversikt over testbrukere i prosjektet. Dette skal bare bli brukt lokalt, og de blir slettet før prod. Jeg valgte å skrive det i plain-text, fordi jeg bruker det over flere enheter (hjemme-pc og skole-pc).  


