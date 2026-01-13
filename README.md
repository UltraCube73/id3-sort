### Simple sort of .mp3 tracks by its artist/album name

Sample usage:
```
git clone https://disnuts.ignorelist.com/gitea/shooter/id3-sort.git
python3 -m venv venv
source venv/bin/activate
python3 -m pip install mutagen
python3 main.py ~/unsorted-tracks
```
Sorted collection will appear under `out` directory.