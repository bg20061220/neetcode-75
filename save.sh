#!/usr/bin/env bash
set -e
git add .
git commit -m "solve: $1"
git push
