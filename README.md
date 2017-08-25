# Inverse Index

 A simple class for creating inverse indexing using given json data.
 Searches can be done on fields *npi, name, address*. The query should be of json type.
 Eg.
 
    Idx = InverseIndex()
    Idx.create_index("../data/source_data.json")
    print(Idx.search({"first_name": "Quinton", "last_name":"Mollie"}))
  
 This will give result as a json with the number of documents scanned, number of documents matched and the matched documents.
 Eg.
 
    {
    "total_docs": 11231,
    "doc_matched_count": 1,
    "doc_scanned_count": 16,
    "doc": [
        {
            "doctor": {
                "first_name": "Quinton",
                "npi": "36233383542350521233",
                "last_name": "Mollie"
            },
            "practices": [
                {
                    "lat": "81.37417480720865",
                    "street": "8496 Kennedi Inlet",
                    "state": "OR",
                    "street_2": "Suite 815",
                    "lon": "-95.33450729432164",
                    "city": "Nealville",
                    "zip": "52665-6811"
                },
                {
                    "lat": "69.84837521604314",
                    "street": "29483 Nader Wall",
                    "state": "UT",
                    "street_2": "Apt. 748",
                    "lon": "87.36942972635728",
                    "city": "Rashadborough",
                    "zip": "46006-3437"
                },
                {
                    "lat": "84.90377842497296",
                    "street": "2122 Wintheiser Valleys",
                    "state": "AK",
                    "street_2": "Suite 855",
                    "lon": "177.28706015725533",
                    "city": "South Daronland",
                    "zip": "99372"
                }]
            }
        ]
    }

