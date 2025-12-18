# Systemarkitektur - Support Desk Prosjekt

```
SUPPORT-DESK-PROSJEKTOPPGAVE2025/
├── DjangoParentSupportDesk/
│   ├── ProsjektHøst.sql                    
│   ├── requirements.txt                    
│   └── DjangoSupportDesk/
│       ├── .env                           
│       ├── manage.py                      
│       │
│       ├── DjangoProjectSupportDesk/       
│       │   ├── settings.py                
│       │   ├── urls.py                    
│       │   ├── wsgi.py                     
│       │   └── asgi.py                    
│       │
│       ├── AuthApp/                        
│       │   ├── views.py                    
│       │   ├── urls.py                     
│       │   ├── middleware.py               
│       │   ├── models.py                   
│       │   └── static/
│       │       └── styling.css
│       │
│       ├── UserApp/                       
│       │   ├── views.py                   
│       │   ├── urls.py                     
│       │   └── models.py                   
│       │
│       ├── CaseManagerApp/                
│       │   ├── views.py                   
│       │   ├── urls.py                     
│       │   └── models.py                   
│       │
│       ├── SharedApp/                     
│       │   ├── views.py                    
│       │   ├── urls.py                     
│       │   ├── models.py                  
│       │   └── static/
│       │       └── css/
│       │
│       ├── templates/                                    
│       │   ├── home.html                   
│       │   ├── scrLogin.html               
│       │   ├── scrRegister.html            
│       │   ├── scrLogoutPage.html         
│       │   ├── scrSettings.html            
│       │   ├── scrUserMain.html            
│       │   ├── scrUserTable.html           
│       │   ├── scrUserView.html           
│       │   ├── scrCaseManagerMain.html    
│       │   ├── scrCaseManagerTable.html    
│       │   ├── scrCaseManagerView.html    
│       │   └── scrNewCase.html            
│       │
│       └── staticfiles/                    
│           ├── css/
│           │   ├── auth.css
│           │   ├── base.css
│           │   ├── casemanager.css
│           │   ├── shared.css
│           │   └── userapp.css
│           ├── django_tables2/            
│           └── admin/                      
│
├── docs/                                   
│   ├── SystemArkitektur.md                 
│   ├── Funksjoner.md                       
│   ├── currentStack.md                    
│   ├── stack.md                           
│   └── Testbrukere.md                      
│
├── .gitignore                           
└── README.md                     
```
