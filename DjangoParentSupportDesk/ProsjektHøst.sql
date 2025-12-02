select * from public.auth_user

create table Case_Model(
	Case_ID Serial Primary Key,
	CaseManager_ID Integer References public.auth_user(id),
	User_ID integer References public.auth_user(id),
	Title varchar(100),
	Description varchar(500),
	Category varchar(10) Check (Category IN ('Pc', 'Mac', 'Teams', 'Office365')),
	Urgency varchar(6) Check(Urgency IN ('low', 'middel', 'high')),
	Status varchar(14) Check(Status IN ('pending', 'Case_Created','Under_process','Assigned_date', 'Completed')),
	Created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    Changed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	Appointment_date TIMESTAMP NULL,
	Have_Comments BOOLEAN DEFAULT FALSE
)


create table Comments_Model(
 	Comments_ID Serial Primary key,
	Case_ID Integer References Case_Model(Case_ID),
	Author_ID Integer References public.auth_user(id),
	Text varchar(600),
	Created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)