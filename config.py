import fb_auth_token
import credential

fb_username = credential.fb_username
fb_password = credential.fb_password
fb_access_token = fb_auth_token.get_fb_access_token(fb_username, fb_password)
fb_user_id = fb_auth_token.get_fb_id(fb_access_token)
host = 'https://api.gotinder.com'
#leave tinder_token empty if you don't use phone verification
tinder_token = "Your tinder token goes here"