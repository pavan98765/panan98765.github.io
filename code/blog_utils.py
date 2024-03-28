from pathlib import Path
import shutil
import os

from bs4 import BeautifulSoup as Soup
from git import Repo


def create_new_blog(path_to_content, title, content, cover_image=Path("cover_img.png")):
    cover_image = Path(cover_image)

    files = len(list(path_to_content.glob("*.html")))
    safe_title = title.replace(" ", "_")

    path_to_new_content = path_to_content / f"{safe_title}.html"

    if not os.path.exists(path_to_new_content):
        with open(path_to_new_content, "w") as f:
            f.write("<!DOCTYPE html>\n")
            f.write("<html>\n")
            f.write("<head>\n")
            f.write(f"<title> {title} </title>\n")
            f.write(
                """
            <style>
                body {
                    font-family: 'Georgia', serif;
                    padding: 20px;
                    background-color: #fafafa;
                    color: #333;
                }
                h1 {
                    text-align: center;
                    margin-bottom: 30px;
                    color: #f26da7;
                    border-bottom: 1px solid #ddd;
                    padding-bottom: 10px;
                }
                img {
                    display: block;
                    margin: 20px auto;
                    max-width: 90%;
                    border-radius: 10px;
                    box-shadow: 0px 10px 15px rgba(0, 0, 0, 0.1);
                }
                .content {
                    text-align: justify;
                    line-height: 1.8;
                    font-size: 18px;
                    color: #555;
                    margin: 0 auto;
                    max-width: 800px;
                }
                .content p {
                    margin-bottom: 20px;
                }
                .back-button {
                    display: block;
                    width: 200px;
                    height: 50px;
                    margin: 20px auto;
                    background-color: #444;
                    color: #fff;
                    text-align: center;
                    line-height: 50px;
                    border-radius: 10px;
                    text-decoration: none;
                }
                .back-button:hover {
                    background-color: #666;
                }
            </style>
            """
            )
            f.write("</head>\n")

            f.write("<body>\n")
            f.write(f"<h1> {title} </h1>")
            f.write(f"<img src='{cover_image.name}' alt='Cover Image'>\n")
            f.write("<div class='content'>\n")
            f.write(content.replace("\n", "<br />\n"))
            f.write("</div>\n")
            f.write("<a class='back-button' href='/'>Home</a>\n")
            f.write("</body>\n")
            f.write("</html>\n")
            print("Blog created")
            return path_to_new_content
    else:
        raise FileExistsError("File already exist! Abort")


def check_for_duplicate_links(path_to_new_content, links):
    urls = [str(link.get("href")) for link in links]
    content_path = str(Path(*path_to_new_content.parts[-2:]))
    return content_path in urls


def write_to_index(path_to_blog, path_to_new_content):
    with open(path_to_blog / "index.html") as index:
        soup = Soup(index.read(), features="lxml")

    links = soup.find_all("a")
    last_link = links[-1]

    if check_for_duplicate_links(path_to_new_content, links):
        raise ValueError("Link does already exist!")

    link_to_new_blog = soup.new_tag("a", href=Path(*path_to_new_content.parts[-2:]))
    link_to_new_blog.string = path_to_new_content.name.split(".")[0]
    last_link.insert_after(link_to_new_blog)

    with open(path_to_blog / "index.html", "w") as f:
        f.write(str(soup.prettify(formatter="html")))


def update_blog(path_to_blog_repo, commit_message="Updated blog"):
    repo = Repo(path_to_blog_repo)
    repo.git.add(all=True)
    repo.index.commit(commit_message)
    origin = repo.remote(name="origin")
    origin.push()
