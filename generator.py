import base64
from M2Crypto.EVP import hmac

KEY = 'iSLJVA4c5TmIM103GHPWM6fz5NIHnGuAPU0x8t6UxyWi1F6wulrJilkbqk7cgma'

def get_code(badge_id, award_id):
    award = badge_id*256+award_id
    code = hmac(KEY, '%d' % award)
    award_64 = base64.b64encode(str(award), "-_").strip()
    code_64 = base64.b64encode(code, "-_").strip()
    print "blooper.me/h/%s/%s" % (award_64, code_64)
    
if __name__ == "__main__":
    get_code(100, 40)
    