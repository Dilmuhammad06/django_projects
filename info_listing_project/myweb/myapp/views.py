from django.shortcuts import render

names = {
    "John": {"user_id": 1, "surname": "Doe", "age": 30, "profession": "Engineer", "about": "John Doe is an engineer with a passion for technology."},
    "Alice": {"user_id": 2, "surname": "Smith", "age": 28, "profession": "Doctor", "about": "Alice Smith is a dedicated medical professional."},
    "David": {"user_id": 3, "surname": "Brown", "age": 35, "profession": "Architect", "about": "David Brown is an experienced architect specializing in sustainable design."},
    "Emily": {"user_id": 4, "surname": "Jones", "age": 22, "profession": "Student", "about": "Emily Jones is a student pursuing a degree in computer science."},
    "Michael": {"user_id": 5, "surname": "Taylor", "age": 40, "profession": "Entrepreneur", "about": "Michael Taylor is a successful entrepreneur with a background in finance."},
    "Sophia": {"user_id": 6, "surname": "White", "age": 27, "profession": "Graphic Designer", "about": "Sophia White is a creative graphic designer passionate about visual storytelling."},
    "Daniel": {"user_id": 7, "surname": "Miller", "age": 32, "profession": "Lawyer", "about": "Daniel Miller is a dedicated lawyer with expertise in corporate law."},
    "Olivia": {"user_id": 8, "surname": "Clark", "age": 25, "profession": "Artist", "about": "Olivia Clark is a talented artist specializing in oil paintings."},
    "Ethan": {"user_id": 9, "surname": "Ward", "age": 29, "profession": "Software Developer", "about": "Ethan Ward is a skilled software developer passionate about creating innovative solutions."},
    "Ava": {"user_id": 10, "surname": "Baker", "age": 26, "profession": "Marketing Manager", "about": "Ava Baker is a results-driven marketing manager with a focus on digital strategies."}
}


def index(request):
    data = {'names':names}
    return render(request,'myapp/index.html',data)

def main(request):
    return render(request,'myapp/main.html')

def info(request,id):
    for key,val in names.items():
        if val['user_id'] == id:
            return render(request,'myapp/info.html',{'value':val})
    return render(request,'myapp/info.html')