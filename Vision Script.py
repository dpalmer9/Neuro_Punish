## Import ##

import numpy as np
import pandas as pd
from PIL import Image

## Import Image ##

Test_Image = Image.open('Meow - 00.bmp')

Current_Size = Test_Image.size
Current_X = Current_Size[0]
Current_Y = Current_Size[1]

X_cols = list(range(0,(Current_X - 1)))
Y_cols = list(range(0,(Current_Y - 1)))

image_df = pd.DataFrame(index=Y_cols,columns=X_cols)


for a in X_cols:
    for b in Y_cols:
        image_df.at[str(b),str(a)] = Test_Image.getpixel((a,b))[0]
