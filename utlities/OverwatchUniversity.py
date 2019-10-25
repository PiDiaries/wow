
#! usr/bin/env python3
import praw
from importlib import reload
import os

import sys
reload(sys)

reddit = praw.Reddit('script', user_agent='script user agent')

if os.path.exists("../Overwatchleague/owu.xml"):
    os.remove('../Overwatchleague/owu.xml')
    
    
for submission in reddit.subreddit('OverwatchUniversity').search('site:youtube.com OR site:clips.twitch.tv', limit=100, sort='hot', time_filter='all'):
    print(submission.title)
    with open('../Overwatchleague/owu.xml', 'a') as file:
        if "playlist" in submission.url:
            file.write('<plugin>\n<title>[B]')
            file.write(submission.title)
            file.write('[/B]</title>\n<link>')
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
            file.write('<summary>Youtube Affiliate Links wont work.  SORRY</summary> \n')
            file.write('</plugin>\n\n\n')
        elif "twitch" in submission.url:
            file.write('<plugin>\n<title>[B][COLORff6441a5]')
            file.write(submission.title)
            file.write('[/B][/COLOR]</title>\n<link>')
            file.write(submission.url)
            file.write('</link>\n<thumbnail>')
            file.write('http://mirrors.kodi.tv/addons/leia/plugin.video.twitch/icon.png')
            file.write('</thumbnail>\n</plugin>\n\n\n')

in_ = open('../Overwatchleague/owu.xml').read()
out = open('../Overwatchleague/owu.xml', 'w')
replacements = {'https://www.youtube.com/playlist?list=':'plugin://plugin.video.youtube/play/?playlist_id=', 'https://m.youtube.com/watch?v=':'https://youtube.com/watch?v=', 'https://clips.twitch.tv/':'plugin://plugin.video.twitch/?use_player=True&mode=play&amp;slug='  ''}
for i in replacements.keys():
    in_ = in_.replace(i, replacements[i])
out.write(in_)
out.close