import json
from collections import defaultdict


class InverseIndex():

    def __init__(self):
        self.npi_index = defaultdict()
        self.name_index = defaultdict()
        self.address_index = defaultdict()
        self.data = []
        self.numdoc = 0
        self.qry_criteria = {"npi": self.npi_index,
                             "first_name": self.name_index,
                             "last_name": self.name_index,
                             "street": self.address_index,
                             "street_2": self.address_index,
                             "zip": self.address_index,
                             "city": self.address_index,
                             "state": self.address_index}

    def create_index(self, filepath):
        '''
        :param filepath: json file path
        :return:
        '''
        try:
            with open(filepath, 'r') as fin:
                for line in fin:
                    doc = json.loads(line.strip())
                    doctor_details = doc.get("doctor", None)
                    practices_details = doc.get("practices", None)
                    if doctor_details:
                        for key in doctor_details:
                            if key in self.qry_criteria:
                                index = self.qry_criteria.get(key)
                                self._add_index(index, doctor_details.get(key), self.numdoc)
                    if practices_details:
                        for items in practices_details:
                            for key in items:
                                if key in self.qry_criteria:
                                    index = self.qry_criteria.get(key)
                                    self._add_index(index, items.get(key), self.numdoc)
                    self.data.append(doc)
                    self.numdoc += 1
        except:
            raise "Error creating index"

    def search(self, query):
        '''
        :param query: json
        :return: json
        '''
        result = {}
        total_doc_ids = set()
        matched_doc_ids = set()
        result["total_docs"] = self.numdoc
        result["doc"] = []
        for key in query:
            if key not in self.qry_criteria:
                result["error"] = "Invalid search parameter ({0})".format(key)
                return result
            doc_ids = self.qry_criteria.get(key).get(query.get(key))
            total_doc_ids.update(doc_ids)
            if not matched_doc_ids:
                matched_doc_ids.update(doc_ids)
            else:
                matched_doc_ids = matched_doc_ids.intersection(doc_ids)
        result["doc_scanned_count"] = len(total_doc_ids)
        result["doc_matched_count"] = len(matched_doc_ids)
        for ids in matched_doc_ids:
            result["doc"].append(self.data[ids])
        return json.dumps(result)

    def _add_index(self, index, key, doc_num):
        if index.get(key):
            index[key].add(doc_num)
        else:
            index[key] = set([doc_num])

if __name__ == "__main__":
    Idx = InverseIndex()
    Idx.create_index("../data/source_data.json")
    print(Idx.search({"first_name": "Quinton", "last_name":"Mollie"}))
    print(Idx.search({"npi": "36556623055822736995"}))