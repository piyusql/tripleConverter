from django.db import models
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os

class OverwriteStorage(FileSystemStorage):
    def get_available_name(self, name):
        """
            make the slug file name available to the folder to write the code content
        """
        # If the filename already exists, remove it as if it was a true file system
        file_path = os.path.join(settings.MEDIA_ROOT, name)
        if self.exists(file_path):
            os.remove(file_path)
        return file_path

class Database( models.Model ):
    """
        list of supported database in the application
    """
    name = models.CharField( max_length = 50 )
    version = models.PositiveSmallIntegerField()
    slug = models.CharField( max_length = 55, unique = True )
    description = models.TextField( null = True , blank = True, default = "what does it supports...?")
    code_file = models.FileField( upload_to = 'converter/hooks', null = True, blank = True, storage = OverwriteStorage())
    code = models.TextField( null = True , blank = True)
    location = models.CharField( max_length = 15 , help_text = "IP of the database system")
    db_name = models.CharField( max_length = 50 , help_text = "Default database to connect")
    username = models.CharField( max_length = 50 )
    password = models.CharField( max_length = 50 )
    active = models.BooleanField( default = True )
    created_on = models.DateField( auto_now_add = True )
    
    class Meta:
        unique_together = ( 'name', 'version' )
    
    def __unicode__( self ):
        return "%s - %s" %( self.name, self.version )

    def save(self, *args, **kwargs):
        if self.code_file:
            self.code = self.code_file.read()
        super(Database, self).save(*args, **kwargs)
