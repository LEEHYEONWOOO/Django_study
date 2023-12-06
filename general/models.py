import datetime

from django.contrib.auth.models import User
from django.db import models
from django.db.models import OuterRef, Subquery
from django.utils import timezone


class CustomBaseModelManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_delete=False)


class BaseAbstractModel(models.Model):
    create_at = models.DateTimeField(default=timezone.now,
                                     null=True,
                                     blank=True,
                                     verbose_name='생성일')

    update_at = models.DateTimeField(auto_now=True,
                                     blank=True,
                                     null=True,
                                     verbose_name='수정일')

    create_user = models.ForeignKey(to=User,
                                    null=True,
                                    blank=True,
                                    on_delete=models.SET_NULL,
                                    verbose_name='생성자')

    is_delete = models.BooleanField(default=False,
                                    blank=True,
                                    null=True,
                                    verbose_name='삭제 여부')

    active = models.BooleanField(default=True,
                                 blank=True,
                                 null=True,
                                 verbose_name='활성 여부')

    objects = CustomBaseModelManager()

    class Meta:
        abstract = True
        default_manager_name = 'objects'
        ordering = ['-pk']


# 공지사항
class NormalNotice(BaseAbstractModel):
    id = models.AutoField(primary_key=True)

    title = models.CharField(max_length=150,
                             verbose_name='제목')

    content = models.TextField(null=True,
                               blank=True,
                               verbose_name='공지내용')

    attachment = models.FileField(null=True,
                                  blank=True,
                                  upload_to='common_notice',
                                  verbose_name='첨부파일')

    top_fixed = models.BooleanField(default=False,
                                    blank=True,
                                    null=True,
                                    verbose_name='상단고정여부')

    is_temporary = models.BooleanField(default=False,
                                       null=True,
                                       blank=True,
                                       verbose_name='임시저장여부')


class SystemNotice(BaseAbstractModel):
    id = models.AutoField(primary_key=True)

    title = models.CharField(max_length=150,
                             verbose_name='제목')

    content = models.TextField(null=True,
                               blank=True,
                               verbose_name='공지내용')

    top_fixed = models.BooleanField(default=False,
                                    blank=True,
                                    null=True,
                                    verbose_name='상단고정여부')

    is_temporary = models.BooleanField(default=False,
                                       null=True,
                                       blank=True,
                                       verbose_name='임시저장여부')


class CommonSelect(BaseAbstractModel):
    id = models.AutoField(primary_key=True)

    select_name = models.CharField(max_length=50,
                                   verbose_name='구분')

    select_value = models.CharField(max_length=150,
                                    verbose_name='코드명')

    more_info = models.JSONField(null=True,
                                 blank=True,
                                 verbose_name='추가정보')

    sort_order = models.IntegerField(blank=True,
                                     null=True,
                                     verbose_name='정렬순위')

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=('select_name', 'select_value'),
                                    violation_error_message='중복된 데이터 입니다',
                                    name='unique_common_select')
        ]

    def __str__(self):
        return self.select_value


class GeneralInfo(BaseAbstractModel):
    id = models.AutoField(primary_key=True)

    name = models.CharField(max_length=150,
                            verbose_name='회사명')

    representative = models.CharField(max_length=150,
                                      null=True,
                                      blank=True,
                                      verbose_name='대표자')

    founding_date = models.DateField(null=True,
                                     blank=True,
                                     verbose_name='설립일')

    business_number = models.CharField(max_length=150,
                                       null=True,
                                       blank=True,
                                       verbose_name='사업자등록번호')

    corporate_number = models.CharField(max_length=150,
                                        null=True,
                                        blank=True,
                                        verbose_name='법인등록번호')

    email = models.CharField(max_length=150,
                             null=True,
                             blank=True,
                             verbose_name='이메일')

    tell = models.CharField(max_length=150,
                            null=True,
                            blank=True,
                            verbose_name='전화번호')

    fax = models.CharField(max_length=150,
                           null=True,
                           blank=True,
                           verbose_name='팩스')

    business_type = models.CharField(max_length=150,
                                     null=True,
                                     blank=True,
                                     verbose_name='업태')

    address = models.CharField(max_length=150,
                               null=True,
                               blank=True,
                               verbose_name='주소')

    management_json = models.JSONField(null=True,
                                       blank=True,
                                       verbose_name='담당자목록')

    more_json = models.JSONField(null=True,
                                 blank=True,
                                 verbose_name='추가정보')

    main_img1 = models.ImageField(null=True,
                                  blank=True,
                                  max_length=255,
                                  upload_to='main_img',
                                  verbose_name='사진1')

    main_img2 = models.ImageField(null=True,
                                  blank=True,
                                  max_length=255,
                                  upload_to='main_img',
                                  verbose_name='사진2')

    main_img3 = models.ImageField(null=True,
                                  blank=True,
                                  max_length=255,
                                  upload_to='main_img',
                                  verbose_name='사진3')

    def __str__(self):
        return self.name


class Office(BaseAbstractModel):
    id = models.AutoField(primary_key=True)

    office_name = models.CharField(max_length=150,
                                   unique=True,
                                   verbose_name='영업소명')

    office_address = models.CharField(max_length=150,
                                      null=True,
                                      blank=True,
                                      verbose_name='주소')

    office_tell = models.CharField(max_length=150,
                                   null=True,
                                   blank=True,
                                   verbose_name='전화번호')

    def __str__(self):
        return self.office_name


class Route(BaseAbstractModel):
    id = models.AutoField(primary_key=True)

    route_number = models.CharField(max_length=150,
                                    unique=True,
                                    verbose_name='노선')

    route_type = models.CharField(max_length=50,
                                  null=True,
                                  blank=True,
                                  verbose_name='노선타입')

    total_qty = models.IntegerField(null=True,
                                    blank=True,
                                    verbose_name='총운행대수')

    reserve_qty = models.IntegerField(null=True,
                                      blank=True,
                                      verbose_name='총예비대수')

    reserve_funds = models.IntegerField(null=True,
                                        blank=True,
                                        verbose_name='예비금')

    is_profit = models.BooleanField(null=True,
                                    blank=True,
                                    verbose_name='수익노선여부')

    office = models.ForeignKey(to=Office,
                               on_delete=models.SET_NULL,
                               null=True,
                               blank=True,
                               verbose_name='영업소')

    def __str__(self):
        return self.route_number


class EmployeeManager(models.Manager):
    def emp_status_annotate_qs(self):
        last_child_subquery = EmpDateHistory.objects.filter(emp=OuterRef('pk')).order_by('-id')[:1]
        return self.get_queryset().annotate(last_status=Subquery(last_child_subquery.values('status')))

    def emp_status_qs(self, status):
        qs = self.emp_status_annotate_qs()
        return qs.filter(last_status=status)


class Employee(BaseAbstractModel):
    id = models.AutoField(primary_key=True)

    division = models.CharField(max_length=50,
                                null=True,
                                blank=True,
                                verbose_name='구분')

    user = models.OneToOneField(to=User,
                                on_delete=models.SET_NULL,
                                null=True,
                                blank=True,
                                related_name='rel_emp_user',
                                verbose_name='계정')

    name = models.CharField(max_length=150,
                            verbose_name='이름')

    number = models.CharField(max_length=150,
                              unique=True,
                              verbose_name='사번')

    birth = models.DateField(null=True,
                             blank=True,
                             verbose_name='생년월일')

    office = models.ForeignKey(to=Office,
                               on_delete=models.SET_NULL,
                               null=True,
                               blank=True,
                               verbose_name='영업소')

    route = models.ForeignKey(to=Route,
                              on_delete=models.SET_NULL,
                              null=True,
                              blank=True,
                              verbose_name='대표노선')

    reg_num = models.CharField(max_length=150,
                               null=True,
                               blank=True,
                               verbose_name='주민등록번호')

    department = models.ForeignKey(to=CommonSelect,
                                   on_delete=models.SET_NULL,
                                   null=True,
                                   blank=True,
                                   related_name='rel_department',
                                   verbose_name='부서')

    rank = models.ForeignKey(to=CommonSelect,
                             on_delete=models.SET_NULL,
                             null=True,
                             blank=True,
                             related_name='rel_emp_job_title',
                             verbose_name='직급')

    position = models.ForeignKey(to=CommonSelect,
                                 on_delete=models.SET_NULL,
                                 null=True,
                                 blank=True,
                                 related_name='rel_emp_position_title',
                                 verbose_name='직책')

    employ_type = models.CharField(max_length=50,
                                   null=True,
                                   blank=True,
                                   verbose_name='정규직/계약직')

    work_type = models.ForeignKey(to=CommonSelect,
                                  on_delete=models.SET_NULL,
                                  null=True,
                                  blank=True,
                                  related_name='rel_work_type',
                                  verbose_name='근무타입')

    cal_ho_bong = models.ForeignKey(to=CommonSelect,
                                    on_delete=models.SET_NULL,
                                    null=True,
                                    blank=True,
                                    related_name='rel_emp_ho_bong',
                                    verbose_name='호봉/레벨')

    union = models.ForeignKey(to=CommonSelect,
                              on_delete=models.SET_NULL,
                              null=True,
                              blank=True,
                              related_name='rel_emp_union',
                              verbose_name='조합')

    union_join = models.DateField(null=True,
                                  blank=True,
                                  verbose_name='노조가입일')

    tell = models.CharField(max_length=150,
                            null=True,
                            blank=True,
                            verbose_name='전화번호')

    address = models.CharField(max_length=150,
                               null=True,
                               blank=True,
                               verbose_name='주소')

    kiosk = models.CharField(max_length=150,
                             null=True,
                             blank=True,
                             verbose_name='키오스크인증코드')

    email = models.CharField(max_length=150,
                             null=True,
                             blank=True,
                             verbose_name='이메일')

    account_name = models.CharField(max_length=150,
                                    null=True,
                                    blank=True,
                                    verbose_name='예금주명')

    account_number = models.CharField(max_length=150,
                                      null=True,
                                      blank=True,
                                      verbose_name='계좌번호')

    img = models.ImageField(max_length=255,
                            null=True,
                            blank=True,
                            upload_to='employee',
                            verbose_name='사진')

    note = models.CharField(max_length=150,
                            null=True,
                            blank=True,
                            verbose_name='비고')

    push_token = models.TextField(null=True, blank=True, verbose_name='푸쉬토큰')

    custom_objects = EmployeeManager()

    def __str__(self):
        return self.name

    @property
    def get_status(self):
        obj = self.empdatehistory_set.all().order_by('-id').first()
        return obj.status.title if obj else None

    @property
    def get_ho_bong(self):
        emp_date = self.get_start_date

        cal_ho_bong = ''
        if self.cal_ho_bong:
            cal_ho_bong = self.cal_ho_bong.select_value

        if cal_ho_bong == '자동계산':
            if emp_date:
                emp_year = emp_date.year
                emp_month = emp_date.month
                date = datetime.datetime.strptime(str(emp_year) + '-' + str(emp_month).zfill(2) + '-01', '%Y-%m-%d')
                current_year = datetime.datetime.now().year
                current_month = datetime.datetime.now().month

                a = abs((datetime.datetime(year=current_year, month=current_month, day=1) - date).days)
                result_month = (a / 365) * 12

                if 12 > result_month:
                    return 1
                elif result_month < 24:
                    return 2
                elif result_month < 36:
                    return 3
                elif result_month < 48:
                    return 4
                elif result_month < 60:
                    return 5
                elif result_month < 72:
                    return 6
                elif result_month < 84:
                    return 7
                elif result_month < 96:
                    return 8
                elif result_month < 108:
                    return 9
                elif result_month < 120:
                    return 10
                elif result_month < 132:
                    return 11
                elif result_month < 144:
                    return 12
                elif result_month < 156:
                    return 13
                elif result_month < 168:
                    return 14
                elif result_month < 180:
                    return 15
                elif result_month < 196:
                    return 16
                elif result_month < 208:
                    return 17
                elif result_month < 220:
                    return 18
                elif result_month < 232:
                    return 19
                elif result_month < 244:
                    return 20
                else:
                    return 21

        return None


class License(BaseAbstractModel):
    id = models.AutoField(primary_key=True)

    emp = models.ForeignKey(to=Employee,
                            on_delete=models.SET_NULL,
                            null=True,
                            blank=True,
                            verbose_name='승무주임')

    license_name = models.CharField(max_length=150,
                                    null=True,
                                    blank=True,
                                    verbose_name='자격증이름')

    license_division = models.CharField(max_length=50,
                                        null=True,
                                        blank=True,
                                        verbose_name='구분')

    number = models.CharField(max_length=150,
                              null=True,
                              blank=True,
                              verbose_name='자격증번호')

    creation_region = models.CharField(max_length=150,
                                       null=True,
                                       blank=True,
                                       verbose_name='발급지역')

    creation_date = models.DateField(null=True,
                                     blank=True,
                                     verbose_name='발급일자')

    date_expire = models.DateField(null=True,
                                   blank=True,
                                   verbose_name='만료일')


class Family(models.Model):
    id = models.AutoField(primary_key=True)

    emp = models.ForeignKey(to=Employee,
                            on_delete=models.SET_NULL,
                            null=True,
                            blank=True,
                            verbose_name='승무주임')

    name = models.CharField(max_length=150,
                            null=True,
                            blank=True,
                            verbose_name='이름')

    relationship = models.CharField(max_length=50,
                                    null=True,
                                    blank=True,
                                    verbose_name='관계')

    reg_num = models.CharField(max_length=150,
                               null=True,
                               blank=True,
                               verbose_name='주민등록번호')

    live_flag = models.BooleanField(default=False,
                                    null=True,
                                    blank=True,
                                    verbose_name='부양유무')

    disable_flag = models.BooleanField(default=False,
                                       null=True,
                                       blank=True,
                                       verbose_name='장애유무')

    def __str__(self):
        return self.name


class EmpDateHistory(BaseAbstractModel):
    id = models.AutoField(primary_key=True)

    emp = models.ForeignKey(to=Employee,
                            on_delete=models.SET_NULL,
                            null=True,
                            blank=True,
                            verbose_name='승무주임')

    date = models.DateField(verbose_name='날짜')

    status = models.CharField(max_length=50,
                              verbose_name='재직/휴직/퇴직')

    description = models.CharField(max_length=150,
                                   null=True,
                                   blank=True,
                                   verbose_name='비고')


class Car(BaseAbstractModel):
    id = models.AutoField(primary_key=True)

    number = models.CharField(max_length=150,
                              unique=True,
                              verbose_name='번호')

    rest_day = models.CharField(max_length=50,
                                null=True,
                                blank=True,
                                verbose_name='휴무일')

    route = models.ForeignKey(to=Route,
                              on_delete=models.SET_NULL,
                              null=True,
                              blank=True,
                              verbose_name='대표노선')

    car_name = models.CharField(max_length=150,
                                null=True,
                                blank=True,
                                verbose_name='차명')

    car_type = models.CharField(max_length=150,
                                null=True,
                                blank=True,
                                verbose_name='차종')

    model_year = models.IntegerField(null=True,
                                     blank=True,
                                     verbose_name='연식')

    registration_date = models.DateField(null=True,
                                         blank=True,
                                         verbose_name='차량등록일')

    expiration_date = models.DateField(null=True,
                                       blank=True,
                                       verbose_name='차량만료일')

    serial_number = models.CharField(max_length=150,
                                     null=True,
                                     blank=True,
                                     verbose_name='차대번호')

    prime_mover = models.CharField(max_length=150,
                                   null=True,
                                   blank=True,
                                   verbose_name='원동기형식')

    engine_volume = models.FloatField(null=True,
                                      blank=True,
                                      verbose_name='배기량')

    engine_power = models.FloatField(max_length=150,
                                     null=True,
                                     blank=True,
                                     verbose_name='정격출력')

    maker = models.CharField(max_length=150,
                             null=True,
                             blank=True,
                             verbose_name='제조사')

    passengers = models.IntegerField(null=True,
                                     blank=True,
                                     verbose_name='승차정원')

    usage = models.CharField(max_length=50,
                             null=True,
                             blank=True,
                             verbose_name='상용/예비/업무')

    length = models.FloatField(null=True,
                               blank=True,
                               verbose_name='전장(mm)')

    width = models.FloatField(null=True,
                              blank=True,
                              verbose_name='전폭(mm)')

    height = models.FloatField(null=True,
                               blank=True,
                               verbose_name='전고(mm)')

    weight = models.FloatField(null=True,
                               blank=True,
                               verbose_name='중량(kg)')

    work_type = models.CharField(max_length=50,
                                 null=True,
                                 blank=True,
                                 verbose_name='고정/교대')

    oil_type = models.CharField(max_length=50,
                                null=True,
                                blank=True,
                                verbose_name='연료')

    valve_type = models.CharField(max_length=150,
                                  null=True,
                                  blank=True,
                                  verbose_name='밸브타입')

    canister_made = models.CharField(max_length=150,
                                     null=True,
                                     blank=True,
                                     verbose_name='가스용기제조사')

    canister_cnt = models.IntegerField(null=True,
                                       blank=True,
                                       verbose_name='가스용기개수')

    canister_size = models.FloatField(null=True,
                                      blank=True,
                                      verbose_name='가스용기용량(㎥)')

    fuel_efficiency = models.FloatField(null=True,
                                        blank=True,
                                        verbose_name='연비(km/ℓ)')

    def __str__(self):
        return self.number
