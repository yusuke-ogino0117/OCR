from PIL import Image
import sys
import pyocr
import pyocr.builders

tools = pyocr.get_available_tools()
if len(tools) == 0:
    print("No OCR tool found")
    sys.exit(1)

tool = tools[0]
print("Will use tool '%s'" % (tool.get_name()))

txt = tool.image_to_string(
  #画像へのpathを明示的に表現
    Image.open('card_image/zairyucard_omote.jpg'),
    lang="jpn",
    builder=pyocr.builders.TextBuilder(tesseract_layout=6)
)
print(txt)
# txt.to_csv

# （実行コマンド）python3 ocr.py