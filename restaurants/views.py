from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):

    context = {
    	"my_list" : [
			{
			"restaurant_name": "Cane's Chicken",
			"food_type" : "Chicken",
			},
			{
			"restaurant_name": "Pizza Hut",
			"food_type" : "Pizza",
			},
			{
			"restaurant_name" : "Johnny Rockets",
			"food_type" : "Burgers",
			},
    	]

    }
    return render(request, 'list.html', context)


def restaurant_detail(request):

    context = {
    	"my_object" :
    		{
    		"restaurant_name" : "Burger Boutique",
    		"food_type" : "Burgers",
    		},
 
    }
    return render(request, 'detail.html', context)
