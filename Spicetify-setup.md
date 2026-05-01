# Installation de Spotify avec Spicetify

> 🚀 **Tu veux aller vite ?** Des scripts d'installation automatique sont disponibles :
>
> | Plateforme | Script | Utilisation |
> |---|---|---|
> | 🪟 Windows | [`install-spicetify.ps1`](install-spicetify.ps1) | PowerShell sans admin |
> | 🐧 Linux | [`install-spicetify.sh`](install-spicetify.sh) | `bash install-spicetify.sh` |
>
> Les guides manuels ci-dessous restent utiles pour comprendre chaque étape ou dépanner.

---

## 🪟 Installation manuelle — Windows

### ⚠️ Important
Ne **PAS** utiliser la version Microsoft Store de Spotify — elle n'est pas compatible avec Spicetify.

---

### Étape 1 : Désinstaller Spotify complètement

```powershell
winget uninstall Spotify.Spotify
```

Puis supprimer les dossiers résiduels :
- `%APPDATA%\Spotify`
- `%LOCALAPPDATA%\Spotify`

*(Appuie sur `Win + R`, colle le chemin, `Entrée`)*

---

### Étape 2 : Télécharger Spotify standalone

Télécharge l'installeur officiel depuis :
```
https://download.scdn.co/SpotifyFullSetup.exe
```

**OU** depuis la version recommandée :
```
https://github.com/SpotifyImporter/spotify-cdn/releases/tag/1.2.52.442
```

---

### Étape 3 : Installer Spotify

Lance l'installeur `SpotifyFullSetup.exe` normalement.

⚠️ **Ne pas ouvrir Spotify** après l'installation — passe directement à l'étape 4.

---

### Étape 4 : Bloquer les mises à jour automatiques

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

### Étape 5 : Installer Spicetify

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

### Étape 6 : Appliquer Spicetify

Dans la même PowerShell (sans admin), colle :

```powershell
spicetify backup apply
```

Spotify va se lancer automatiquement avec Spicetify actif. ✅

---

## 🐧 Installation manuelle — Linux

### ⚠️ Important
- Ne **PAS** utiliser la version **Snap** de Spotify — elle n'est pas compatible avec Spicetify.
- Ne **PAS** lancer les commandes Spicetify en `sudo` / root.

---

### Étape 1 : Installer Spotify standalone

**Ubuntu / Debian :**
```bash
curl -sS https://download.spotify.com/debian/pubkey_6224F9941A8AA6D1.gpg \
    | sudo gpg --dearmor --yes -o /etc/apt/trusted.gpg.d/spotify.gpg

echo "deb http://repository.spotify.com stable non-free" \
    | sudo tee /etc/apt/sources.list.d/spotify.list

sudo apt-get update && sudo apt-get install -y spotify-client
```

**Arch Linux (AUR) :**
```bash
yay -S spotify   # ou : paru -S spotify
```

**Fedora (Flatpak) :**
```bash
flatpak install flathub com.spotify.Client
```
> ⚠️ Le support Spicetify est limité avec la version Flatpak.

---

### Étape 2 : Bloquer les mises à jour automatiques

```bash
mkdir -p ~/.config/spotify
rm -rf ~/.config/spotify/Update
touch ~/.config/spotify/Update
echo "✓ Mises à jour bloquées !"
```

---

### Étape 3 : Installer Spicetify CLI

```bash
curl -fsSL https://raw.githubusercontent.com/spicetify/cli/main/install.sh | sh
```

Ajouter Spicetify au PATH (si besoin) :
```bash
echo 'export PATH="$PATH:$HOME/.spicetify"' >> ~/.bashrc
source ~/.bashrc
```

---

### Étape 4 : Installer le Marketplace

```bash
curl -fsSL https://raw.githubusercontent.com/spicetify/marketplace/main/resources/install.sh | sh
```

---

### Étape 5 : Appliquer Spicetify

```bash
spicetify backup apply
```

Spotify va se lancer avec Spicetify actif. ✅

---

## ✅ Vérification finale (toutes plateformes)

- Spotify s'ouvre avec le thème Spicetify
- Les mises à jour automatiques sont bloquées
- Tu peux installer des thèmes/extensions via le **Marketplace**

---

## 🔧 Troubleshooting

### 🪟 Windows

| Erreur | Cause | Solution |
|---|---|---|
| "Impossible de trouver une partie du chemin d'accès" | Droits insuffisants | Relance en **mode administrateur** pour l'étape 4 |
| "Spicetify should NOT be run with administrator privileges" | Lancé en admin | Ferme et ouvre une **PowerShell normale** pour les étapes 5-6 |
| Spotify se met à jour tout seul | Étape 4 non appliquée | Réessaie le blocage des mises à jour en admin |
| Spotify affiche une fenêtre noire | Chargement en cours | Attends quelques secondes |

### 🐧 Linux

| Erreur | Cause | Solution |
|---|---|---|
| `spicetify: command not found` | PATH non configuré | Ajoute `$HOME/.spicetify` au PATH et recharge ton shell |
| "cannot find Spotify" | Chemin Spotify non détecté | Lance `spicetify config spotify_path /usr/bin/spotify` |
| Spotify version Snap incompatible | Snap non supporté | Désinstalle via `sudo snap remove spotify`, réinstalle via `.deb` |
| Spicetify se réinitialise après update | Mise à jour Spotify non bloquée | Réapplique l'étape 2 puis `spicetify backup apply` |
