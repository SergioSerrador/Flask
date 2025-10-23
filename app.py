from flask import Flask, render_template
import random

app = Flask(__name__)

# list of cat images
images = [
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQRqAIkinMg4hgDEyZUtTM3HE1KVAgVICr7vg&s",
    "https://i.pinimg.com/originals/ea/8b/13/ea8b137fbc46bea2f12cc9087e57053d.gif",
    "https://graziamagazine.com/es/wp-content/uploads/sites/12/2016/02/16162042/pYzop6.gif",
    "https://media0.giphy.com/media/v1.Y2lkPTZjMDliOTUyejhoMjg4YXl1b3hlbDdram02NXMxY251MHFzaXV2MDIweW9sd3l6cSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/tRoH9EYLs3lok/200w.gif",
    "https://i.pinimg.com/originals/f5/a5/ac/f5a5acd6ea20f156c65146b5dc5a6354.gif",
    "https://i.pinimg.com/originals/30/29/51/3029517e824f67d07d86af9bf0b0d795.gif"
    ]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0")