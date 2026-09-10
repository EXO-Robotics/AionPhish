# AionPhish

A small email demo repository for [AionGuard](https://github.com/EXO-Robotics/AionGuard). The Boat Fairy sample uses humorous fishing-themed copy and a real, editable HTML call-to-action button.

## Preview

Open `demo/email.html` in a browser. Keep `demo/boat-fairy.png` beside it.

## Customize

Edit `BUTTON_URL`, `BUTTON_TEXT`, and optionally `SUBJECT` in `demo/build_email.py`, then run:

```sh
python3 demo/build_email.py
```

This rebuilds both `demo/email.html` and `demo/boat-fairy-draft.eml`. The current button URL is `https://example.com/REPLACE-WITH-YOUR-LINK`.

## Use in the demo

The `.eml` contains a plain-text body, an HTML body, and embedded artwork. Open it in an email client that supports editing drafts, or use its Edit as New / Resend feature. Choose the sender and intended demo recipient before sending. See `demo/README.txt` for HTML import details.

This repository supplies sample email artifacts; it does not send mail, collect credentials, track clicks, or implement an AionGuard integration. Email-client rendering and delivery have not been tested.

## Files

- `demo/build_email.py` — dependency-free Python generator and editable settings.
- `demo/email.html` — browser preview and email HTML source.
- `demo/boat-fairy-draft.eml` — generated draft with CID-embedded artwork.
- `demo/boat-fairy.png` — AI-edited artwork based on the supplied reference.
- `demo/README.txt` — editing, sending, and artwork notes.
