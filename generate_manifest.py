import json
import os
from pathlib import Path

# Get all JSON files in outputs folder
outputs_dir = Path('outputs')
json_files = sorted([f.name for f in outputs_dir.glob('*.json')])

# Create manifest
manifest = {
    "files": json_files,
    "count": len(json_files)
}

# Write manifest
with open('outputs/manifest.json', 'w') as f:
    json.dump(manifest, f, indent=2)

print(f"Generated manifest with {len(json_files)} files")
