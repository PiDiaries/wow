#http://www.storybench.org/how-to-scrape-reddit-with-python/
#! usr/bin/env python3
import praw
import os
import re


reddit = praw.Reddit(client_id='DJ7c54TdxLex2g', \
                     client_secret='UMihRd5ZmgWNyXqsX042rwjKRxk', \
                     user_agent='Pi-Diaries', \
                     )
if os.path.exists("../Overwatchleague/owc.xml"):
    os.remove('../Overwatchleague/owc.xml')

for submission in reddit.subreddit('Competitiveoverwatch').search('site:youtube.com', limit=100, sort='new'):
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
replacements = {'https://www.youtube.com/playlist?list=':'plugin://plugin.video.youtube/playlist/', 'https://m.youtube.com/watch?v=':'https://youtube.com/watch?v='}
for i in replacements.keys():
    in_ = in_.replace(i, replacements[i])
out.write(in_)
out.close