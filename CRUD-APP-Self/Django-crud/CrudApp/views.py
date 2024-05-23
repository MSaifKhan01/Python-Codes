from django.shortcuts import render

from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from .models import Student
from .serializers import StudentSerializer


from django.urls import resolve

@csrf_exempt
def studentApi(request, id=0):
    # print("----",request)
    
    # Use resolve to get the resolved URL information
    resolved_url = resolve(request.path_info)
    # print("Resolved URL:", resolved_url.route)
    if request.method == 'GET':
        if(resolved_url.route=="student"):
            students = Student.objects.all()
            
            #  # Sorting
            # sort_by = request.GET.get('sort_by', None)
            # if sort_by:
            #     students = students.order_by(sort_by)
            
            
            # Sorting-02
            sort_by = request.GET.get('sort_by', None)
            sort_order = request.GET.get('sort_order', 'asc')  # default to ascending
            print("-------",sort_order)
            print("---1",sort_by)

            if sort_by:
                if sort_order == 'desc':
                    print("---2",sort_by)
                    sort_by = f'-{sort_by}'
                    print("---3",sort_by)
                students = students.order_by(sort_by)

            # Filtering
            name = request.GET.get('name', None)
            address = request.GET.get('address', None)
            fee = request.GET.get('fee', None)

            if name:
                students = students.filter(name__icontains=name)
            if address:
                students = students.filter(address__icontains=address)
            if fee:
                students = students.filter(fee=fee)

            serializer = StudentSerializer(students, many=True)
            return JsonResponse(serializer.data, safe=False)
        else:
            return JsonResponse({"message": "Welcome on my CRUD app"})
    
        
    elif request.method == 'POST':
        student_data = JSONParser().parse(request)
        serializer = StudentSerializer(data=student_data)
        # print("----serializer-----",serializer,"------request-----",request,"studenData",student_data)
    
        # if(serializer.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    
    
   
    # """ or we can perform post with below approach which is commented below"""

    # elif request.method == 'POST':
    #     student_data = JSONParser().parse(request)
    
    #     print(student_data)
    #     # Create a new Student instance with the data
    #     new_student = Student(name=student_data['name'], address=student_data['address'], fee=student_data['fee'])
    
    #     # Save the new_student instance to the database
    #     new_student.save()
    
    #     return JsonResponse("Added Successfully", safe=False)

    elif request.method == 'PUT':
        student_data = JSONParser().parse(request)
        student = Student.objects.get(id=id)
        serializer = StudentSerializer(student, data=student_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update", safe=False)
    elif request.method == 'DELETE':
        student = Student.objects.get(id=id)
        student.delete()
        return JsonResponse("Deleted Successfully", safe=False)
