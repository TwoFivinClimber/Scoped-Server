import base64
import json


with open("./soccer.png", "rb") as image_file:
  encoded = base64.b64encode(image_file.read()).decode('utf-8')
  with open("soccer.json", "w") as f:
    f.write(json.dumps(encoded))
    
    
    
    
