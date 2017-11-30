import logging
from login.models import Credentials
from login.serializer import listUserSerializer
logger = logging.getLogger(__name__)

def register(req_body):
    name = req_body.get("name")
    email = req_body.get("email")
    password = req_body.get("password")
    isadmin = ( name =="appadmin")
    log_obj = Credentials()
    log_obj.name = name
    log_obj.email = email
    log_obj.password = password
    log_obj.isadmin = isadmin
    log_obj.save()
    logger.info("New user %s is successfully created" %(name))
    status = "Row is successfully created"
    return status
    
def update(req_body):
    name = req_body.get('name')
    mypass = req_body.get('password')
    if Credentials.objects.filter(name=name,password=mypass):
        print "Login Success"
        logger.error("Login Success..")
    else:
        print "Failure"
        logger.error("Login Failure...wrong username/password")
    new_pass = req_body.get('newpassword')
    log_obj = Credentials.objects.get(name=name)
    log_obj.password =new_pass
    log_obj.save()
    logger.error("Password reset for user %s" %(name))


def deleteUser(req_body):
    id = req_body.get('id')
    Credentials.objects.get(id=id).delete()
    logger.info("User successfully Deleted")    


def listAllUsers():
    lst = Credentials.objects.all().order_by("name")
    serialize = listUserSerializer(lst,many=True)
    return serialize.data

def login(req_str):
    name = req_str.get("name")
    password = req_str.get("password")
    check = Credentials.objects.filter(name=name, password=password)
    serialize = listUserSerializer(check,many=True)
    if check:
        val ="Login successful"
        logger.error("Login success")
    else:
        val ="failed"
        logger.error("Login Failure...wrong username/password")
    return serialize.data
