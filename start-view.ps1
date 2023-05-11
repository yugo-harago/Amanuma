# start-vite-projects.ps1

$front = Start-Process -NoNewWindow -FilePath 'npm.cmd' -ArgumentList 'run', 'dev' -WorkingDirectory 'front' -PassThru
$office = Start-Process -NoNewWindow -FilePath 'npm.cmd' -ArgumentList 'run', 'dev' -WorkingDirectory 'office' -PassThru

$front.WaitForExit()
$office.WaitForExit()
