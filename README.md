# 🧠💬 Psychologue IA

Psychologue IA est un chatbot web bienveillant qui offre écoute et accompagnement émotionnel.  
Il analyse les émotions exprimées par l'utilisateur et génère des réponses empathiques adaptées grâce à l'IA Gemini.

---

## ✨ Fonctionnalités

✅ Interface web simple et apaisante  
✅ Analyse des émotions (stress, tristesse, joie, etc.)  
✅ Réponses douces et contextualisées  
✅ Historique de la conversation conservé pour un suivi personnalisé  
✅ Filtrage des questions hors contexte psychologique  

---

## 📂 Structure du projet

```
mon_chatbot_psy/
│
├── app.py                 # Application Flask principale
│
├── static/
│   ├── image.png          # Image d'arrière-plan page d'accueil
│   └── image2.png         # Image d'arrière-plan chatbot
│
├── templates/
│   ├── landing.html       # Page d'accueil
│   └── index.html         # Page du chatbot
│
└── README.md              # Ce fichier
```

---

## 🛠️ Technologies utilisées

- Python 3
- Flask
- Flask-CORS
- LangChain
- Google Generative AI (Gemini 2.0 Flash)
- HTML / CSS / JavaScript

---

## 🚀 Installation et lancement

> **Prérequis :**
> - Python 3 installé
> - Une clé API Gemini valide

1️⃣ Clonez le projet ou créez le dossier :

```bash
git clone <url-du-dépôt>
cd mon_chatbot_psy
```

2️⃣ Installez les dépendances Python :

```bash
pip install flask flask-cors google-generativeai langchain
```

3️⃣ Configurez la clé API Gemini :

- Sous **Linux/macOS** :
  ```bash
  export GEMINI_API_KEY="VOTRE_CLE_API"
  ```
- Sous **Windows PowerShell** :
  ```powershell
  setx GEMINI_API_KEY "VOTRE_CLE_API"
  ```
*(Redémarrez le terminal si nécessaire)*

4️⃣ Lancez l’application :

```bash
python app.py
```

5️⃣ Ouvrez le navigateur :

[http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🎨 Pages incluses

- **Landing Page** (`/`)  
  Présentation et bouton "Passer au chatbot"

- **Chatbot Page** (`/chatbot`)  
  Interface pour poser des questions et recevoir les réponses de l’IA

---

## 🧠 Exemple d’utilisation

**Utilisateur :**
> Je me sens très stressé en ce moment.

**Psychologue IA :**
> Je comprends ce que tu ressens. Le stress peut être accablant, mais tu es capable de trouver du réconfort. Prends une grande respiration et concentre-toi sur une pensée positive.

---

## ⚠️ Avertissement

Ce chatbot ne remplace **en aucun cas** un suivi médical ou psychologique professionnel.  
En cas de détresse grave, veuillez contacter un spécialiste de santé mentale.

---

## 📄 Licence

Ce projet est proposé à des fins éducatives. Vous pouvez le modifier et le partager en citant l’auteur original.

---

## 🙏 Remerciements

- [LangChain](https://python.langchain.com/)
- [Google Generative AI](https://ai.google.dev/)
- La communauté open-source

---

## 💡 Contact

**Auteur :** Rihem Mersani  
📧 Email : *rihemmersani05@gmail.com*

---
