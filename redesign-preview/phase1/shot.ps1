param($Name, $Path, $H = 2600)
$ch = "C:\Program Files\Google\Chrome\Application\chrome.exe"
$dir = $PSScriptRoot
& $ch --headless=new --hide-scrollbars --virtual-time-budget=8000 --window-size=1440,$H "--screenshot=$dir\$Name-desktop.png" "http://localhost:4322$Path" *>&1 | Out-Null
$html = "<!doctype html><body style='margin:0;background:#888'><iframe src='http://localhost:4322$Path' style='width:390px;height:${H}px;border:0;display:block;background:#fff'></iframe></body>"
Set-Content -Path "$dir\_m-$Name.html" -Value $html
& $ch --headless=new --hide-scrollbars --virtual-time-budget=8000 --window-size=390,$H "--screenshot=$dir\$Name-mobile.png" "file:///$($dir.Replace([string][char]92,'/'))/_m-$Name.html" *>&1 | Out-Null


