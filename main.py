#!/usr/bin/env python3
"""Entry for make.fun news-image-20261124.

Writes the poster (entry.png, shipped in this repository) to the
output location. It uses only the Python standard library, makes
no network calls and uses no randomness, so repeated runs write
byte-identical output.
"""
import os
import shutil


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    here = os.path.dirname(os.path.abspath(__file__))
    dest = os.path.join(out_dir, "entry.png")
    shutil.copyfile(os.path.join(here, "entry.png"), dest)
    print("wrote", dest, os.path.getsize(dest), "bytes")


if __name__ == "__main__":
    main()
