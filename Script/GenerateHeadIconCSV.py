#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os

CSVFileName = "DT_HeadIcon.csv"
HeadIconRoot = "..\Content\MySanGuo\DataTable\HeadIcon"

if __name__ == "__main__":
    headIconArray = [["---", "HeadIconBig", "HeadIconSmallLeft", "HeadIconSmallRight"]]
    for _, _, files in os.walk(HeadIconRoot):
        for file in files:
            nativeName = os.path.splitext(file)[0].decode("CP936").encode("UTF-8")
            index = int(nativeName[0:4])
            textureName = "\"Texture2D\'/Game/MySanGuo/DataTable/HeadIcon/" + nativeName + "." + nativeName + "\'\""
            headIconEntry = [str(index), textureName, textureName, textureName]
            headIconArray.append(headIconEntry)

    with open(CSVFileName, 'wb') as csvfile:
        for headIconEntry in headIconArray:
            csvfile.writelines(",".join(headIconEntry) + "\n")