from django.db import models

class Products(models.Model):
    product_name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.product_name
    
class Versions(models.Model):
    version = models.CharField(max_length=10)
    product_name = models.ForeignKey(Products, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.version
    
class Model(models.Model):
    model_name = models.CharField(max_length=50)
    version = models.ForeignKey(Versions, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.model_name

class CommReq(models.Model):
    req_name = models.CharField(max_length=100)
    spec_num = models.CharField(max_length=20)
    model_name = models.ForeignKey(Model, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.req_name
    
class HLTP(models.Model):
    epic = models.CharField(max_length=10)
    source = models.CharField(max_length=100)
    comments = models.CharField(max_length=300)
    requirement = models.ForeignKey(CommReq, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.epic
    
class MLTP(models.Model):
    test_section = models.CharField(max_length=50)
    test_scenario_name = models.CharField(max_length=256)
    test_scenario_notes = models.CharField(max_length=500)
    source = models.CharField(max_length=100)
    fw_dev = models.BooleanField()
    req_question = models.BooleanField()
    tdd = models.CharField(max_length=100)
    user_story = models.CharField(max_length=10)
    product_spec = models.CharField(max_length=200)
    team = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    hltp = models.ForeignKey(HLTP, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.test_scenario_name
    
class Test_Case_Inventory(models.Model):
    suite_name = models.CharField(max_length=100)
    test_case_name = models.CharField(max_length=100)
    automated = models.BooleanField()
    new_test = models.BooleanField()
    notes = models.CharField(max_length=200)
    file_path = models.FilePathField()
    mltp = models.ManyToManyField(MLTP)
    
    def __str__(self):
        return "{}.{}".format(self.suite_name, self.test_case_name)
    