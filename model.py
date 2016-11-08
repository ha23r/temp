from google.appengine.ext import ndb
from protorpc import messages


class user(ndb.Model):
    username = ndb.StringProperty(required=True)
    password = ndb.StringProperty(required=True)

class Person(ndb.Model):
    personal = Personal()
    economic_strength = EconomicStrength()
    credibility = Credibility()
    business_experience = BusinessExperience()
    social = Social()

class Personal_Status(messages.Enum):
    Unknown = 0
    Single = 1
    Married = 2
    Devorced = 3


class EconomicStrength(ndb.Model):
    temp = ndb.IntegerProperty

class Credibility(ndb.Model)
    temp = ndb.IntegerProperty

class BusinessExperience(ndb.Model)
    temp = ndb.IntegerProperty

class Social(ndb.Model)
    temp = ndb.IntegerProperty

class Gender(messages.Enum):
    Unknown = 0
    Male = 1
    Female = 2
    Other = 3


class Name(ndb.Model):
    first_name = ndb.StringProperty(required=True)
    middle_name = ndb.StringProperty()
    last_name = ndb.StringProperty(required=True)


class Personal(ndb.Model):
    name = Name()
    english_name = Name()
    nickname = Name()
    id_number = ndb.StringProperty()
    year_of_birth = ndb.DateProperty()
    status = Personal_Status(0)
    gender = Gender(0)
    address = ndb.StringProperty()

