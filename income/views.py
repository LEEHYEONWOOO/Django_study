from django.db.models import Sum, F, Avg, ExpressionWrapper, IntegerField, Value
from django.views.generic import TemplateView
from itertools import chain
from income.models import IncomeData
from general.models import Route


class index_view(TemplateView):
    template_name = 'income/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()

        return context


class income_view(TemplateView):
    template_name = 'income/income.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        income = IncomeData.objects.all()

        route = Route.objects.all().order_by('route_number')
        print(route)

        search_date_required = self.request.GET.get('search_date_required')
        select_route = self.request.GET.get('select_route')
        is_profit = self.request.GET.get('is_profit')
        print(f"search_date_required = {search_date_required}")
        print(f"select_route = {select_route}")
        print(f"is_profit = {is_profit}")

        if select_route != '' and is_profit != '':
            search_result = income.filter(route_id=select_route, save_is_profit=is_profit, date=search_date_required)
        elif is_profit != '':
            search_result = income.filter(date=search_date_required)
        elif select_route != '':
            search_result = income.filter(route_id=select_route, date=search_date_required)
        else:
            search_result = income.filter(date=search_date_required)

        search_result = search_result.annotate(
            coin_tot=ExpressionWrapper(F('cash_10') + F('cash_50') + F('cash_100')
                                       + F('cash_500'), output_field=IntegerField()),
            income_tot=ExpressionWrapper(F('cash_10') + F('cash_50') + F('cash_100') + F('cash_500')
                                         + F('cash_paper') + F('card_smt') + F('card_transfer')
                                         - F('reserve_funds') + F('reserve_balance'), output_field=IntegerField()),
            reverse_diff=ExpressionWrapper(-F('reserve_funds') + F('reserve_balance'), output_field=IntegerField()))

        Sum_result = (search_result.values('route__route_number').annotate(
            all_card_smt=Sum('card_smt'),
            all_card_transfer=Sum('card_transfer'),
            all_coin_tot=Sum('coin_tot'),
            all_cash_paper=Sum('cash_paper'),
            all_income_tot=Sum('income_tot'))
        )

        # test = search_result.filter(route__route_number=100).values('route__route_number').aggregate(Avg('card_smt'))
        # print(test)

        Avg_result = (search_result.values('route__route_number').annotate(
            avg_card_smt=ExpressionWrapper(Avg('card_smt'), output_field=IntegerField()),
            avg_card_transfer=ExpressionWrapper(Avg('card_transfer'), output_field=IntegerField()),
            avg_coin_tot=ExpressionWrapper(Avg('coin_tot'), output_field=IntegerField()),
            avg_cash_paper=ExpressionWrapper(Avg('cash_paper'), output_field=IntegerField()),
            avg_income_tot=ExpressionWrapper(Avg('income_tot'), output_field=IntegerField()))
        )

        combine_list = []
        for row in route:
            a = search_result.filter(route_id=row)
            b = Sum_result.filter(route_id=row)
            c = Avg_result.filter(route_id=row)
            combine_list = list(chain(combine_list, a))
            combine_list = list(chain(combine_list, b))
            combine_list = list(chain(combine_list, c))

        context['search_result'] = combine_list
        context['route'] = route

        return context