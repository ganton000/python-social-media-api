from fastapi import FastAPI
from app.routers import auth, post, user, vote
from fastapi.middleware.cors import CORSMiddleware

#Command moved towards alembic target metadata in env
#models.Base.metadata.create_all(bind=engine)

app = FastAPI()

#Domains allowed to talk to the API
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)


@app.get("/")
def root():
    return {"message":"Welcome to Harry's API!"}

