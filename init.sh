#/usr/bin/env bash

set -euo pipefail

cd "$(dirname "${BASH_SOURCE[0]}")"

if [ ! -d ".venv" ]; then
  echo "-----Creating virtual environment and installing dependencies-----"
  python3 -m venv .venv && \
  source .venv/bin/activate &&\
  pip install --upgrade pip &&\
  pip install -r requirements.txt
fi

source .venv/bin/activate && exec python -m src.main
