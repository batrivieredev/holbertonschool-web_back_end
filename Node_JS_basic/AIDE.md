# Guide des Exercices Node.js

## Structure du Projet
```
Node_JS_basic/
├── .eslintrc.js          # Configuration ESLint
├── babel.config.js       # Configuration Babel
├── package.json          # Dépendances et scripts
├── database.csv          # Données des étudiants
└── full_server/
    ├── controllers/
    ├── routes/
    └── utils.js
```

## Configuration et Outils

### Commandes Importantes
```bash
# Installation
npm install

# Tests
npm test

# Linting
npm run check-lint

# Développement
npm run dev
```

### Pièges Courants à Éviter
1. Configuration :
   - Vérifier la version de Node.js
   - Installer toutes les dépendances
   - Respecter la structure des dossiers

2. ESLint :
   - Suivre les règles du fichier .eslintrc.js
   - Utiliser les bonnes importations
   - Respecter le style de code

3. Tests :
   - Tester tous les cas d'erreur
   - Vérifier les formats de sortie
   - Utiliser les bons chemins de fichiers

## Guide par Exercice

### Exercice 0: Module Node.js Basique
Points clés :
- Comprendre l'export de modules Node.js
- Utilisation simple de console.log
- Structure de base d'une fonction

### Exercice 1: Process stdin/stdout
À étudier :
- Events de process.stdin
- Différence entre mode interactif et pipe
- Gestion des événements Node.js

### Exercice 2: Lecture Synchrone de Fichier
Concepts importants :
- Lecture synchrone de fichiers
- Parsing de données CSV
- Gestion des erreurs avec try/catch
- Groupement et comptage de données

### Exercice 3: Lecture Asynchrone de Fichier
À comprendre :
- Promesses en JavaScript
- Async/Await
- Gestion asynchrone des fichiers
- Différence avec la version synchrone

### Exercice 4: Serveur HTTP Simple
Concepts clés :
- Module http de Node.js
- Création de serveur
- Headers HTTP
- Gestion de base des requêtes

### Exercice 5: Serveur HTTP Complexe
Points importants :
- Routing basique
- Intégration avec la lecture de fichiers
- Gestion des différentes URLs
- Format des réponses HTTP

### Exercice 6: Express Basique
À étudier :
- Installation et configuration d'Express
- Routing avec Express
- Différences avec le serveur HTTP natif
- Gestion des erreurs Express

### Exercice 7: Express avec Base de Données
Concepts clés :
- Middleware Express
- Intégration des fonctionnalités précédentes
- Organisation du code
- Gestion des promesses avec Express

### Exercice 8: Structure Complète
Points essentiels :

1. Organisation :
   - Séparation des responsabilités
   - Structure MVC
   - Utilisation des modules ES6

2. Utils :
   - Lecture de fichiers
   - Traitement des données
   - Gestion des erreurs

3. Controllers :
   - Logique métier
   - Gestion des requêtes/réponses
   - Validation des entrées

4. Routes :
   - Organisation des endpoints
   - Paramètres d'URL
   - Middleware

## Bonnes Pratiques

### 1. Gestion du Code
- Commentaires utiles et pertinents
- Noms de variables explicites
- Functions courtes et focalisées
- DRY (Don't Repeat Yourself)

### 2. Gestion des Erreurs
- Messages clairs et utiles
- Validation des entrées
- Gestion des cas limites
- Codes d'erreur appropriés

### 3. Performance
- Optimisation des lectures fichiers
- Gestion de la mémoire
- Utilisation appropriée de async/await

### 4. Tests
- Tests unitaires complets
- Tests d'intégration
- Tests des cas d'erreur
- Validation des formats

## Méthodologie de Travail

### 1. Préparation
- Lire les requirements
- Comprendre les objectifs
- Identifier les points clés
- Planifier l'approche

### 2. Développement
- Commencer simple
- Tester régulièrement
- Refactoring progressif
- Validation continue

### 3. Vérification
- Tests automatisés
- Tests manuels
- Validation des formats
- Check de performance

## Ressources

### Documentation
- Node.js : https://nodejs.org/docs
- Express : https://expressjs.com/fr/
- ESLint : https://eslint.org/docs/rules/

### Outils Conseillés
- VS Code
- Postman
- curl
- nodemon

## Conclusion
- Suivre la méthodologie pas à pas
- Valider chaque étape
- Maintenir un code propre
- Respecter les standards
