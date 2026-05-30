#!/bin/bash
cd "$(dirname "$0")"
echo "Starting EPPP Practice Tests server..."
echo "Open http://localhost:8080 in your browser"
echo "Press Ctrl+C to stop"
python3 -m http.server 8080
