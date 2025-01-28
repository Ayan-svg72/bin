# Bin Info

> api for getting bin info and getting encrypted card details for adyen.

![GitHub stars](https://img.shields.io/github/stars/Ayan-svg72/bin)
![GitHub forks](https://img.shields.io/github/forks/Ayan-svg72/bin)
[![Maintenance](https://img.shields.io/badge/maintained-yes-green.svg)](https://github.com/Ayan-avg72/bin/commits/master)
[![Website shields.io](https://img.shields.io/badge/website-up-yellow)](http://varadbhogayata.github.io/)
[![Ask Me Anything !](https://img.shields.io/badge/ask%20me-Telegram-blue.svg)](https://www.linkedin.com/in/varadbhogayata/)
[![License](http://img.shields.io/:license-MIT-blue.svg?style=flat-square)](http://badges.mit-license.org)

## Installation
> Local Installation
```
git clone http://www.github.com/r0ld3x/adyen-enc-and-bin-info
cd adyen-enc-and-bin-info
pip install -r requirements.txt
uvicorn index:app
```

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/Ayan-svg72/bin.git)


## Usage
> website.com = your heroku website name

**BIN INFO**:-
```curl
curl -X 'GET' \
  'https://1c30-109-123-255-29.eu.ngrok.io/bin/458578' \
  -H 'accept: application/json'
```
> Request URL: https://1c30-109-123-255-29.eu.ngrok.io/bin/458578
__Return__: 
```
{
  "bin": "458578",
  "bank": "PJSC CB EUROBANK",
  "country_iso": "UA",
  "country": "UA",
  "flag": "🇺🇦",
  "vendor": "VISA",
  "type": "DEBIT",
  "level": "CLASSIC",
  "prepaid": false
}
```
> Return status code 200 if success else return 404 if bin not found

#### • MADE BY > [Ayan](https://github.com/Ayan-svg)

## License
[MIT](https://choosealicense.com/licenses/mit/)
