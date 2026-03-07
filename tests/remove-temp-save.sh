#!/usr/bin/env bash

set -euo pipefail

SAVE="/tmp/temp_save.json"

if [ -e "$SAVE" ]; then
  rm "${SAVE}"
  exit 0
else
  echo "Temp file does not exist" >&2
  exit 1
fi
