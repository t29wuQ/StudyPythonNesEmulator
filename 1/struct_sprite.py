import sys
import numpy as np
from PIL import Image

if __name__ == '__main__':
    #こ↑こ↓から


    
    #こ↑こ↓まで
     
    image_binary = []
    for i in sprite_memory[65]:
        print(i)
        for j in i:
            if j != 0:
                image_binary.append((0, 0, 0))
            else:
                image_binary.append((0xff, 0xff, 0xff))
                
    img = Image.new("RGB", (8, 8))
    img.putdata(image_binary)
    img.show()


            
            