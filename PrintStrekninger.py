# -*- coding: UTF-8 -*-
import arcpy


def skrivuttema(Tema):

    print ('AApner dokumentet')

    mxd = arcpy.mapping.MapDocument(r"O:\616937\01\08_GIS\09_Mxd\KU_MASTER_Verdi_Ds.mxd")

    PositionX = 0.00000

    # Finner posisjoner for tegnforklaring utenfor og innenfor
    TegnforklaringY = 0
    PlassertUtenforY = 0
    for elm in arcpy.mapping.ListLayoutElements(mxd, "GRAPHIC_ELEMENT"):
        if (elm.name == "VerdiForklaring"):
            print "Funnet " + elm.name
            TegnforklaringY = elm.elementPositionY
        if (elm.name == "SaarbarhetForklaring"):
            print "Funnet " + elm.name
            PlassertUtenforY = elm.elementPositionY

    # Plasserer alterntiv tegnforklaring innenfor
    for elm in arcpy.mapping.ListLayoutElements(mxd, "GRAPHIC_ELEMENT"):
        if (elm.name == "SaarbarhetForklaring") and (Tema == "Vannmiljø sårbarhet"):
            print "Plasserer " + elm.name
            elm.elementPositionY = TegnforklaringY
        if (Tema == "Kulturmiljø"):
            # Denne skal ikke med likevel
            # if (elm.name == "KulturForklaring"):
            #    print "Plasserer " + elm.name
            #    elm.elementPositionY = TegnforklaringY
            if (elm.name == "KulturminnerForklaring"):
                print "Plasserer " + elm.name
                elm.elementPositionY = 1.7992
        if (Tema == "Friuftsliv, by og bygdeliv") and (elm.name == "ByBygdelivForklaring"):
            print "Plasserer " + elm.name
            elm.elementPositionY = TegnforklaringY
        if (Tema == "Innspill") and (elm.name == "Innspillforklaring"):
            print "Plasserer " + elm.name
            elm.elementPositionY = TegnforklaringY
        if (Tema == "Løsmasser") and (elm.name == "LosmasserForklaring"):
            print "Plasserer " + elm.name
            elm.elementPositionY = 1.7992

        # Plasserer verdiforklaring utenfor
        if (elm.name == "VerdiForklaring") and ((Tema == "Vannmiljø sårbarhet") or (Tema == "Friuftsliv, by og bygdeliv") or
            (Tema == "Innspill") or (Tema == "Løsmasser") or (Tema == "Linjer og kryss")):
            print "Plasserer utenfor " + elm.name
            elm.elementPositionY = PlassertUtenforY

    # Setter en tekstlinje utenfor hvos nødvendig
    for elm in arcpy.mapping.ListLayoutElements(mxd, "TEXT_ELEMENT"):
        if elm.name == "Verdi":
            print elm.name
            PositionX = elm.elementPositionX
            if (Tema == "Vannmiljø sårbarhet") or (Tema == "Innspill") or (Tema == "Løsmasser") or (Tema == "Linjer og kryss"):
                elm.elementPositionY = PlassertUtenforY

    # Setter tiktig tittel på kartet
    for elm in arcpy.mapping.ListLayoutElements(mxd, "TEXT_ELEMENT"):
        if elm.name == "Tittel":
            print elm.name
            elm.text = Tema
            elm.elementPositionX = PositionX

    df = arcpy.mapping.ListDataFrames(mxd, "Verdikartramme")[0]

    for lyr in arcpy.mapping.ListLayers(mxd, "*", df):
    #     print lyr.name
        if (lyr.name == "KUfase ByOgBygdelivRegistreringer") and (Tema == "Friuftsliv, by og bygdeliv"):
            lyr.visible = True
        if (lyr.name == "N50_Arealdekke_omrade (ByBygdeliv)") and (Tema == "Friuftsliv, by og bygdeliv"):
            lyr.visible = True
        if (lyr.name == "Okologiske_funksjonsomraader_Original (q TemakartID)") and (Tema == "Økologiske funksjonsområder"):
            lyr.visible = True
        if (lyr.name == "Naturtypelokaliteter") and (Tema == "Naturmangfold"):
            lyr.visible = True
        if (lyr.name == "Fisk_ferskvann_Dissolve") and (Tema == "Fisk og ferskvannsorganismer"):
            lyr.visible = True
        if (lyr.name == "N50_Arealdekke_omrade vannflate") and (Tema == "Fisk og ferskvannsorganismer"):
            lyr.visible = False
        if (lyr.name == "Vilttrekk O") and (Tema == "Vilttrekk"):
            lyr.visible = True
        if (lyr.name == "KUfase LandskapsbildeRgistreringer") and (Tema == "Landskapsbilde"):
            lyr.visible = True
        if (lyr.name == "KUfase Naturressursregistreringer Mineralressurser") and (Tema == "Mineralressurser"):
            lyr.visible = True
        if (lyr.name == "KUfase DyrketMarkregistreringer") and (Tema == "Dyrket mark"):
            lyr.visible = True
        if (lyr.name == "KUfase Naturressursregistreringer (vann) DS") and (Tema == "Vannressurs"):
            lyr.visible = True
        if (lyr.name == "Oekologisktilstandeller_potensial_innsjoe_MedVerdi") and (Tema == "Vannmiljø sårbarhet"):
            lyr.visible = True
        if (lyr.name == "ElvOkologiskTilstand_MedVerdisetting") and (Tema == "Vannmiljø sårbarhet"):
            lyr.visible = True
        if (lyr.name == "KUfase Kulturmiljoregistreringer") and (Tema == "Kulturmiljø"):
            lyr.visible = True
        if (lyr.name == "Riksantikvaren - SEFRAK - revet") and (Tema == "Kulturmiljø"):
            lyr.visible = True
        if (lyr.name == "Riksantikvaren - SEFRAK - ikke revet") and (Tema == "Kulturmiljø"):
            lyr.visible = True
        if (lyr.name == "Kulturminner - Lokalitetsikoner") and (Tema == "Kulturmiljø"):
            lyr.visible = True
        if (lyr.name == "Kulturminner - Lokaliteter") and (Tema == "Kulturmiljø"):
            lyr.visible = True
        if (lyr.name == "TilbakemeldingerEksternt") and (Tema == "Innspill"):
            lyr.visible = True
        if (lyr.name == "TilbakemeldingerEksterntRedigert") and (Tema == "Innspill"):
            lyr.visible = True
        if (lyr.name.find("flate SOSI-koder") > -1) and (Tema == "Løsmasser"):
            lyr.visible = True


    for pageNum in range(1, mxd.dataDrivenPages.pageCount + 1):
      mxd.dataDrivenPages.currentPageID = pageNum
      pageRow = mxd.dataDrivenPages.pageRow
      Nr = str(pageRow.getValue("DelstrekningNr"))
      print "Skriver ut " + Nr
      arcpy.mapping.ExportToJPEG(mxd, r"O:\616937\01\08_GIS\99_Eksport\KU_verdikart\KU_" + Tema + "_strekning_" + Nr + ".jpg", None, 4178, 6000, 400, world_file=False, color_mode="24-BIT_TRUE_COLOR", jpeg_quality=100)
    del mxd


# skrivuttema("Landskapsbilde")
# skrivuttema("Vilttrekk")
# skrivuttema("Naturmangfold")
# skrivuttema("Økologiske funksjonsområder")
skrivuttema("Fisk og ferskvannsorganismer")
# skrivuttema("Friuftsliv, by og bygdeliv")
# skrivuttema("Mineralressurser")
# skrivuttema("Dyrket mark")
# skrivuttema("Vannressurs")
# skrivuttema("Vannmiljø sårbarhet")
# skrivuttema("Kulturmiljø")
#
# skrivuttema("Innspill")
# skrivuttema("Løsmasser")

# skrivuttema("Linjer og kryss")