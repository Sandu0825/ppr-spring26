-- Procedure 1: insert new contact or update phone if name already exists
CREATE OR REPLACE PROCEDURE upsert_contact(p_name VARCHAR, p_phone VARCHAR)
LANGUAGE plpgsql
AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM contacts WHERE first_name = p_name) THEN
        UPDATE contacts
        SET phone = p_phone
        WHERE first_name = p_name;
    ELSE
        INSERT INTO contacts(first_name, phone)
        VALUES (p_name, p_phone);
    END IF;
END;
$$;


-- Procedure 2: delete contact by name or by phone
CREATE OR REPLACE PROCEDURE delete_contact(p_name VARCHAR, p_phone VARCHAR)
LANGUAGE plpgsql
AS $$
BEGIN
    IF p_name IS NOT NULL THEN
        DELETE FROM contacts WHERE first_name = p_name;
    ELSIF p_phone IS NOT NULL THEN
        DELETE FROM contacts WHERE phone = p_phone;
    END IF;
END;
$$;


-- Procedure 3: insert many contacts
-- Uses LOOP and IF
-- Checks phone format
CREATE OR REPLACE PROCEDURE insert_many_contacts(
    p_names VARCHAR[],
    p_phones VARCHAR[]
)
LANGUAGE plpgsql
AS $$
DECLARE
    i INT;
BEGIN
    FOR i IN 1..array_length(p_names, 1) LOOP
        -- Check if phone starts with 87 and has 11 digits
        IF p_phones[i] ~ '^87[0-9]{9}$' THEN
            INSERT INTO contacts(first_name, phone)
            VALUES (p_names[i], p_phones[i])
            ON CONFLICT (phone) DO NOTHING;
        ELSE
            RAISE NOTICE 'Incorrect phone: %, %', p_names[i], p_phones[i];
        END IF;
    END LOOP;
END;
$$;