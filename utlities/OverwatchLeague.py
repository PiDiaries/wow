#! usr/bin/env python3

import praw
from importlib import reload
import os

import sys
reload(sys)


reddit = reddit = praw.Reddit(client_id='nza3RQ0hwoEOZA',
                     client_secret='v0nAe9D3PDm4F2tb4k7MriTJjgk',
                     user_agent='Watch Overwatch b /u/My-PiDiaries',
                     username='My-PiDiaries')

if os.path.exists("../Overwatchleague/owl.xml"):
    os.remove('../Overwatchleague/owl.xml')
for submission in reddit.subreddit('OverwatchLeague').search('site:youtube.com OR site:clips.twitch.tv', limit=100, sort='hot', time_filter='all'):
    print(submission.title)
    with open('../Overwatchleague/owl.xml', 'a') as file:
        if "playlist" in submission.url:
            file.write('<plugin>\n<title>')
            file.write(submission.title)
            file.write('</title>\n<link>')
            file.write(submission.url)
            file.write('</link>\n<thumbnail>')
            file.write('http://mirrors.kodi.tv/addons/leia/plugin.video.youtube/icon.png')
            file.write('</thumbnail>\n')
            file.write('<summary>Seems to be an Issue with Youtube Playlists on some versions of Kodi</summary> \n')
            file.write('</plugin>\n\n\n')
        elif "youtube" in submission.url:
            file.write('<item>\n<title>[B][COLORffff0000]')
            file.write(submission.title)
            file.write('[/B][/COLOR]</title>\n<link>')
            file.write(submission.url)
            file.write('</link>\n<thumbnail>')
            file.write('http://mirrors.kodi.tv/addons/leia/plugin.video.youtube/icon.png')
            file.write('</thumbnail>\n')
            file.write('<summary>Youtube Affiliate Links wont work.  SORRY</summary>\n')
            file.write('</item>\n\n\n')
        elif "twitch" in submission.url:
            file.write('<plugin>\n<title>[B][COLORff6441a5]')
            file.write(submission.title)
            file.write('[/B][/COLOR]</title>\n<link>')
            file.write(submission.url)
            file.write('</link>\n<thumbnail>')
            file.write('http://mirrors.kodi.tv/addons/leia/plugin.video.twitch/icon.png')
            file.write('</thumbnail>\n</plugin>\n\n\n')

in_ = open('../Overwatchleague/owl.xml').read()
out = open('../Overwatchleague/owl.xml', 'w')
replacements = {'https://www.youtube.com/playlist?list=':'plugin://plugin.video.youtube/play/?playlist_id=', 'https://m.youtube.com/watch?v=':'https://youtube.com/watch?v=', 'https://clips.twitch.tv/':'plugin://plugin.video.twitch/?use_player=True&mode=play&amp;slug='  ''}
for i in replacements.keys():
    in_ = in_.replace(i, replacements[i])
out.write(in_)
out.close
