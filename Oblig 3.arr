use context starter2024
include shared-gdrive("dcic-2021", "1wyQZj_L0qqV9Ekgr9au6RX2iqt2Ga8Ep")
include gdrive-sheets
include data-source
ssid = "1RYN0i4Zx_UETVuYacgaGfnFcv4l9zd9toQTTdkQkj7g"


my-table = table: navn :: String, Etter-navn :: String, Gruppe, alder :: Number
  
  
   

  row: "Christel", "Litherland", "2A", 34
  row: "Veda", "Seiller", "2B", 27
  row: "Adham", "Wynch", "2A", 37
  row: "York", "Andover", "2B", 22
  row: "Benn", "Drawmer", "2B", 28
  row: "Delila", "Tackes", "2A", 38
  row: "Myrtia", "Eary", "2A", 32
 
end


person_one_age=my-table.row-n(0)["Gruppe"]
person_two_age=my-table.row-n(1)["Gruppe"]
person_three_age=my-table.row-n(2)["Gruppe"]
person_four_age=my-table.row-n(3)["Gruppe"]
person_five_age_=my-table.row-n(4)["Gruppe"]
person_six_age=my-table.row-n(5)["Gruppe"]
person_seven_age=my-table.row-n(6)["Gruppe"]

#funkjson på å finne gruppe 2 A
Ovre_gruppe = filter-with(my-table, lam(r): (r["alder"] > 30) and (r["alder"] < 50)end)


#funksjon på å finne gruppe 2 B
Lavere_gruppe = filter-with(my-table, lam(r): (r["alder"] > 20) and (r["alder"] < 30)end)

Ovre_gruppe
Lavere_gruppe