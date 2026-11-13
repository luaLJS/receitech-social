#!/bin/bash
# Recria os caminhos que os scripts esperam (/home/claude/assets, posts, fotos, cut, cut2).
set -e
G="$(cd "$(dirname "$0")" && pwd)"
for d in assets posts fotos cut cut2; do
  if [ ! -e /home/claude/$d ]; then ln -s "$G/$d" /home/claude/$d; fi
done
mkdir -p /mnt/user-data/outputs/artifacts/969fa822-132d-4a02-8ed1-b92e5c3beee1/project
pip install --break-system-packages -q playwright pillow rembg 2>/dev/null || true
which google-chrome || echo "AVISO: /usr/bin/google-chrome não encontrado; use playwright install chromium e troque executable_path"
echo "setup ok"
