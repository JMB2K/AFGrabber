stations = [
        {
            "serviceAreaId": "29571892-da88-4089-83f0-24135852c2e4",
            "serviceAreaName": "Miami (UFL2) - Fresh Online"
        },
        {
            "serviceAreaId": "d39e54d6-1a53-46a9-a22d-309342256ef0",
            "serviceAreaName": "Miami Davie (C072) - Whole Foods"
        },
        {
            "serviceAreaId": "d15e18ec-66c7-42ae-8599-9f27f82b19cc",
            "serviceAreaName": "Fort Lauderdale - (C465) Whole Foods"
        },
        {
            "serviceAreaId": "fd440da5-dc81-43bf-9afe-f4910bfd4090",
            "serviceAreaName": "Miami Pembroke Pines (C074) - Whole Foods"
        },
        {
            "serviceAreaId": "ffbac4b5-8850-48e8-86bd-4403685d46d7",
            "serviceAreaName": "Miami (DMI9) - Amazon.com"
        },
        {
            "serviceAreaId": "b90b085e-874f-48da-8150-b0c215efff08",
            "serviceAreaName": "South Miami (C314) - Whole Foods"
        },
        {
            "serviceAreaId": "f4342003-fb20-4761-9998-a1aca8133c23",
            "serviceAreaName": "Pompano Beach (DMF3)- Amazon.com"
        },
        {
            "serviceAreaId": "50ade688-5ae2-48ce-a83c-f0af3fa4a22a",
            "serviceAreaName": "Virginia Gardens - (DMI3) AMZL"
        },
        {
            "serviceAreaId": "d98c442b-9688-4427-97b9-59a4313c2f66",
            "serviceAreaName": "Miami Downtown Miami (C073) - Whole Foods"
        },
        {
            "serviceAreaId": "d42d1888-f102-49e1-b524-6db352dd6d31",
            "serviceAreaName": "Hialeah (DMF1)- Amazon.com"
        },
        {
            "serviceAreaId": "a6b8cf91-1a26-495e-bc7a-6b7f5324a17d",
            "serviceAreaName": "Miami (DVB7)-Amazon.com"
        },
        {
            "serviceAreaId": "dd00cb2b-349b-480c-a2d0-5aff2c3fd293",
            "serviceAreaName": "Sunrise - (DMI4) AMZL"
        },
        {
            "serviceAreaId": "fd409ef8-f297-4543-9b93-6a5e93184313",
            "serviceAreaName": "Miami - (DMI6) AMZL"
        },
        {
            "serviceAreaId": "a5e1a8d5-c368-4cb8-a2c6-3b71b3eb8178",
            "serviceAreaName": "Hialeah FL (VFL2) - Sub Same-Day"
        },
        {
            "serviceAreaId": "5540b055-ee3c-4274-9997-de65191d6932",
            "serviceAreaName": "Miami (UFL6) - Fresh Online"
        },
        {
            "serviceAreaId": "09cc7bbd-919c-4dec-be50-9a71ab0ca07e",
            "serviceAreaName": "Mizner Park (PMAQ) - Retail Delivery"
        },
        {
            "serviceAreaId": "ad13a80a-0d93-444c-a660-1b5f65e53626",
            "serviceAreaName": "Pembroke Park (RFL1) - Community Delivery"
        },
        {
            "serviceAreaId": "5891b812-04ab-405b-8336-355a1f75e48e",
            "serviceAreaName": "Pembroke Park (DVB5)-Amazon.com"
        },
        {
            "serviceAreaId": "00091261-49d3-4d1f-9720-d76cbd2b2401",
            "serviceAreaName": "Aventura Mall (PAAD) – Retail Delivery"
        },
        {
            "serviceAreaId": "724fcdc1-82a8-4cf9-90db-ba6f5b7e246e",
            "serviceAreaName": "Miami Boca Raton (C070) - Whole Foods"
        },
        {
            "serviceAreaId": "c059f4c8-35bd-4a43-848f-38cb7d9eec9c",
            "serviceAreaName": "Miami South Beach - (C492) Whole Foods"
        },
        {
            "serviceAreaId": "37fe42b7-2a8e-4aca-8b5d-7836e38ff1c4",
            "serviceAreaName": "Miami FL (NMI2)"
        },
        {
            "serviceAreaId": "49d080a7-a765-47cf-a29e-0f1842958d4a",
            "serviceAreaName": "North Miami (C125) - Whole Foods"
        },
        {
            "serviceAreaId": "8c81c54f-6a60-405c-b095-43d9b9bc99c2",
            "serviceAreaName": "Tamarac FL (VFL3) - Sub Same-Day"
        },
        {
            "serviceAreaId": "f9530032-4659-4a14-b9e1-19496d97f633",
            "serviceAreaName": "Miami Dadeland (C071) - Whole Foods"
        },
        {
            "serviceAreaId": "e7765dce-8d20-41b6-a038-9856323d4db6",
            "serviceAreaName": "West Palm Beach - (DMI7) AMZL"
        },
        {
            "serviceAreaId": "5e29665d-f6d5-4ff2-8558-fc197eeb84a1",
            "serviceAreaName": "Fort Lauderdale (DFH1)- Amazon.com"
        },
        {
            "serviceAreaId": "12bb7066-fac1-4412-83e8-a63247d4a946",
            "serviceAreaName": "Miami West Palm Beach (C075) - Whole Foods"
        },
        {
            "serviceAreaId": "f78af44a-613a-4cea-bfd4-7ad17da2719d",
            "serviceAreaName": "Miami (DMF5)- Amazon.com"
        },
        {
            "serviceAreaId": "dbff6260-ad56-4ee2-8ec0-423a12d8d7fa",
            "serviceAreaName": "Deerfield Beach (DVB4)- Amazon.com"
        },
        {
            "serviceAreaId": "221c60b4-2825-4fdf-80de-360cdc73e8f4",
            "serviceAreaName": "Boca Raton (DMO6)- Amazon.com"
        },
        {
            "serviceAreaId": "ca2b3909-034b-4009-bbcb-1c27db8ae86c",
            "serviceAreaName": "Town Center at Boca Raton (PTAI) - Retail Delivery"
        }
    ]



with open("stationlist.txt", "w") as file:
    for station in stations:
        file.write(f"{station['serviceAreaId']}\t{station['serviceAreaName']}\n") 