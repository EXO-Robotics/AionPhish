from pathlib import Path
from email.message import EmailMessage
from email.policy import SMTP
from html import escape

# Edit these two values, then run: python3 build_email.py
BUTTON_URL = "https://example.com/REPLACE-WITH-YOUR-LINK"
BUTTON_TEXT = "CLAIM YOUR FREE BOAT"
SUBJECT = "🎣 A FREE BOAT is waiting for you!"

folder = Path(__file__).resolve().parent
url = escape(BUTTON_URL, quote=True)
label = escape(BUTTON_TEXT)

def html(image_source):
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>The Boat Fairy</title></head>
<body style="margin:0;padding:0;background-color:#eaf5f9;">
<table role="presentation" width="100%" cellspacing="0" cellpadding="0" border="0" style="background-color:#eaf5f9;"><tr><td align="center" style="padding:20px 8px;">
<table role="presentation" width="560" cellspacing="0" cellpadding="0" border="0" style="width:100%;max-width:560px;background-color:#fff4de;">
<tr><td><img src="{image_source}" width="560" alt="The Boat Fairy has spoken! You get a FREE BOAT! No strings attached! No credit card required! Totally legit! (probably). Because you're awesome! A captain points at you while a seagull wears sunglasses." style="display:block;width:100%;max-width:560px;height:auto;border:0;"></td></tr>
<tr><td align="center" style="padding:12px 20px 20px;">
<!-- EDITABLE BUTTON: change the href for the destination and the anchor text for the label. -->
<table role="presentation" cellspacing="0" cellpadding="0" border="0"><tr><td align="center" bgcolor="#e52323" style="background-color:#e52323;border-radius:8px;border-bottom:4px solid #b31318;mso-padding-alt:20px 28px;">
<a href="{url}" target="_blank" style="display:inline-block;padding:20px 28px;border:1px solid #e52323;border-radius:8px;color:#ffffff;font-family:Arial,Helvetica,sans-serif;font-size:23px;line-height:28px;font-weight:bold;text-decoration:none;text-align:center;mso-padding-alt:0;">{label}</a>
</td></tr></table>
</td></tr>
<tr><td align="center" style="padding:0 20px 22px;color:#343434;font-family:Arial,Helvetica,sans-serif;font-size:12px;line-height:18px;">Offer expires when the fish learn to read.</td></tr>
</table></td></tr></table>
</body></html>'''

(folder / "email.html").write_text(html("boat-fairy.png"))
message = EmailMessage(policy=SMTP)
message["Subject"] = SUBJECT
message["X-Unsent"] = "1"
message.set_content(f"The Boat Fairy has spoken! You get a FREE BOAT!\n\n{BUTTON_TEXT}: {BUTTON_URL}\n\nOffer expires when the fish learn to read.")
message.add_alternative(html("cid:boat-fairy-art"), subtype="html")
message.get_payload()[1].add_related((folder / "boat-fairy.png").read_bytes(), maintype="image", subtype="png", cid="<boat-fairy-art>", filename="boat-fairy.png", disposition="inline")
(folder / "boat-fairy-draft.eml").write_bytes(bytes(message))
print("Created email.html and boat-fairy-draft.eml")
