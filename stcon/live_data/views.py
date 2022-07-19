from django.http import Http404, HttpResponse, HttpResponseNotFound, JsonResponse
from django.shortcuts import render
#Calendar
from datetime import datetime


from .models import *
#Список моделей
station_object_list = {"30":St30, "31":St31}        #  "32":St32, "33":St33
station_object_list_normel = {"1":StNormel1 }       #  "2":StNormel2, "3":StNormel3, "4":StNormel4


def index(request):
    station_list = ListSt.objects.order_by("number")
    station_normel_list = NormelListSt.objects.order_by("number")
    context = {
        'station_list': station_list,
        'station_normel_list': station_normel_list,
        'title': 'Home'
    }
    return render(request, 'live_data/index.html', context=context)

def logs(request, st_id=0):
    station_list = ListSt.objects.order_by("number")
    station_normel_list = NormelListSt.objects.order_by("number")
    logs_list = LogsSt.objects.all()
    context = {
        'station_list': station_list,
        'station_normel_list': station_normel_list,
        'logs_list' : logs_list,
        'title': 'Logs',
        'st_id': str(st_id)
    }
    return render(request, 'live_data/logs.html', context=context)


def control(request):
    station_list = ListSt.objects.order_by("number")
    station_normel_list = NormelListSt.objects.order_by("number")
    context = {
        'station_list': station_list,
        'station_normel_list': station_normel_list,
        'title': 'Control'
    }
    return render(request, 'live_data/control.html', context=context)


def contacts(request):
    station_list = ListSt.objects.order_by("number")
    station_normel_list = NormelListSt.objects.order_by("number")
    context = {
        'station_list': station_list,
        'station_normel_list': station_normel_list,
        'title': 'Contacts'
    }
    return render(request, 'live_data/contacts.html', context=context)


def help_site(request):
    station_list = ListSt.objects.order_by("number")
    station_normel_list = NormelListSt.objects.order_by("number")
    context = {
        'station_list': station_list,
        'station_normel_list': station_normel_list,
        'title': 'Help'
    }
    return render(request, 'live_data/help_site.html', context=context)


def about(request):
    station_list = ListSt.objects.order_by("number")
    station_normel_list = NormelListSt.objects.order_by("number")
    context = {
        'station_list': station_list,
        'station_normel_list': station_normel_list,
        'title': 'About'
    }
    return render(request, 'live_data/about.html', context=context)



def station(request, st_id):
    station_list = ListSt.objects.order_by("number")
    station_normel_list = NormelListSt.objects.order_by("number")

    st = station_object_list.get(str(st_id))
    if not st: raise Http404(f'No station {st_id}')
    station_data = st.objects.order_by('-id')[:10]

    station_address = ListSt.objects.get(number=st_id).address

    #var for js script first chart
    u = str(station_data[0].u) 
    i = str(station_data[0].i) 
    p1 = str(station_data[0].p1) 
    p2 = str(station_data[0].p2) 
    
    #var for js script second chart
    list_chart_data = []
    for st in station_data:
        list_chart_data.append( {'x':st.time_create.strftime("%d/%m/%Y %H:%M"), 'y':st.p1})
    list_chart_data.reverse()
    str_list_chart2 = list_chart_data

    #-----------------------------------------------------------------------------------
    context = {
        'station_list': station_list,
        'station_normel_list': station_normel_list,
        'station_address': station_address,
        'station_data': station_data,
        'title': 'Data',
        'st_id': str(st_id),
        'u': u,
        'i': i,
        'p1': p1,
        'p2': p2,
        'str_list_chart2': str_list_chart2
    }
    return render(request, 'live_data/station.html', context=context)


def station_normel(request, st_id):
    station_list = ListSt.objects.order_by("number")
    station_normel_list = NormelListSt.objects.order_by("number")

    st = station_object_list_normel.get(str(st_id))
    if not st: raise Http404(f'No station {st_id}')
    station_data = st.objects.order_by('-id')[:10]

    station_address = NormelListSt.objects.get(number=st_id).address

    #var for js script first chart
    u_in_f1 = str(station_data[0].u_in_f1) 
    u_in_f2 = str(station_data[0].u_in_f2) 
    u_in_f3 = str(station_data[0].u_in_f3) 
    u_out_f1 = str(station_data[0].u_out_f1) 
    u_out_f2 = str(station_data[0].u_out_f2) 
    u_out_f3 = str(station_data[0].u_out_f3) 
    
    #var for js script second chart
    list_chart_data = []
    for st in station_data:
        list_chart_data.append( {'x':st.time_create.strftime("%d/%m/%Y %H:%M"), 'y':st.u_in_f1})
    list_chart_data.reverse()
    str_list_chart2 = list_chart_data

    #-----------------------------------------------------------------------------------
    context = {
        'station_list': station_list,
        'station_normel_list': station_normel_list,
        'station_address': station_address,
        'station_data': station_data,
        'title': 'Data',
        'st_id': str(st_id),
        'u_in_f1': u_in_f1,
        'u_in_f2': u_in_f2,
        'u_in_f3': u_in_f3,
        'u_out_f1': u_out_f1,
        'u_out_f2': u_out_f2,
        'u_out_f3': u_out_f3,
        'str_list_chart2': str_list_chart2
    }
    return render(request, 'live_data/station_normel.html', context=context)



# ----------------------------------------------------------------------------------------
# XMLHttpRequest()

def getdata(request):
    if request.method == 'GET':
        return JsonResponse({"key":"post"})    #save=False => any type, else only dict
    elif request.method == 'POST':
        try:
            st_id = request.POST["st_id"]
            day_left = request.POST["day_left"]
            month_left  = request.POST["month_left"]
            year_left  = request.POST["year_left"]
            day_right = request.POST["day_right"]
            month_right  = request.POST["month_right"]
            year_right  = request.POST["year_right"]
        except:
            raise Http404(f'request.POST: parameters is undefine')

        # определение величины интервала

        # получение списка данных
        st = station_object_list.get(st_id)
        if not st: raise Http404(f'No station {st_id}')

        try:
            day_left = int(day_left)
            month_left = int(month_left)
            year_left = int(year_left)
            day_right = int(day_right)
            month_right = int(month_right)
            year_right = int(year_right)
        except ValueError:
            raise Http404(f'request.POST parametrs: str to int error')

        date_time1 = datetime(day=day_left, month=month_left, year=year_left)
        date_time2 = datetime(day=day_right, month=month_right, year=year_right, hour=23 , minute=59, second=59)

        station_data = st.objects.order_by('id').filter(time_create__gte=date_time1).filter(time_create__lte=date_time2)
        len_station_data = len(station_data)

        list_chart_data = []
        if len_station_data <= 1440:
            for st in station_data:
                list_chart_data.append( {'x':st.time_create.strftime("%d/%m/%Y %H:%M"), 'y':st.p1})
        else:
            delitel = len_station_data // 740
            ostatoc = len_station_data % 740
            index_std = 0
            for i in range(0, 720):
                sum_pot = 0
                time_create_str = station_data[index_std].time_create.strftime("%d/%m/%Y %H:%M")
                for j in range(0, delitel):
                    sum_pot = sum_pot + station_data[index_std].p1
                    index_std = index_std + 1

                sum_pot = sum_pot / delitel     #получить среднее значение
                list_chart_data.append({'x':time_create_str, 'y':sum_pot})

            sum_pot = 0
            for j in range(0, ostatoc):
                sum_pot = sum_pot + station_data[index_std].p1
                index_std = index_std + 1
            time_create_str = station_data[index_std - 1].time_create.strftime("%d/%m/%Y %H:%M")
            sum_pot = sum_pot / ostatoc     #получить среднее значение
            list_chart_data.append({'x':time_create_str, 'y':sum_pot})

        return JsonResponse( list_chart_data, safe=False )






def getdatanormel(request):
    if request.method == 'GET':
        return JsonResponse({"key":"post"})    #save=False => any type, else only dict
    elif request.method == 'POST':
        try:
            st_id = request.POST["st_id"]
            day_left = request.POST["day_left"]
            month_left  = request.POST["month_left"]
            year_left  = request.POST["year_left"]
            day_right = request.POST["day_right"]
            month_right  = request.POST["month_right"]
            year_right  = request.POST["year_right"]
        except:
            raise Http404(f'request.POST: parameters is undefine')

        # определение величины интервала

        # получение списка данных
        st = station_object_list_normel.get(str(st_id))
        if not st: raise Http404(f'No station {st_id}')

        try:
            day_left = int(day_left)
            month_left = int(month_left)
            year_left = int(year_left)
            day_right = int(day_right)
            month_right = int(month_right)
            year_right = int(year_right)
        except ValueError:
            raise Http404(f'request.POST parametrs: str to int error')

        date_time1 = datetime(day=day_left, month=month_left, year=year_left)
        date_time2 = datetime(day=day_right, month=month_right, year=year_right, hour=23 , minute=59, second=59)

        station_data = st.objects.order_by('id').filter(time_create__gte=date_time1).filter(time_create__lte=date_time2)
        len_station_data = len(station_data)

        list_chart_data = []
        if len_station_data <= 1440:
            for st in station_data:
                list_chart_data.append( {'x':st.time_create.strftime("%d/%m/%Y %H:%M"), 'y':st.u_in_f1})
        else:
            delitel = len_station_data // 740
            ostatoc = len_station_data % 740
            index_std = 0
            for i in range(0, 720):
                sum_pot = 0
                time_create_str = station_data[index_std].time_create.strftime("%d/%m/%Y %H:%M")
                for j in range(0, delitel):
                    sum_pot = sum_pot + station_data[index_std].u_in_f1
                    index_std = index_std + 1

                sum_pot = sum_pot / delitel     #получить среднее значение
                list_chart_data.append({'x':time_create_str, 'y':sum_pot})

            sum_pot = 0
            for j in range(0, ostatoc):
                sum_pot = sum_pot + station_data[index_std].u_in_f1
                index_std = index_std + 1
            time_create_str = station_data[index_std - 1].time_create.strftime("%d/%m/%Y %H:%M")
            sum_pot = sum_pot / ostatoc     #получить среднее значение
            list_chart_data.append({'x':time_create_str, 'y':sum_pot})

        return JsonResponse( list_chart_data, safe=False )








def pageNotFound(request, exception):
    station_list = ListSt.objects.order_by("number")
    station_normel_list = NormelListSt.objects.order_by("number")

    #-----------------------------------------------------------------------------------
    context = {
        'station_list': station_list,
        'station_normel_list': station_normel_list,
        'exception': exception
    }

    return render(request, 'live_data/not_found.html', context=context)

