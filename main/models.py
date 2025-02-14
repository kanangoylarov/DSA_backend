from django.db import models

class Apply(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} {self.surname}'


class Contact(models.Model):
    CATEGORY_CHOICES = [
        ('Data Science Bootcamp', 'Data Science Bootcamp'),
        ('SPSS Modeler Bootcamp', 'SPSS Modeler Bootcamp'),
        ('Kredit-Risk Analitikası', 'Kredit-Risk Analitikası'),
        ('Korporativ Təlimlər', 'Korporativ Təlimlər'),
        ('Data ilə əlaqəli işçi axtarırsınız', 'Data ilə əlaqəli işçi axtarırsınız'),
        ('Ödənişli proyekt köməyi', 'Ödənişli proyekt köməyi'),
        ('Ödənişsiz proyekt köməyi', 'Ödənişsiz proyekt köməyi')
    ]
    
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES, default='Data Science Bootcamp')

    def __str__(self):
        return f'{self.name} {self.surname} - {self.category}'

    
    
class Subscribe(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    event_date = models.DateField(help_text="Etkinlik tarihini seçin", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email

## Models for Data Science Bootcamp--------------------------------------------------------------------------------------------------
    
    
class Scripts(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.TextField(max_length=100)
    description = models.TextField()
    information = models.TextField()
    image = models.ImageField(upload_to='scripts/')
    for_who = models.TextField()
    certificates = models.TextField()
    certificate_image = models.ImageField(upload_to='certificates/')
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.title
    

class Sessions(models.Model):
    script = models.ForeignKey(Scripts, on_delete=models.CASCADE, related_name='sessions',default=1)
    session_number = models.IntegerField()
    date = models.DateField()
    hour = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.session_number} - {self.date} - {self.hour}'
    

class Broadcasts(models.Model):
    script = models.OneToOneField(Scripts, on_delete=models.CASCADE, related_name='broadcast')
    title = models.CharField(max_length=100)
    info = models.TextField()
    link = models.TextField()
    trainer = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    

class Syllabus(models.Model):
    script = models.ForeignKey(Scripts, on_delete=models.CASCADE, related_name='syllabus', default=1)
    title = models.CharField(max_length=100)
    description = models.TextField()
    label = models.CharField(max_length=100,null=True)
    information = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    