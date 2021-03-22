import csv


def ClassFactory(class_name, dictionary):
    return type(class_name, (object,), dictionary)


class CsvReader:
    data = []

    def __init__(self, filepath):
        with open(filepath):
            csv_data = csv.Dictreader(text_data, delimiter='')
            for row in csv_data:
                self.data.append(row)
        pass

    def return_data_as_class(self, class_name):
        objects = []
        for row in self.data:
            objects.append(ClassFactory(class_name, row))
        return objects
