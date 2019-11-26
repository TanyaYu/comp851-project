class Lead:

    def __init__(self,
        registration_dttm = '',
        id = 0,
        first_name = '',
        last_name = '',
        email = '',
        gender = '',
        ip_address = '',
        cc = '',
        country = '',
        birthdate = '',
    	salary = '',
        title = ''):
        self.registration_dttm = registration_dttm
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.gender = gender
        self.ip_address = ip_address
        self.country = country
        self.cc = cc
        self.birthdate = birthdate
        self.salary = salary
        self.title = title

    def __str__(self):
        seperator = ', '
        return seperator.join(self.fields)

    @property
    def fields(self):
        return [str(self.registration_dttm),
        str(self.id),
        str(self.first_name),
        str(self.last_name),
        str(self.email),
        str(self.gender),
        str(self.ip_address),
        str(self.cc),
        str(self.country),
        str(self.birthdate),
    	str(self.salary),
        str(self.title)]
