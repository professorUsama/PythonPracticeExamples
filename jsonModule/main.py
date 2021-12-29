import json
if __name__ == '__main__':
    book = {}
    book["Python"] = {
        "Name":"Python",
        "Language":"English",
        "Code Examples":150
    }
    book["C++"] = {
        "Name":"Cpp",
        "Language":"English",
        "Code Examples":"200"
    }
    # print(book)
    s = json.dumps(book)
    print(s)
    with open('jsonModule/jsonData.txt','w') as f:
        f.write(s)
        print(f"Sucessfully writteen")
