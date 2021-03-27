import requests as req

ses = req.Session()
ss = ses.get("https://ejust-campus.ejust.edu.eg/login"
             )
ssdf = ss.content
token = (ssdf[ssdf.find(b"_token"):].split(b'"')[2])
dd = {"email": "fadi.alahmad@ejust.edu.eg", "password": "fady8009645",
      "_token": token}
nss = ses.post("https://ejust-campus.ejust.edu.eg/login"
               , data=dd
               )
ndd = {"_token": token,"breakfast_meal": "1", "lunch_meal": "1", "dinner_meal": '1'}
ses.get("https://ejust-campus.ejust.edu.eg/add/applicant/nutrition/reservation",
                )
nnss = ses.post("https://ejust-campus.ejust.edu.eg/add/applicant/nutrition/reservation/save",
                data=ndd)

if nnss.status_code == 200:
    print("DONE SUCCESSFULLY")
else:
    print(f"ERROR {nss.status_code}")
