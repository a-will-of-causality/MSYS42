bless_the_children_ehr
sql_master_user
h3@rt0fL1ne!D0ggo61
localhost
3306
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Msys42AppAllergycondition(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=100)

    class Meta:
        managed = False
        db_table = 'msys42app_allergycondition'


class Msys42AppAnnualmedicalcheck(models.Model):
    id = models.BigAutoField(primary_key=True)
    date = models.DateField()
    height = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True)
    weight = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True)
    bmi = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    hemoglobin = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    condition = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    child = models.ForeignKey('Msys42AppChild', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'msys42app_annualmedicalcheck'


class Msys42AppChild(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(unique=True, max_length=7)
    birth = models.DateField()
    blood_group = models.CharField(max_length=3, blank=True, null=True)
    address = models.TextField()
    philhealth_number = models.CharField(max_length=14, blank=True, null=True)
    fourps_number = models.CharField(max_length=20, blank=True, null=True)
    guardian_relationship = models.CharField(max_length=25)
    guardian_sex = models.CharField(max_length=6)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=25)
    middlename = models.CharField(max_length=25, blank=True, null=True)
    sex = models.CharField(max_length=6)
    age = models.IntegerField()
    guardian_firstname = models.CharField(max_length=50)
    guardian_lastname = models.CharField(max_length=25)
    guardian_middlename = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'msys42app_child'


class Msys42AppContactnumber(models.Model):
    id = models.BigAutoField(primary_key=True)
    number = models.CharField(max_length=11)
    child = models.ForeignKey(Msys42AppChild, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'msys42app_contactnumber'


class Msys42AppFamilymedicalrecord(models.Model):
    id = models.BigAutoField(primary_key=True)
    date = models.DateField()
    age = models.PositiveSmallIntegerField(blank=True, null=True)
    height = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)
    weight = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)
    bp = models.CharField(max_length=5, blank=True, null=True)
    temp = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    med_stat = models.CharField(max_length=50, blank=True, null=True)
    medication = models.CharField(max_length=100, blank=True, null=True)
    remarks = models.CharField(max_length=100, blank=True, null=True)
    member = models.ForeignKey('Msys42AppFamilymember', models.DO_NOTHING)
    bmi = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'msys42app_familymedicalrecord'


class Msys42AppFamilymember(models.Model):
    id = models.BigAutoField(primary_key=True)
    fm_lastname = models.CharField(max_length=25)
    fm_firstname = models.CharField(max_length=25)
    fm_middlename = models.CharField(max_length=25, blank=True, null=True)
    fm_relationship = models.CharField(max_length=25)
    fm_sex = models.CharField(max_length=6)
    child = models.ForeignKey(Msys42AppChild, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'msys42app_familymember'


class Msys42AppImmunization(models.Model):
    id = models.BigAutoField(primary_key=True)
    date = models.DateField()
    immunization_given = models.CharField(max_length=255)
    medical_history = models.ForeignKey('Msys42AppMedicalhistory', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'msys42app_immunization'


class Msys42AppMedicalhistory(models.Model):
    id = models.BigAutoField(primary_key=True)
    medical_status = models.CharField(max_length=255)
    medical_status_history = models.TextField()
    disability_status = models.CharField(max_length=255)
    disability_status_history = models.TextField()
    allergies_history = models.TextField()
    child = models.OneToOneField(Msys42AppChild, models.DO_NOTHING)
    other_condition = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'msys42app_medicalhistory'


class Msys42AppMedicalhistoryAllergiesConditions(models.Model):
    id = models.BigAutoField(primary_key=True)
    medicalhistory = models.ForeignKey(Msys42AppMedicalhistory, models.DO_NOTHING)
    allergycondition = models.ForeignKey(Msys42AppAllergycondition, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'msys42app_medicalhistory_allergies_conditions'
        unique_together = (('medicalhistory', 'allergycondition'),)


class Msys42AppPhysiciansexam(models.Model):
    id = models.BigAutoField(primary_key=True)
    year = models.IntegerField()
    grade = models.CharField(max_length=2)
    height = models.CharField(max_length=2)
    weight = models.CharField(max_length=2)
    bp = models.CharField(max_length=2)
    vision_right = models.CharField(max_length=2)
    vision_left = models.CharField(max_length=2)
    hearing_right = models.CharField(max_length=2)
    hearing_left = models.CharField(max_length=2)
    eyes = models.CharField(max_length=2)
    ears = models.CharField(max_length=2)
    nose = models.CharField(max_length=2)
    throat = models.CharField(max_length=2)
    teeth = models.CharField(max_length=2)
    heart = models.CharField(max_length=2)
    lungs = models.CharField(max_length=2)
    abdomen = models.CharField(max_length=2)
    nervous_system = models.CharField(max_length=2)
    skin = models.CharField(max_length=2)
    nutrition = models.CharField(max_length=2)
    other = models.CharField(max_length=2)
    other_label = models.CharField(max_length=20)
    child = models.ForeignKey(Msys42AppChild, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'msys42app_physiciansexam'
