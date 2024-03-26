import requests
import sys, os

def shorten_url(url):
    api_url = f"http://tinyurl.com/api-create.php?url={url}"
    response = requests.get(api_url)
    return response.text

# Example usage
#long_url = "https://www.microsoft.com/en-us/research/blog/deepspeed-advancing-moe-inference-and-training-to-power-next-generation-ai-scale/"
long_url = sys.argv[1]
short_url = shorten_url(long_url)
print("Shortened URL:", short_url)
