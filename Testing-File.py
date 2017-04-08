'''
Rabidus-Scriptor.py   is    a    simple,
prompt-based, Python-written program, to
use Google Blogger through Google's Data
Python Library &  the Google Blogger API
Credential.
'''

__version__ = "0.0.1"
__author__ = "nomagev"
__maintainer__ = "nomagev"
__license__ = "GPL 2.0"
__email__ = "vegamontesino@msn.com"
__status__ = "Testing"

# ---- TO BE DELETED BEFORE RELEASE ----
# Working  Notes:  Establishing  Handshake.
# Establishing basic functioning structure.
# ---- TO BE DELETED BEFORE RELEASE ----

import sys
from oauth2client import client
from googleapiclient import sample_tools

def main(argv):
    '''
    Triggers  Google's  Recommended  way  to
    Authenticate and construct service.
    NOTE: Until further understanding on the
    way Authentication  and  Handling works,
    this  segment  of the code is derivative
    work from  Google's  API  Python  Client
    Blogger  Example,  under  APACHE license
    version 2.0, hosted at:
    https://github.com/google/google-api-
    python-client/blob/master/samples/
    blogger/blogger.py

    Details  on  APACHE  License version 2.0
    can be found at:
    http://www.apache.org/licenses/LICENSE-2.0
    '''

    service, flags = sample_tools.init(
        argv, 'blogger', 'v3', __doc__, __file__,
        scope='https://www.googleapis.com/auth/blogger')

    try:
        blogs = service.blogs()
        thisusersblog = blogs.listByUser(userId='self').execute()
        for blog in thisusersblogs['items']:
            print "The blog named \'%s\' is at: %s" % (blog['name'], blog['url'])

        users = service.users()
        thisuser = users.get(userId='self').execute()
        print "This user\'s display name is: %s" % thisuser['displayName']

        pages = service.pages()
        thisuserpages = pages.listByUser(userId='self').execute()
        for pages in thisuserpages['items']:
            print "The blog named \'%s\' is at: %s" % (blog['name'], blog['url'])


        posts = service.posts()
        for blog in thisusersblogs['items']:
            print "The posts for %s:" % blog['name']
            request = posts.list(blogId=blog['id'])
            while request != None:
                posts_doc = request.execute()
                if 'items' in posts_doc and not (posts_doc['items'] is None):
                    for post in posts_doc['items']:
                        print"  %s (%s)" % (post['title'], post['url'])
                request = posts.list_next(request, posts_doc)
        
        comments = service.comments()

    except client.AccessTokenRefreshError:
        print "The credentials have been revoked or expired, please re-run \
        the application to re-authorize it"

if __name__ == '__main__':
  main(sys.argv)


# End of program.