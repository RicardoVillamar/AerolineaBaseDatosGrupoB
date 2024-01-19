# Init Project

## Specification

In Powersheel mode admin execute the command:

```sh
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser ​
```

## Install Dependencies

- [Download Python](https://www.python.org/downloads/windows/)
- [Download OracleDB 21c xe](https://www.oracle.com/database/technologies/xe-downloads.html)
- [Custom Tkinker](https://customtkinter.tomschimansky.com/documentation/)
- [Download Git](https://git-scm.com/download/win)

## Developer Folder

```sh
cd C:\Users\nameUser\Documents\
mkdir Developer
cd Developer
```

## clone repository

```sh
git clone https://github.com/RicardoVillamar/AerolineaBaseDatosGrupoB.git
cd AerolineaBaseDatosGrupoB
```

## Config git user

```sh
git config --global user.name "username"
git config --global user.email "email@gmail.com"
```

please using your username and email from github

## Create Virtual Environment

```sh
py -m venv venv.
```

## Activate Virtual Environment

```sh
.\venv\Scripts\activate
```

## update pip

```sh
python.exe -m pip install --upgrade pip
```

## Dependencies Environment

```sh
pip install -r requirements.txt
```

## Environment Variables

Replace .env.template by .env

```sh
SECRET_KEY='secret'
DATABASE_HOST='localhost'
DATABASE_PASSWORD='password'
DATABASE_USER='user'
DATABASE_PORT=1521
DATABASE_NAME='xe'
```

Enter the database credentials

## Run Project in normal mode

```sh
py -m client.views.view
```

## Push and pull changes

```sh
git pull --set-upstream origin main
git push --set-upstream origin main
```
