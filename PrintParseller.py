# -*- coding: UTF-8 -*-
import arcpy

def skrivuttema(Tema):

    print ('AApner dokumentet')
    strekningsLabel = ""



    if Tema == "Oversikt":
        mxd = arcpy.mapping.MapDocument(r"O:\616937\01\08_GIS\09_Mxd\KU_Delstrekning_Parsell.mxd")
        df = arcpy.mapping.ListDataFrames(mxd, "Delstrekningramme")[0]
        for elm in arcpy.mapping.ListLayoutElements(mxd, "TEXT_ELEMENT"):
            if elm.name == "DSTittel":
                strekningsLabel = elm

    elif Tema == "Anbefalte linjer og eksempellinjer":
        mxd = arcpy.mapping.MapDocument(r"O:\616937\01\08_GIS\09_Mxd\KU_MASTER_Parsell_RodtPaaBlaatt.mxd")
        df = arcpy.mapping.ListDataFrames(mxd, "Verdikartramme")[0]
        for elm in arcpy.mapping.ListLayoutElements(mxd, "TEXT_ELEMENT"):
            if elm.name == "DSTittel":
                strekningsLabel = elm

    else:
        mxd = arcpy.mapping.MapDocument(r"O:\616937\01\08_GIS\09_Mxd\KU_MASTER_Parsell.mxd")
        df = arcpy.mapping.ListDataFrames(mxd, "Verdikartramme")[0]


        # Finner posisjoner for tegnforklaring utenfor og innenfor
        TegnforklaringY = 0
        PlassertUtenforY = 0
        for elm in arcpy.mapping.ListLayoutElements(mxd, "GRAPHIC_ELEMENT"):
            if (elm.name == "VerdiForklaring"):
                print "Funnet " + elm.name
                TegnforklaringY = elm.elementPositionY
            if (elm.name == "KulturForklaring"):
                print "Funnet " + elm.name
                PlassertUtenforY = elm.elementPositionY


        # Plasserer alterntiv tegnforklaring innenfor
        for elm in arcpy.mapping.ListLayoutElements(mxd, "GRAPHIC_ELEMENT"):

            if (Tema == "Kulturmiljø"):
                if (elm.name == "KulturForklaring"):
                    print "Plasserer " + elm.name
                    elm.elementPositionY = TegnforklaringY
            if (Tema == "Friuftsliv, by og bygdeliv") and (elm.name == "ByBygdelivForklaring"):
                print "Plasserer " + elm.name
                elm.elementPositionY = TegnforklaringY
            if (Tema == "Løsmasser"):
                if (elm.name == "LosmasserForklaring"):
                    print "Plasserer " + elm.name
                    elm.elementPositionY = 1.5
            if (Tema == "Innspill"):
                if (elm.name == "Innspillforklaring"):
                    print "Plasserer " + elm.name
                    elm.elementPositionY = TegnforklaringY


            # Plasserer verdiforklaring utenfor
            if (elm.name == "VerdiForklaring") and ((Tema == "Kulturmiljø") or (
                    Tema == "Friuftsliv, by og bygdeliv") or (Tema == "Løsmasser") or (Tema == "Innspill")):
                print "Plasserer utenfor " + elm.name
                elm.elementPositionY = PlassertUtenforY


        PositionX = 0.00000

        for elm in arcpy.mapping.ListLayoutElements(mxd, "TEXT_ELEMENT"):
            if elm.name == "Verdi":
                print elm.name
                PositionX = elm.elementPositionX

        for elm in arcpy.mapping.ListLayoutElements(mxd, "TEXT_ELEMENT"):
            if elm.name == "DSTittel":
                strekningsLabel = elm
            if elm.name == "Tittel":
                print elm.name
                elm.text = Tema
                elm.elementPositionX = PositionX

        # Setter en tekstlinje utenfor hvis nødvendig
        for elm in arcpy.mapping.ListLayoutElements(mxd, "TEXT_ELEMENT"):
            if elm.name == "Verdi":
                print elm.name
                PositionX = elm.elementPositionX
                if (Tema == "Vannmiljø sårbarhet") or (Tema == "Innspill") or (Tema == "Løsmasser") or (Tema == "Innspill"):
                    elm.elementPositionY = PlassertUtenforY

        for lyr in arcpy.mapping.ListLayers(mxd, "*", df):
            # print lyr.name
            if (lyr.name == "KUfase ByOgBygdelivRegistreringer") and (Tema == "Friuftsliv, by og bygdeliv"):
                lyr.visible = True
            if (lyr.name == "N50_Arealdekke_omrade (ByBygdeliv)") and (Tema == "Friuftsliv, by og bygdeliv"):
                lyr.visible = True
            if (lyr.name == "KUfase LandskapsbildeRgistreringer") and (Tema == "Landskapsbilde"):
                lyr.visible = True
            if (lyr.name == "KUfase Naturressursregistreringer Mineralressurser") and (Tema == "Mineralressurser"):
                lyr.visible = True
            if (lyr.name == "KUfase DyrketMarkregistreringer") and (Tema == "Dyrket mark"):
                lyr.visible = True
            if (lyr.name == "KUfase Naturressursregistreringer (vann) DS") and (Tema == "Vannressurs"):
                lyr.visible = True
            if (lyr.name == "KUfase Kulturmiljoregistreringer") and (Tema == "Kulturmiljø"):
                lyr.visible = True
            if (lyr.name.find("flate SOSI-koder") > -1) and (Tema == "Løsmasser"):
                lyr.visible = True
            if (lyr.name == "TilbakemeldingerEksternt") and (Tema == "Innspill"):
                lyr.visible = True
            if (lyr.name == "TilbakemeldingerEksterntRedigert") and (Tema == "Innspill"):
                lyr.visible = True

    for bkmk in arcpy.mapping.ListBookmarks(mxd, data_frame=df):
        extentFlytt = bkmk.extent
        BreddeJustering = (extentFlytt.XMax - extentFlytt.XMin) / 4
        HoydeJustering = (extentFlytt.YMax - extentFlytt.YMin) / 4
        Xmax = extentFlytt.XMax - BreddeJustering
        Xmin = extentFlytt.XMin + BreddeJustering
        Ymax = extentFlytt.YMax - HoydeJustering
        Ymin = extentFlytt.YMin + HoydeJustering
        nyExtent = arcpy.Extent(Xmin,Ymin,Xmax,Ymax)
        df.extent = nyExtent
        kartnavn = ""
        if bkmk.name == "AG":
            kartnavn = "Delstrekning Arendal - Grimstad"
        else:
            kartnavn = "Delstrekning Dørdal - Tvedestrand"
        print "Skriver ut " + kartnavn + " " + Tema

        strekningsLabel.text = kartnavn
        arcpy.mapping.ExportToJPEG(mxd, r"O:\616937\01\08_GIS\99_Eksport\KU_verdikart\KU_" + Tema.replace("ø","o") + "_Delstrekning_" + bkmk.name + ".jpg", None, 4178, 6000, 400, world_file=False, color_mode="24-BIT_TRUE_COLOR", jpeg_quality=100)
    del mxd


# skrivuttema("Oversikt")

skrivuttema("Anbefalte linjer og eksempellinjer")

#skrivuttema("Landskapsbilde")
#skrivuttema("Kulturmiljø")
#skrivuttema("Friuftsliv, by og bygdeliv")
#skrivuttema("Mineralressurser")
#skrivuttema("Dyrket mark")
#skrivuttema("Vannressurs")
#skrivuttema("Løsmasser")
#skrivuttema("Innspill")