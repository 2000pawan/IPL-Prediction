# Import Important Library.

import joblib
import streamlit as st 
from PIL import Image


# Load Model & Scaler & Polynomial Features

model=joblib.load('model.pkl')

year=([2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026,2027,2028,2029,2030])
encode = {'team1': {'MI':1,'KKR':2,'RCB':3,'DC':4,'CSK':5,'RR':6,'DD':7,'GL':8,'KXIP':9,'SRH':10,'RPS':11,'KTK':12,'PW':13,'GT':14,'LSG':15},'team2': {'MI':1,'KKR':2,'RCB':3,'DC':4,'CSK':5,'RR':6,'DD':7,'GL':8,'KXIP':9,'SRH':10,'RPS':11,'KTK':12,'PW':13,'GT':14,'LSG':15},'toss_winner': {'MI':1,'KKR':2,'RCB':3,'DC':4,'CSK':5,'RR':6,'DD':7,'GL':8,'KXIP':9,'SRH':10,'RPS':11,'KTK':12,'PW':13,'GT':14,'LSG':15},'toss_decision':{'field':0,'bat':1},
'city':{'Hyderabad':0, 'Pune':1, 'Rajkot':2, 'Indore':3, 'Bangalore':4, 'Mumbai':5,'Kolkata':6, 'Delhi':7, 'Chandigarh':8, 'Kanpur':9, 'Jaipur':10, 'Chennai':11,'Cape Town':12, 'Port Elizabeth':13, 'Durban':14, 'Centurion':15,'East London':16, 'Johannesburg':17, 'Kimberley':18, 'Bloemfontein':19,'Ahmedabad':20, 'Cuttack':21, 'Nagpur':22, 'Dharamsala':23, 'Kochi':24,'Visakhapatnam':25, 'Raipur':26, 'Ranchi':27, 'Abu Dhabi':28, 'Sharjah':29,'Dubai':30},'venue':{'Rajiv Gandhi International Stadium, Uppal':0,'Maharashtra Cricket Association Stadium':1,'Saurashtra Cricket Association Stadium':2, 'Holkar Cricket Stadium':3,'M Chinnaswamy Stadium':4, 'Wankhede Stadium':5, 'Eden Gardens':6,'Arun Jaitley Stadium':7,'Punjab Cricket Association IS Bindra Stadium, Mohali':8,'Green Park':9, 'Punjab Cricket Association Stadium, Mohali':8,'Sawai Mansingh Stadium':10, 'MA Chidambaram Stadium, Chepauk':11,'Dr DY Patil Sports Academy':5, 'Newlands':12, "St George's Park":13,'Kingsmead':14, 'SuperSport Park':15, 'Buffalo Park':16,'New Wanderers Stadium':17, 'De Beers Diamond Oval':18,'OUTsurance Oval':19, 'Brabourne Stadium':19,'Narendra Modi Stadium, Motera':20, 'Barabati Stadium':21,'Vidarbha Cricket Association Stadium, Jamtha':22,'Himachal Pradesh Cricket Association Stadium':23, 'Nehru Stadium':24,'Dr. Y.S. Rajasekhara Reddy ACA-VDCA Cricket Stadium':25,'Subrata Roy Sahara Stadium':1,'Shaheed Veer Narayan Singh International Stadium':26,'JSCA International Stadium Complex':27, 'Sheikh Zayed Stadium':28,'Sharjah Cricket Stadium':29, 'Dubai International Cricket Stadium':30}}  
teams = ['MI', 'KKR', 'RCB', 'DC', 'CSK', 'RR', 'DD', 'GL', 'KXIP', 'SRH', 'RPS', 'KTK', 'PW','GT','LSG']
# Load Image

image=Image.open('img.jpg')

# Streamlit Function For Building Button & app.

def main():
    st.image(image,width=650)
    st.title('IPL Prediction')
    html_temp='''
    <div style='background-color:red; padding:12px'>
    <h1 style='color:  #000000; text-align: center;'>IPL Prediction Machine Learning Model</h1>
    <h3 style='color:black; text_align: center;'>This Model is Trained on data from (2008-2017). So,This Model is only for educational purpose if this model predict wrong then it will happen due to lack of data.🙏🏼🙏🏼🙏🏼😔😔</h3>
    </div>
    <h2 style='color:  red; text-align: center;'>Please Enter Input</h2>
    '''
    st.markdown(html_temp,unsafe_allow_html=True)
    season=st.selectbox('Select Match Year.',year)
    team1 = st.selectbox("Select First Team", teams)
    remaining_teams = teams.copy()
    remaining_teams.remove(team1)
    team2 = st.selectbox("Select Second Team", remaining_teams)
    toss_winner_options = [team for team in [team1, team2]]
    toss_winner = st.selectbox("Select Which Team Won The Toss", toss_winner_options)
    toss_decision= st.selectbox("Select,Team Decision after Winning Toss (0->Fielding,1->Batting)",encode['toss_decision'].keys())
    venue= st.selectbox("Select Stadium Where Match held",encode['venue'].keys())
    team0=encode['team1'][team1]
    team=encode['team2'][team2]
    toss_winner0=encode['toss_winner'][toss_winner]
    toss_decision0=encode['toss_decision'][toss_decision]
    venue0=encode['venue'][venue]
    input=[season,team0,team,toss_winner0,toss_decision0,venue0]
    result=''
    if st.button('Predict',''):
        result=prediction(input)
    temp='''
     <div style='background-color:navy; padding:8px'>
     <h1 style='color: gold  ; text-align: center;'>{}</h1>
     </div>
     '''.format(result)
    st.markdown(temp,unsafe_allow_html=True)
    

# Prediction Function to predict from model.
# Albania	Soybeans	1990	7000	1485.0	121.00	16.37
# input=['Albania','Soybeans',1485.0,121.00,16.37]

def prediction(input):
    test=[input]
    predict=model.predict(test)
    key = next(key for key, value in encode['team1'].items() if value == predict[0])
    return (f'{key} will Win the Match.🎉🎉🎉🎉🎉😊😊😊😊😊')

if __name__=='__main__':
    main()


