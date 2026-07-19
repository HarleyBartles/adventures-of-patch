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

$scriptArgs = @((Join-Path $scriptDir 'validate_agent_mesh.py'))
if ($Check) { $scriptArgs += '--check' }
if ($ChangedFrom) { $scriptArgs += @('--changed-from', $ChangedFrom) }
if ($python -eq 'py') { & $python -3 @scriptArgs } else { & $python @scriptArgs }
exit $LASTEXITCODE
