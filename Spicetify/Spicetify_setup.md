# Installing Spotify with Spicetify — Key Steps Summary
## Installation for windows: 
### ⚠️ Important

Do **NOT** use the Microsoft Store version of Spotify — it is not compatible with Spicetify.

---

### Step 1: Completely uninstall Spotify

```
winget uninstall Spotify.Spotify
```

Then delete the leftover folders:

* `%APPDATA%\Spotify`
* `%LOCALAPPDATA%\Spotify`

*(Press `Win + R`, paste the path, hit `Enter`)*

---

### Step 2: Download the standalone Spotify installer

Download the official installer from:

```
https://download.scdn.co/SpotifyFullSetup.exe
```

**OR** from the recommended pinned version:

```
https://github.com/SpotifyImporter/spotify-cdn/releases/tag/1.2.52.442
```

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

```
iwr -useb https://raw.githubusercontent.com/spicetify/cli/main/install.ps1 | iex
```

Then install the Marketplace:

```
iwr -useb https://raw.githubusercontent.com/spicetify/marketplace/main/resources/install.ps1 | iex
```

---

### Step 6: Apply Spicetify

In the same PowerShell (without admin), paste:

```
spicetify backup apply
```

Spotify will launch automatically with Spicetify active. ✅

---

### Final Verification

* Spotify opens with the Spicetify theme applied
* Automatic updates are blocked
* You can install themes and extensions via the Marketplace

---

### Troubleshooting

#### Error: "Could not find part of the path"

→ PowerShell doesn't have enough rights. Relaunch in **Administrator mode** for Step 4.

#### Error: "Spicetify should NOT be run with administrator privileges"

→ You're in admin mode. Close and open a **regular PowerShell** for Step 6.

#### Spotify updates itself automatically

→ Step 4 (blocking updates) didn't work. Retry the commands above as Administrator.

#### Spotify shows a black window

→ Wait a few seconds — Spotify is loading Spicetify.
