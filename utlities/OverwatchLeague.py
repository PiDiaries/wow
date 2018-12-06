#http://www.storybench.org/how-to-scrape-reddit-with-python/
#! usr/bin/env python3
import praw
import os
import re


reddit = praw.Reddit(client_id='DJ7c54TdxLex2g', \
                     client_secret='UMihRd5ZmgWNyXqsX042rwjKRxk', \
                     user_agent='Pi-Diaries', \
                     )

if os.path.exists("../Overwatchleague/owl.xml"):
    os.remove('../Overwatchleague/owl.xml')
for submission in reddit.subreddit('OverwatchLeague').search('site:youtube.com', limit=100, sort='top', time_filter='all'):
    print(submission.title)
    with open('../Overwatchleague/owl.xml', 'a') as file:
        #file.write('<item>\n<title>{}</title>\n<link>{}</link>\n</item>\n  '.format(submission.title, submission.url))
        file.write('<item>\n<title>')
        file.write(submission.title)
        file.write('</title>\n<link>')
        file.write(submission.url)
        file.write('</link>\n</item>\n\n\n')

in_ = open('../Overwatchleague/owl.xml').read()
out = open('../Overwatchleague/owl.xml', 'w')
replacements = {'https://www.youtube.com/playlist?list=':'plugin://plugin.video.youtube/playlist/', 'https://m.youtube.com/watch?v=':'https://youtube.com/watch?v=' ''}
for i in replacements.keys():
    in_ = in_.replace(i, replacements[i])
out.write(in_)
out.close
