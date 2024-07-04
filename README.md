# Caller ID Spoofer

`spoofcall.py` is a Python script that allows you to update the caller ID for your SpoofWave account using the SpoofWave API. This script takes your username and a new caller ID as command-line arguments to make the API request.

## Overview

With the `spoofcall.py` script, you can easily change the caller ID used in your SpoofWave account. This is useful for updating the caller ID for outgoing calls. The script uses the [SpoofWave API](https://spoofwave.com/api/call) to perform this operation.

## Requirements

To use this script, you will need:

- **Python 3.x**: The script is compatible with Python 3.
- **`requests` Library**: A Python library for making HTTP requests.

## Installation

Follow these steps to set up and use the `spoofcall.py` script:

1. **Download or Clone the Repository**

   Get the `spoofcall.py` script from the [repository](https://github.com/your-repo/spoofcall) or download the file directly.

2. **Install the Required Library**

   Install the `requests` library, if you don't have it already:

   ```bash
   pip install requests
   ```
   ## Usage
   To run the script, use the following command format:

```bash
python3 spoofcall.py YOUR_USERNAME CALLER_ID
```

If you do not have a SpoofWave account, you can [sign up here](https://spoofwave.com/signup) to create a new account and obtain your credentials.

## Example Usage

Here is a full example of running the script:

```bash
$ python3 spoofcall.py your_username +351123456789
Caller ID updated successfully.
Balance: 50.0000
