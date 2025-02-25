#3.1 txt dosyalarını oku yaz
mesagge = input("Mesajınızı giriniz: ")
# yazma 
with open("./data.txt","a",encoding="UTF-8") as file:
    file.write(f"{mesagge} \n")
    print("mesajınız eklendi. ")

# okuma 
import json

with open("./data.txt","r",encoding="UTF-8") as file:
    # read = file.readline() # satır satır okur
    # read = file.readlines() # her satır bir liste halinde verir
    read = file.read() # dosyayı komple okur

    print("\n data.tx: \n ", read)

#3.2 jyson dosyasını oku yaz 
# JSON dosyasına yazma
data = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
# JSON dosyasına yazma
with open("data.json", "w", encoding="UTF-8") as json_file:
    json.dump(data, json_file, ensure_ascii=False, indent=4)
    print("Veri JSON dosyasına yazıldı.")

# JSON dosyasını okuma
with open("data.json", "r", encoding="UTF-8") as json_file:
    data = json.load(json_file)
    print("JSON dosyasından okunan veri:")
    print(data)
