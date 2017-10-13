#!/usr/bin/env python
import os, sys, json


def add_metadata(seed_file, metadata_file):
    """Add metadata to json file."""

    with open(metadata_file) as f:
        metadata = json.load(f)

    with open(seed_file) as f:
        seed = json.load(f)
        metadata.update(seed)

    # overwrite metadata json file
    with open(metadata_file, 'w') as f:
        json.dump(metadata, f, indent=2, sort_keys=True)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("%s <seed metadata JSON file> <metadata JSON file>" % sys.argv[0])
        sys.exit(1)

    add_metadata(sys.argv[1], sys.argv[2])
    sys.exit(0)
