import logging
from login.models import Credentials
from login.serializer import listUserSerializer
logger = logging.getLogger(__name__)

def register(req_body):
    log_obj = Credentials()
    log_obj.name,log_obj.email,log_obj.password,log_obj.isadmin = req_body['name'],req_body['email'],req_body['password'],req_body['isadmin']
    log_obj.save()
    logger.info("New user %s is successfully created" %(req_body['name']))
    status = "Row is successfully created"
    return status
    
def update(req_body):
    if Credentials.objects.filter(name=req_body.get('name'),password=req_body.get('password')):
        print "Login Success"
        logger.error("Login Success..")
    else:
        print "Failure"
        logger.error("Login Failure...wrong username/password")
    log_obj = Credentials.objects.get(name=req_body.get('name'))
    log_obj.password = req_body.get('newpassword')
    log_obj.save()
    logger.error("Password reset for user %s" %(req_body['name']))


def deleteUser(req_body):
    Credentials.objects.get(id=req_body.get('id')).delete()
    logger.info("User successfully Deleted")    


def listAllUsers():
    lst = Credentials.objects.all().order_by("name")
    serialize = listUserSerializer(lst,many=True)
    return serialize.data

def login(req_str):
    check = Credentials.objects.filter(name=req_body.get('name'),password=req_body.get('password'))
    serialize = listUserSerializer(check,many=True)
    if check:
        val ="Login successful"
        logger.error("Login success")
    else:
        val ="failed"
        logger.error("Login Failure...wrong username/password")
    return serialize.data

def downloadLog():
    file_name = "log_file.log"
    filename = os.path.join(MEDIA_ROOT,file_name)
    wrapper = FileWrapper(file(filename))
    response = HttpResponse(wrapper)
    file_size = os.path.getsize(filename)
    content_type = mimetypes.guess_type(filename)[0]
    response['Content-Type'] = content_type
    response['Content-Length'] = str(file_size)
    response['Content-Disposition'] = "attachment ; filename=%s"%(file_name)
    return response
