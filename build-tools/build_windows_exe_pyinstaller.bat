pyinstaller --hidden-import=xml --hidden-import=xml.etree --hidden-import=xml.etree.ElementTree --hidden-import=lxml.etree -F -n LabelImg --windowed  "labelImg.py"  -p libs -p "../LabelImg" --add-data "resources/strings/string-en-US.properties;./resources/strings/" -y