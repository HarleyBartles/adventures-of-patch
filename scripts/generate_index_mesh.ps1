<#[
.SYNOPSIS
  Generate or validate the repository-wide INDEX.md mesh.
#>
[CmdletBinding()]
param(
    [switch]$Check,
    [switch]$AllowSharedCheckout
)

$ErrorActionPreference = 'Stop'
Set-StrictMode -Version Latest

$pythonScript = Join-Path $PSScriptRoot 'generate_index_mesh.py'
if (-not (Test-Path -LiteralPath $pythonScript)) {
    throw "Generator script not found at $pythonScript"
}

$launchers = @('py', 'python', 'python3')
$launcher = $null
foreach ($candidate in $launchers) {
    try {
        $null = Get-Command $candidate -ErrorAction Stop
        $launcher = $candidate
        break
    } catch {
        # Try the next launcher.
    }
}
if (-not $launcher) {
    throw "No Python launcher found. Tried: $($launchers -join ', ')."
}

$arguments = @($pythonScript)
if ($Check) { $arguments += '--check' }
if ($AllowSharedCheckout) { $arguments += '--allow-shared-checkout' }

if ($launcher -eq 'py') {
    & $launcher -3 @arguments
} else {
    & $launcher @arguments
}
exit $LASTEXITCODE
