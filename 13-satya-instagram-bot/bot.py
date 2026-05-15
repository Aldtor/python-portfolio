# imports
from instapy import InstaPy
from instapy import smart_run

# login credentials
insta_username = 'ytgaming.91'
insta_password = 'huahahahgagaguaua'

comments = ['Nice shot! @{ytgaming.91}',
        'I love your profile! @{ytgaming.91}',
        'Your feed is an inspiration :thumbsup:',
        'Just incredible :open_mouth:',
        'What camera did you use @{ytgaming.91}?',
        'Love your posts @{ytgaming.91}',
        'Looks awesome @{ytgaming.91}',
        'Getting inspired by you @{ytgaming.91}',
        ':raised_hands: Yes!',
        'I love your profile! @{ytgaming.91}',
        'Your feed is an inspiration :thumbsup:',
        'Just incredible :open_mouth:',
        'What camera did you use @{ytgaming.91}?',
        'Love your posts @{ytgaming.91}',
        'I can feel your passion @{ytgaming.91} :muscle:']

# get an InstaPy session!
# set headless_browser=True to run InstaPy in the background
session = InstaPy(username="ytgaming.91",
password="huahahahgagaguaua", headless_browser=False , want_check_browser=False)

with smart_run(session):
  """ Activity flow """		
  # general settings		
  session.set_dont_include(["drago_satya", "ytgaming.92", ])		
  
  # activity		
  session.like_by_tags(["gaming"], amount=10)

  # Joining Engagement Pods
  session.set_do_comment(enabled=True, percentage=35)
  session.set_comments(comments)
  session.join_pods(topic='sports', engagement_mode='no_comments')