# -*- coding: UTF-8 -*-
import arcpy

print ('Åpner dokumentet')
mxd = arcpy.mapping.MapDocument(r"V:\516\41\5164152\BIM\GIS\02_ProduksjonsData\03_Mxd\Temakart\Planavgrensning\Reguleringsplangrense.mxd")
exportPath = r"V:\516\41\5164152\BIM\GIS\03_Eksport\02_EksportKart\Temakart\Reguleringsplangrense\"
title = "Reguleringsplangrense"

for pageNum in range(1, mxd.dataDrivenPages.pageCount + 1):
    mxd.dataDrivenPages.currentPageID = pageNum
    pageRow = mxd.dataDrivenPages.pageRow
    Nr = str(pageRow.getValue("Sortering"))
    print "Skriver ut " + Nr
    arcpy.mapping.ExportToJPEG(mxd, exportPath + title + "_" + Nr + ".jpg", None, 4178, 6000, 400, world_file=False, color_mode="24-BIT_TRUE_COLOR", jpeg_quality=100)
del mxd