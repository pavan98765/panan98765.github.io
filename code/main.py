from pathlib import Path
import blog_utils
import openai_utils

# Define your paths here
PATH_TO_BLOG_REPO = Path("C:\\Users\\Jarvis\\Desktop\\Web\\coder1791.github.io\\.git")
PATH_TO_BLOG = PATH_TO_BLOG_REPO.parent
PATH_TO_CONTENT = PATH_TO_BLOG / "content"
PATH_TO_CONTENT.mkdir(exist_ok=True, parents=True)

# Define a title and get the blog content from OpenAI
title = input("Enter the title of the blog: ")
print(openai_utils.create_prompt(title))
blog_content = openai_utils.get_blog_from_openai(title)

# Use existing cover image
cover_image_save_path = PATH_TO_CONTENT / "cover_img.jpg"

# Create the blog
path_to_new_content = blog_utils.create_new_blog(
    PATH_TO_CONTENT, title, blog_content, cover_image_save_path
)
blog_utils.write_to_index(PATH_TO_BLOG, path_to_new_content)

# Update the blog
blog_utils.update_blog(PATH_TO_BLOG_REPO)
