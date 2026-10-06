# Run from PowerShell: .\setup_env.ps1
# Create the notebook runtime with Python 3.11.
$ErrorActionPreference = 'Stop'

& py -3.11 -m venv (Join-Path $PSScriptRoot '.venv')
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }

$notebookPython = Join-Path $PSScriptRoot '.venv\Scripts\python.exe'
& $notebookPython -m pip install --upgrade pip
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }

& $notebookPython -m pip install 'jupyterlab>=4,<5' 'ipykernel>=7,<8'
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }

Write-Host 'Environment ready. Open JupyterLab:'
Write-Host '.\.venv\Scripts\python.exe -m jupyterlab'
