# Facebook crawler with selenium

# 1. Introduction

This program is designed to crawl Facebook pages for given URLs, retrieving post IDs, number of likes, and publication times, among other information.

# **2. Dependencies**

```shell
pip install -r requirements.txt
```

# 3. Basic Usage

## 3.1. Login information

To crawl Facebook pages, the user must first login. The login information can be set in JSON format and stored as "credential.json" in the asset folder.

```json
{
  "email": "user's email",
  "password": "user's password"
}
```

## 3.2. Target URLs

Users need to specify a list of URLs as targets, which can be set in JSON format and stored as "target_urls.json" in the asset folder.

```json
[
  "https://mobile.facebook.com/target_url_1",
  "https://mobile.facebook.com/target_url_2"
]
```

## 3.3. Line Command

Users can execute the program using the following code in the terminal. By adding the `-help` flag, users can view all available input parameters. For example, the number of posts to retrieve can be set via `post_limit`.

```bash
python main.py
python main.py --help
python main.py --post_limit=10
```

## Result

The result is stored in the result folder. The user can load it by using the following command in Python. The screenshots are stored in the result/screenshot folder.

```python
import pickle

with open("filename", "rb") as f:
    data = pickle.load(f)
```