#!/data/data/com.termux/files/usr/bin/bash
set -e
URL="$1"
if [ -z "$URL" ]; then
  echo "Usage:"
  echo "  bash test_gpu.sh 'https://YOUR-GPU-ENDPOINT.modal.run'"
  exit 1
fi
curl -fsSL "$URL"
echo
