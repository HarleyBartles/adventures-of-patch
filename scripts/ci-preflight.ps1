<#
.SYNOPSIS
  Run the repository's deterministic agent-surface preflight.
#>
[CmdletBinding()]
param(
    [switch]$Check,
    [string]$ChangedFrom
)

$ErrorActionPreference = 'Stop'
Set-StrictMode -Version Latest

$scriptDir = (Resolve-Path $PSScriptRoot).Path
$python = @('py', 'python', 'python3') | Where-Object {
    Get-Command $_ -ErrorAction SilentlyContinue
} | Select-Object -First 1
if (-not $python) { throw 'No Python launcher found.' }

function Invoke-PythonScript {
    param(
        [Parameter(Mandatory = $true)][string]$Script,
        [string[]]$Arguments = @()
    )

    $scriptArgs = @((Join-Path $scriptDir $Script)) + $Arguments
    if ($python -eq 'py') { & $python -3 @scriptArgs } else { & $python @scriptArgs }
    if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
}

$checkArgs = @()
if ($Check) { $checkArgs += '--check' }
Invoke-PythonScript 'refresh_agent_surfaces.py' $checkArgs

$meshArgs = @()
if ($Check) { $meshArgs += '--check' }
if ($ChangedFrom) { $meshArgs += @('--changed-from', $ChangedFrom) }
Invoke-PythonScript 'validate_agent_mesh.py' $meshArgs

Push-Location (Join-Path $scriptDir '..')
try {
    if ($python -eq 'py') {
        & $python -3 -m unittest discover -s (Join-Path $scriptDir 'tests') -p 'test_*.py' -v
    } else {
        & $python -m unittest discover -s (Join-Path $scriptDir 'tests') -p 'test_*.py' -v
    }
    if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
} finally {
    Pop-Location
}

if ($ChangedFrom) {
    git diff --check "$ChangedFrom...HEAD"
} else {
    git diff --check
}
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }

Write-Host 'OK agent-surface preflight'
