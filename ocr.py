from paddleocr import PaddleOCR, draw_ocr
import os 
from PIL import Image

# Paddleocr目前支持的多语言语种可以通过修改lang参数进行切换
# 例如`ch`, `en`, `fr`, `german`, `korean`, `japan`

ocr = PaddleOCR(use_angle_cls=True, lang="en")  
for i in os.listdir('ouu'):
    # need to run only once to download and load model into memory
    img_path = 'ouu/'+i
    result = ocr.ocr(img_path, cls=True)
    # print(result)
    for idx in range(len(result)):
        res = result[idx]
        for line in res:
            # print(line[1][0])

    # # 显示结果
    print(result)
    result = result[0]
    # print(result)
    image = Image.open(img_path).convert('RGB')
    boxes = [line[0] for line in result]
    txts = [line[1][0] for line in result]
    # scores = [line[1][1] for line in result]
    print(txts)
    
    im_show = draw_ocr(image,boxes, txts,  font_path='2.ttf')
    im_show = Image.fromarray(im_show)
    im_show.save(f'ouu/{i}_result.jpg') 