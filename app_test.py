import os
import psutil
import time
import subprocess
import fnmatch
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from tkinter import *
from PIL import ImageFilter,Image
from tkinter import filedialog, messagebox
from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import RandomForestRegressor
from math import sqrt
from sklearn.metrics import mean_absolute_percentage_error
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from sklearn.preprocessing import LabelEncoder
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    if request.method == 'POST':
        age = int(request.form['age'])
        veg = int(request.form['veg_or_nonveg'])
        weight = float(request.form['weight'])
        height = float(request.form['height'])
        kategori = int(request.form['kategori'])

        if kategori == 0 :
            rekomendasi = "Breakfast"
            # siang(age,veg,weight,height)
            data = pd.read_csv('food_ori.csv')

            # Data dari kolom "Breakfast", "Lunch", dan "Dinner" dipisahkan dan disimpan dalam daftar terpisah
            Breakfastdata = data['Breakfast']
            BreakfastdataNumpy = Breakfastdata.to_numpy()
            Lunchdata = data['Lunch']
            LunchdataNumpy = Lunchdata.to_numpy()
            Dinnerdata = data['Dinner']
            DinnerdataNumpy = Dinnerdata.to_numpy()

            #nama item makanan
            Food_itemsdata = data['Food_items']

            #Vegan or Non-Veg
            VegNovVeg = data['VegNovVeg']
            
            ##Memisahkan Item Makanan Berdasarkan Kategori Waktu Makan

            #menyimpan nama item makanan yang telah dipisahkan
            print()
            breakfastfoodseparated=[]
            print(breakfastfoodseparated)
            print('breakfastfoodseparated')
            print()


            Lunchfoodseparated=[]
            print('Lunchfoodseparated')
            print(Lunchfoodseparated)
            print()

            Dinnerfoodseparated=[]
            print('Dinnerfoodseparated')
            print(Dinnerfoodseparated)
            print()


            #menyimpan indeks (posisi) yang sesuai dalam data asli untuk item-item 
            print()
            breakfastfoodseparatedID=[]
            print('breakfastfoodseparatedID')
            print(breakfastfoodseparatedID)
            print()

            LunchfoodseparatedID=[]
            print('LunchfoodseparatedID')
            print(LunchfoodseparatedID)
            print()

            DinnerfoodseparatedID=[]
            print('DinnerfoodseparatedID')
            print(DinnerfoodseparatedID)
            print()

            #Loop for berulang melalui panjang Seri Breakfastdata (mengasumsikan semua Seri memiliki panjang yang sama)
            for i in range(len(Breakfastdata)):
                #memeriksa apakah nilai pada indeks saat ini (i) di array BreakfastdataNumpy = 1 (Benar) / Representasi Biner
                if BreakfastdataNumpy[i]==1:
                    #menyimpan makanan
                    breakfastfoodseparated.append(Food_itemsdata[i])

                    print()
                    print('breakfastfoodseparated')
                    print ('BREAKFAST FOOD LIST')
                    print(breakfastfoodseparated)
                    print('#########')
                    print()

                    # menyimpan indeks baris item sarapan
                    breakfastfoodseparatedID.append(i)
                    print('breakfastfoodseparatedID')
                    print(breakfastfoodseparatedID)
                    print('#########')
                    print()

                if LunchdataNumpy[i]==1:
                    Lunchfoodseparated.append(Food_itemsdata[i])
                    print()
                    print('Lunchfoodseparated')
                    print ('LUNCH FOOD LIST')
                    print(Lunchfoodseparated)
                    print('#########')
                    print()
                    LunchfoodseparatedID.append(i)
                    print('LunchfoodseparatedID')
                    print(LunchfoodseparatedID)
                    print('#########')
                    print()
                if DinnerdataNumpy[i]==1:
                    Dinnerfoodseparated.append(Food_itemsdata[i])

                    print()
                    print('Dinnerfoodseparated')
                    print ('DINNER FOOD LIST')
                    print(Dinnerfoodseparated)
                    print('#########')
                    print()

                    DinnerfoodseparatedID.append(i)
                    print('DinnerfoodseparatedID')
                    print(DinnerfoodseparatedID)
                    print('#########')
                    print()

            #pengambilan baris tertentu dari DataFrame data berdasarkan ID yang disimpan dalam daftar breakfastfoodseparatedID, LunchfoodseparatedID, dan DinnerfoodseparatedID.
            #iloc adalah metode pengindeksan yang kuat dalam pandas yang memungkinkan  memilih baris dan kolom berdasarkan indeks integer atau daftar indeks karena lebih efisien daripada menggunakan pengindeksan baris tradisional (misalnya, data[0]) untuk memilih beberapa baris atau menerapkan logika pengindeksan yang kompleks.

            #Baris ini mengekstrak baris dari DataFrame data pada indeks yang ditentukan dalam daftar breakfastfoodseparatedID. Misalnya, jika breakfastfoodseparatedID berisi [10, 25, 32], baris ini akan mengekstrak baris pada indeks 10, 25, dan 32 dari DataFrame data.
            breakfastfoodseparatedIDdata = data.iloc[breakfastfoodseparatedID]
            print()
            print('breakfastfoodseparatedIDdata')
            print(breakfastfoodseparatedIDdata)
            print('#1')
            #mentranspos DataFrame breakfastfoodseparatedIDdata yang diekstrak. Transpos pada dasarnya menukar baris dan kolom.
            breakfastfoodseparatedIDdata=breakfastfoodseparatedIDdata.T
            print('breakfastfoodseparatedIDdata')
            print(breakfastfoodseparatedIDdata)
            print('#2')
            #membuat daftar val yang berisi bilangan bulat dari 5 hingga 14 (inklusif).
            val=list(np.arange(5,15))
            print()
            print('val')
            print(val)
            #membuat daftar baru Valapnd dengan menambahkan elemen 0 di awal daftar val. Daftar yang dihasilkan akan menjadi [0, 5, 6, 7, ..., 14].
            Valapnd=[0]+val
            print()
            print('Valapnd')
            print(Valapnd)
            #Baris ini mengekstrak baris dari DataFrame breakfastfoodseparatedIDdata yang ditranspos berdasarkan indeks dalam daftar Valapnd
            #Misalnya, jika Valapnd adalah [0, 5, 6, 7, ..., 14], baris ini akan memilih baris pertama (indeks 0) dan baris 5 hingga 14 dari DataFrame yang ditranspos.
            breakfastfoodseparatedIDdata=breakfastfoodseparatedIDdata.iloc[Valapnd]
            print()
            print('breakfastfoodseparatedIDdata')
            print(breakfastfoodseparatedIDdata)
            print('#3')
            #Baris ini mentranspos DataFrame breakfastfoodseparatedIDdata yang diekstrak kembali ke bentuk aslinya.
            breakfastfoodseparatedIDdata=breakfastfoodseparatedIDdata.T
            print("Breakfast Data")
            print("breakfastfoodseparatedIDdata")
            print (breakfastfoodseparatedIDdata)
            print()

            LunchfoodseparatedIDdata = data.iloc[LunchfoodseparatedID]
            print()
            print('LunchfoodseparatedIDdata')
            print(LunchfoodseparatedIDdata)
            print('#1')

            LunchfoodseparatedIDdata=LunchfoodseparatedIDdata.T
            print('LunchfoodseparatedIDdata')
            print(LunchfoodseparatedIDdata)
            print('#2')


            val=list(np.arange(5,15))
            print()
            print('val')
            print(val)

            Valapnd=[0]+val
            print()
            print('Valapnd')
            print(Valapnd)

            LunchfoodseparatedIDdata=LunchfoodseparatedIDdata.iloc[Valapnd]
            print()
            print('LunchfoodseparatedIDdata')
            print(LunchfoodseparatedIDdata)
            print('#3')

            LunchfoodseparatedIDdata=LunchfoodseparatedIDdata.T
            print()
            print("Lunch Data")
            print('LunchfoodseparatedIDdata')
            print(LunchfoodseparatedIDdata)
            print()


            DinnerfoodseparatedIDdata = data.iloc[DinnerfoodseparatedID]
            print()
            print('DinnerfoodseparatedIDdata')
            print(DinnerfoodseparatedIDdata)
            print('#1')


            DinnerfoodseparatedIDdata=DinnerfoodseparatedIDdata.T
            print('DinnerfoodseparatedIDdata')
            print(DinnerfoodseparatedIDdata)
            print('#2')

            val=list(np.arange(5,15))
            print()
            print('val')
            print(val)


            Valapnd=[0]+val
            print()
            print('Valapnd')
            print(Valapnd)


            DinnerfoodseparatedIDdata=DinnerfoodseparatedIDdata.iloc[Valapnd]
            print()
            print('DinnerfoodseparatedIDdata')
            print(DinnerfoodseparatedIDdata)
            print('#3')

            DinnerfoodseparatedIDdata=DinnerfoodseparatedIDdata.T
            print()
            print("Dinner Data")
            print('DinnerfoodseparatedIDdata')
            print (DinnerfoodseparatedIDdata)
            print()

            bmi = weight/((height / 100) ** 2)
            
            for lp in range (0,100,20):
                test_list=np.arange(lp,lp+20)
                print(test_list)

                for i in test_list: 
                    if(i == age):
                        print('Age is between',str(lp),str(lp+10))
                        print('agecl')
                        agecl=round(lp/20)   
                        print(agecl)

            # Menentukan kategori BMI
            print("Your body mass index (BMI) is: ", bmi)
            if ( bmi < 16):
                hasilbmi = "According to your BMI, you are very thin"
                clbmi=4
            elif ( bmi >= 16 and bmi < 18.5):
                hasilbmi ="According to your BMI, you are Thin"
                clbmi=3
            elif ( bmi >= 18.5 and bmi < 25):
                hasilbmi ="According to your BMI, you are healthy"
                clbmi=2
            elif ( bmi >= 25 and bmi < 30):
                hasilbmi = "According to your BMI, you are overweight"
                clbmi=1
            elif ( bmi >=30):
                hasilbmi = "According to your BMI, you are very overweight"
                clbmi=0

            ti=(bmi+agecl)/2
            print('ti')
            print(ti)

            DinnerfoodseparatedIDdata=DinnerfoodseparatedIDdata.to_numpy()
            print()
            print('DinnerfoodseparatedIDdata to numpy')
            print(DinnerfoodseparatedIDdata)
            print()

            LunchfoodseparatedIDdata=LunchfoodseparatedIDdata.to_numpy()
            print()
            print('LunchfoodseparatedIDdata to numpy')
            print(LunchfoodseparatedIDdata)
            print()


            breakfastfoodseparatedIDdata=breakfastfoodseparatedIDdata.to_numpy()
            print()
            print('breakfastfoodseparatedIDdata to numpy')
            print(breakfastfoodseparatedIDdata)
            print()

            

            Datacalorie=DinnerfoodseparatedIDdata[1:,1:len(DinnerfoodseparatedIDdata)]
            print()
            print('Datacalorie DinnerfoodseparatedIDdata')
            print(Datacalorie)

            X = np.array(Datacalorie)
            print()
            print('X')
            print(X)
            print()

            kmeans = KMeans(n_clusters=3, random_state=0).fit(X)
            print()
            print('kmeans')
            print(kmeans)
            print()

            print ('## Result Prediksi ##')
            print(kmeans.labels_)
            print()
            # XValu=np.arange(0,len(kmeans.labels_))
            # fig,axs=plt.subplots(1,1,figsize=(15,5))
            # plt.bar(XValu,kmeans.labels_)
            dnrlbl=kmeans.labels_
            print()
            print("dnrlbl")
            print(dnrlbl)
            print (len(dnrlbl))
            plt.title("Makanan dengan Kalori Rendah-Tinggi")
            print()

            Datacalorie=LunchfoodseparatedIDdata[1:,1:len(LunchfoodseparatedIDdata)]
            print()
            print("Datacalorie LunchfoodseparatedIDdata")
            print(Datacalorie)
            print()

            X = np.array(Datacalorie)
            kmeans = KMeans(n_clusters=3, random_state=0).fit(X)
            print()
            print('X')
            print(X)
            print()

            print ('## Hasil Prediksi ##')
            print(kmeans.labels_)
            print()
            # XValu=np.arange(0,len(kmeans.labels_))
            # fig,axs=plt.subplots(1,1,figsize=(15,5))
            # plt.bar(XValu,kmeans.labels_)
            lnchlbl=kmeans.labels_
            print('lnchlbl')
            print(lnchlbl)
            print (len(lnchlbl))
            plt.title("Makanan dengan Kalori Rendah-Tinggi")
            print()

            Datacalorie=breakfastfoodseparatedIDdata[1:,1:len(breakfastfoodseparatedIDdata)]
            print()
            print("Datacalorie breakfastfoodseparatedIDdata")
            print(Datacalorie)
            print()

            X = np.array(Datacalorie)
            print()
            print('X')
            print(X)
            print()

            kmeans = KMeans(n_clusters=3, random_state=0).fit(X)
            print ('## Hasil Prediksi ##')
            print(kmeans.labels_)
            print()
            # XValu=np.arange(0,len(kmeans.labels_))
            # fig,axs=plt.subplots(1,1,figsize=(15,5))
            # plt.bar(XValu,kmeans.labels_)
            brklbl=kmeans.labels_
            print('brklbl')
            print(brklbl)
            print (len(brklbl))
            plt.title("Makanan dengan Kalori Rendah-Tinggi")
            print()

            
            print('Breakfast')
            print(brklbl)
            print('Lunch')
            print(lnchlbl)
            print("Dinner")
            print(dnrlbl)

            datafin = pd.read_csv('nutrition_distriution.csv')
            datafin.head(5)

            dataTog=datafin.T
            print()
            print('dataTog')
            print(dataTog)

            bmicls=[0,1,2,3,4]
            agecls=[0,1,2,3,4]
            healthycat = dataTog.iloc[[1,2,7,8]]

            print("healthycat=")
            print(healthycat)
            print(len(healthycat))

            healthycat=healthycat.T
            healthycatDdata=healthycat.to_numpy()
            print('healthycatDdata')
            print(healthycatDdata)

            healthycat=healthycatDdata[1:,0:len(healthycatDdata)]
            print("healthycat")
            print(healthycat)

            healthycatfin=np.zeros((len(healthycat)*5,6),dtype=np.float32)
            print('healthycatfin')
            print(healthycatfin)
            print()
            s=0
            ys=[]

            for zz in range(5):
                for jj in range(len(healthycat)):
                    valloc=list(healthycat[jj])
                    print('valloc#1')
                    print(valloc)
                    print()
                    valloc.append(bmicls[zz])
                    print('valloc#2')
                    print(valloc)
                    print()
                    valloc.append(agecls[zz])
                    print('valloc#3')
                    print(valloc)
                    print()
                    healthycatfin[s]=np.array(valloc)
                    print('healthycatfin[s]')
                    print(healthycatfin[s])
                    print()
                    # ys.append(dnrlbl[jj])
                    ys.append(brklbl[jj])
                    # ys.append(lnchlbl[jj])
                    print('ys')
                    print(ys)
                    s+=1
            X_test=np.zeros((len(healthycat)*5,6),dtype=np.float32)
            print()
            print('X_test#1')
            print(X_test)
            print('####################')


            for jj in range(len(healthycat)):
                valloc=list(healthycat[jj])
                print('valloc#11')
                print(valloc)
                print()
                valloc.append(agecl)
                print('valloc#22')
                print(valloc)
                print()
                valloc.append(clbmi)
                print('valloc#33')
                print(valloc)
                print()
                X_test[jj]=np.array(valloc)*ti
            print()
            print('X_test#2')
            print (X_test)
            print()

            X_train=healthycatfin# Features
            print()
            print('X_train')
            print(X_train)
            print()

            y_train=ys # Labels
            print()
            print('y_train')
            print(y_train)
            print()

            clf=RandomForestClassifier(n_estimators=100)
            clf.fit(X_train,y_train)
            print()
            print('clf')
            print(clf)
            print()

            print('X_test[1]')
            print (X_test[1])

            y_pred=clf.predict(X_test)
            print()
            print('y_pred')
            print(y_pred)
            print()
            print('ok')
            print()
        
            total_rekomendasi = 0
            print('\nRekomendasi Makanan yang cocok:')
            for ii in range(len(y_pred)):
                if ii < len(Food_itemsdata) and y_pred[ii] == 0:
                    if int(veg) == 0 and VegNovVeg[ii] == 0:
                        print(Food_itemsdata[ii])
                        total_rekomendasi += 1
                    elif int(veg) == 1 and VegNovVeg[ii] == 1:
                        print(Food_itemsdata[ii])
                        total_rekomendasi += 1

            print('\nTotal makanan yang direkomendasikan:', total_rekomendasi)

            # # Calculating feature importance
            # importances = clf.feature_importances_

            # # Pastikan jumlah nama fitur sesuai dengan jumlah fitur dalam data
            # feature_names = list(dataTog.index) + ['bmi_class', 'age_class']
            # if len(importances) != len(feature_names):
            #     print("Jumlah fitur tidak sesuai dengan nama fitur. Menggunakan indeks fitur sebagai nama.")
            #     feature_names = [f'feature_{i}' for i in range(len(importances))]

            # # Menampilkan pentingnya fitur
            # feature_importances = pd.DataFrame(importances, index=feature_names, columns=['importance'])
            # feature_importances = feature_importances.sort_values('importance', ascending=False)
            # print('\nFeature Importances:')
            # print(feature_importances)
            

            # Menambahkan kode untuk mencetak 10 makanan terbaik
            print("\nMakanan Terbaik:")
            diet_recommendations = [] 
            if total_rekomendasi >= 5 or total_rekomendasi<= 5:
                count = 0
                for ii in range(len(y_pred)):
                    if ii < len(Food_itemsdata) and y_pred[ii] == 0 and count < 5:
                        if int(veg) == 0 and VegNovVeg[ii] == 0:
                            print(Food_itemsdata[ii])
                            diet_recommendations.append(Food_itemsdata[ii])
                            count += 1
                        elif int(veg) == 1 and VegNovVeg[ii] == 1:
                            print(Food_itemsdata[ii])
                            diet_recommendations.append(Food_itemsdata[ii])
                            count += 1

        

            total_error = 0
            total_items = len(y_pred)

            for i in range(total_items):
                if i < len(Food_itemsdata) and y_pred[i] == 0:
                    if int(veg) == 0 and VegNovVeg[i] == 0:
                        total_error += 1
                    elif int(veg) == 1 and VegNovVeg[i] == 1:
                        total_error += 1

            mape = (total_error / total_items) * 100
            print("MAPE:", mape, "%")

            print()
            data = pd.read_csv('strong.csv')
            df = pd.DataFrame(data)

            X = df[['Weight', 'Set Order', 'Reps']]
            y = df['Exercise Name']

            label_encoder = LabelEncoder()
            y_encoded = label_encoder.fit_transform(y)
            print(y_encoded)

            X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.3, random_state=42)

            print('X_train')
            print(X_train)
            print('X_test')
            print(X_test)
            print('y_train')
            print(y_train)
            print('y_test')
            print(y_test)

            rf = RandomForestRegressor(n_estimators=100, max_depth=10, min_samples_split=5, random_state=42)
            rf.fit(X_train, y_train)

            weight_to_predict = weight
            predicted_exercise = rf.predict([[weight_to_predict, 0, 0]])
            predicted_exercise_label = label_encoder.inverse_transform(predicted_exercise.astype(int))

            try:
                result = df[df['Exercise Name'] == predicted_exercise_label[0]][['Set Order', 'Reps']]
                set_order = result.iloc[0]['Set Order']
                reps = result.iloc[0]['Reps']
                exercise_recommendations = f"Best exercise : {predicted_exercise_label[0]} | Set Order: {set_order} | Reps: {reps}"
                print(f"Best exercise: {predicted_exercise_label[0]}, Set Order: {set_order}, Reps: {reps}")
            except IndexError:
                print("Tidak ada latihan fisik yang dapat diprediksi berdasarkan berat yang dimasukkan.")

            predicted_proba = rf.predict([[weight_to_predict, 0, 0]])

            top_3_exercises_indices = (-predicted_proba).argsort()[:3]
            
            for i, exercise_idx in enumerate(top_3_exercises_indices):
                exercise_name = label_encoder.inverse_transform([exercise_idx])[0]
                result = df[df['Exercise Name'] == exercise_name][['Set Order', 'Reps']]
                set_order = result.iloc[0]['Set Order']
                reps = result.iloc[0]['Reps']
                exercise_recommendationslain = f"Other Recommendation : {exercise_name} | Set Order: {set_order} | Reps: {reps}"
                print(f"Other Recommendation :{exercise_name}, Set Order: {set_order}, Reps: {reps}")

            print()    
            # Predict MAE
            y_pred = rf.predict(X_test)
            mae = mean_absolute_error(y_test, y_pred)
            # Calculate MAPE
            mape = (mae / y_test.mean()) * 100  
            print(f"MAPE Latihan Fisik: {mape} %")
            print()
            
            return render_template('result.html', age = age , veg = veg,  weight = weight , height = height , bmi =bmi , hasilbmi = hasilbmi ,rekomendasi = rekomendasi ,diet_recommendations=diet_recommendations,exercise_recommendations = exercise_recommendations,exercise_recommendationslain = exercise_recommendationslain)
        
        if kategori == 1 :
            rekomendasi = "Lunch"
            # sore(age,veg,weight,height)
            data = pd.read_csv('food_ori.csv')

            # Data dari kolom "Breakfast", "Lunch", dan "Dinner" dipisahkan dan disimpan dalam daftar terpisah
            Breakfastdata = data['Breakfast']
            BreakfastdataNumpy = Breakfastdata.to_numpy()
            Lunchdata = data['Lunch']
            LunchdataNumpy = Lunchdata.to_numpy()
            Dinnerdata = data['Dinner']
            DinnerdataNumpy = Dinnerdata.to_numpy()

            #nama item makanan
            Food_itemsdata = data['Food_items']

            #Vegan or Non-Veg
            VegNovVeg = data['VegNovVeg']
            
            ##Memisahkan Item Makanan Berdasarkan Kategori Waktu Makan

            #menyimpan nama item makanan yang telah dipisahkan
            print()
            breakfastfoodseparated=[]
            print(breakfastfoodseparated)
            print('breakfastfoodseparated')
            print()


            Lunchfoodseparated=[]
            print('Lunchfoodseparated')
            print(Lunchfoodseparated)
            print()

            Dinnerfoodseparated=[]
            print('Dinnerfoodseparated')
            print(Dinnerfoodseparated)
            print()


            #menyimpan indeks (posisi) yang sesuai dalam data asli untuk item-item 
            print()
            breakfastfoodseparatedID=[]
            print('breakfastfoodseparatedID')
            print(breakfastfoodseparatedID)
            print()

            LunchfoodseparatedID=[]
            print('LunchfoodseparatedID')
            print(LunchfoodseparatedID)
            print()

            DinnerfoodseparatedID=[]
            print('DinnerfoodseparatedID')
            print(DinnerfoodseparatedID)
            print()

            #Loop for berulang melalui panjang Seri Breakfastdata (mengasumsikan semua Seri memiliki panjang yang sama)
            for i in range(len(Breakfastdata)):
                #memeriksa apakah nilai pada indeks saat ini (i) di array BreakfastdataNumpy = 1 (Benar) / Representasi Biner
                if BreakfastdataNumpy[i]==1:
                    #menyimpan makanan
                    breakfastfoodseparated.append(Food_itemsdata[i])

                    print()
                    print('breakfastfoodseparated')
                    print ('BREAKFAST FOOD LIST')
                    print(breakfastfoodseparated)
                    print('#########')
                    print()

                    # menyimpan indeks baris item sarapan
                    breakfastfoodseparatedID.append(i)
                    print('breakfastfoodseparatedID')
                    print(breakfastfoodseparatedID)
                    print('#########')
                    print()

                if LunchdataNumpy[i]==1:
                    Lunchfoodseparated.append(Food_itemsdata[i])
                    print()
                    print('Lunchfoodseparated')
                    print ('LUNCH FOOD LIST')
                    print(Lunchfoodseparated)
                    print('#########')
                    print()
                    LunchfoodseparatedID.append(i)
                    print('LunchfoodseparatedID')
                    print(LunchfoodseparatedID)
                    print('#########')
                    print()
                if DinnerdataNumpy[i]==1:
                    Dinnerfoodseparated.append(Food_itemsdata[i])

                    print()
                    print('Dinnerfoodseparated')
                    print ('DINNER FOOD LIST')
                    print(Dinnerfoodseparated)
                    print('#########')
                    print()

                    DinnerfoodseparatedID.append(i)
                    print('DinnerfoodseparatedID')
                    print(DinnerfoodseparatedID)
                    print('#########')
                    print()

            #pengambilan baris tertentu dari DataFrame data berdasarkan ID yang disimpan dalam daftar breakfastfoodseparatedID, LunchfoodseparatedID, dan DinnerfoodseparatedID.
            #iloc adalah metode pengindeksan yang kuat dalam pandas yang memungkinkan  memilih baris dan kolom berdasarkan indeks integer atau daftar indeks karena lebih efisien daripada menggunakan pengindeksan baris tradisional (misalnya, data[0]) untuk memilih beberapa baris atau menerapkan logika pengindeksan yang kompleks.

            #Baris ini mengekstrak baris dari DataFrame data pada indeks yang ditentukan dalam daftar breakfastfoodseparatedID. Misalnya, jika breakfastfoodseparatedID berisi [10, 25, 32], baris ini akan mengekstrak baris pada indeks 10, 25, dan 32 dari DataFrame data.
            breakfastfoodseparatedIDdata = data.iloc[breakfastfoodseparatedID]
            print()
            print('breakfastfoodseparatedIDdata')
            print(breakfastfoodseparatedIDdata)
            print('#1')
            #mentranspos DataFrame breakfastfoodseparatedIDdata yang diekstrak. Transpos pada dasarnya menukar baris dan kolom.
            breakfastfoodseparatedIDdata=breakfastfoodseparatedIDdata.T
            print('breakfastfoodseparatedIDdata')
            print(breakfastfoodseparatedIDdata)
            print('#2')
            #membuat daftar val yang berisi bilangan bulat dari 5 hingga 14 (inklusif).
            val=list(np.arange(5,15))
            print()
            print('val')
            print(val)
            #membuat daftar baru Valapnd dengan menambahkan elemen 0 di awal daftar val. Daftar yang dihasilkan akan menjadi [0, 5, 6, 7, ..., 14].
            Valapnd=[0]+val
            print()
            print('Valapnd')
            print(Valapnd)
            #Baris ini mengekstrak baris dari DataFrame breakfastfoodseparatedIDdata yang ditranspos berdasarkan indeks dalam daftar Valapnd
            #Misalnya, jika Valapnd adalah [0, 5, 6, 7, ..., 14], baris ini akan memilih baris pertama (indeks 0) dan baris 5 hingga 14 dari DataFrame yang ditranspos.
            breakfastfoodseparatedIDdata=breakfastfoodseparatedIDdata.iloc[Valapnd]
            print()
            print('breakfastfoodseparatedIDdata')
            print(breakfastfoodseparatedIDdata)
            print('#3')
            #Baris ini mentranspos DataFrame breakfastfoodseparatedIDdata yang diekstrak kembali ke bentuk aslinya.
            breakfastfoodseparatedIDdata=breakfastfoodseparatedIDdata.T
            print("Breakfast Data")
            print("breakfastfoodseparatedIDdata")
            print (breakfastfoodseparatedIDdata)
            print()

            LunchfoodseparatedIDdata = data.iloc[LunchfoodseparatedID]
            print()
            print('LunchfoodseparatedIDdata')
            print(LunchfoodseparatedIDdata)
            print('#1')

            LunchfoodseparatedIDdata=LunchfoodseparatedIDdata.T
            print('LunchfoodseparatedIDdata')
            print(LunchfoodseparatedIDdata)
            print('#2')


            val=list(np.arange(5,15))
            print()
            print('val')
            print(val)

            Valapnd=[0]+val
            print()
            print('Valapnd')
            print(Valapnd)

            LunchfoodseparatedIDdata=LunchfoodseparatedIDdata.iloc[Valapnd]
            print()
            print('LunchfoodseparatedIDdata')
            print(LunchfoodseparatedIDdata)
            print('#3')

            LunchfoodseparatedIDdata=LunchfoodseparatedIDdata.T
            print()
            print("Lunch Data")
            print('LunchfoodseparatedIDdata')
            print(LunchfoodseparatedIDdata)
            print()


            DinnerfoodseparatedIDdata = data.iloc[DinnerfoodseparatedID]
            print()
            print('DinnerfoodseparatedIDdata')
            print(DinnerfoodseparatedIDdata)
            print('#1')


            DinnerfoodseparatedIDdata=DinnerfoodseparatedIDdata.T
            print('DinnerfoodseparatedIDdata')
            print(DinnerfoodseparatedIDdata)
            print('#2')

            val=list(np.arange(5,15))
            print()
            print('val')
            print(val)


            Valapnd=[0]+val
            print()
            print('Valapnd')
            print(Valapnd)


            DinnerfoodseparatedIDdata=DinnerfoodseparatedIDdata.iloc[Valapnd]
            print()
            print('DinnerfoodseparatedIDdata')
            print(DinnerfoodseparatedIDdata)
            print('#3')

            DinnerfoodseparatedIDdata=DinnerfoodseparatedIDdata.T
            print()
            print("Dinner Data")
            print('DinnerfoodseparatedIDdata')
            print (DinnerfoodseparatedIDdata)
            print()

            bmi = weight/((height / 100) ** 2)
            
            for lp in range (0,100,20):
                test_list=np.arange(lp,lp+20)
                print(test_list)

                for i in test_list: 
                    if(i == age):
                        print('Age is between',str(lp),str(lp+10))
                        print('agecl')
                        agecl=round(lp/20)   
                        print(agecl)

            # Menentukan kategori BMI
            print("Your body mass index (BMI) is: ", bmi)
            if ( bmi < 16):
                hasilbmi = "According to your BMI, you are very thin"
                clbmi=4
            elif ( bmi >= 16 and bmi < 18.5):
                hasilbmi ="According to your BMI, you are Thin"
                clbmi=3
            elif ( bmi >= 18.5 and bmi < 25):
                hasilbmi ="According to your BMI, you are healthy"
                clbmi=2
            elif ( bmi >= 25 and bmi < 30):
                hasilbmi = "According to your BMI, you are overweight"
                clbmi=1
            elif ( bmi >=30):
                hasilbmi = "According to your BMI, you are very overweight"
                clbmi=0

            ti=(bmi+agecl)/2
            print('ti')
            print(ti)

            DinnerfoodseparatedIDdata=DinnerfoodseparatedIDdata.to_numpy()
            print()
            print('DinnerfoodseparatedIDdata to numpy')
            print(DinnerfoodseparatedIDdata)
            print()

            LunchfoodseparatedIDdata=LunchfoodseparatedIDdata.to_numpy()
            print()
            print('LunchfoodseparatedIDdata to numpy')
            print(LunchfoodseparatedIDdata)
            print()


            breakfastfoodseparatedIDdata=breakfastfoodseparatedIDdata.to_numpy()
            print()
            print('breakfastfoodseparatedIDdata to numpy')
            print(breakfastfoodseparatedIDdata)
            print()

            

            Datacalorie=DinnerfoodseparatedIDdata[1:,1:len(DinnerfoodseparatedIDdata)]
            print()
            print('Datacalorie DinnerfoodseparatedIDdata')
            print(Datacalorie)

            X = np.array(Datacalorie)
            print()
            print('X')
            print(X)
            print()

            kmeans = KMeans(n_clusters=3, random_state=0).fit(X)
            print()
            print('kmeans')
            print(kmeans)
            print()

            print ('## Result Prediksi ##')
            print(kmeans.labels_)
            print()
            print('Predict')
            # print (kmeans.predict([Datacalorie[0]]))
            # XValu=np.arange(0,len(kmeans.labels_))
            # fig,axs=plt.subplots(1,1,figsize=(15,5))
            # plt.bar(XValu,kmeans.labels_)
            dnrlbl=kmeans.labels_
            print()
            print("dnrlbl")
            print(dnrlbl)
            print (len(dnrlbl))
            plt.title("Makanan dengan Kalori Rendah-Tinggi")
            print()

            Datacalorie=LunchfoodseparatedIDdata[1:,1:len(LunchfoodseparatedIDdata)]
            print()
            print("Datacalorie LunchfoodseparatedIDdata")
            print(Datacalorie)
            print()

            X = np.array(Datacalorie)
            kmeans = KMeans(n_clusters=3, random_state=0).fit(X)
            print()
            print('X')
            print(X)
            print()

            print ('## Hasil Prediksi ##')
            print(kmeans.labels_)
            print()
            print('Predict')

            # print (kmeans.predict([Datacalorie[0]]))
            # XValu=np.arange(0,len(kmeans.labels_))
            # fig,axs=plt.subplots(1,1,figsize=(15,5))
            # plt.bar(XValu,kmeans.labels_)
            lnchlbl=kmeans.labels_
            print('lnchlbl')
            print(lnchlbl)
            print (len(lnchlbl))
            plt.title("Makanan dengan Kalori Rendah-Tinggi")
            print()

            Datacalorie=breakfastfoodseparatedIDdata[1:,1:len(breakfastfoodseparatedIDdata)]
            print()
            print("Datacalorie breakfastfoodseparatedIDdata")
            print(Datacalorie)
            print()

            X = np.array(Datacalorie)
            print()
            print('X')
            print(X)
            print()

            kmeans = KMeans(n_clusters=3, random_state=0).fit(X)
            print ('## Hasil Prediksi ##')
            print(kmeans.labels_)
            print()
            print('Predict')

            # print (kmeans.predict([Datacalorie[0]]))
            # XValu=np.arange(0,len(kmeans.labels_))
            # fig,axs=plt.subplots(1,1,figsize=(15,5))
            # plt.bar(XValu,kmeans.labels_)
            brklbl=kmeans.labels_
            print('brklbl')
            print(brklbl)
            print (len(brklbl))
            plt.title("Makanan dengan Kalori Rendah-Tinggi")
            print()
            print('Breakfast')
            print(brklbl)
            print('Lunch')
            print(lnchlbl)
            print("Dinner")
            print(dnrlbl)

            datafin = pd.read_csv('nutrition_distriution.csv')
            datafin.head(5)

            dataTog=datafin.T
            print()
            print('dataTog')
            print(dataTog)

            bmicls=[0,1,2,3,4]
            agecls=[0,1,2,3,4]
            healthycat = dataTog.iloc[[0,1,2,3,4,7,9,10]]

            print("healthycat=")
            print(healthycat)
            print(len(healthycat))

            healthycat=healthycat.T
            healthycatDdata=healthycat.to_numpy()
            print('healthycatDdata')
            print(healthycatDdata)

            healthycat=healthycatDdata[1:,0:len(healthycatDdata)]
            print("healthycat")
            print(healthycat)

            healthycatfin=np.zeros((len(healthycat)*5,10),dtype=np.float32)
            print('healthycatfin')
            print(healthycatfin)
            print()
            s=0
            ys=[]

            for zz in range(5):
                for jj in range(len(healthycat)):
                    valloc=list(healthycat[jj])
                    print('valloc#1')
                    print(valloc)
                    print()
                    valloc.append(bmicls[zz])
                    print('valloc#2')
                    print(valloc)
                    print()
                    valloc.append(agecls[zz])
                    print('valloc#3')
                    print(valloc)
                    print()
                    healthycatfin[s]=np.array(valloc)
                    print('healthycatfin[s]')
                    print(healthycatfin[s])
                    print()
                    # ys.append(dnrlbl[jj])
                    # ys.append(brklbl[jj])
                    ys.append(lnchlbl[jj])
                    print('ys')
                    print(ys)
                    s+=1
            X_test=np.zeros((len(healthycat)*5,10),dtype=np.float32)
            print()
            print('X_test#1')
            print(X_test)
            print('####################')


            for jj in range(len(healthycat)):
                valloc=list(healthycat[jj])
                print('valloc#11')
                print(valloc)
                print()
                valloc.append(agecl)
                print('valloc#22')
                print(valloc)
                print()
                valloc.append(clbmi)
                print('valloc#33')
                print(valloc)
                print()
                X_test[jj]=np.array(valloc)*ti
            print()
            print('X_test#2')
            print (X_test)
            print()

            X_train=healthycatfin# Features
            print()
            print('X_train')
            print(X_train)
            print()

            y_train=ys # Labels
            print()
            print('y_train')
            print(y_train)
            print()

            clf=RandomForestClassifier(n_estimators=100)
            clf.fit(X_train,y_train)
            print()
            print('clf')
            print(clf)
            print()

            print('X_test[1]')
            print (X_test[1])

            y_pred=clf.predict(X_test)
            print()
            print('y_pred')
            print(y_pred)
            print()
            print('ok')
            print()
        
            total_rekomendasi = 0
            print('\nRekomendasi Makanan yang cocok:')
            for ii in range(len(y_pred)):
                if ii < len(Food_itemsdata) and y_pred[ii] == 0:
                    if int(veg) == 0 and VegNovVeg[ii] == 0:
                        print(Food_itemsdata[ii])
                        total_rekomendasi += 1
                    elif int(veg) == 1 and VegNovVeg[ii] == 1:
                        print(Food_itemsdata[ii])
                        total_rekomendasi += 1

            print('\nTotal makanan yang direkomendasikan:', total_rekomendasi)

            # Menambahkan kode untuk mencetak 10 makanan terbaik
            print("\n5 Makanan Terbaik:")
            diet_recommendations = [] 
            if total_rekomendasi >= 5 or total_rekomendasi <= 5:
                count = 0
                for ii in range(len(y_pred)):
                    if ii < len(Food_itemsdata) and y_pred[ii] == 0 and count < 5:
                        if int(veg) == 0 and VegNovVeg[ii] == 0:
                            print(Food_itemsdata[ii])
                            diet_recommendations.append(Food_itemsdata[ii])
                            count += 1
                        elif int(veg) == 1 and VegNovVeg[ii] == 1:
                            print(Food_itemsdata[ii])
                            diet_recommendations.append(Food_itemsdata[ii])
                            count += 1
    
            total_error = 0
            total_items = len(y_pred)

            for i in range(total_items):
                if i < len(Food_itemsdata) and y_pred[i] == 0:
                    if int(veg) == 0 and VegNovVeg[i] == 0:
                        total_error += 1
                    elif int(veg) == 1 and VegNovVeg[i] == 1:
                        total_error += 1

            # Menggunakan mean_absolute_percentage_error untuk menghitung MAPE
            mape = mean_absolute_percentage_error([total_items - total_error], [total_items]) * 100
            print("MAPE Rekomendasi Makan:", mape, "%")

            total_error = 0
            total_items = len(y_pred)

            for i in range(total_items):
                if i < len(Food_itemsdata) and y_pred[i] == 0:
                    if int(veg) == 0 and VegNovVeg[i] == 0:
                        total_error += 1
                    elif int(veg) == 1 and VegNovVeg[i] == 1:
                        total_error += 1

            mape = (total_error / total_items) * 100
            print("MAPE #5:", mape, "%")

            print()
            data = pd.read_csv('strong.csv')
            df = pd.DataFrame(data)

            X = df[['Weight', 'Set Order', 'Reps']]
            y = df['Exercise Name']

            label_encoder = LabelEncoder()
            y_encoded = label_encoder.fit_transform(y)
            print(y_encoded)

            X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.3, random_state=0)

            print('X_train')
            print(X_train)
            print('X_test')
            print(X_test)
            print('y_train')
            print(y_train)
            print('y_test')
            print(y_test)

            rf = RandomForestRegressor(n_estimators=100, max_depth=10, min_samples_split=5, random_state=0)
            rf.fit(X_train, y_train)

            weight_to_predict = weight
            predicted_exercise = rf.predict([[weight_to_predict, 0, 0]])
            print("predicted_exercise")
            print(predicted_exercise)
            predicted_exercise_label = label_encoder.inverse_transform(predicted_exercise.astype(int))

            try:
                result = df[df['Exercise Name'] == predicted_exercise_label[0]][['Set Order', 'Reps']]
                set_order = result.iloc[0]['Set Order']
                reps = result.iloc[0]['Reps']
                exercise_recommendations = f"Best exercise : {predicted_exercise_label[0]} | Set Order: {set_order} | Reps: {reps}"
                print(f"Best exercise: {predicted_exercise_label[0]}, Set Order: {set_order}, Reps: {reps}")
            except IndexError:
                print("Tidak ada latihan fisik yang dapat diprediksi berdasarkan berat yang dimasukkan.")

            predicted_proba = rf.predict([[weight_to_predict, 0, 0]])

            top_3_exercises_indices = (-predicted_proba).argsort()[:3]
            
            for i, exercise_idx in enumerate(top_3_exercises_indices):
                exercise_name = label_encoder.inverse_transform([exercise_idx])[0]
                result = df[df['Exercise Name'] == exercise_name][['Set Order', 'Reps']]
                set_order = result.iloc[0]['Set Order']
                reps = result.iloc[0]['Reps']
                exercise_recommendationslain = f"Other Recommendation : {exercise_name} | Set Order: {set_order} | Reps: {reps}"
                print(f"Other Recommendation : Exercise Name: {exercise_name}, Set Order: {set_order}, Reps: {reps}")

            print()    
            # Predict MAE
            y_pred = rf.predict(X_test)
            mae = mean_absolute_error(y_test, y_pred)
            # Calculate MAPE
            mape = (mae / y_test.mean()) * 100  
            print(f"MAPE Latihan Fisik: {mape} %")
            print()
            
            return render_template('result.html', age = age , veg = veg,  weight = weight , height = height , bmi =bmi , hasilbmi = hasilbmi ,  rekomendasi = rekomendasi ,diet_recommendations=diet_recommendations,exercise_recommendations = exercise_recommendations,exercise_recommendationslain = exercise_recommendationslain)
        
        if kategori == 3 :
            rekomendasi = "Dinner"
            # sore(age,veg,weight,height)
            data = pd.read_csv('food_ori.csv')

            # Data dari kolom "Breakfast", "Lunch", dan "Dinner" dipisahkan dan disimpan dalam daftar terpisah
            Breakfastdata = data['Breakfast']
            BreakfastdataNumpy = Breakfastdata.to_numpy()
            Lunchdata = data['Lunch']
            LunchdataNumpy = Lunchdata.to_numpy()
            Dinnerdata = data['Dinner']
            DinnerdataNumpy = Dinnerdata.to_numpy()

            #nama item makanan
            Food_itemsdata = data['Food_items']

            #Vegan or Non-Veg
            VegNovVeg = data['VegNovVeg']
            
            ##Memisahkan Item Makanan Berdasarkan Kategori Waktu Makan

            #menyimpan nama item makanan yang telah dipisahkan
            print()
            breakfastfoodseparated=[]
            print(breakfastfoodseparated)
            print('breakfastfoodseparated')
            print()


            Lunchfoodseparated=[]
            print('Lunchfoodseparated')
            print(Lunchfoodseparated)
            print()

            Dinnerfoodseparated=[]
            print('Dinnerfoodseparated')
            print(Dinnerfoodseparated)
            print()


            #menyimpan indeks (posisi) yang sesuai dalam data asli untuk item-item 
            print()
            breakfastfoodseparatedID=[]
            print('breakfastfoodseparatedID')
            print(breakfastfoodseparatedID)
            print()

            LunchfoodseparatedID=[]
            print('LunchfoodseparatedID')
            print(LunchfoodseparatedID)
            print()

            DinnerfoodseparatedID=[]
            print('DinnerfoodseparatedID')
            print(DinnerfoodseparatedID)
            print()

            #Loop for berulang melalui panjang Seri Breakfastdata (mengasumsikan semua Seri memiliki panjang yang sama)
            for i in range(len(Breakfastdata)):
                #memeriksa apakah nilai pada indeks saat ini (i) di array BreakfastdataNumpy = 1 (Benar) / Representasi Biner
                if BreakfastdataNumpy[i]==1:
                    #menyimpan makanan
                    breakfastfoodseparated.append(Food_itemsdata[i])

                    print()
                    print('breakfastfoodseparated')
                    print ('BREAKFAST FOOD LIST')
                    print(breakfastfoodseparated)
                    print('#########')
                    print()

                    # menyimpan indeks baris item sarapan
                    breakfastfoodseparatedID.append(i)
                    print('breakfastfoodseparatedID')
                    print(breakfastfoodseparatedID)
                    print('#########')
                    print()

                if LunchdataNumpy[i]==1:
                    Lunchfoodseparated.append(Food_itemsdata[i])
                    print()
                    print('Lunchfoodseparated')
                    print ('LUNCH FOOD LIST')
                    print(Lunchfoodseparated)
                    print('#########')
                    print()
                    LunchfoodseparatedID.append(i)
                    print('LunchfoodseparatedID')
                    print(LunchfoodseparatedID)
                    print('#########')
                    print()
                if DinnerdataNumpy[i]==1:
                    Dinnerfoodseparated.append(Food_itemsdata[i])

                    print()
                    print('Dinnerfoodseparated')
                    print ('DINNER FOOD LIST')
                    print(Dinnerfoodseparated)
                    print('#########')
                    print()

                    DinnerfoodseparatedID.append(i)
                    print('DinnerfoodseparatedID')
                    print(DinnerfoodseparatedID)
                    print('#########')
                    print()

            #pengambilan baris tertentu dari DataFrame data berdasarkan ID yang disimpan dalam daftar breakfastfoodseparatedID, LunchfoodseparatedID, dan DinnerfoodseparatedID.
            #iloc adalah metode pengindeksan yang kuat dalam pandas yang memungkinkan  memilih baris dan kolom berdasarkan indeks integer atau daftar indeks karena lebih efisien daripada menggunakan pengindeksan baris tradisional (misalnya, data[0]) untuk memilih beberapa baris atau menerapkan logika pengindeksan yang kompleks.

            #Baris ini mengekstrak baris dari DataFrame data pada indeks yang ditentukan dalam daftar breakfastfoodseparatedID. Misalnya, jika breakfastfoodseparatedID berisi [10, 25, 32], baris ini akan mengekstrak baris pada indeks 10, 25, dan 32 dari DataFrame data.
            breakfastfoodseparatedIDdata = data.iloc[breakfastfoodseparatedID]
            print()
            print('breakfastfoodseparatedIDdata')
            print(breakfastfoodseparatedIDdata)
            print('#1')
            #mentranspos DataFrame breakfastfoodseparatedIDdata yang diekstrak. Transpos pada dasarnya menukar baris dan kolom.
            breakfastfoodseparatedIDdata=breakfastfoodseparatedIDdata.T
            print('breakfastfoodseparatedIDdata')
            print(breakfastfoodseparatedIDdata)
            print('#2')
            #membuat daftar val yang berisi bilangan bulat dari 5 hingga 14 (inklusif).
            val=list(np.arange(5,15))
            print()
            print('val')
            print(val)
            #membuat daftar baru Valapnd dengan menambahkan elemen 0 di awal daftar val. Daftar yang dihasilkan akan menjadi [0, 5, 6, 7, ..., 14].
            Valapnd=[0]+val
            print()
            print('Valapnd')
            print(Valapnd)
            #Baris ini mengekstrak baris dari DataFrame breakfastfoodseparatedIDdata yang ditranspos berdasarkan indeks dalam daftar Valapnd
            #Misalnya, jika Valapnd adalah [0, 5, 6, 7, ..., 14], baris ini akan memilih baris pertama (indeks 0) dan baris 5 hingga 14 dari DataFrame yang ditranspos.
            breakfastfoodseparatedIDdata=breakfastfoodseparatedIDdata.iloc[Valapnd]
            print()
            print('breakfastfoodseparatedIDdata')
            print(breakfastfoodseparatedIDdata)
            print('#3')
            #Baris ini mentranspos DataFrame breakfastfoodseparatedIDdata yang diekstrak kembali ke bentuk aslinya.
            breakfastfoodseparatedIDdata=breakfastfoodseparatedIDdata.T
            print("Breakfast Data")
            print("breakfastfoodseparatedIDdata")
            print (breakfastfoodseparatedIDdata)
            print()

            LunchfoodseparatedIDdata = data.iloc[LunchfoodseparatedID]
            print()
            print('LunchfoodseparatedIDdata')
            print(LunchfoodseparatedIDdata)
            print('#1')

            LunchfoodseparatedIDdata=LunchfoodseparatedIDdata.T
            print('LunchfoodseparatedIDdata')
            print(LunchfoodseparatedIDdata)
            print('#2')


            val=list(np.arange(5,15))
            print()
            print('val')
            print(val)

            Valapnd=[0]+val
            print()
            print('Valapnd')
            print(Valapnd)

            LunchfoodseparatedIDdata=LunchfoodseparatedIDdata.iloc[Valapnd]
            print()
            print('LunchfoodseparatedIDdata')
            print(LunchfoodseparatedIDdata)
            print('#3')

            LunchfoodseparatedIDdata=LunchfoodseparatedIDdata.T
            print()
            print("Lunch Data")
            print('LunchfoodseparatedIDdata')
            print(LunchfoodseparatedIDdata)
            print()


            DinnerfoodseparatedIDdata = data.iloc[DinnerfoodseparatedID]
            print()
            print('DinnerfoodseparatedIDdata')
            print(DinnerfoodseparatedIDdata)
            print('#1')


            DinnerfoodseparatedIDdata=DinnerfoodseparatedIDdata.T
            print('DinnerfoodseparatedIDdata')
            print(DinnerfoodseparatedIDdata)
            print('#2')

            val=list(np.arange(5,15))
            print()
            print('val')
            print(val)


            Valapnd=[0]+val
            print()
            print('Valapnd')
            print(Valapnd)


            DinnerfoodseparatedIDdata=DinnerfoodseparatedIDdata.iloc[Valapnd]
            print()
            print('DinnerfoodseparatedIDdata')
            print(DinnerfoodseparatedIDdata)
            print('#3')

            DinnerfoodseparatedIDdata=DinnerfoodseparatedIDdata.T
            print()
            print("Dinner Data")
            print('DinnerfoodseparatedIDdata')
            print (DinnerfoodseparatedIDdata)
            print()

            bmi = weight/((height / 100) ** 2)
            
            for lp in range (0,100,20):
                test_list=np.arange(lp,lp+20)
                print(test_list)

                for i in test_list: 
                    if(i == age):
                        print('Age is between',str(lp),str(lp+10))
                        print('agecl')
                        agecl=round(lp/20)   
                        print(agecl)

            # Menentukan kategori BMI
            print("Your body mass index (BMI) is: ", bmi)
            if ( bmi < 16):
                hasilbmi = "According to your BMI, you are very thin"
                clbmi=4
            elif ( bmi >= 16 and bmi < 18.5):
                hasilbmi ="According to your BMI, you are Thin"
                clbmi=3
            elif ( bmi >= 18.5 and bmi < 25):
                hasilbmi ="According to your BMI, you are healthy"
                clbmi=2
            elif ( bmi >= 25 and bmi < 30):
                hasilbmi = "According to your BMI, you are overweight"
                clbmi=1
            elif ( bmi >=30):
                hasilbmi = "According to your BMI, you are very overweight"
                clbmi=0

            ti=(bmi+agecl)/2
            print('ti')
            print(ti)

            DinnerfoodseparatedIDdata=DinnerfoodseparatedIDdata.to_numpy()
            print()
            print('DinnerfoodseparatedIDdata to numpy')
            print(DinnerfoodseparatedIDdata)
            print()

            LunchfoodseparatedIDdata=LunchfoodseparatedIDdata.to_numpy()
            print()
            print('LunchfoodseparatedIDdata to numpy')
            print(LunchfoodseparatedIDdata)
            print()


            breakfastfoodseparatedIDdata=breakfastfoodseparatedIDdata.to_numpy()
            print()
            print('breakfastfoodseparatedIDdata to numpy')
            print(breakfastfoodseparatedIDdata)
            print()

            

            Datacalorie=DinnerfoodseparatedIDdata[1:,1:len(DinnerfoodseparatedIDdata)]
            print()
            print('Datacalorie DinnerfoodseparatedIDdata')
            print(Datacalorie)

            X = np.array(Datacalorie)
            print()
            print('X')
            print(X)
            print()

            kmeans = KMeans(n_clusters=3, random_state=0).fit(X)
            print()
            print('kmeans')
            print(kmeans)
            print()

            print ('## Result Prediksi ##')
            print(kmeans.labels_)
            print()
            print('Predict')
            # print (kmeans.predict([Datacalorie[0]]))
            # XValu=np.arange(0,len(kmeans.labels_))
            # fig,axs=plt.subplots(1,1,figsize=(15,5))
            # plt.bar(XValu,kmeans.labels_)
            dnrlbl=kmeans.labels_
            print()
            print("dnrlbl")
            print(dnrlbl)
            print (len(dnrlbl))
            plt.title("Makanan dengan Kalori Rendah-Tinggi")
            print()

            Datacalorie=LunchfoodseparatedIDdata[1:,1:len(LunchfoodseparatedIDdata)]
            print()
            print("Datacalorie LunchfoodseparatedIDdata")
            print(Datacalorie)
            print()

            X = np.array(Datacalorie)
            kmeans = KMeans(n_clusters=3, random_state=0).fit(X)
            print()
            print('X')
            print(X)
            print()

            print ('## Hasil Prediksi ##')
            print(kmeans.labels_)
            print()
            print('Predict')

            # print (kmeans.predict([Datacalorie[0]]))
            # XValu=np.arange(0,len(kmeans.labels_))
            # fig,axs=plt.subplots(1,1,figsize=(15,5))
            # plt.bar(XValu,kmeans.labels_)
            lnchlbl=kmeans.labels_
            print('lnchlbl')
            print(lnchlbl)
            print (len(lnchlbl))
            plt.title("Makanan dengan Kalori Rendah-Tinggi")
            print()

            Datacalorie=breakfastfoodseparatedIDdata[1:,1:len(breakfastfoodseparatedIDdata)]
            print()
            print("Datacalorie breakfastfoodseparatedIDdata")
            print(Datacalorie)
            print()

            X = np.array(Datacalorie)
            print()
            print('X')
            print(X)
            print()

            kmeans = KMeans(n_clusters=3, random_state=0).fit(X)
            print ('## Hasil Prediksi ##')
            print(kmeans.labels_)
            print()
            print('Predict')

            # print (kmeans.predict([Datacalorie[0]]))
            # XValu=np.arange(0,len(kmeans.labels_))
            # fig,axs=plt.subplots(1,1,figsize=(15,5))
            # plt.bar(XValu,kmeans.labels_)
            brklbl=kmeans.labels_
            print('brklbl')
            print(brklbl)
            print (len(brklbl))
            plt.title("Makanan dengan Kalori Rendah-Tinggi")
            print()
            print('Breakfast')
            print(brklbl)
            print('Lunch')
            print(lnchlbl)
            print("Dinner")
            print(dnrlbl)

            datafin = pd.read_csv('nutrition_distriution.csv')
            datafin.head(5)

            dataTog=datafin.T
            print()
            print('dataTog')
            print(dataTog)

            bmicls=[0,1,2,3,4]
            agecls=[0,1,2,3,4]
            healthycat = dataTog.iloc[[0,1,2,3,4,7,9,10]]

            print("healthycat=")
            print(healthycat)
            print(len(healthycat))

            healthycat=healthycat.T
            healthycatDdata=healthycat.to_numpy()
            print('healthycatDdata')
            print(healthycatDdata)

            healthycat=healthycatDdata[1:,0:len(healthycatDdata)]
            print("healthycat")
            print(healthycat)

            healthycatfin=np.zeros((len(healthycat)*5,10),dtype=np.float32)
            print('healthycatfin')
            print(healthycatfin)
            print()
            s=0
            ys=[]

            for zz in range(5):
                for jj in range(len(healthycat)):
                    valloc=list(healthycat[jj])
                    print('valloc#1')
                    print(valloc)
                    print()
                    valloc.append(bmicls[zz])
                    print('valloc#2')
                    print(valloc)
                    print()
                    valloc.append(agecls[zz])
                    print('valloc#3')
                    print(valloc)
                    print()
                    healthycatfin[s]=np.array(valloc)
                    print('healthycatfin[s]')
                    print(healthycatfin[s])
                    print()
                    ys.append(dnrlbl[jj])
                    # ys.append(brklbl[jj])
                    # ys.append(lnchlbl[jj])
                    print('ys')
                    print(ys)
                    s+=1
            X_test=np.zeros((len(healthycat)*5,10),dtype=np.float32)
            print()
            print('X_test#1')
            print(X_test)
            print('####################')


            for jj in range(len(healthycat)):
                valloc=list(healthycat[jj])
                print('valloc#11')
                print(valloc)
                print()
                valloc.append(agecl)
                print('valloc#22')
                print(valloc)
                print()
                valloc.append(clbmi)
                print('valloc#33')
                print(valloc)
                print()
                X_test[jj]=np.array(valloc)*ti
            print()
            print('X_test#2')
            print (X_test)
            print()

            X_train=healthycatfin# Features
            print()
            print('X_train')
            print(X_train)
            print()

            y_train=ys # Labels
            print()
            print('y_train')
            print(y_train)
            print()

            clf=RandomForestClassifier(n_estimators=100)
            clf.fit(X_train,y_train)
            print()
            print('clf')
            print(clf)
            print()

            print('X_test[1]')
            print (X_test[1])

            y_pred=clf.predict(X_test)
            print()
            print('y_pred')
            print(y_pred)
            print()
            print('ok')
            print()
        
            total_rekomendasi = 0
            print('\nRekomendasi Makanan yang cocok:')
            for ii in range(len(y_pred)):
                if ii < len(Food_itemsdata) and y_pred[ii] == 0:
                    if int(veg) == 0 and VegNovVeg[ii] == 0:
                        print(Food_itemsdata[ii])
                        total_rekomendasi += 1
                    elif int(veg) == 1 and VegNovVeg[ii] == 1:
                        print(Food_itemsdata[ii])
                        total_rekomendasi += 1

            print('\nTotal makanan yang direkomendasikan:', total_rekomendasi)

            # Menambahkan kode untuk mencetak 10 makanan terbaik
            print("\n5 Makanan Terbaik:")
            diet_recommendations = [] 
            if total_rekomendasi >= 5 or total_rekomendasi <= 5:
                count = 0
                for ii in range(len(y_pred)):
                    if ii < len(Food_itemsdata) and y_pred[ii] == 0 and count < 5:
                        if int(veg) == 0 and VegNovVeg[ii] == 0:
                            print(Food_itemsdata[ii])
                            diet_recommendations.append(Food_itemsdata[ii])
                            count += 1
                        elif int(veg) == 1 and VegNovVeg[ii] == 1:
                            print(Food_itemsdata[ii])
                            diet_recommendations.append(Food_itemsdata[ii])
                            count += 1
    
            total_error = 0
            total_items = len(y_pred)

            for i in range(total_items):
                if i < len(Food_itemsdata) and y_pred[i] == 0:
                    if int(veg) == 0 and VegNovVeg[i] == 0:
                        total_error += 1
                    elif int(veg) == 1 and VegNovVeg[i] == 1:
                        total_error += 1

            # Menggunakan mean_absolute_percentage_error untuk menghitung MAPE
            mape = mean_absolute_percentage_error([total_items - total_error], [total_items]) * 100
            print("MAPE Rekomendasi Makan:", mape, "%")

            total_error = 0
            total_items = len(y_pred)

            for i in range(total_items):
                if i < len(Food_itemsdata) and y_pred[i] == 0:
                    if int(veg) == 0 and VegNovVeg[i] == 0:
                        total_error += 1
                    elif int(veg) == 1 and VegNovVeg[i] == 1:
                        total_error += 1

            mape = (total_error / total_items) * 100
            print("MAPE #5:", mape, "%")

            print()
            data = pd.read_csv('strong.csv')
            df = pd.DataFrame(data)

            X = df[['Weight', 'Set Order', 'Reps']]
            y = df['Exercise Name']

            label_encoder = LabelEncoder()
            y_encoded = label_encoder.fit_transform(y)
            print(y_encoded)

            X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.3, random_state=42)

            print('X_train')
            print(X_train)
            print('X_test')
            print(X_test)
            print('y_train')
            print(y_train)
            print('y_test')
            print(y_test)

            rf = RandomForestRegressor(n_estimators=100, max_depth=10, min_samples_split=5, random_state=42)
            rf.fit(X_train, y_train)

            weight_to_predict = weight
            predicted_exercise = rf.predict([[weight_to_predict, 0, 0]])
            predicted_exercise_label = label_encoder.inverse_transform(predicted_exercise.astype(int))

            try:
                result = df[df['Exercise Name'] == predicted_exercise_label[0]][['Set Order', 'Reps']]
                set_order = result.iloc[0]['Set Order']
                reps = result.iloc[0]['Reps']
                exercise_recommendations = f"Best exercise:  {predicted_exercise_label[0]} | Set Order: {set_order} | Reps: {reps}"
                print(f"Best exercise: {predicted_exercise_label[0]}, Set Order: {set_order}, Reps: {reps}")
            except IndexError:
                print("Tidak ada latihan fisik yang dapat diprediksi berdasarkan berat yang dimasukkan.")

            predicted_proba = rf.predict([[weight_to_predict, 0, 0]])

            top_3_exercises_indices = (-predicted_proba).argsort()[:3]
            
            for i, exercise_idx in enumerate(top_3_exercises_indices):
                exercise_name = label_encoder.inverse_transform([exercise_idx])[0]
                result = df[df['Exercise Name'] == exercise_name][['Set Order', 'Reps']]
                set_order = result.iloc[0]['Set Order']
                reps = result.iloc[0]['Reps']
                exercise_recommendationslain = f"Other Recommendation: {exercise_name} | Set Order: {set_order} | Reps: {reps}"
                print(f"Other Recommendation : Exercise Name: {exercise_name}, Set Order: {set_order}, Reps: {reps}")

            print()    
            # Predict MAE
            y_pred = rf.predict(X_test)
            mae = mean_absolute_error(y_test, y_pred)
            # Calculate MAPE
            mape = (mae / y_test.mean()) * 100  
            print(f"MAPE Latihan Fisik: {mape} %")
            print()

            
            return render_template('result.html', age = age , veg = veg,  weight = weight , height = height , bmi =bmi , hasilbmi = hasilbmi , diet_recommendations=diet_recommendations,rekomendasi = rekomendasi ,exercise_recommendations = exercise_recommendations,exercise_recommendationslain = exercise_recommendationslain)
        
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)
