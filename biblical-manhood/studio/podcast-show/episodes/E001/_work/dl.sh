#!/bin/bash
# dl.sh K SESSION GEN DATE SIG
U="https://storage.googleapis.com/xi-backend/database/workspace/ea42bee26f8e41c8bb8c50503aff0d11/content_generation/$2/$3/content.mp3?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=xi-backend-prod%40xi-labs.iam.gserviceaccount.com%2F20261003%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=$4&X-Goog-Expires=7200&X-Goog-SignedHeaders=host&X-Goog-Signature=$5"
curl -sS -f -o raw/$1.mp3 "$U" && echo "$1 $(ffprobe -v error -show_entries format=duration -of csv=p=0 raw/$1.mp3)"
