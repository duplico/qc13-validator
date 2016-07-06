import pickle
from datetime import datetime, timedelta
import base64

from M2Crypto.EVP import hmac
from flask import render_template, flash, redirect, session, request, url_for

from blooperweb import app

KEY = 'iSLJVA4c5TmIM103GHPWM6fz5NIHnGuAPU0x8t6UxyWi1F6wulrJilkbqk7cgma'

@app.route('/h/<award_code>/<hash>')
def hmac_validate(award_code, hash):
    award_is_good = False
    try:
        award = base64.b64decode(str(award_code), '-_')
        code_candidate = base64.b64decode(str(hash), '-_')
        code_to_match = hmac(KEY, award)
        badge_id = int(award) / 256
        award_id = int(award) % 256
        print code_candidate, code_to_match
        if code_candidate == code_to_match:
            award_is_good = True
    except Exception: # Gotta catch em all
        award_is_good = False
    
    if not award_is_good:
        return "BAD"
    else:
        if 'handler' in session:
            return "Award %d to badge %d" % (award_id, badge_id)
        else:
            return "GOOD"

@app.route('/c/wQELM3NFTBmbuOFVwatNHYAxni6kX/mhPwg4HvnzB5RyLJ/GIVEMECOOKIES')
def drop_cookie():
    session['handler'] = 'yes'
    return '''<PRE><B>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; .---. .---.&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; :&nbsp;&nbsp;&nbsp;&nbsp; : o&nbsp;&nbsp; :&nbsp;&nbsp;&nbsp; me want cookie!
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; _..-:&nbsp;&nbsp; o :&nbsp;&nbsp;&nbsp;&nbsp; :-.._&nbsp;&nbsp;&nbsp; /
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; .-\'\'&nbsp; \'&nbsp; `---\' `---\' "&nbsp;&nbsp; ``-.&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp; .\'&nbsp;&nbsp; "&nbsp;&nbsp; \'&nbsp; "&nbsp; .&nbsp;&nbsp;&nbsp; "&nbsp; . \'&nbsp; "&nbsp; `.&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp; :&nbsp;&nbsp; \'.---.,,.,...,.,.,.,..---.&nbsp; \' ;
&nbsp;&nbsp;&nbsp; `. " `.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; .\' " .\'
&nbsp;&nbsp;&nbsp;&nbsp; `.&nbsp; \'`.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; .\' \' .\'
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `.&nbsp;&nbsp;&nbsp; `-._&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; _.-\' "&nbsp; .\'&nbsp; .----.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `. "&nbsp;&nbsp;&nbsp; \'"--...--"\'&nbsp; . \' .\'&nbsp; .\'&nbsp; o&nbsp;&nbsp; `.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; .\'`-._\'&nbsp;&nbsp;&nbsp; " .&nbsp;&nbsp;&nbsp;&nbsp; " _.-\'`. :&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; o&nbsp; :
&nbsp; jgs .\'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ```--.....--\'\'\'&nbsp;&nbsp;&nbsp; \' `:_ o&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; :
&nbsp;&nbsp;&nbsp; .\'&nbsp;&nbsp;&nbsp; "&nbsp;&nbsp;&nbsp;&nbsp; \'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; "&nbsp;&nbsp;&nbsp;&nbsp; "&nbsp;&nbsp; ; `.;";";";\'
&nbsp;&nbsp; ;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; \'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; \'&nbsp;&nbsp;&nbsp;&nbsp; . ; .\' ; ; ;
&nbsp; ;&nbsp;&nbsp;&nbsp;&nbsp; \'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; \'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; \'&nbsp;&nbsp; "&nbsp;&nbsp;&nbsp; .\'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; .-\'
&nbsp; \'&nbsp; "&nbsp;&nbsp;&nbsp;&nbsp; "&nbsp;&nbsp; \'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; "&nbsp;&nbsp;&nbsp; _.-\'</B></PRE>
'''
        
@app.route('/')
def index():
    return "It works!"
