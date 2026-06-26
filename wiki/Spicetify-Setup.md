# Spicetify Setup

A step-by-step guide to install **Spicetify + Marketplace** on standalone Spotify. Includes automatic update blocking and troubleshooting. Available on **Windows**, **macOS**, and **Linux**.

## 📋 Table of Contents

- [Overview](#overview)
- [Installation for Windows](#installation-for-windows)
- [Installation for macOS](#installation-for-macos)
- [Installation for Linux](#installation-for-linux)
- [Troubleshooting](#troubleshooting)

---

## 📖 Overview

**Spicetify** is a command-line tool to customize Spotify. It allows you to apply custom themes, extensions, and modifications to your Spotify client.

> ⚠️ **Important**: Do **NOT** use the Microsoft Store / Mac App Store / Snap or Flatpak version of Spotify — they are sandboxed and not compatible with Spicetify. Use the standalone installer only.

### Automated Installation Scripts

| Platform | Script | Usage |
| --- | --- | --- |
| **Windows** | [`install-spicetify.ps1`](https://github.com/epicvixen73-arch/Projects/blob/main/Spicetify/install-spicetify.ps1) | PowerShell (without admin) |
| **Linux** | [`install-spicetify.sh`](https://github.com/epicvixen73-arch/Projects/blob/main/Spicetify/install-spicetify.sh) | `bash install-spicetify.sh` |

---

## 🪟 Installation for Windows

### Step 1: Completely uninstall Spotify

```powershell
winget uninstall Spotify.Spotify
```

Then delete the leftover folders:
- `%APPDATA%\Spotify`
- `%LOCALAPPDATA%\Spotify`

*(Press `Win + R`, paste the path, hit `Enter`)*

---

### Step 2: Download the standalone Spotify installer

Download the official installer from:
- https://download.scdn.co/SpotifyFullSetup.exe

**OR** from the recommended pinned version:
- https://github.com/SpotifyImporter/spotify-cdn/releases/tag/1.2.52.442

---

### Step 3: Install Spotify

Run the `SpotifyFullSetup.exe` installer normally.

⚠️ **Do not open Spotify** after installation — go straight to Step 4.

---

### Step 4: Block automatic updates

Open **PowerShell as Administrator** and paste:

```powershell
# Make sure the parent folder exists
$spotifyPath = "$env:LOCALAPPDATA\Spotify"
if (-not (Test-Path $spotifyPath)) {
    New-Item -Path $spotifyPath -ItemType Directory -Force | Out-Null
}

# Create a file named "Update" instead of an Update folder
$updatePath = "$spotifyPath\Update"
New-Item -Path $updatePath -ItemType File -Force | Out-Null

Write-Host "✓ Updates blocked!"
```

**Expected output:** `✓ Updates blocked!`

---

### Step 5: Install Spicetify

Close the admin PowerShell and open a **new PowerShell WITHOUT admin rights**.

Paste:
```powershell
iwr -useb https://raw.githubusercontent.com/spicetify/cli/main/install.ps1 | iex
```

Then install the Marketplace:
```powershell
iwr -useb https://raw.githubusercontent.com/spicetify/marketplace/main/resources/install.ps1 | iex
```

---

### Step 6: Apply Spicetify

In the same PowerShell (without admin), paste:
```powershell
spicetify backup apply
```

Spotify will launch automatically with Spicetify active. ✅

---

### Final Verification

* Spotify opens with the Spicetify theme applied
* Automatic updates are blocked
* You can install themes and extensions via the Marketplace

---

## 🍎 Installation for macOS

### Step 1: Completely uninstall Spotify

If installed via Homebrew:
```bash
brew uninstall --cask spotify
```

If installed manually, drag Spotify from **Applications** to the Trash, then delete the leftover folders:
- `~/Library/Application Support/Spotify`
- `~/Library/Caches/com.spotify.client`

*(Open Finder → Go → Go to Folder... and paste the path)*

---

### Step 2: Download the standalone Spotify installer

Download the official `.dmg` installer from:
- https://www.spotify.com/download/mac/

---

### Step 3: Install Spotify

Open the `.dmg` file and drag Spotify to your **Applications** folder.

⚠️ **Do not open Spotify** after installation — go straight to Step 4.

---

### Step 4: Block automatic updates

Open **Terminal** and paste:

```bash
# Block Spotify auto-updates
SPOTIFY_PATH="$HOME/Library/Application Support/Spotify"
mkdir -p "$SPOTIFY_PATH"
UPDATE_PATH="$SPOTIFY_PATH/Update"
touch "$UPDATE_PATH" && chmod 444 "$UPDATE_PATH"
echo "✓ Updates blocked!"
```

**Expected output:** `✓ Updates blocked!`

---

### Step 5: Install Spicetify

In Terminal, paste:
```bash
curl -fsSL https://raw.githubusercontent.com/spicetify/cli/main/install.sh | sh
```

Then install the Marketplace:
```bash
curl -fsSL https://raw.githubusercontent.com/spicetify/marketplace/main/resources/install.sh | sh
```

---

### Step 6: Apply Spicetify

In the same Terminal, paste:
```bash
spicetify backup apply
```

Spotify will launch automatically with Spicetify active. ✅

---

### Final Verification

* Spotify opens with the Spicetify theme applied
* Automatic updates are blocked
* You can install themes and extensions via the Marketplace

---

## 🐧 Installation for Linux

### Step 1: Completely uninstall Spotify

If installed via Snap (incompatible):
```bash
sudo snap remove spotify
```

If installed via `apt`:
```bash
sudo apt remove spotify-client
```

Then delete leftover folders:
- `~/.config/spotify`
- `~/.cache/spotify`

---

### Step 2: Add the official Spotify repository

Open **Terminal** and paste:

```bash
curl -sS https://download.spotify.com/debian/pubkey_C85668DF69375001.gpg \
  | sudo gpg --dearmor --yes -o /etc/apt/trusted.gpg.d/spotify.gpg

echo "deb http://repository.spotify.com stable non-free" \
  | sudo tee /etc/apt/sources.list.d/spotify.list

sudo apt update
```

---

### Step 3: Install Spotify

```bash
sudo apt install spotify-client
```

⚠️ **Do not open Spotify** after installation — go straight to Step 4.

---

### Step 4: Block automatic updates

In Terminal, paste:

```bash
# Block Spotify auto-updates
SPOTIFY_PATH="$HOME/.config/spotify"
mkdir -p "$SPOTIFY_PATH"
UPDATE_PATH="$SPOTIFY_PATH/Update"
touch "$UPDATE_PATH" && chmod 444 "$UPDATE_PATH"
echo "✓ Updates blocked!"
```

**Expected output:** `✓ Updates blocked!`

---

### Step 5: Install Spicetify

In Terminal, paste:
```bash
curl -fsSL https://raw.githubusercontent.com/spicetify/cli/main/install.sh | sh
```

Then install the Marketplace:
```bash
curl -fsSL https://raw.githubusercontent.com/spicetify/marketplace/main/resources/install.sh | sh
```

---

### Step 6: Apply Spicetify

In the same Terminal, paste:
```bash
spicetify backup apply
```

Spotify will launch automatically with Spicetify active. ✅

---

### Final Verification

* Spotify opens with the Spicetify theme applied
* Automatic updates are blocked
* You can install themes and extensions via the Marketplace

---

## 🔧 Troubleshooting

### Windows

| Error | Solution |
| --- | --- |
| **"Could not find part of the path"** | → PowerShell doesn't have enough rights. Relaunch in **Administrator mode** for Step 4 |
| **"Spicetify should NOT be run with administrator privileges"** | → You're in admin mode. Close and open a **regular PowerShell** for Step 6 |
| **Spotify updates itself automatically** | → Step 4 didn't work. Retry the commands as Administrator |
| **Spotify shows a black window** | → Wait a few seconds — Spotify is loading Spicetify |

### macOS

| Error | Solution |
| --- | --- |
| **"spicetify: command not found"** | → Close and reopen Terminal, or run `source ~/.zshrc` (or `~/.bashrc`) |
| **Spicetify has no effect / Spotify looks normal** | → Make sure you're using the standalone `.dmg` version, not the App Store version |
| **Spotify updates itself automatically** | → Step 4 didn't work properly. Re-run the command and check that the file is read-only: `ls -la ~/Library/Application\ Support/Spotify/Update` |

### Linux

| Error | Solution |
| --- | --- |
| **"spicetify: command not found"** | → Close and reopen Terminal, or run `source ~/.bashrc` (or `~/.zshrc`) |
| **Spicetify has no effect** | → Make sure Spotify was installed via `apt` and not via Snap or Flatpak |
| **Spotify updates itself automatically** | → Step 4 didn't work. Re-run the blocking command and verify permissions: `ls -la ~/.config/spotify/Update` |
| **"Permission denied" on `spicetify backup apply`** | → Do **not** run the command with `sudo` — Spicetify must be run as your regular user |

---

## 📄 License

This project is licensed under the MIT License.

---

## 👤 Author

**epicvixen73-arch** — feel free to contribute or report bugs!

---

*Enjoy your customized Spotify experience!* 🎵
