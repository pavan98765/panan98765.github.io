import os
import requests
import shutil

import openai

openai.api_key = "API Key"


def create_prompt(title):
    prompt = """My Website
 
 Biography
    I am a blogger and explorer.I write clear consise and easy to understand blogs.

 Blog

 Title: {}
 Full text:""".format(
        title
    )
    return prompt


# tags: tech, machine-learning, radiology
# Summary:  This is a blog post about why dinosaurs are awesome.


def get_blog_from_openai(blog_title):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant and a python and AI expert.",
            },
            {"role": "user", "content": create_prompt(blog_title)},
        ],
        max_tokens=512,  # we increased the tokens to get a longer blog post
        temperature=0.7,
    )
    return response["choices"][0]["message"]["content"]


def dalle2_prompt(title):
    prompt = f"art showing '{title}'."
    return prompt


def save_image(image_url, file_name):
    image_res = requests.get(image_url, stream=True)

    if image_res.status_code == 200:
        with open(file_name, "wb") as f:
            shutil.copyfileobj(image_res.raw, f)
    else:
        print("Error downloading image!")
    return image_res.status_code, file_name


def get_cover_image(title, save_path):
    response = openai.Image.create(prompt=dalle2_prompt(title), n=1, size="512x512")
    image_url = response["data"][0]["url"]
    status_code, file_name = save_image(image_url, save_path)
    return status_code, file_name
