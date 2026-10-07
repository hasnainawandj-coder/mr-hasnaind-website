from flask import Flask, request
from PIL import Image
import os

app = Flask(__name__)
W, H = 413, 531

HTML = """
<html><head><style>
body{font-family:Arial;text-align:center;background:#f0f0f0;padding:20px}
.box{background:white;padding:20px;border-radius:15px;max-width:500px;margin:auto;box-shadow:0 5px 15px rgba(0,0,0,0.2)}
button{background:#E91E63;color:white;padding:12px 25px;border:none;border-radius:8px;font-size:18px;cursor:pointer;margin:5px}
button:hover{background:#C2185B}
</style></head><body>
<div class="box">
<h2 style="color:#E91E63">📸 Passport Photo Maker Pro</h2>
<form method="post" enctype="multipart/form-data">
<input type="file" name="photo" required><br><br>
<label>Background:</label>
<select name="bg"><option value="white">White</option><option value="blue">Blue</option></select><br><br>
<button>✨ Photo Banao</button>
</form>
</div></body></html>
"""

@app.route('/', methods=['GET','POST'])
def home():
    if request.method == 'POST':
        f = request.files['photo']
        bg_color = request.form.get('bg','white')
        bg_rgb = (255,255,255) if bg_color=='white' else (0,100,255)
        
        img = Image.open(f).convert("RGB").resize((W, H))
        a4 = Image.new("RGB", (2480, 3508), "white")
        os.makedirs("static", exist_ok=True)
        
        x,y = 100,100
        for i in range(6):
            for j in range(5):
                if i==0 and j==0: 
                    # first photo with border example
                    pass
                a4.paste(img, (x+j*(W+20), y+i*(H+20)))
                if j>=3: break
            if i>=1: break
            
        # Make 8 photos layout properly
        a4 = Image.new("RGB", (1200, 1800), "white")
        px, py = 50, 50
        for r in range(2):
            for c in range(4):
                a4.paste(img, (px+c*(W+20), py+r*(H+20)))
        
        a4.save("static/result.jpg")
        return f'<div style="text-align:center;font-family:Arial"><h1>Ban Gaya! Mubarak Ho!</h1><img src="/static/result.jpg" width="400" style="border:2px solid #E91E63"><br><br><a href="/static/result.jpg" download><button style="background:#E91E63;color:white;padding:12px 25px;border:none;border-radius:8px">📥 Download Karo</button></a><br><br><a href="/">🔙 Wapas</a></div>'
    return HTML

if __name__ == '__main__':
    if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)