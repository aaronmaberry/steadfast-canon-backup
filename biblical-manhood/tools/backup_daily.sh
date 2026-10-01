#!/usr/bin/env bash
# Local half of the Steadfast daily backup: build today's snapshot + lean tgz, then prune to 3 days.
set -euo pipefail
cd "$(dirname "$0")"
python3 backup_daily.py build "$@"
python3 backup_daily.py prune --keep-days 3
