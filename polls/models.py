"""
backend model by Louis
"""
from django.db import models

class User(models.Model):
    # userid
    UserId = models.AutoField('UserId', primary_key=True)
    # username
    UserName = models.CharField('UserName', unique=True,max_length=15)
    # password
    Password = models.CharField('Password', null=False, max_length=15)
    # createtime set the time
    CreateTime = models.DateTimeField(auto_now=True)

    # change the defalut name of the table
    # if not set,the name will be 'database_tablename'
    class Meta:
        db_table = 'User'

class Book(models.Model):
    # Bookid
    BkId = models.AutoField('Bkid', primary_key=True)
    # Book Title(name)
    BkTitle = models.CharField('BkTitle', max_length=15)
    # Book Author(s)
    BkAuthor = models.CharField('BkAuthor', max_length=15)
    # Book Publisher
    BkPublisher = models.CharField('BkPublisher', max_length=15)
    # Book publication date
    BkPubDate = models.CharField('BkPubDate', max_length=8)
    # Book category
    Category = models.CharField('Category', max_length=15)
    # rating is out of file but can have 2 decimals
    Rating = models.DecimalField('Rating', null=True, max_digits=4, decimal_places=2)
    # The total review number
    ReviewNum = models.IntegerField('ReviewField', null=True)

    # change the defalut name of the table
    class Meta:
        db_table = 'Book'

class Collection(models.Model):
    # collectionId
    CoId = models.AutoField('CoId', primary_key=True)
    # collection Name set by the owner
    CoName = models.CharField('CoName', max_length=15)
    # owner --foreign key of user
    CoOwner = models.ForeignKey('User', on_delete=models.CASCADE)
    # createtime --won't change after set
    CoCreateDate = models.DateTimeField(auto_now_add=True)
    # updatedate --Everytime being update the time will change
    CoUpdateDate = models.DateTimeField(auto_now=True)

    # change the defalut name of the table
    class Meta:
        db_table = 'Collection'

class Review(models.Model):
    # review id
    ReviewId = models.AutoField('ReviewId', primary_key=True)
    # book id --foreign key of table 'Book'
    BkId = models.ForeignKey('Book', on_delete=models.CASCADE)
    # user id --foreign key of table 'User'
    UserId = models.ForeignKey('User', on_delete=models.CASCADE)
    # review content
    ReviewCont = models.TextField('ReviewCont')
    # review date
    ReviewDate = models.DateField(auto_now_add=True)
    # rating cannot be null can be a number of 1-5 and with a 0.5
    Rating = models.DecimalField('Rating', null=False, max_digits=4, decimal_places=1)

    # change the defalut name of the table
    class Meta:
        db_table = 'Review'

class CoBk(models.Model):
    #two foreign keys
    CoId = models.ForeignKey('Collection',on_delete=models.CASCADE)
    BkId = models.ForeignKey('Book',on_delete=models.CASCADE)

    # change the defalut name of the table
    class Meta:
        db_table = 'CoBk'
