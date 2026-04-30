# Installation de Spotify avec Spicetify - Résumé des étapes clés

## ⚠️ Important
Ne **PAS** utiliser la version Microsoft Store de Spotify — elle n'est pas compatible avec Spicetify.

---

## Étape 1 : Désinstaller Spotify complètement

```powershell
winget uninstall Spotify.Spotify
```

Puis supprimer les dossiers résiduels :
- `%APPDATA%\Spotify`
- `%LOCALAPPDATA%\Spotify`

*(Appuie sur `Win + R`, colle le chemin, `Entrée`)*

---

## Étape 2 : Télécharger Spotify standalone

Télécharge l'installeur officiel depuis :
```
https://download.scdn.co/SpotifyFullSetup.exe
```

**OU** depuis la version recommandée :
```
https://github.com/SpotifyImporter/spotify-cdn/releases/tag/1.2.52.442
```

---

## Étape 3 : Installer Spotify

Lance l'installeur `SpotifyFullSetup.exe` normalement.

⚠️ **Ne pas ouvrir Spotify** après l'installation — passe directement à l'étape 4.

---

## Étape 4 : Bloquer les mises à jour automatiques

Lance **PowerShell en mode administrateur** et colle :

```powershell
# S'assure que le dossier parent existe
$spotifyPath = "$env:LOCALAPPDATA\Spotify"
if (-not (Test-Path $spotifyPath)) {
    New-Item -Path $spotifyPath -ItemType Directory -Force | Out-Null
}

# Crée un fichier "Update" à la place du dossier Update
$updatePath = "$spotifyPath\Update"
New-Item -Path $updatePath -ItemType File -Force | Out-Null

Write-Host "✓ Mises à jour bloquées !"
```

**Résultat attendu :** `✓ Mises à jour bloquées !`

---

## Étape 5 : Installer Spicetify

Ferme PowerShell admin et ouvre une **nouvelle PowerShell SANS admin**.

Colle :
```powershell
iwr -useb https://raw.githubusercontent.com/spicetify/cli/main/install.ps1 | iex
```

Puis installe le Marketplace :
```powershell
iwr -useb https://raw.githubusercontent.com/spicetify/marketplace/main/resources/install.ps1 | iex
```

---

## Étape 6 : Appliquer Spicetify

Dans la même PowerShell (sans admin), coble :

```powershell
spicetify backup apply
```

Spotify va se lancer automatiquement avec Spicetify actif. ✅

---

## ✅ Vérification finale

- Spotify s'ouvre avec le thème Spicetify
- Les mises à jour automatiques sont bloquées
- Tu peux installer des thèmes/extensions via le Marketplace

---

## 🔧 Troubleshooting

### Erreur : "Impossible de trouver une partie du chemin d'accès"
→ PowerShell n'a pas assez de droits. Relance en **mode administrateur** pour l'étape 4.

### Erreur : "Spicetify should NOT be run with administrator privileges"
→ Tu es en mode admin. Ferme et ouvre une **PowerShell normale** pour l'étape 6.

### Spotify se met à jour tout seul
→ L'étape 4 (blocage des mises à jour) n'a pas fonctionné. Réessaie avec les commandes ci-dessus en admin.

### Spotify affiche une fenêtre noire
→ Attends quelques secondes, Spotify charge Spicetify.
