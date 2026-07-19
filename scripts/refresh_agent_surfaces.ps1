[CmdletBinding()]
param([switch]$Check)

$ErrorActionPreference = 'Stop'
Set-StrictMode -Version Latest

$scriptDir = (Resolve-Path $PSScriptRoot).Path
$python = @('py', 'python', 'python3') | Where-Object {
    Get-Command $_ -ErrorAction SilentlyContinue
} | Select-Object -First 1
if (-not $python) { throw 'No Python launcher found.' }

$scriptArgs = @((Join-Path $scriptDir 'refresh_agent_surfaces.py'))
if ($Check) { $scriptArgs += '--check' }
if ($python -eq 'py') { & $python -3 @scriptArgs } else { & $python @scriptArgs }
exit $LASTEXITCODE
