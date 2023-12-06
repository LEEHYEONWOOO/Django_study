from django.db import models

from general.models import BaseAbstractModel, Route, Car, CommonSelect, Employee


class IncomeData(BaseAbstractModel):
    id = models.AutoField(primary_key=True)

    date = models.DateField(verbose_name='날짜')

    route = models.ForeignKey(to=Route,
                              on_delete=models.SET_NULL,
                              null=True,
                              blank=True,
                              verbose_name='노선')

    car = models.ForeignKey(to=Car,
                            on_delete=models.SET_NULL,
                            null=True,
                            blank=True,
                            verbose_name='차량')

    save_is_profit = models.BooleanField(null=True,
                                         blank=True,
                                         verbose_name='수익노선여부')

    save_work_type_a = models.ForeignKey(to=CommonSelect,
                                         on_delete=models.SET_NULL,
                                         null=True,
                                         blank=True,
                                         related_name='income_work_type_a',
                                         verbose_name='시점근무타입A')

    save_work_type_b = models.ForeignKey(to=CommonSelect,
                                         on_delete=models.SET_NULL,
                                         null=True,
                                         blank=True,
                                         related_name='income_work_type_b',
                                         verbose_name='시점근무타입B')

    emp_a = models.ForeignKey(to=Employee,
                              on_delete=models.SET_NULL,
                              null=True,
                              blank=True,
                              related_name='income_emp_a',
                              verbose_name='승무주임A')

    emp_b = models.ForeignKey(to=Employee,
                              on_delete=models.SET_NULL,
                              null=True,
                              blank=True,
                              related_name='income_emp_b',
                              verbose_name='승무주임B')

    reserve_funds = models.IntegerField(default=0,
                                        null=True,
                                        blank=True,
                                        verbose_name='고정예비금')

    reserve_balance = models.IntegerField(default=0,
                                          null=True,
                                          blank=True,
                                          verbose_name='예비금잔액')

    cash_10 = models.IntegerField(default=0,
                                  null=True,
                                  blank=True,
                                  verbose_name='10원')

    cash_50 = models.IntegerField(default=0,
                                  null=True,
                                  blank=True,
                                  verbose_name='50원')

    cash_100 = models.IntegerField(default=0,
                                   null=True,
                                   blank=True,
                                   verbose_name='100원')

    cash_500 = models.IntegerField(default=0,
                                   null=True,
                                   blank=True,
                                   verbose_name='500원')

    cash_paper = models.IntegerField(default=0,
                                     null=True,
                                     blank=True,
                                     verbose_name='지폐금액')

    cash_1000 = models.IntegerField(default=0,
                                    null=True,
                                    blank=True,
                                    verbose_name='1,000원')

    cash_5000 = models.IntegerField(default=0,
                                    null=True,
                                    blank=True,
                                    verbose_name='5,000원')

    cash_10000 = models.IntegerField(default=0,
                                     null=True,
                                     blank=True,
                                     verbose_name='10,000원')

    cash_50000 = models.IntegerField(default=0,
                                     null=True,
                                     blank=True,
                                     verbose_name='50,000원')

    card_smt = models.IntegerField(default=0,
                                   null=True,
                                   blank=True,
                                   verbose_name='교통카드결제금액')

    card_transfer = models.IntegerField(default=0,
                                        null=True,
                                        blank=True,
                                        verbose_name='교통카드환승금액')

    note = models.CharField(max_length=150,
                            null=True,
                            blank=True,
                            verbose_name='비고')

    @property
    def get_cash_total(self):
        paper = self.cash_paper if self.cash_paper else 0
        funds = self.reserve_funds if self.reserve_funds else 0
        balance = self.reserve_balance if self.reserve_balance else 0
        c_500 = self.cash_500 if self.cash_500 else 0
        c_100 = self.cash_100 if self.cash_100 else 0
        c_10 = self.cash_10 if self.cash_10 else 0
        c_50 = self.cash_50 if self.cash_50 else 0
        result = (paper + c_500 + c_100 + c_10 + c_50) - (funds - balance)
        return result


# 레거시 모델 -------------------------------------------------------------------------------------------------------------
class Income(models.Model):
    """
    date = models.DateField(null=True)  # 일자
    route = models.ForeignKey(Route, models.CASCADE, null=True)
    car = models.ForeignKey(Car, models.DO_NOTHING, null=True)  # 차량 외부키
    employee = models.ForeignKey(Employee, models.DO_NOTHING, null=True)
    vaultCash = models.IntegerField(default=0)      # 예비금 잔액
    income_10 = models.IntegerField(default=0)
    income_50 = models.IntegerField(default=0)
    income_100 = models.IntegerField(default=0)
    income_500 = models.IntegerField(default=0)
    income_paper = models.IntegerField(default=0)
    income_smt = models.IntegerField(default=0)
    income_smt_transfer = models.IntegerField(default=0)
    income_total = models.IntegerField(default=0)
    # 예비금 추가 - 2021-12-10
    reserveFunds = models.IntegerField(default=0)
    dispatchMark = models.CharField(max_length=10, default="전일")  # 근태일지 표시용
    remarks = models.CharField(max_length=50, default='', null=True, blank=True)  # 비고
    # 비수익 노선 추가
    profit_List = ((False, '수익'), (True, '비수익'))
    non_profit_bus = models.BooleanField(choices=profit_List, default=False, blank=True)  # 비수익 노선
    class Meta:
        indexes = [
            models.Index(fields=["date", ]),
            models.Index(fields=["vaultCash", "income_10", "income_50", "income_100", "income_500",
                                 "income_smt", "income_smt_transfer", "income_total", "reserveFunds", "remarks",
                                 "non_profit_bus"]),
        ]
    """
    id = models.AutoField(primary_key=True)

    date = models.DateField(null=True,
                            blank=True,
                            verbose_name='날짜')

    route = models.ForeignKey(to=Route,
                              on_delete=models.SET_NULL,
                              null=True,
                              blank=True,
                              verbose_name='노선')

    car = models.ForeignKey(to=Car,
                            on_delete=models.SET_NULL,
                            null=True,
                            blank=True,
                            verbose_name='차량')

    employee = models.ForeignKey(to=Employee,
                                 on_delete=models.SET_NULL,
                                 null=True,
                                 blank=True,
                                 verbose_name='운수직')

    vaultCash = models.IntegerField(default=0,
                                    null=True,
                                    blank=True,
                                    verbose_name='')

    income_10 = models.IntegerField(default=0,
                                    null=True,
                                    blank=True,
                                    verbose_name='')

    income_50 = models.IntegerField(default=0,
                                    null=True,
                                    blank=True,
                                    verbose_name='')

    income_100 = models.IntegerField(default=0,
                                     null=True,
                                     blank=True,
                                     verbose_name='')

    income_500 = models.IntegerField(default=0,
                                     null=True,
                                     blank=True,
                                     verbose_name='')

    income_paper = models.IntegerField(default=0,
                                       null=True,
                                       blank=True,
                                       verbose_name='')

    income_smt = models.IntegerField(default=0,
                                     null=True,
                                     blank=True,
                                     verbose_name='')

    income_smt_transfer = models.IntegerField(default=0,
                                              null=True,
                                              blank=True,
                                              verbose_name='')

    income_total = models.IntegerField(default=0,
                                       null=True,
                                       blank=True,
                                       verbose_name='')

    reserveFunds = models.IntegerField(default=0,
                                       null=True,
                                       blank=True,
                                       verbose_name='')

    dispatchMark = models.CharField(max_length=150,
                                    verbose_name='근태일지 표시용')

    remarks = models.CharField(max_length=150,
                               null=True,
                               blank=True,
                               verbose_name='비고')

    non_profit_bus = models.BooleanField(default=False,
                                         null=True,
                                         blank=True,
                                         verbose_name='비수익 노선')
