#!/usr/bin/env bash
set -euo pipefail

script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
check_args=()
changed_from=""
committed_only="false"

while (($# > 0)); do
  case "$1" in
    --check)
      check_args+=(--check)
      shift
      ;;
    --changed-from)
      if (($# < 2)); then
        echo "--changed-from requires a ref" >&2
        exit 2
      fi
      changed_from="$2"
      shift 2
      ;;
    --committed-only)
      committed_only="true"
      shift
      ;;
    *)
      echo "Unknown argument: $1" >&2
      exit 2
      ;;
  esac
done

python_launchers=(python3 python py)
python_launcher=""
for launcher in "${python_launchers[@]}"; do
  if command -v "$launcher" >/dev/null 2>&1; then
    python_launcher="$launcher"
    break
  fi
done
if [[ -z "$python_launcher" ]]; then
  echo "No Python launcher found. Tried: ${python_launchers[*]}" >&2
  exit 1
fi

run_python() {
  if [[ "$python_launcher" == "py" ]]; then
    "$python_launcher" -3 "$@"
  else
    "$python_launcher" "$@"
  fi
}

refresh_args=("${check_args[@]}")
if [[ "$committed_only" == "true" ]]; then
  refresh_args+=(--committed-only)
fi
run_python "$script_dir/refresh_agent_surfaces.py" "${refresh_args[@]}"

mesh_args=()
if ((${#check_args[@]} > 0)); then
  mesh_args+=(--check)
fi
if [[ -n "$changed_from" ]]; then
  mesh_args+=(--changed-from "$changed_from")
fi
run_python "$script_dir/validate_agent_mesh.py" "${mesh_args[@]}"

run_python -m unittest discover -s "$script_dir/tests" -p 'test_*.py' -v

if [[ -n "$changed_from" ]]; then
  git diff --check "$changed_from...HEAD"
else
  git diff --check
fi

echo "OK agent-surface preflight"
