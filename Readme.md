# Automated Blog

## Overview

The Automated Blog project harnesses the capabilities of OpenAI's API to automatically generate blog posts from topics provided by users. This tool streamlines the content creation process, offering a valuable asset for bloggers, writers, and content creators in generating fresh ideas or full articles with ease.

**Check out the live blog here: [Automated Blog Site](https://pavan98765.github.io/)**

## Features

- **Automated Content Generation**: Creates blog posts automatically by processing user-given topics through OpenAI's API.
- **GitHub Integration**: Ensures that the blog is consistently updated with new content by automatically pushing generated posts to GitHub.

## How It Works

1. **Input**: Users input a topic via the provided interface.
2. **Prompt Generation**: The system constructs a custom prompt from the topic.
3. **Content Generation**: This prompt is sent to OpenAI's API, returning a uniquely crafted blog post.
4. **Publication**: The new blog post is then automatically published to the blog site via GitHub.

## Setup

1. Clone the project repository:

   ```bash
   git clone https://github.com/pavan98765/pavan98765.github.io.git

   ```

2. Place your OpenAI API key in the [openai_utils.py](Code/openai_utils.py).

3. Run the main.py script.
