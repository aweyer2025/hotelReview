--Creating file pointer

create directory Hotelfile as '/home/aweyer/my_windows_folder/SQL_Projects/individualProject';

-- COMMIT;

-- SELECT * FROM ALL_DIRECTORIES WHERE DIRECTORY_NAME = 'MYCSV1';
-- CREATE OR REPLACE DIRECTORY MYCSV1 AS 'C:\Users\Anthony Weyer\SQL_Projects\Week3';


-- Importing data
DECLARE
      F UTL_FILE.FILE_TYPE;
      V_LINE VARCHAR2 (20000);
      V_SID number;
      V_CID NUMBER;
      V_review varchar2(20000);
      V_value NUMBER;
    BEGIN
      F := UTL_FILE.FOPEN ('MYCSV1', 'seedWords.csv', 'R', 20000);
      IF UTL_FILE.IS_OPEN(F) THEN
        LOOP
          BEGIN
--            DBMS_OUTPUT.PUT_LINE('Start');
            UTL_FILE.GET_LINE(F, V_LINE);
--            DBMS_OUTPUT.PUT_LINE(V_LINE);
            IF V_LINE IS NULL THEN
              EXIT;
            END IF;
             hotelID := REGEXP_SUBSTR(V_LINE, '[^,]+', 1, 1);
             name  := REGEXP_SUBSTR(V_LINE, '[^,]+', 1, 2);
             city   := REGEXP_SUBSTR(V_LINE, '[^,]+', 1, 3);
            
            INSERT INTO Hotel VALUES(hotelID, name, city);
            
            COMMIT;
          EXCEPTION
          WHEN NO_DATA_FOUND THEN
            EXIT;
          END;
        END LOOP;
      END IF;
      UTL_FILE.FCLOSE(F);
  END;


