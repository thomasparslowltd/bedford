Facebook Audience Count
=======================

tom@tomparslow.co.uk 


Asking the facebook ads API how many people are in the audience for ads in certain cities and demographics.

Facebook do seem to round the numbers. There is some overlap between mobile and desktop, a lot of users have both.


Getting a facebook access code
------------------------------

See: https://developers.facebook.com/docs/reference/ads-api/guides/chapter-1-Setup-and-Authentication

1. Create an app, set http://youngfoundation.org/ as callback url
2. Go to https://www.facebook.com/dialog/oauth?client_id=<yourappid>&redirect_uri=http://youngfoundation.org/&scope=ads_management
3. After redirect to Young Foundation site code will be in ?code=<your auth code>
4. Exchange code for access token at https://graph.facebook.com/oauth/access_token?client_id=<app_id>&redirect_uri=http://youngfoundation.org/&client_secret=<app_secret>&code=<CODE> 