#!/usr/bin/env bash

# shellcheck disable=SC2034
CONDA_ENV_NAME="etl"

enable_conda_in_script() {
  eval "$(conda shell.bash hook)"
}

print_divisor() {
  printf '=%.0s' {1..100}
  echo
}
