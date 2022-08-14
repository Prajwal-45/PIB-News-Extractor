import pyrebase

config = {
  "apiKey": "AIzaSyBM8A957jonW-DHp1Gl9h9AFoG6qfOph3E",
  "authDomain": "pib-news-application.firebaseapp.com",
  "databaseURL": "https://pib-news-application-default-rtdb.firebaseio.com",
  "storageBucket": "pib-news-application.appspot.com"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()
authe = firebase.auth()
storage = firebase.storage()


languages = {
  "English":1,
  "Hindi" :2,
  "Urdu":3,
  "Kannada":8,
  "Tamil":11,
  "Telugu":16,
  "Punjabi":6,
  "Bengali":4,
  "Marathi" :9,
  "Odia":18,
  "Gujarati":13,
  "Assamese":10,
  "Malayalam":15,

}
abbr = {
        "Marathi": "mr",
        "English" : "en",
        "Hindi" : "hi",
        "Urdu" : "ur",
        "Punjabi":"pa",
        "Malayalam":"ml",
        "Odia":"od",
        "Telugu":"te",
        "Tamil":"Ta",
        "Bengali":"bn",
        "Gujrati":"gu",
        "Kannada":"kn",
        "Assamese":"as"
    }


language_mapping ={
  "Delhi":{"English","Hindi","Urdu"},
  "Mumbai":{"English","Marathi"},
  "Hyderabad":{"English","Telugu"},
  "Begaluru":{"English","Kannada"},
  "Chennai":{"English","Tamil"},
  "Chandigarh":{"English","Punjabi"},
  "Kolkata":{"English","Bengali"},
  "Ahemadabad":{"English","Gujrati"},
  "Guwahati":{"English","Assamese"},
  "Thiruvunathapuram":{"English","Malayalam"},
  "Bhubaneshwar":{"English","Odia"},  
}

regid = {
"Delhi":3,
  "Mumbai":1,
  "Hyderabad":5,
  "Bengaluru":20,
  "Chennai":6,
  "Chandigarh":17,
  "Kolkata":19,
  "Ahemadabad":22,
  "Guwahati":23,
  "Thiruvunathapuram":24,
  "Bhubaneshwar":21,  
}
lang_reg = {
    "English":"Delhi",
  "Hindi" :"Delhi",
  "Urdu":"Delhi",
  "Kannada":"Bengaluru",
  "Tamil":"Chennai",
  "Telugu":'Hyderabad',
  "Punjabi":"Chandigarh",
  "Bengali":"Kolkata",
  "Marathi" :"Mumbai",
  "Odia":"Bhubaneshwar",
  "Gujarati":"Ahemadabad",
  "Assamese":"Guwahati",
  "Malayalam":"Thiruvunathapuram",
}
