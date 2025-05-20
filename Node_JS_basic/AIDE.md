# Guide Complet Node.js

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

## Guide des Fichiers à Implémenter

### Configuration
- `.eslintrc.js` : Déjà configuré, définit les règles de style de code
- `babel.config.js` : Configuration Babel pour ES6
- `package.json` : Gestion des dépendances et scripts

### 0-console.js
**Objectif** : Créer une fonction simple d'affichage
- Créer la fonction displayMessage
- Gérer l'affichage dans STDOUT
- Exporter la fonction correctement

### 1-stdin.js
**Objectif** : Gérer les entrées/sorties
- Utiliser process.stdout pour les messages
- Gérer les événements de process.stdin
- Gérer la fin du programme

### 2-read_file.js
**Objectif** : Lecture synchrone de fichier
- Implémenter countStudents
- Lire le fichier database.csv
- Traiter les données par domaine
- Gérer les erreurs

### 3-read_file_async.js
**Objectif** : Version asynchrone de 2-read_file.js
- Utiliser les Promesses
- Garder la même logique de traitement
- Gérer l'asynchronicité correctement

### 4-http.js
**Objectif** : Serveur HTTP basique
- Créer un serveur avec http.createServer
- Configurer le port 1245
- Gérer une réponse simple
- Exporter l'app

### 5-http.js
**Objectif** : Serveur HTTP avec routes
- Réutiliser la logique de 3-read_file_async.js
- Gérer différentes routes
- Formater les réponses correctement

### 6-http_express.js
**Objectif** : Serveur Express basique
- Installer et utiliser Express
- Configurer une route simple
- Gérer la réponse

### 7-http_express.js
**Objectif** : Serveur Express avec routes
- Adapter 5-http.js vers Express
- Garder la même logique de traitement
- Utiliser le routing Express

### full_server/
**Structure à créer** :
```
full_server/
├── utils.js
├── server.js
├── routes/
│   └── index.js
└── controllers/
    ├── AppController.js
    └── StudentsController.js
```

#### utils.js
**Objectif** : Fonction de lecture de base de données
- Implémenter readDatabase
- Retourner une Promise
- Organiser les données par field

#### controllers/AppController.js
**Objectif** : Contrôleur pour la page d'accueil
- Créer la classe AppController
- Implémenter getHomepage
- Gérer la réponse HTTP

#### controllers/StudentsController.js
**Objectif** : Contrôleur pour les données étudiants
- Créer la classe StudentsController
- Implémenter getAllStudents
- Implémenter getAllStudentsByMajor
- Gérer les erreurs

#### routes/index.js
**Objectif** : Configuration des routes
- Configurer les routes avec Express
- Lier les routes aux contrôleurs
- Gérer les paramètres

#### server.js
**Objectif** : Point d'entrée du serveur
- Configurer Express
- Utiliser les routes
- Gérer le port
- Exporter l'application

## Bonnes Pratiques

### Gestion du Code
- Commentaires utiles et pertinents
- Noms de variables explicites
- Functions courtes et focalisées
- DRY (Don't Repeat Yourself)

### Format des Données
- Respecter exactement les formats de sortie demandés
- Gérer les lignes vides dans le CSV
- Trier les données comme demandé

### Gestion des Erreurs
- Messages clairs et utiles
- Validation des entrées
- Gestion des cas limites
- Codes d'erreur appropriés

### Performance
- Optimisation des lectures fichiers
- Gestion de la mémoire
- Utilisation appropriée de async/await

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

### 3. Tests
- Tests unitaires
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

## Points de Vigilance

### ES6 et Babel
- Utiliser la syntaxe ES6 appropriée
- Configurer Babel correctement
- Gérer les imports/exports

### Tests
- Vérifier avec npm test
- Valider le linting
- Tester tous les cas d'usage

## Conclusion
- Suivre la méthodologie pas à pas
- Valider chaque étape
- Maintenir un code propre
- Respecter les standards
