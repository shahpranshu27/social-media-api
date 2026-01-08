from fastapi import FastAPI, HTTPException
from app.schemas import PostCreate

app = FastAPI()

text_posts = {
    1: {"title": "text post", "content": "test text post"},
    2: {"title": "announcement post", "content": "this is a sample announcement"},
    3: {"title": "update post", "content": "system update completed successfully"},
    4: {"title": "news post", "content": "breaking news goes here"},
    5: {"title": "info post", "content": "general information text"},
    6: {"title": "alert post", "content": "please pay attention to this alert"},
    7: {"title": "reminder post", "content": "this is a friendly reminder"},
    8: {"title": "status post", "content": "current status is active"},
    9: {"title": "feedback post", "content": "user feedback sample text"},
    10: {"title": "promo post", "content": "check out this promotion"},
    11: {"title": "summary post", "content": "short summary content"},
}

# limit: int = None -> optional query parameter
# limit: int -> mandatory query parameter
@app.get("/posts")
def get_all_posts(limit: int = None):
    if limit:
        return list(text_posts.values())[:limit]
    return text_posts


# path parameter
@app.get("/posts/{id}")
def get_post(id: int):
    if id not in text_posts:
        raise HTTPException(status_code=404, detail="Post not found!")
    return text_posts.get(id)


@app.post("/posts")
def create_post(post: PostCreate): # for validation
    new_post = {"title": post.title, "content": post.content}
    text_posts[max(text_posts.keys()) + 1] = new_post
    return new_post