## spotify2csv
======================
 
## Purpose
Create a CSV file based on any spotify playlist

## Playlists
If you just want to listen to some playlist, you could check out this [collection of playlists](https://open.spotify.com/user/11123260766?si=aaa69784965e4b51).

## Usage
run pip to ensure all requirements are fulfilled
 
```bash
pip3 install -r requirements.txt
```
ensure that you register for a free spotify developers account [here](https://developer.spotify.com/)
and replace the placeholders for SPOTIFY_USERNAME, SPOTIFY_CLIENT_ID and SPOTIFY_CLIENT_SECRET with your personal.

now you can run the script by providing an url:
```bash
i.e. main.py -u https://www1.wdr.de/radio/1live/on-air/sendungen/1live-fiehe/index.html
```

## License
This code is licensed under the [GNU General Public License v3.0](https://choosealicense.com/licenses/gpl-3.0/). <p>
For more details, please take a look at the [LICENSE file](https://github.com/argv1/1live-on-spotify/blob/main/LICENSE).

## Outlook
- [x] Create base functions

More liek a PoC, but please feel free to adjust the code. Things that worth to be done are:
- [ ] Improving unicode & character encoding
- [ ] Add a filter to mark songs, which are no longer available on spotify 


