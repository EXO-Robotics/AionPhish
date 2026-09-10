BOAT FAIRY — EDITABLE EMAIL

The red button is real HTML text and a hyperlink, separate from the artwork.
Current placeholder: https://example.com/REPLACE-WITH-YOUR-LINK

Files
- email.html: preview and editable HTML source. Keep boat-fairy.png beside it.
- boat-fairy-draft.eml: email draft with the artwork embedded as a CID attachment.
- build_email.py: change BUTTON_URL and BUTTON_TEXT at the top, then run
  python3 build_email.py to rebuild both files together.

Sending
Open the .eml in an email app that supports editing message drafts. If it opens
as a received message, use that app's Edit as New / Resend feature if available.
Add your actual sender and intended demo recipient. No sender or recipient has
been configured, and nothing has been sent.

For an HTML-capable email service, import email.html and upload boat-fairy.png,
then replace the image src with the service's hosted image URL. Do not paste raw
HTML into a normal email composer or attach the HTML expecting it to be the body.

The .eml embeds the image; email.html uses a local image for preview. Email app
rendering varies and delivery has not been tested. Test with yourself first.

Artwork was edited using the built-in imagegen tool. Prompt: remove the email
client chrome, painted red button, and tiny footer; preserve the captain, sea,
headline, free-boat speech bubble, checklist and seagull. Add the button and
footer separately in editable HTML. The resulting artwork is a regenerated
variation of the reference, not a pixel-identical crop.
