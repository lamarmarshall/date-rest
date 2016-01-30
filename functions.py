import uuid
from PIL import Image

def send_simple_message():
    print("email sent");
    '''
    return requests.post(
        "https://api.mailgun.net/v3/sandbox3f8db76ed3e1491e8aaeeb4a3d9082b7.mailgun.org/messages",
        auth=("api", "key-250982e2bf0b4804743ab25df9141da3"),
        data={"from": "Mailgun Sandbox <postmaster@sandbox3f8db76ed3e1491e8aaeeb4a3d9082b7.mailgun.org>",
              "to": "lamar marshall <lamarmarshall75@gmail.com>",
              "subject": "Hello lamar marshall",
              "text": "Congratulations lamar marshall, you just sent an email with Mailgun!  You are truly awesome!  You can see a record of this email in your logs: https://mailgun.com/cp/log .  You can send up to 300 emails/day from this sandbox server.  Next, you should add your own domain so you can send 10,000 emails/month for free."})
    '''

def get_ip(request):
    return "ip"
def thumbnail(infile, outfile):
    try:
        size=  250, 250
        img = Image.open(infile)
        img.load()
        img.thumbnail(size)
        img.save(outfile, "JPEG")
    except IOError :
        print("cannot create thumbnail for", infile)


def generate_name():
    return str( uuid.uuid4() )

def file_ext( type ):

    if type == "image/jpeg" :
        return ".jpg"
    else:
        raise TypeError("must be jpeg")
