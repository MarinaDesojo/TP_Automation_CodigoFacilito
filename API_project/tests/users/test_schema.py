from API_project.utils.settings import fake

user_schema = {
    "type": "object",
    "required": ["id", "email", "full_name", "role"],
    "properties": {
        "id": {"type": "string"},
        "email": {"type": "string", "format": "email"},
        "full_name": {"type": "string"},
        "role": {"type": "string", "enum": ["admin", "passenger"]},
    },
    "additionalProperties": True
}

user_schema_array = {
    "type": "array",
    "items": user_schema
}

good_user_data = {
        "email": "us_er.na'me+tag3@7exam-ple.co.uk",
        "password": "123456",
        "full_name": "Alejo Pepe Sanchez",
        "role": "passenger"
    }

created_user_data = {

}

changed_user_data = {
    "email": "user_user-1234@userdata.com",
    "password": "yes_a_password",
    "full_name": "Violeta Juarez"
}


bad_user_data = [{
    "email": "",
    "password": "123456",
    "full_name": "Juan",
    "role": "passenger"
    },{
    "email": " ",
    "password": "123456",
    "full_name": "Juan",
    "role": "passenger"
    },{
    "email": "notanemail",
    "password": "123456",
    "full_name": "Juan",
    "role": "passenger"
    },{
    "email": "notanemail@",
    "password": "123456",
    "full_name": "Juan",
    "role": "passenger"
    },{
    "email": "@notanemail",
    "password": "123456",
    "full_name": "Juan",
    "role": "passenger"
    },{
    "email": "@",
    "password": "123456",
    "full_name": "Juan",
    "role": "passenger"
    },{
    "email": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa@example-very-long-domain-subdomain-123456789.com", #254
    "password": "123456",
    "full_name": "Juan",
    "role": "passenger"
    },{
    "email": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa@example-very-long-domain-subdomain-123456789.com", #255
    "password": "123456",
    "full_name": "Juan",
    "role": "passenger"
    },{
    "email": "usernametag@@example.co",
    "password": "123456",
    "full_name": "Juan",
    "role": "passenger"
    },{
    "email": "user(name)tag@example.co",
    "password": "123456",
    "full_name": "Juan",
    "role": "passenger"
    },{
    "email": "usernametag@example!.co",
    "password": "123456",
    "full_name": "Juan",
    "role": "passenger"
    },{
    "email": "usernametag@ex_ample.co",
    "password": "123456",
    "full_name": "Juan",
    "role": "passenger"
    },{
    "email": "usernametag@.example.co",
    "password": "123456",
    "full_name": "Juan",
    "role": "passenger"
    },{
    "email": "usernametag.@example.co",
    "password": "123456",
    "full_name": "Juan",
    "role": "passenger"
    },{
    "email": ".usernametag@example.co",
    "password": "123456",
    "full_name": "Juan",
    "role": "passenger"
    },{
    "email": "username..tag@example.co",
    "password": "123456",
    "full_name": "Juan",
    "role": "passenger"
    },{
    "email": fake.email(),
    "password": "",
    "full_name": "Juan",
    "role": "passenger"
    },{
    "email": fake.email(),
    "password": " ",
    "full_name": "Juan",
    "role": "passenger"
    },{
    "email": fake.email(),
    "password": "12345",
    "full_name": "Juan",
    "role": "passenger"
    },{
    "email": fake.email(),
    "password": "123456",
    "full_name": "",
    "role": "passenger"
    },{
    "email": fake.email(),
    "password": "123456",
    "full_name": " ",
    "role": "passenger"
    },{
    "email": fake.email(),
    "password": "123456",
    "full_name": 123,
    "role": "passenger"
    },{
    "email": fake.email(),
    "password": 123456,
    "full_name": "Juan",
    "role": "passenger"
    },{
    "email": 123546,
    "password": "123456",
    "full_name": "Juan",
    "role": "passenger"
    },{
    "email": fake.email(),
    "password": "123456",
    "full_name": "Juan",
    "role": ""
    },{
    "email": fake.email(),
    "password": "123456",
    "full_name": "Juan",
    "role": " "
    },{
    "email": fake.email(),
    "password": "123456",
    "full_name": "Juan",
    "role": 123
    },{
    "email": fake.email(),
    "password": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", #128
    "full_name": "Juan",
    "role": "passenger"
    },{
    "email": fake.email(),
    "password": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", #129
    "full_name": "Juan",
    "role": "passenger"
    },{
    "email": fake.email(),
    "password": "123456",
    "full_name": "Juan",
    "role": "captain"
    },{
    "email": fake.email(),
    "password": "123456",
    "full_name": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
    "role": "passenger"
    }
    ]