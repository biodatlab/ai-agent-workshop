# Windows setup: powershell -NoProfile -ExecutionPolicy Bypass -File .\setup.ps1
param([switch]$NoLaunch)
$ErrorActionPreference = 'Stop'
Set-Location -LiteralPath $PSScriptRoot

function Invoke-RequiredCommand {
    param([string]$Executable, [string[]]$Arguments)
    & $Executable @Arguments
    if ($LASTEXITCODE -ne 0) {
        throw "Command failed (exit $LASTEXITCODE): $Executable $($Arguments -join ' ')"
    }
}

function Find-Python311 {
    $launcher = Get-Command py -ErrorAction SilentlyContinue
    if ($launcher) {
        try {
            $resolved = & $launcher.Source -3.11 -c 'import sys; print(sys.executable)' 2>$null
            if ($LASTEXITCODE -eq 0 -and $resolved) { return ($resolved | Select-Object -Last 1) }
        } catch { }
    }
    $candidates = @(
        (Join-Path $env:LOCALAPPDATA 'Programs\Python\Python311\python.exe'),
        (Join-Path $env:ProgramFiles 'Python311\python.exe')
    )
    foreach ($candidate in $candidates) {
        if (Test-Path -LiteralPath $candidate) {
            & $candidate -c 'import sys; sys.exit(0 if sys.version_info[:2] == (3, 11) else 1)'
            if ($LASTEXITCODE -eq 0) { return $candidate }
        }
    }
}

Write-Host '[1/5] Preparing Python 3.11'
$python311 = Find-Python311
if (-not $python311) {
    $winget = Get-Command winget -ErrorAction SilentlyContinue
    if (-not $winget) {
        throw 'Install Python 3.11 from https://www.python.org/downloads/release/python-3119/ then run setup.ps1 again.'
    }
    Invoke-RequiredCommand $winget.Source @('install', '--id', 'Python.Python.3.11', '--exact', '--source', 'winget', '--silent', '--accept-package-agreements', '--accept-source-agreements')
    $python311 = Find-Python311
    if (-not $python311) { throw 'Python 3.11 was installed. Open a new PowerShell window and run setup.ps1 again.' }
}

Write-Host '[2/5] Preparing .venv and Jupyter'
Invoke-RequiredCommand $python311 @('-m', 'venv', (Join-Path $PSScriptRoot '.venv'))
$notebookPython = Join-Path $PSScriptRoot '.venv\Scripts\python.exe'
Invoke-RequiredCommand $notebookPython @('-m', 'pip', 'install', '--upgrade', 'pip')
Invoke-RequiredCommand $notebookPython @('-m', 'pip', 'install', 'jupyterlab>=4,<5', 'ipykernel>=7,<8')

Write-Host '[3/5] Starting Ollama if needed'
$ollamaCommand = Get-Command ollama -ErrorAction SilentlyContinue
$ollamaExe = if ($ollamaCommand) { $ollamaCommand.Source } else { Join-Path $env:LOCALAPPDATA 'Programs\Ollama\ollama.exe' }
if (-not (Test-Path -LiteralPath $ollamaExe)) {
    throw 'Install Ollama from https://ollama.com/download/windows then run setup.ps1 again.'
}
function Test-OllamaReady {
    try {
        $null = Invoke-RestMethod -Uri 'http://127.0.0.1:11434/api/version' -TimeoutSec 2
        return $true
    } catch { return $false }
}
if (-not (Test-OllamaReady)) {
    Start-Process -FilePath $ollamaExe -ArgumentList 'serve' -WindowStyle Hidden | Out-Null
    $deadline = (Get-Date).AddSeconds(30)
    do {
        Start-Sleep -Milliseconds 500
        $ready = Test-OllamaReady
    } until ($ready -or (Get-Date) -ge $deadline)
    if (-not $ready) { throw 'Ollama did not start on 127.0.0.1:11434. Run ollama serve to see the startup error, then rerun setup.ps1.' }
}

Write-Host '[4/5] Downloading workshop models (existing models are reused)'
Invoke-RequiredCommand $ollamaExe @('pull', 'qwen3:4b')
Invoke-RequiredCommand $ollamaExe @('pull', 'bge-m3')

Write-Host '[5/5] Ready: open a notebook and select Run > Run All Cells'
Write-Host 'Each notebook installs its own lesson packages in its first code cell.'
if (-not $NoLaunch) {
    Invoke-RequiredCommand $notebookPython @('-m', 'jupyterlab', '--notebook-dir', $PSScriptRoot)
}
