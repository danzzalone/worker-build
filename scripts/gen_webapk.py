#!/usr/bin/env python3
import argparse
import os
import zipfile

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--src", required=True)
    parser.add_argument("--name", required=True)
    parser.add_argument("--out", required=True)
    args = parser.parse_args()

    os.makedirs(os.path.dirname(os.path.abspath(args.out)), exist_ok=True)
    with zipfile.ZipFile(args.out, "w", zipfile.ZIP_DEFLATED) as zf:
        zf.writestr("AndroidManifest.xml", f'<manifest package="com.azazel.{args.name}"/>')
        for root, _, files in os.walk(args.src):
            for f in files:
                full = os.path.join(root, f)
                rel = os.path.relpath(full, args.src)
                zf.write(full, f"assets/web/{rel}")

if __name__ == "__main__":
    main()
