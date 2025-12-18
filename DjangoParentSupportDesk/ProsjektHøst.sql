
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


Create or replace Function NewCase(inpTitle varchar, inpDescription varchar, inpCategory varchar, inpUrgency varchar, inpStatus varchar, inpUser_ID integer)
Returns Table(caseId INTEGER, success BOOLEAN, message text)
Language plpgsql
as $$
Begin 
Insert Into Case_Model(Title, Description, Category, Urgency, Status, User_ID) 
Values(inpTitle, inpDescription, inpCategory, inpUrgency, inpStatus, inpUser_ID)
Returning Case_ID into caseId;

success := TRUE;
message := 'Case Created';
Return next; 

exception when others then
caseId := NULL;
success := FALSE;
message:= SQLERRM;
return next;
end;
$$;

CREATE OR REPLACE FUNCTION UpdateCase(
    inpCase_ID INTEGER, 
    inpStatus VARCHAR, 
    inpAppointment_Date TIMESTAMP,
	inpCaseManager_ID INTEGER
)
RETURNS TABLE(caseId INTEGER, success BOOLEAN, message TEXT)
LANGUAGE plpgsql
AS $$
BEGIN 
    IF inpStatus IS NULL AND inpAppointment_Date IS NULL AND inpCaseManager_ID IS NULL THEN
        caseId := inpCase_ID;
        success := FALSE;
        message := 'No changes specified';
        RETURN NEXT;
        RETURN;
    END IF;
    UPDATE Case_Model 
    SET 
        Status = COALESCE(inpStatus, Status),
        Appointment_date = COALESCE(inpAppointment_Date, Appointment_date),
        CaseManager_ID = COALESCE(inpCaseManager_ID, CaseManager_ID),
        Changed_at = CURRENT_TIMESTAMP
    WHERE Case_ID = inpCase_ID
    RETURNING Case_ID INTO caseId;

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

CREATE OR REPLACE FUNCTION GetComments(inpcase_id INTEGER)
RETURNS TABLE(
    comments_id INTEGER,
    case_id INTEGER,
    author_id INTEGER,
    author_username VARCHAR,
    text VARCHAR,
    created_at TIMESTAMP
)
LANGUAGE plpgsql
AS $$
BEGIN 
    RETURN QUERY
    SELECT 
        c.Comments_ID,
        c.Case_ID,
        c.Author_ID,
        u.username,
        c.Text,
        c.Created_at
    FROM Comments_Model c
    JOIN public.auth_user u ON c.Author_ID = u.id
    WHERE c.Case_ID = inpcase_id
    ORDER BY c.Created_at ASC;
END;
$$;

Create or replace Function NewComment(inpAuthor_id INTEGER, inpCase_id INTEGER, inpText varchar )
Returns Table(caseId INTEGER, success BOOLEAN, message text)
Language plpgsql
as $$
Begin 
Insert Into Comments_Model(Author_id, case_id, Text) 
Values(inpAuthor_id, inpCase_id, inpText)
RETURNING case_id INTO caseId;

success := TRUE;
message := 'Comment Created';
Return next; 

exception when others then
caseId := NULL;
success := FALSE;
message:= SQLERRM;
return next;
end;
$$;

