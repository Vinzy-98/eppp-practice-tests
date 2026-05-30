Set-Location $PSScriptRoot
Write-Host "Starting EPPP Practice Tests server..."
Write-Host "Open http://localhost:8080 in your browser"
Write-Host "Press Ctrl+C to stop"

$pythonCmd = if (Get-Command python -ErrorAction SilentlyContinue) { "python" }
             elseif (Get-Command python3 -ErrorAction SilentlyContinue) { "python3" }
             else { $null }

if ($pythonCmd) {
    & $pythonCmd -m http.server 8080
} else {
    Write-Host "ERROR: Python is not installed or not in PATH." -ForegroundColor Red
    Write-Host "Download Python from https://www.python.org/downloads/"
    Read-Host "Press Enter to exit"
}
