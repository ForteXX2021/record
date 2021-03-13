from django.shortcuts import render, redirect, get_object_or_404
from .forms import DayCreateForm
from .models import Day
from django_pandas.io import read_frame
import numpy as np

def index(request):
    context = {
        'list':Day.objects.all()
    }
    return render(request, 'record/list.html',context)

def add(request):
    form = DayCreateForm(request.POST or None)
    if request.method =='POST' and form.is_valid():
        form.save()
        return redirect('record:index')
 
    context = {
        'form':DayCreateForm()
    }
    return render(request,'record/form.html',context)



def update(request, pk):
    day = get_object_or_404(Day, pk=pk)
    form = DayCreateForm(request.POST or None, instance = day)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('record:index')
    
    context = {
        'form':form
    }
    return render(request,'record/form.html', context)

def delete(request, pk):
    day = get_object_or_404(Day, pk=pk)
    if request.method == 'POST':
        day.delete()
        return redirect('record:index')
    
    context = {
        'day':day
    }
    return render(request,'record/day_delete_confirm.html', context)


def all_delete(request):
    if request.method == 'POST':
        Day.objects.all().delete()

    context= {}

    return render(request,'record/all_delete_confirm.html', context)

def next_matrix(request):
    if request.method == 'POST':
        Days = Day.objects.all()
        df_all = read_frame(Days, fieldnames = ['date', 'number', 'types', 'place', 'company'])
        df = df_all.number

        count_matrix = np.zeros((38,38))
        neighbor_matrix = np.array([[	0	,	35	,	14	,	2	,	0	,	28	,	9	,	26	],
[	1	,	24	,	36	,	13	,	1	,	37	,	27	,	10	],
[	2	,	23	,	35	,	14	,	2	,	0	,	28	,	9	],
[	3	,	22	,	34	,	15	,	3	,	24	,	36	,	13	],
[	4	,	21	,	33	,	16	,	4	,	23	,	35	,	14	],
[	5	,	20	,	32	,	17	,	5	,	22	,	34	,	15	],
[	6	,	19	,	31	,	18	,	6	,	21	,	33	,	16	],
[	7	,	26	,	30	,	11	,	7	,	20	,	32	,	17	],
[	8	,	25	,	29	,	12	,	8	,	19	,	31	,	18	],
[	9	,	2	,	0	,	28	,	9	,	26	,	30	,	11	],
[	10	,	1	,	37	,	27	,	10	,	25	,	29	,	12	],
[	11	,	9	,	26	,	30	,	11	,	7	,	20	,	32	],
[	12	,	10	,	25	,	29	,	12	,	8	,	19	,	31	],
[	13	,	3	,	24	,	36	,	13	,	1	,	37	,	27	],
[	14	,	4	,	23	,	35	,	14	,	2	,	0	,	28	],
[	15	,	5	,	22	,	34	,	15	,	3	,	24	,	36	],
[	16	,	6	,	21	,	33	,	16	,	4	,	23	,	35	],
[	17	,	7	,	20	,	32	,	17	,	5	,	22	,	34	],
[	18	,	8	,	19	,	31	,	18	,	6	,	21	,	33	],
[	19	,	29	,	12	,	8	,	19	,	31	,	18	,	6	],
[	20	,	30	,	11	,	7	,	20	,	32	,	17	,	5	],
[	21	,	31	,	18	,	6	,	21	,	33	,	16	,	4	],
[	22	,	32	,	17	,	5	,	22	,	34	,	15	,	3	],
[	23	,	33	,	16	,	4	,	23	,	35	,	14	,	2	],
[	24	,	34	,	15	,	3	,	24	,	36	,	13	,	1	],
[	25	,	37	,	27	,	10	,	25	,	29	,	12	,	8	],
[	26	,	0	,	28	,	9	,	26	,	30	,	11	,	7	],
[	27	,	13	,	1	,	37	,	27	,	10	,	25	,	29	],
[	28	,	14	,	2	,	0	,	28	,	9	,	26	,	30	],
[	29	,	27	,	10	,	25	,	29	,	12	,	8	,	19	],
[	30	,	28	,	9	,	26	,	30	,	11	,	7	,	20	],
[	31	,	12	,	8	,	19	,	31	,	18	,	6	,	21	],
[	32	,	11	,	7	,	20	,	32	,	17	,	5	,	22	],
[	33	,	18	,	6	,	21	,	33	,	16	,	4	,	23	],
[	34	,	17	,	5	,	22	,	34	,	15	,	3	,	24	],
[	35	,	16	,	4	,	23	,	35	,	14	,	2	,	0	],
[	36	,	15	,	3	,	24	,	36	,	13	,	1	,	37	],
[	37	,	36	,	13	,	1	,	37	,	27	,	10	,	25	]],
)
        results_matrix = np.array([[	2	,	0	],
[	0	,	0	],
[	28	,	0	],
[	9	,	0	],
[	26	,	0	],
[	30	,	0	],
[	11	,	0	],
[	7	,	0	],
[	20	,	0	],
[	32	,	0	],
[	17	,	0	],
[	5	,	0	],
[	22	,	0	],
[	34	,	0	],
[	15	,	0	],
[	3	,	0	],
[	24	,	0	],
[	36	,	0	],
[	13	,	0	],
[	1	,	0	],
[	37	,	0	],
[	27	,	0	],
[	10	,	0	],
[	25	,	0	],
[	29	,	0	],
[	12	,	0	],
[	8	,	0	],
[	19	,	0	],
[	31	,	0	],
[	18	,	0	],
[	6	,	0	],
[	21	,	0	],
[	33	,	0	],
[	16	,	0	],
[	4	,	0	],
[	23	,	0	],
[	35	,	0	],
[	14	,	0	]])


        
        df = df.replace(100, 37)
        df_length = len(df)-1
        now1 = df.tail(1)
        now = now1.iloc[0]
        next_numbers = count_matrix[now,:]
        
        for i in range(1, df_length):
            x = df.iloc[i]
            y = df.iloc[i-  1]
            
            for j in range(1,8):
                count_matrix[y,neighbor_matrix[x,j]] = count_matrix[y,neighbor_matrix[x,j]] + 1
                  
        for l in range(38):
            m = results_matrix[l,0]   
            n = next_numbers[m]    
            results_matrix[l,1] = n
    
        results = results_matrix         
        my_app = {'result' : results}
        return render(request,'record/next_matrix.html', my_app)

    context = {}
    return render(request,'record/next_matrix.html', context)


