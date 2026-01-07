from fastapi import FastAPI, HTTPException

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


@app.get("/posts")
def get_all_posts():
    return text_posts


# path parameter
@app.get("/posts/{id}")
def get_post(id: int):
    if id not in text_posts:
        raise HTTPException(status_code=404, detail="Post not found!")
    return text_posts.get(id)
