from flask import Flask

app = Flask(__name__)
app.secret_key = 'f_Gxiaje-h\9+M0Q&.VVB]IfM9Ac3Nh{[E.D:Xb<P>c'

import blooperweb.views
