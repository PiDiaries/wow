
#! usr/bin/env python3
import praw
from importlib import reload
import os

import sys
reload(sys)

reddit = praw.Reddit('script', user_agent='script user agent')

if os.path.exists("../Overwatchleague/owc.xml"):
    os.remove('../Overwatchleague/owc.xml')

for submission in reddit.subreddit('OverwatchCompetitive').search('(site:youtube.com OR site:clips.twitch.tv)', limit=100, sort='hot', time_filter='all'):
    print(submission.title)
    with open('../Overwatchleague/owc.xml', 'a') as file:
        #file.write('<item>\n<title>{}</title>\n<link>{}</link>\n</item>\n  '.format(submission.title, submission.url))
        file.write('<item>\n<title>')
        file.write(submission.title)
        file.write('</title>\n<link>')
        file.write(submission.url)
        file.write('</link>\n</item>\n\n\n')

in_ = open('../Overwatchleague/owc.xml').read()
out = open('../Overwatchleague/owc.xml', 'w')
replacements = {'https://www.youtube.com/playlist?list=':'plugin://plugin.video.youtube/playlist/', 'https://m.youtube.com/watch?v=':'https://youtube.com/watch?v=', 'https://m.youtube.com/watch?v=':'https://youtube.com/watch?v=', 'https://clips.twitch.tv/':'plugin://plugin.video.twitch/?mode=play&amp;slug='  ''}
for i in replacements.keys():
    in_ = in_.replace(i, replacements[i])
out.write(in_)
out.close