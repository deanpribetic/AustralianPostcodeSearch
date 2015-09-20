# AustralianPostcodeSearch
A little script for searching for Australian Postcodes via the Australia Post API.

In order to use this script you will need to get a free API key from Australia Post. To do so, complete the form [here](https://developers.auspost.com.au/apis/pacpcs-registration).

## Setup

Once you have your API key, navigate to the line:

```python
headers = {AUTH-KEY-GOES-HERE}
```

and replace `AUTH-KEY-GOES-HERE` with your API key, like this:

```python
headers = {"auth-key":"YOUR API KEY"}
```

## Usage

To get a postcode, run it via:

```bash
python postcode.py
```

The script will prompt you for a suburb. You can enter a full, or partial, suburb name and the query will return the suburb(s) and their postcodes.

