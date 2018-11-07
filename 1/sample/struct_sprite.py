import sys
import numpy as np
from PIL import Image

if __name__ == '__main__':
    with open(sys.argv[1], 'rb') as f:
        rom = bytearray(f.read())
        
    program_rom = rom[0x10:0x10 + rom[4] * 0x4000]
    character_rom = rom[0x10 + rom[4] * 0x4000:0x10 + rom[4] * 0x4000 + rom[5] * 0x2000]
    
    sprite_sum = (int)(len(character_rom) / 16)
    sprite_memory = np.zeros((sprite_sum, 8, 8))
    for i in range(sprite_sum):
        for j in range(8):
            low = format(character_rom[i * 16 + j], '08b')
            high = format(character_rom[i * 16 + j+ 8], '08b')
            for l, h, r in zip(low, high, range(8)):
                sprite_memory[i][j][r] = int(h + l, 2)
     
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


            
            