# rFCC
Radio channel Allocation for the ReconnectedCC Server.
This serves to prevent crosstalk between channels and applications.

Any channel currently unlicensed with the rFCC is afforded no aid and is public access.

## Bands
The radio range is seperated in specific bands and usage types, commercial or personal. Commercial use on personal bands (even if unlicensed) is not allowed. Commercial allocation might be subject to a bidding process or payment.

## Requests
Allocation requests can be submitted with a pull request. a request may be submitted for any channel or channel range, but a smaller allocation or an allocation that doesn't split an available block in half is more likely to get accepted. The file name should be the channel (range), appended with `.md`. For example, `12345.md`, or `12300-12345.md` and should be stored in `radio`. You must follow the template in `radio/template.md`
A protocol allocation may also be suggested if the protocol is to be used by anyone, set `owner` as `public`.

## Abuse Reports
Abuse reports can be submitted by submitting an issue in this repository with the appropriate type, a form will show up and allow an abuse report to be made.