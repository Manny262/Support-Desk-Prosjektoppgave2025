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
);


create table Comments_Model(
 	Comments_ID Serial Primary key,
	Case_ID Integer References Case_Model(Case_ID),
	Author_ID Integer References public.auth_user(id),
	Text varchar(600),
	Created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


Create Function NewCase(inpTitle varchar, inpDescription varchar, inpCategory varchar, inpUrgency varchar, inpStatus varchar, inpUser_ID integer)
Returns Table(caseId INTEGER, succes BOOLEAN, message text)
Language plpgsql
as $$
Begin 
Insert Into Case_Model(Title, Description, Category, Urgency, Status, User_ID) 
Values(inpTitle, inpDescription, inpCategory, inpUrgency, inpStatus, inpUser_ID)
Returning Case_ID into caseId;

succes := TRUE;
message := 'Case Created';
Return next; 

exception when others then
caseId := NULL;
succes := FALSE;
message:= SQLERRM;
return next
end;
$$ 

CREATE OR REPLACE FUNCTION UpdateCase(
    inpCase_ID INTEGER, 
    inpStatus VARCHAR, 
    inpAppointment_Date TIMESTAMP
)
RETURNS TABLE(caseId INTEGER, success BOOLEAN, message TEXT)
LANGUAGE plpgsql
AS $$
BEGIN 
    
    IF inpStatus IS NOT NULL AND inpAppointment_Date IS NOT NULL THEN
        UPDATE Case_Model 
        SET Status = inpStatus, 
            Appointment_date = inpAppointment_Date,
            Changed_at = CURRENT_TIMESTAMP
        WHERE Case_ID = inpCase_ID
        RETURNING Case_ID INTO caseId;
        
    ELSIF inpStatus IS NOT NULL AND inpAppointment_Date IS NULL THEN
        UPDATE Case_Model 
        SET Status = inpStatus,
            Changed_at = CURRENT_TIMESTAMP
        WHERE Case_ID = inpCase_ID
        RETURNING Case_ID INTO caseId;
        
    ELSIF inpStatus IS NULL AND inpAppointment_Date IS NOT NULL THEN
        UPDATE Case_Model 
        SET Appointment_date = inpAppointment_Date,
            Changed_at = CURRENT_TIMESTAMP
        WHERE Case_ID = inpCase_ID
        RETURNING Case_ID INTO caseId;
    END IF;

    success := TRUE;
    message := 'Case Updated';
    RETURN NEXT; 

EXCEPTION WHEN OTHERS THEN
    caseId := NULL;
    success := FALSE;
    message := SQLERRM;
    RETURN NEXT;
END;
$$;

CREATE OR REPLACE FUNCTION GetCase(inpcase_id INTEGER)
RETURNS SETOF Case_Model
LANGUAGE plpgsql
AS $$
BEGIN 
    RETURN QUERY
    SELECT * 
    FROM Case_Model 
    WHERE Case_ID = inpcase_id;
END;
$$;

CREATE OR REPLACE FUNCTION GetCaseComments(inpcase_id INTEGER)
RETURNS SETOF Comments_Model
LANGUAGE plpgsql
AS $$
BEGIN 
    RETURN QUERY
    SELECT * 
    FROM Comments_Model 
    WHERE Case_ID = inpcase_id;
END;
$$;


