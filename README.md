### F1Visualizer
# English Version
This project is meant to enable me to learn how to use API calls and to enhance my Python level.
Im french and this is the english part of the readme, if you want it in french, go lower in the file.
Im willing to write All the code and the interface in english first, and maybe translate the interface in french later.

## The dependancies are:
* OpenF1 API
* requests
* streamlit
* plotly

## To use the app: you need to have python 3 installed and :
### to install the dependancies:

```bash
python -m pip install -r requirement.txt
```
### in order to launch the app: (from a shell in the app root) 

```bash
python -m streamlit run test.py
```

## I want to be able to do these things:
(*note: sprint races and qualifying works the same as in grand prix*)
- Race:
    - [x] pilot ranking with points
    - [x] position graph 
    - [x] compound tyre Graph
    - [ ] gap between pilots for each lap
    - [ ] best pit stop
    - [ ] reprodution of the grand prix on a map x100 speed 
- Qualifying:
    - [x] final grid with best sectors and best lap time
- Free practice:
    - [x] final ranking with best time
    - [x] tyre Graph
- Championship wide:
    - for a pilot:
        - [ ] point evolution through the championship
        - [ ] comparison with other team member
        - [ ] comparison with other chosen pilot
    - for a team:
        - [ ] point evolution through the championship
        - [ ] comparison with other chosen team
- Between championship
    - [ ] compare results from a team season wide (for teams that don't change)
    - [ ] compare results from a pilot season wide (for pilots that don't change)
    - [ ] comparison for best lap on each grand prix 
    - [ ] comparison for best pit stop

## Thanks for passing by, if you have any advice or demand, please leave it.

# Version Française:
Ce projet a pour but de me faire apprendre comment utiliser les appels API et d'ameilliorer mon niveau en Python.
J'espère traduire l'interface de l'application en français, mais sachez qu'elle a été pensée pour l'anglais.
Evidemment le code est écrit en anglais (variables/fonctions) car il est destiné pour un publique international.

## Les modules utilisées sont :
* OpenF1 API
* requests
* streamlit
* plotly

## Pour utiliser l'application: vous avez besoin d'avoir python3 d'installé et:
### pour installer les modules: 
```bash
python -m pip install -r requirement.txt
```
### pour lancer l'application: (depuis un shell à la racine de l'app) 
```bash
python -m streamlit run test.py
```

## J'aimerais ajouter ces fonctionalitées:
(*ps: les courses sprint et leurs qualifications fonctionnent comme pour les GP*)
- Course:
    - [x] classement pilote avec les points
    - [x] graphique des positions
    - [x] graphique des composants de pneus
    - [ ] différence entre des pilotes pour chaque tour 
    - [ ] meilleur passage aux stands
    - [ ] reproduction du grand prix sur une carte en vitesse x100
- Qualifications:
    - [x] classement final avec meilleurs secteurs et temps du meilleur tour
- Essais libres:
    - [x] classement final avec meilleur temp au tour
    - [x] graphique pneus
- Sur une saison complète:
    - pour un certain pilote:
        - [ ] évolution des points du pilote pendant la saison
        - [ ] comparaison avec l'autre membre de l'équipe
        - [ ] comparaison avec un autre pilote au choix
    - pour une certaine écurie:
        - [ ] évolution des points de l'écurie pendant la saison
        - [ ] comparaison avec une certaine écurie au choix
- Entre plusieurs saisons:
    - [ ] comparaison des résultats d'une écurie (si cette écurie est présente sur les différentes saisons sélectionnées)
    - [ ] comparaison des résultats d'un pilote (si ce pilote est présent sur les différentes saisons sélectionnées)
    - [ ] comparaison des meilleurs tours pour chaque GP
    - [ ] comparaison des meilleurs passages aux stands pour chaque GP 

## Merci d'être passé par là, si vous avez quelconque conseil ou demande, ne vous gênez surtout pas.
