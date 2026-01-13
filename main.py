import mutagen
from mutagen.easyid3 import EasyID3
import os
import sys
import shutil

def collect_paths(path=None):
    files = []
    entries = os.listdir(path)
    if files.count("out") != 0:
        files.pop(files.index("out"))
    for entry in entries:
        if os.path.isdir(os.path.join(path, entry)):
            files.extend(collect_paths(os.path.join(path, entry)))
        else:
            files.append(os.path.join(path, entry))
    return files

def main(args=[]):
    path = args[1]
    files = collect_paths(path)
    if os.listdir(path).count("out") !=1:
        os.mkdir("out")
    for file in files:
        track = EasyID3(file)
        artist = track["artist"][0].split("/")[0]
        album = track["album"][0]
        dest = os.path.join(path, "out", artist, album)
        try:
            os.makedirs(dest)
        except FileExistsError:
            pass
        shutil.move(file, dest)

if __name__ == "__main__":
    main(sys.argv)