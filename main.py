from tkinter import *
from distance_variables import *

PURPLE = "#521262"
FONT = "Monoton"
LOCATIONS = ["BATANGAS CITY", "LIPA CITY", "TANAUAN CITY", "BACOOR CITY", "CAVITE CITY", "DASMARINAS CITY", "IMUS CITY", "TAGAYTAY CITY","TRECE MARTIRES CITY", "BINAN CITY","CABUYAO CITY","SAN PABLO CITY", "SANTA ROSA CITY","LUCENA CITY","TAYABAS CITY","ANTIPOLO CITY","CALAMBA CITY"]
BACKGROUND = "#FFDEFA"
WHITE = "#FFFFFF"
EXPRESS_FARE_PER_KM = 13
NORMAL_FARE_PER_KM = 5

#APP'S BRAIN
def checking_infos(mode,distance):
    if mode == 0:
        fare = round(distance * EXPRESS_FARE_PER_KM)
        fees_to_pay.config(text=f"₱{fare}")
        distance_text.config(text=f"{distance}Km")
    else:
        fare = round(distance * NORMAL_FARE_PER_KM)
        fees_to_pay.config(text=f"₱{fare}")
        distance_text.config(text=f"{distance}Km")

def calculate():
    locality1 = first_locality.get().lower()
    locality2 = second_locality.get().lower()
    mode = r.get()
    #BATANGAS
    if locality1 == "batangas city" and locality2 == "lipa city" or locality1 == "lipa city" and locality2 == "batangas city":
        global BATANGAS_TO_LIPA
        distance = BATANGAS_TO_LIPA
        checking_infos(mode,distance)
    elif locality1 == "batangas city" and locality2 == "tanauan city" or locality1 == "tanauan city" and locality2 == "batangas city":
        global BATANGAS_TO_TANAUAN
        distance = BATANGAS_TO_TANAUAN
        checking_infos(mode, distance)
    elif locality1 == "batangas city" and locality2 == "bacoor city" or locality1 == "bacoor city" and locality2 == "batangas city":
        global BATANGAS_TO_BACOOR
        distance = BATANGAS_TO_BACOOR
        checking_infos(mode, distance)
    elif locality1 == "batangas city" and locality2 == "cavite city" or locality1 == "cavite city" and locality2 == "batangas city":
        global BATANGAS_TO_CAVITE
        distance = BATANGAS_TO_CAVITE
        checking_infos(mode, distance)
    elif locality1 == "batangas city" and locality2 == "dasmarinas city" or locality1 == "dasmarinas city" and locality2 == "batangas city":
        global BATANGAS_TO_DASMA
        distance = BATANGAS_TO_DASMA
        checking_infos(mode, distance)
    elif locality1 == "batangas city" and locality2 == "imus city" or locality1 == "imus city" and locality2 == "batangas city":
        global BATANGAS_TO_IMUS
        distance = BATANGAS_TO_IMUS
        checking_infos(mode, distance)
    elif locality1 == "batangas city" and locality2 == "tagaytay city" or locality1 == "tagaytay city" and locality2 == "batangas city":
        global BATANGAS_TO_TAGAYTAY
        distance = BATANGAS_TO_TAGAYTAY
        checking_infos(mode, distance)
    elif locality1 == "batangas city" and locality2 == "trece martires city" or locality1 == "trece martires city" and locality2 == "batangas city":
        global BATANGAS_TO_TRECE_MARTIRES
        distance = BATANGAS_TO_TRECE_MARTIRES
        checking_infos(mode, distance)
    elif locality1 == "batangas city" and locality2 == "binan city" or locality1 == "binan city" and locality2 == "batangas city":
        global BATANGAS_TO_BINAN
        distance = BATANGAS_TO_BINAN
        checking_infos(mode, distance)
    elif locality1 == "batangas city" and locality2 == "cabuyao city" or locality1 == "cabuyao city" and locality2 == "batangas city":
        global BATANGAS_TO_CABUYAO
        distance = BATANGAS_TO_CABUYAO
        checking_infos(mode, distance)
    elif locality1 == "batangas city" and locality2 == "san pablo city" or locality1 == "san pablo city" and locality2 == "batangas city":
        global BATANGAS_TO_SAN_PABLO
        distance = BATANGAS_TO_SAN_PABLO
        checking_infos(mode, distance)
    elif locality1 == "batangas city" and locality2 == "santa rosa city" or locality1 == "santa rosa city" and locality2 == "batangas city":
        global BATANGAS_TO_SANTA_ROSA
        distance = BATANGAS_TO_SANTA_ROSA
        checking_infos(mode, distance)
    elif locality1 == "batangas city" and locality2 == "lucena city" or locality1 == "lucena city" and locality2 == "batangas city":
        global BATANGAS_TO_LUCENA
        distance = BATANGAS_TO_LUCENA
        checking_infos(mode, distance)
    elif locality1 == "batangas city" and locality2 == "tayabas city" or locality1 == "tayabas city" and locality2 == "batangas city":
        global BATANGAS_TO_TAYABAS
        distance = BATANGAS_TO_TAYABAS
        checking_infos(mode, distance)
    elif locality1 == "batangas city" and locality2 == "antipolo city" or locality1 == "antipolo city" and locality2 == "batangas city":
        global BATANGAS_TO_ANTIPOLO
        distance = BATANGAS_TO_ANTIPOLO
        checking_infos(mode, distance)
    elif locality1 == "batangas city" and locality2 == "calamba city" or locality1 == "calamba city" and locality2 == "batangas city":
        global BATANGAS_TO_CALAMBA
        distance = BATANGAS_TO_CALAMBA
        checking_infos(mode, distance)
    #LIPA
    elif locality1 == "lipa city" and locality2 == "tanauan city" or locality1 == "lipa city" and locality2 == "lipa city":
        global LIPA_TO_TANAUAN
        distance = LIPA_TO_TANAUAN
        checking_infos(mode, distance)
    elif locality1 == "lipa city" and locality2 == "bacoor city" or locality1 == "bacoor city" and locality2 == "lipa city":
        global LIPA_TO_BACOOR
        distance = LIPA_TO_BACOOR
        checking_infos(mode, distance)
    elif locality1 == "lipa city" and locality2 == "cavite city" or locality1 == "cavite city" and locality2 == "lipa city":
        global LIPA_TO_CAVITE
        distance = LIPA_TO_CAVITE
        checking_infos(mode, distance)
    elif locality1 == "lipa city" and locality2 == "dasmarinas city" or locality1 == "dasmarinas city" and locality2 == "lipa city":
        global LIPA_TO_DASMA
        distance = LIPA_TO_DASMA
        checking_infos(mode, distance)
    elif locality1 == "lipa city" and locality2 == "imus city" or locality1 == "imus city" and locality2 == "lipa city":
        global LIPA_TO_IMUS
        distance = LIPA_TO_IMUS
        checking_infos(mode, distance)
    elif locality1 == "lipa city" and locality2 == "tagaytay city" or locality1 == "tagaytay city" and locality2 == "batangas city":
        global LIPA_TO_TAGAYTAY
        distance = LIPA_TO_TAGAYTAY
        checking_infos(mode, distance)
    elif locality1 == "lipa city" and locality2 == "trece martires city" or locality1 == "trece martires city" and locality2 == "lipa city":
        global LIPA_TO_TRECE_MARTIRES
        distance = LIPA_TO_TRECE_MARTIRES
        checking_infos(mode, distance)
    elif locality1 == "lipa city" and locality2 == "binan city" or locality1 == "binan city" and locality2 == "lipa city":
        global LIPA_TO_BINAN
        distance = LIPA_TO_BINAN
        checking_infos(mode, distance)
    elif locality1 == "lipa city" and locality2 == "cabuyao city" or locality1 == "cabuyao city" and locality2 == "lipa city":
        global LIPA_TO_CABUYAO
        distance = LIPA_TO_CABUYAO
        checking_infos(mode, distance)
    elif locality1 == "lipa city" and locality2 == "san pablo city" or locality1 == "san pablo city" and locality2 == "lipa city":
        global LIPA_TO_SAN_PABLO
        distance = LIPA_TO_SAN_PABLO
        checking_infos(mode, distance)
    elif locality1 == "lipa city" and locality2 == "santa rosa city" or locality1 == "santa rosa city" and locality2 == "lipa city":
        global LIPA_TO_SANTA_ROSA
        distance = LIPA_TO_SANTA_ROSA
        checking_infos(mode, distance)
    elif locality1 == "lipa city" and locality2 == "lucena city" or locality1 == "lucena city" and locality2 == "lipa city":
        global LIPA_TO_LUCENA
        distance = LIPA_TO_LUCENA
        checking_infos(mode, distance)
    elif locality1 == "lipa city" and locality2 == "tayabas city" or locality1 == "tayabas city" and locality2 == "lipa city":
        global LIPA_TO_TAYABAS
        distance = LIPA_TO_TAYABAS
        checking_infos(mode, distance)
    elif locality1 == "lipa city" and locality2 == "antipolo city" or locality1 == "antipolo city" and locality2 == "lipa city":
        global LIPA_TO_ANTIPOLO
        distance = LIPA_TO_ANTIPOLO
        checking_infos(mode, distance)
    elif locality1 == "lipa city" and locality2 == "calamba city" or locality1 == "calamba city" and locality2 == "lipa city":
        global LIPA_TO_CALAMBA
        distance = LIPA_TO_CALAMBA
        checking_infos(mode, distance)
    #TANAUAN
    elif locality1 == "tanauan city" and locality2 == "bacoor city" or locality1 == "bacoor city" and locality2 == "tanauan city":
        global TANAUAN_TO_BACOOR
        distance = TANAUAN_TO_BACOOR
        checking_infos(mode, distance)
    elif locality1 == "tanauan city" and locality2 == "cavite city" or locality1 == "cavite city" and locality2 == "tanauan city":
        global TANAUAN_TO_CAVITE
        distance = TANAUAN_TO_CAVITE
        checking_infos(mode, distance)
    elif locality1 == "tanauan city" and locality2 == "dasmarinas city" or locality1 == "dasmarinas city" and locality2 == "tanauan city":
        global TANAUAN_TO_DASMA
        distance = TANAUAN_TO_DASMA
        checking_infos(mode, distance)
    elif locality1 == "tanauan city" and locality2 == "imus city" or locality1 == "imus city" and locality2 == "tanauan city":
        global TANAUAN_TO_IMUS
        distance = TANAUAN_TO_IMUS
        checking_infos(mode, distance)
    elif locality1 == "tanauan city" and locality2 == "tagaytay city" or locality1 == "tagaytay city" and locality2 == "tanauan city":
        global TANAUAN_TO_TAGAYTAY
        distance = TANAUAN_TO_TAGAYTAY
        checking_infos(mode, distance)
    elif locality1 == "tanauan city" and locality2 == "trece martires city" or locality1 == "trece martires city" and locality2 == "tanauan city":
        global TANAUAN_TO_TRECE_MARTIRES
        distance = TANAUAN_TO_TRECE_MARTIRES
        checking_infos(mode, distance)
    elif locality1 == "tanauan city" and locality2 == "binan city" or locality1 == "binan city" and locality2 == "tanauan city":
        global TANAUAN_TO_BINAN
        distance = TANAUAN_TO_BINAN
        checking_infos(mode, distance)
    elif locality1 == "tanauan city" and locality2 == "cabuyao city" or locality1 == "cabuyao city" and locality2 == "tanauan city":
        global TANAUAN_TO_CABUYAO
        distance = TANAUAN_TO_CABUYAO
        checking_infos(mode, distance)
    elif locality1 == "tanauan city" and locality2 == "san pablo city" or locality1 == "trece martires city" and locality2 == "san pablo city":
        global TANAUAN_TO_SAN_PABLO
        distance = TANAUAN_TO_SAN_PABLO
        checking_infos(mode, distance)
    elif locality1 == "tanauan city" and locality2 == "santa rosa city" or locality1 == "santa rosa city" and locality2 == "tanauan city":
        global TANAUAN_TO_SANTA_ROSA
        distance = TANAUAN_TO_SANTA_ROSA
        checking_infos(mode, distance)
    elif locality1 == "tanauan city" and locality2 == "lucena city" or locality1 == "lucena city" and locality2 == "tanauan city":
        global TANAUAN_TO_LUCENA
        distance = TANAUAN_TO_LUCENA
        checking_infos(mode, distance)
    elif locality1 == "tanauan city" and locality2 == "tayabas city" or locality1 == "tayabas city" and locality2 == "tanauan city":
        global TANAUAN_TO_TAYABAS
        distance = TANAUAN_TO_TAYABAS
        checking_infos(mode, distance)
    elif locality1 == "tanauan city" and locality2 == "antipolo city" or locality1 == "antipolo city" and locality2 == "tanauan city":
        global TANAUAN_TO_ANTIPOLO
        distance = TANAUAN_TO_ANTIPOLO
        checking_infos(mode, distance)
    elif locality1 == "tanauan city" and locality2 == "calamba city" or locality1 == "calamba city" and locality2 == "tanauan city":
        global TANAUAN_TO_CALAMBA
        distance = TANAUAN_TO_CALAMBA
        checking_infos(mode, distance)
    #BACOOR
    elif locality1 == "bacoor city" and locality2 == "cavite city" or locality1 == "cavite city" and locality2 == "bacoor city":
        global BACOOR_TO_CAVITE
        distance = BACOOR_TO_CAVITE
        checking_infos(mode, distance)
    elif locality1 == "bacoor city" and locality2 == "dasmarinas city" or locality1 == "dasmarinas city" and locality2 == "bacoor city":
        global BACOOR_TO_DASMA
        distance = BACOOR_TO_DASMA
        checking_infos(mode, distance)
    elif locality1 == "bacoor city" and locality2 == "imus city" or locality1 == "imus city" and locality2 == "bacoor city":
        global BACOOR_TO_IMUS
        distance = BACOOR_TO_IMUS
        checking_infos(mode, distance)
    elif locality1 == "bacoor city" and locality2 == "tagaytay city" or locality1 == "tagaytay city" and locality2 == "bacoor city":
        global BACOOR_TO_TAGAYTAY
        distance = BACOOR_TO_TAGAYTAY
        checking_infos(mode, distance)
    elif locality1 == "bacoor city" and locality2 == "trece martires city" or locality1 == "trece martires city" and locality2 == "bacoor city":
        global BACOOR_TO_TRECE_MARTIRES
        distance = BACOOR_TO_TRECE_MARTIRES
        checking_infos(mode, distance)
    elif locality1 == "bacoor city" and locality2 == "binan city" or locality1 == "binan city" and locality2 == "bacoor city":
        global BACOOR_TO_BINAN
        distance = BACOOR_TO_BINAN
        checking_infos(mode, distance)
    elif locality1 == "bacoor city" and locality2 == "cabuyao city" or locality1 == "cabuyao city" and locality2 == "bacoor city":
        global BACOOR_TO_CABUYAO
        distance = BACOOR_TO_CABUYAO
        checking_infos(mode, distance)
    elif locality1 == "bacoor city" and locality2 == "san pablo city" or locality1 == "san pablo city" and locality2 == "bacoor city":
        global BACOOR_TO_SAN_PABLO
        distance = BACOOR_TO_SAN_PABLO
        checking_infos(mode, distance)
    elif locality1 == "bacoor city" and locality2 == "santa rosa city" or locality1 == "santa rosa city" and locality2 == "bacoor city":
        global BACOOR_TO_SANTA_ROSA
        distance = BACOOR_TO_SANTA_ROSA
        checking_infos(mode, distance)
    elif locality1 == "bacoor city" and locality2 == "lucena city" or locality1 == "lucena city" and locality2 == "bacoor city":
        global BACOOR_TO_LUCENA
        distance = BACOOR_TO_LUCENA
        checking_infos(mode, distance)
    elif locality1 == "bacoor city" and locality2 == "tayabas city" or locality1 == "tayabas city" and locality2 == "bacoor city":
        global BACOOR_TO_TAYABAS
        distance = BACOOR_TO_TAYABAS
        checking_infos(mode, distance)
    elif locality1 == "bacoor city" and locality2 == "antipolo city" or locality1 == "antipolo city" and locality2 == "bacoor city":
        global BACOOR_TO_ANTIPOLO
        distance = BACOOR_TO_ANTIPOLO
        checking_infos(mode, distance)
    elif locality1 == "bacoor city" and locality2 == "calamba city" or locality1 == "calamba city" and locality2 == "bacoor city":
        global BACOOR_TO_CALAMBA
        distance = BACOOR_TO_CALAMBA
        checking_infos(mode, distance)
    #CAVITE
    elif locality1 == "cavite city" and locality2 == "dasmarinas city" or locality1 == "dasmarinas city" and locality2 == "cavite city":
        global CAVITE_TO_DASMA
        distance = CAVITE_TO_DASMA
        checking_infos(mode, distance)
    elif locality1 == "cavite city" and locality2 == "imus city" or locality1 == "imus city" and locality2 == "cavite city":
        global CAVITE_TO_IMUS
        distance = CAVITE_TO_IMUS
        checking_infos(mode, distance)
    elif locality1 == "cavite city" and locality2 == "tagaytay city" or locality1 == "tagaytay city" and locality2 == "cavite city":
        global CAVITE_TO_TAGAYTAY
        distance = CAVITE_TO_TAGAYTAY
        checking_infos(mode, distance)
    elif locality1 == "cavite city" and locality2 == "trece martires city" or locality1 == "trece martires city" and locality2 == "cavite city":
        global CAVITE_TO_TRECE_MARTIRES
        distance = CAVITE_TO_TRECE_MARTIRES
        checking_infos(mode, distance)
    elif locality1 == "cavite city" and locality2 == "binan city" or locality1 == "binan city" and locality2 == "cavite city":
        global CAVITE_TO_BINAN
        distance = CAVITE_TO_BINAN
        checking_infos(mode, distance)
    elif locality1 == "cavite city" and locality2 == "cabuyao city" or locality1 == "cabuyao city" and locality2 == "cavite city":
        global CAVITE_TO_CABUYAO
        distance = CAVITE_TO_CABUYAO
        checking_infos(mode, distance)
    elif locality1 == "cavite city" and locality2 == "san pablo city" or locality1 == "san pablo city" and locality2 == "cavite city":
        global CAVITE_TO_SAN_PABLO
        distance = CAVITE_TO_SAN_PABLO
        checking_infos(mode, distance)
    elif locality1 == "cavite city" and locality2 == "santa rosa city" or locality1 == "santa rosa city" and locality2 == "cavite city":
        global CAVITE_TO_SANTA_ROSA
        distance = CAVITE_TO_SANTA_ROSA
        checking_infos(mode, distance)
    elif locality1 == "cavite city" and locality2 == "lucena city" or locality1 == "lucena city" and locality2 == "cavite city":
        global CAVITE_TO_LUCENA
        distance = CAVITE_TO_LUCENA
        checking_infos(mode, distance)
    elif locality1 == "cavite city" and locality2 == "tayabas city" or locality1 == "tayabas city" and locality2 == "cavite city":
        global CAVITE_TO_TAYABAS
        distance = CAVITE_TO_TAYABAS
        checking_infos(mode, distance)
    elif locality1 == "cavite city" and locality2 == "antipolo city" or locality1 == "antipolo city" and locality2 == "cavite city":
        global CAVITE_TO_ANTIPOLO
        distance = CAVITE_TO_ANTIPOLO
        checking_infos(mode, distance)
    elif locality1 == "cavite city" and locality2 == "calamba city" or locality1 == "calamba city" and locality2 == "cavite city":
        global CAVITE_TO_CALAMBA
        distance = CAVITE_TO_CALAMBA
        checking_infos(mode, distance)
    #DASMARINAS
    elif locality1 == "dasmarinas city" and locality2 == "imus city" or locality1 == "imus city" and locality2 == "dasmarinas city":
        global DASMA_TO_IMUS
        distance = DASMA_TO_IMUS
        checking_infos(mode, distance)
    elif locality1 == "dasmarinas city" and locality2 == "tagaytay city" or locality1 == "tagaytay city" and locality2 == "dasmarinas city":
        global DASMA_TO_TAGAYTAY
        distance = DASMA_TO_TAGAYTAY
        checking_infos(mode, distance)
    elif locality1 == "dasmarinas city" and locality2 == "trece martires city" or locality1 == "trece martires city" and locality2 == "dasmarinas city":
        global DASMA_TO_TRECE_MARTIRES
        distance = DASMA_TO_TRECE_MARTIRES
        checking_infos(mode, distance)
    elif locality1 == "dasmarinas city" and locality2 == "binan city" or locality1 == "binan city" and locality2 == "dasmarinas city":
        global DASMA_TO_BINAN
        distance = DASMA_TO_BINAN
        checking_infos(mode, distance)
    elif locality1 == "dasmarinas city" and locality2 == "cabuyao city" or locality1 == "cabuyao city" and locality2 == "dasmarinas city":
        global DASMA_TO_CABUYAO
        distance = DASMA_TO_CABUYAO
        checking_infos(mode, distance)
    elif locality1 == "dasmarinas city" and locality2 == "san pablo city" or locality1 == "san pablo city" and locality2 == "dasmarinas city":
        global DASMA_TO_SAN_PABLO
        distance = DASMA_TO_SAN_PABLO
        checking_infos(mode, distance)
    elif locality1 == "dasmarinas city" and locality2 == "santa rosa city" or locality1 == "santa rosa city" and locality2 == "dasmarinas city":
        global DASMA_TO_SANTA_ROSA
        distance = DASMA_TO_SANTA_ROSA
        checking_infos(mode, distance)
    elif locality1 == "dasmarinas city" and locality2 == "lucena city" or locality1 == "lucena city" and locality2 == "dasmarinas city":
        global DASMA_TO_LUCENA
        distance = DASMA_TO_LUCENA
        checking_infos(mode, distance)
    elif locality1 == "dasmarinas city" and locality2 == "tayabas city" or locality1 == "tayabas city" and locality2 == "dasmarinas city":
        global DASMA_TO_TAYABAS
        distance = DASMA_TO_TAYABAS
        checking_infos(mode, distance)
    elif locality1 == "dasmarinas city" and locality2 == "antipolo city" or locality1 == "antipolo city" and locality2 == "dasmarinas city":
        global DASMA_TO_ANTIPOLO
        distance = DASMA_TO_ANTIPOLO
        checking_infos(mode, distance)
    elif locality1 == "dasmarinas city" and locality2 == "calamba city" or locality1 == "calamba city" and locality2 == "dasmarinas city":
        global DASMA_TO_CALAMBA
        distance = DASMA_TO_CALAMBA
        checking_infos(mode, distance)
    #IMUS
    elif locality1 == "imus city" and locality2 == "tagaytay city" or locality1 == "tagaytay city" and locality2 == "imus city":
        global IMUS_TO_TAGAYTAY
        distance = IMUS_TO_TAGAYTAY
        checking_infos(mode, distance)
    elif locality1 == "imus city" and locality2 == "trece martires city" or locality1 == "trece martires city" and locality2 == "imus city":
        global IMUS_TO_TRECE_MARTIRES
        distance = IMUS_TO_TRECE_MARTIRES
        checking_infos(mode, distance)
    elif locality1 == "imus city" and locality2 == "binan city" or locality1 == "binan city" and locality2 == "imus city":
        global IMUS_TO_BINAN
        distance = IMUS_TO_BINAN
        checking_infos(mode, distance)
    elif locality1 == "imus city" and locality2 == "cabuyao city" or locality1 == "cabuyao city" and locality2 == "imus city":
        global IMUS_TO_CABUYAO
        distance = IMUS_TO_CABUYAO
        checking_infos(mode, distance)
    elif locality1 == "imus city" and locality2 == "san pablo city" or locality1 == "san pablo city" and locality2 == "imus city":
        global IMUS_TO_SAN_PABLO
        distance = IMUS_TO_SAN_PABLO
        checking_infos(mode, distance)
    elif locality1 == "imus city" and locality2 == "santa rosa city" or locality1 == "santa rosa city" and locality2 == "imus city":
        global IMUS_TO_SANTA_ROSA
        distance = IMUS_TO_SANTA_ROSA
        checking_infos(mode, distance)
    elif locality1 == "imus city" and locality2 == "lucena city" or locality1 == "lucena city" and locality2 == "imus city":
        global IMUS_TO_LUCENA
        distance = IMUS_TO_LUCENA
        checking_infos(mode, distance)
    elif locality1 == "imus city" and locality2 == "tayabas city" or locality1 == "tayabas city" and locality2 == "imus city":
        global IMUS_TO_TAYABAS
        distance = IMUS_TO_TAYABAS
        checking_infos(mode, distance)
    elif locality1 == "imus city" and locality2 == "antipolo city" or locality1 == "antipolo city" and locality2 == "imus city":
        global IMUS_TO_ANTIPOLO
        distance = IMUS_TO_ANTIPOLO
        checking_infos(mode, distance)
    elif locality1 == "imus city" and locality2 == "calamba city" or locality1 == "calamba city" and locality2 == "imus city":
        global IMUS_TO_CALAMBA
        distance = IMUS_TO_CALAMBA
        checking_infos(mode, distance)
    #TAGAYTAY
    elif locality1 == "tagaytay city" and locality2 == "trece martires city" or locality1 == "trece martires city" and locality2 == "tagaytay city":
        global TAGAYTAY_TO_TRECE_MARTIRES
        distance = TAGAYTAY_TO_TRECE_MARTIRES
        checking_infos(mode, distance)
    elif locality1 == "tagaytay city" and locality2 == "binan city" or locality1 == "binan city" and locality2 == "tagaytay city":
        global TAGAYTAY_TO_BINAN
        distance = TAGAYTAY_TO_BINAN
        checking_infos(mode, distance)
    elif locality1 == "tagaytay city" and locality2 == "cabuyao city" or locality1 == "cabuyao city" and locality2 == "tagaytay city":
        global TAGAYTAY_TO_CABUYAO
        distance = TAGAYTAY_TO_CABUYAO
        checking_infos(mode, distance)
    elif locality1 == "tagaytay city" and locality2 == "san pablo city" or locality1 == "san pablo city" and locality2 == "tagaytay city":
        global TAGAYTAY_TO_SAN_PABLO
        distance = TAGAYTAY_TO_SAN_PABLO
        checking_infos(mode, distance)
    elif locality1 == "tagaytay city" and locality2 == "santa rosa city" or locality1 == "santa rosa city" and locality2 == "tagaytay city":
        global TAGAYTAY_TO_SANTA_ROSA
        distance = TAGAYTAY_TO_SANTA_ROSA
        checking_infos(mode, distance)
    elif locality1 == "tagaytay city" and locality2 == "lucena city" or locality1 == "lucena city" and locality2 == "tagaytay city":
        global TAGAYTAY_TO_LUCENA
        distance = TAGAYTAY_TO_LUCENA
        checking_infos(mode, distance)
    elif locality1 == "tagaytay city" and locality2 == "tayabas city" or locality1 == "tayabas city" and locality2 == "tagaytay city":
        global TAGAYTAY_TO_TAYABAS
        distance = TAGAYTAY_TO_TAYABAS
        checking_infos(mode, distance)
    elif locality1 == "tagaytay city" and locality2 == "antipolo city" or locality1 == "antipolo city" and locality2 == "tagaytay city":
        global TAGAYTAY_TO_ANTIPOLO
        distance = TAGAYTAY_TO_ANTIPOLO
        checking_infos(mode, distance)
    elif locality1 == "tagaytay city" and locality2 == "calamba city" or locality1 == "calamba city" and locality2 == "tagaytay city":
        global TAGAYTAY_TO_CALAMBA
        distance = TAGAYTAY_TO_CALAMBA
        checking_infos(mode, distance)
    #TRESE MARTIRES
    elif locality1 == "trece martires city" and locality2 == "binan city" or locality1 == "binan city" and locality2 == "trece martires city":
        global TRECE_MARTIRES_TO_BINAN
        distance = TRECE_MARTIRES_TO_BINAN
        checking_infos(mode, distance)
    elif locality1 == "trece martires city" and locality2 == "cabuyao city" or locality1 == "cabuyao city" and locality2 == "trece martires city":
        global TRECE_MARTIRES_TO_CABUYAO
        distance = TRECE_MARTIRES_TO_CABUYAO
        checking_infos(mode, distance)
    elif locality1 == "trece martires city" and locality2 == "san pablo city" or locality1 == "san pablo city" and locality2 == "trece martires city":
        global TRECE_MARTIRES_TO_SAN_PABLO
        distance = TRECE_MARTIRES_TO_SAN_PABLO
        checking_infos(mode, distance)
    elif locality1 == "trece martires city" and locality2 == "santa rosa city" or locality1 == "santa rosa city" and locality2 == "trece martires city":
        global TRECE_MARTIRES_TO_SANTA_ROSA
        distance = TRECE_MARTIRES_TO_SANTA_ROSA
        checking_infos(mode, distance)
    elif locality1 == "trece martires city" and locality2 == "lucena city" or locality1 == "lucena city" and locality2 == "trece martires city":
        global TRECE_MARTIRES_TO_LUCENA
        distance = TRECE_MARTIRES_TO_LUCENA
        checking_infos(mode, distance)
    elif locality1 == "trece martires city" and locality2 == "tayabas city" or locality1 == "tayabas city" and locality2 == "trece martires city":
        global TRECE_MARTIRES_TO_TAYABAS
        distance = TRECE_MARTIRES_TO_TAYABAS
        checking_infos(mode, distance)
    elif locality1 == "trece martires city" and locality2 == "antipolo city" or locality1 == "antipolo city" and locality2 == "trece martires city":
        global TRECE_MARTIRES_TO_ANTIPOLO
        distance = TRECE_MARTIRES_TO_ANTIPOLO
        checking_infos(mode, distance)
    elif locality1 == "trece martires city" and locality2 == "calamba city" or locality1 == "calamba city" and locality2 == "trece martires city":
        global TRECE_MARTIRES_TO_CALAMBA
        distance = TRECE_MARTIRES_TO_CALAMBA
        checking_infos(mode, distance)
    #BINAN
    elif locality1 == "binan city" and locality2 == "cabuyao city" or locality1 == "cabuyao city" and locality2 == "binan city":
        global BINAN_TO_CABUYAO
        distance = BINAN_TO_CABUYAO
        checking_infos(mode, distance)
    elif locality1 == "binan city" and locality2 == "san pablo city" or locality1 == "san pablo city" and locality2 == "binan city":
        global BINAN_TO_SAN_PABLO
        distance = BINAN_TO_SAN_PABLO
        checking_infos(mode, distance)
    elif locality1 == "binan city" and locality2 == "santa rosa city" or locality1 == "santa rosa city" and locality2 == "binan city":
        global BINAN_TO_SANTA_ROSA
        distance = BINAN_TO_SANTA_ROSA
        checking_infos(mode, distance)
    elif locality1 == "binan city" and locality2 == "luce city" or locality1 == "lucena city" and locality2 == "binan city":
        global BINAN_TO_LUCENA
        distance = BINAN_TO_LUCENA
        checking_infos(mode, distance)
    elif locality1 == "binan city" and locality2 == "tayabas city" or locality1 == "tayabas city" and locality2 == "binan city":
        global BINAN_TO_TAYABAS
        distance = BINAN_TO_TAYABAS
        checking_infos(mode, distance)
    elif locality1 == "binan city" and locality2 == "antipolo city" or locality1 == "antipolo city" and locality2 == "binan city":
        global BINAN_TO_ANTIPOLO
        distance = BINAN_TO_ANTIPOLO
        checking_infos(mode, distance)
    elif locality1 == "binan city" and locality2 == "calamba city" or locality1 == "calamba city" and locality2 == "binan city":
        global BINAN_TO_CALAMBA
        distance = BINAN_TO_CALAMBA
        checking_infos(mode, distance)
    #CABUYAO
    elif locality1 == "cabuyao city" and locality2 == "san pablo city" or locality1 == "san pablo city" and locality2 == "cabuyao city":
        global CABUYAO_TO_SAN_PABLO
        distance = CABUYAO_TO_SAN_PABLO
        checking_infos(mode, distance)
    elif locality1 == "cabuyao city" and locality2 == "santa rosa city" or locality1 == "santa rosa city" and locality2 == "cabuyao city":
        global CABUYAO_TO_SANTA_ROSA
        distance = CABUYAO_TO_SANTA_ROSA
        checking_infos(mode, distance)
    elif locality1 == "cabuyao city" and locality2 == "lucena city" or locality1 == "lucena city" and locality2 == "cabuyao city":
        global CABUYAO_TO_LUCENA
        distance = CABUYAO_TO_LUCENA
        checking_infos(mode, distance)
    elif locality1 == "cabuyao city" and locality2 == "tayabas city" or locality1 == "tayabas city" and locality2 == "cabuyao city":
        global CABUYAO_TO_TAYABAS
        distance = CABUYAO_TO_TAYABAS
        checking_infos(mode, distance)
    elif locality1 == "cabuyao city" and locality2 == "antipolo city" or locality1 == "antipolo city" and locality2 == "cabuyao city":
        global CABUYAO_TO_ANTIPOLO
        distance = CABUYAO_TO_ANTIPOLO
        checking_infos(mode, distance)
    elif locality1 == "cabuyao city" and locality2 == "calamba city" or locality1 == "calamba city" and locality2 == "cabuyao city":
        global CABUYAO_TO_CALAMBA
        distance = CABUYAO_TO_CALAMBA
        checking_infos(mode, distance)
    #SAN PABLO
    elif locality1 == "san pablo city" and locality2 == "santa rosa city" or locality1 == "santa rosa city" and locality2 == "san pablo city":
        global SAN_PABLO_TO_SANTA_ROSA
        distance = SAN_PABLO_TO_SANTA_ROSA
        checking_infos(mode, distance)
    elif locality1 == "san pablo city" and locality2 == "lucena city" or locality1 == "lucena city" and locality2 == "san pablo city":
        global SAN_PABLO_TO_LUCENA
        distance = SAN_PABLO_TO_LUCENA
        checking_infos(mode, distance)
    elif locality1 == "san pablo city" and locality2 == "tayabas city" or locality1 == "tayabas city" and locality2 == "san pablo city":
        global SAN_PABLO_TO_TAYABAS
        distance = SAN_PABLO_TO_TAYABAS
        checking_infos(mode, distance)
    elif locality1 == "san pablo city" and locality2 == "antipolo city" or locality1 == "antipolo city" and locality2 == "san pablo city":
        global SAN_PABLO_TO_ANTIPOLO
        distance = SAN_PABLO_TO_ANTIPOLO
        checking_infos(mode, distance)
    elif locality1 == "san pablo city" and locality2 == "calamba city" or locality1 == "calamba city" and locality2 == "san pablo city":
        global SAN_PABLO_TO_CALAMBA
        distance = SAN_PABLO_TO_CALAMBA
        checking_infos(mode, distance)
    #SANTA ROSA
    elif locality1 == "santa rosa city" and locality2 == "lucena city" or locality1 == "lucena city" and locality2 == "santa rosa city":
        global SANTA_ROSA_TO_LUCENA
        distance = SANTA_ROSA_TO_LUCENA
        checking_infos(mode, distance)
    elif locality1 == "santa rosa city" and locality2 == "tayabas city" or locality1 == "tayabas city" and locality2 == "santa rosa city":
        global SANTA_ROSA_TO_TAYABAS
        distance = SANTA_ROSA_TO_TAYABAS
        checking_infos(mode, distance)
    elif locality1 == "santa rosa city" and locality2 == "antipolo city" or locality1 == "antipolo city" and locality2 == "santa rosa city":
        global SANTA_ROSA_TO_ANTIPOLO
        distance = SANTA_ROSA_TO_ANTIPOLO
        checking_infos(mode, distance)
    elif locality1 == "santa rosa city" and locality2 == "calamba city" or locality1 == "calamba city" and locality2 == "santa rosa city":
        global SANTA_ROSA_TO_CALAMBA
        distance = SANTA_ROSA_TO_CALAMBA
        checking_infos(mode, distance)
    #LUCENA
    elif locality1 == "lucena city" and locality2 == "tayabas city" or locality1 == "tayabas city" and locality2 == "lucena city":
        global LUCENA_TO_TAYABAS
        distance = LUCENA_TO_TAYABAS
        checking_infos(mode, distance)
    elif locality1 == "lucena city" and locality2 == "antipolo city" or locality1 == "antipolo city" and locality2 == "lucena city":
        global LUCENA_TO_ANTIPOLO
        distance = LUCENA_TO_ANTIPOLO
        checking_infos(mode, distance)
    elif locality1 == "lucena city" and locality2 == "calamba city" or locality1 == "calamba city" and locality2 == "lucena city":
        global LUCENA_TO_CALAMBA
        distance = LUCENA_TO_CALAMBA
        checking_infos(mode, distance)
    #TAYABAS
    elif locality1 == "tayabas city" and locality2 == "antipolo city" or locality1 == "antipolo city" and locality2 == "tayabas city":
        global TAYABAS_TO_ANTIPOLO
        distance = TAYABAS_TO_ANTIPOLO
        checking_infos(mode, distance)
    elif locality1 == "tayabas city" and locality2 == "calamba city" or locality1 == "calamba city" and locality2 == "tayabas city":
        global TAYABAS_TO_CALAMBA
        distance = TAYABAS_TO_CALAMBA
        checking_infos(mode, distance)
    #ANTIPOLO
    elif locality1 == "antipolo city" and locality2 == "calamba city" or locality1 == "calamba city" and locality2 == "antipolo city":
        global ANTIPOLO_TO_CALAMBA
        distance = ANTIPOLO_TO_CALAMBA
        checking_infos(mode, distance)
    else:
        pass

#---------UI---------------
root=Tk()
root.title("TekaCommute: Commute Fees Calculator")
root.config(padx=50, pady=50, bg=BACKGROUND)
root.rowconfigure(index=1,weight=2)


logo_canvas = Canvas(width=1037, height=241, bg=BACKGROUND, highlightthickness=0)
logo = PhotoImage(file="FINAL LOGO final.png")
logo_canvas.create_image(518.5, 120.5, image=logo)
logo_canvas.grid(column=0, row=0, columnspan=2)


from_text = Label(text="From: ", fg=PURPLE, font=(FONT, 30, "bold"),bg=BACKGROUND)
from_text.grid(column=0,row=1,columnspan=1, sticky="w")

to_text = Label(text="To: ", fg=PURPLE, font=(FONT, 30, "bold"),bg=BACKGROUND)
to_text.grid(column=0,row=3,sticky="w")

option = "Please select a location"
first_locality = StringVar()
first_locality.set("CHOOSE A LOCALITY")
first_choose_locality = OptionMenu(root, first_locality, *LOCATIONS)
first_choose_locality.config(width=50, height=3, bg=WHITE, fg=PURPLE, activebackground=WHITE, borderwidth=0.5, relief="solid", font=(FONT, 13))
first_choose_locality.grid(column=0, row=2, sticky="w")
first_choose_locality.config(highlightbackground=PURPLE, )

second_locality = StringVar()
second_locality.set("CHOOSE A LOCALITY")
second_choose_locality = OptionMenu(root, second_locality, *LOCATIONS)
second_choose_locality.config(width=50, height=3, bg=WHITE, fg=PURPLE, activebackground=WHITE, borderwidth=1, relief="solid", font=(FONT, 13))
second_choose_locality.grid(column=0, row=4, sticky="w")
second_choose_locality.config(highlightbackground=PURPLE)


mode_of_transportation_text = Label(text="Mode of transportation: ", fg=PURPLE, font=(FONT, 30, "bold"), bg=BACKGROUND)
mode_of_transportation_text.grid(column=1, row=1, rowspan=2)
r = IntVar()
express_radio_button = Radiobutton(text="Express(Grab,Uber,Taxi)", variable=r, value=0, font=(FONT, 18), fg=PURPLE, bg=BACKGROUND, highlightthickness=0, activebackground=BACKGROUND)
express_radio_button.grid(column=1, row=2, rowspan=2, sticky="W", columnspan=2)
normal_radio_button = Radiobutton(text="Normal(Jeep,Bus,UV,Tric)", variable=r, value=1, font=(FONT, 18), fg=PURPLE, bg=BACKGROUND, highlightthickness=0, activebackground=BACKGROUND)
normal_radio_button.grid(column=1, row=2, rowspan=3, sticky="W")
calculate = Button(command=calculate,text="CALCULATE", width=40,height=3, fg=WHITE,bg=PURPLE,activebackground=PURPLE,highlightbackground=WHITE, borderwidth=1, relief="solid", font=(FONT))
calculate.grid(column=1,row=4,rowspan=2,columnspan=2)


estimated_time_arrival =Label(text="TOTAL DISTANCE IN KILOMETERS ", fg=PURPLE, font=(FONT, 15, "bold"),bg=BACKGROUND)
estimated_time_arrival.grid(column=0,row=6)
distance_text = Label(text="00.00KM", fg=PURPLE, font=(FONT, 20, "bold"), bg=BACKGROUND)
distance_text.grid(column=0, row=7)

estimated_fees_to_pay = Label(text="ESTIMATED FEES TO PAY FOR TRANSPORT ", fg=PURPLE, font=(FONT, 15, "bold"),bg=BACKGROUND)
estimated_fees_to_pay.grid(column=1,row=6, stick="e")

fees_to_pay = Label(text="₱ 00. 00",fg=PURPLE, font=(FONT, 20, "bold"),bg=BACKGROUND)
fees_to_pay.grid(column=1,row=7)






root.mainloop()