param(
    [string]$Page = "index.html",
    [string]$Out = "render.png"
)
$chrome = "C:\Program Files\Google\Chrome\Application\chrome.exe"
$root = "C:\Users\HP\OneDrive\Desktop\revoult\_build"
& $chrome --headless=new --disable-gpu --hide-scrollbars --force-device-scale-factor=1 `
    --window-size=739,1600 --default-background-color=00000000 `
    --screenshot="$root\$Out" "file:///$($root -replace '\\','/')/$Page" 2>$null | Out-Null
Write-Output "rendered $Out"
