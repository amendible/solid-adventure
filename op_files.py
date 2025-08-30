class F:
    def sequential_search_file(self, filename, value, param):
        index_param = -1
        with open(filename, "r") as file:
            for i, line in enumerate(file):
                arr = line.split(",")
                if( i == 0):
                    try:
                        index_param = arr.index(param)
                    except Exception :
                        return "No encontré la columna" + param
                elif arr[index_param] == value:
                    return arr
        return -1
        
    def read(self, filename):
        with open(filename,"r", encoding = "utf-8") as f:
            for linea in f: 
                print(linea.strip())
    
    def write(self, filename, dictionary):
        enable = 1
        id = 1
        with open(filename,"w", encoding="utf-8") as f:
            labels = list(dictionary[0].keys())
            for label in labels:
                f.write(label + ",")
            f.write("status" + "\n")
            for a in dictionary:
                count = 0
                f.write(str(id)+ ",")
                for d in a.values():
                    f.write(d )
                    count+=1
                    if len(a.values()) > count:
                        f.write(",")
                id+=1
                f.write(str(enable)+"\n")


    def delete(self, filename, id):
        list = []
        with open(filename, "r", encoding="utf-8") as f:
            list = f.readlines()

        newList = []
        for l in list:
            arr = l.strip().split(',')
            if str(arr[0]) == str(id):
                print(id)
                arr[len(arr)-1] = "0"
                ll = ""
                count = 1
                for a in arr:
                    ll = ll + str(a)
                    if count < len(arr):
                        ll = ll + ","
                    count+=1
                l = ll + "\n"
            newList.append(l)
        self.write_array(filename, newList)


def write_array(self, filename, list):
    with open(filename, "w", encoding="utf-8") as f:
        for l in list:
            arr = l.split(',')
            if str (arr[0]) ==str(id):
                print(id)


people = [{"name":"Juan", "lastname": "Perez"},
            {"name":"Luis", "lastname": "Gomez"},
            {"name":"Mario", "lastname": "Ruiz"}, ]

product = [{"name":"PC", "price": "50"},
            {"name":"Mouse", "price": "30"},
            {"name":"Keyboard", "price": "20"}, ]


f = F()
f.write("people.csv", people)
f.write("products.csv", product)
f.delete("notes.txt", 1)