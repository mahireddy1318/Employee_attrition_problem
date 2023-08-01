# app.py
from flask import Flask, render_template, request
import  pickle
app = Flask(__name__)


def business_probelm(job_type, degree, major, industry, miles, experience):
  CEO,CFO,CTO,JANITOR,JUNIOR, MANAGER, SENIOR,VICE_PRECIDENT = 0,0,0,0,0,0,0,0
  if job_type == 'CEO':
    CEO=1
  elif job_type =='CFO':
    CFO=1
  elif job_type=='CTO':
    CTO = 1
  elif job_type == 'JANITOR':
    JANITOR = 1
  elif job_type =='JUNIOR':
    JUNIOR ==1
  elif job_type =='MANAGER':
    MANAGER =1
  elif job_type == 'SENIOR':
    SENIOR = 1
  elif job_type == 'VICE_PRECIDENT':
    VICE_PRECIDENT = 1
  else:
    print('choose from above options')

  BACHELORS, DOCTORAL, HIGHSCHOOL,MASTERS, NONE = 0,0,0,0,0
  if degree == 'BACHELORS':
    BACHELORS = 1
  elif degree == 'DOCTORAL':
    DOCTORAL =1
  elif degree == 'HIGHSCHOOL':
    HIGHSCHOOL =1
  elif degree == 'MASTERS':
    MASTERS = 1
  elif degree == 'NONE':
    NONE = 1
  else:
    print('choose from above options')


  BIOLOGY, BUSINESS, CHEMISTRY, COMPSCI, ENGINEERING, LITARATURE, MATH, NONE, PHYSICS = 0,0,0,0,0,0,0,0,0
  if major == 'BIOLOGY':
    BIOLOGY=1
  elif major =='BUSINESS':
    BUSINESS=1
  elif major=='CHEMISTRY':
    CHEMISTRY = 1
  elif major == 'COMPSCI':
    COMPSCI = 1
  elif major =='ENGINEERING':
    ENGINEERING ==1
  elif major =='LITARATURE':
    LITARATURE =1
  elif major == 'MATH':
    MATH = 1
  elif major == 'NONE':
    NONE = 1
  elif major == 'PHYSICS':
    PHYSICS = 1
  else:
    print('choose from above options')


  AUTO, EDUCATION, FINANCE, HEALTH, OIL, SERVICE, WEB = 0,0,0,0,0,0,0
  if industry == 'AUTO':
    AUTO=1
  elif industry =='EDUCATION':
    EDUCATION=1
  elif industry=='FINANCE':
    FINANCE = 1
  elif industry == 'HEALTH':
    HEALTH = 1
  elif industry =='OIL':
    OIL ==1
  elif industry =='SERVICE':
    SERVICE =1
  elif industry == 'WEB':
    WEB = 1
  else:
    print('choose from above options')

  miles = int(miles)
  experience = int(experience)

  return CEO,CFO,CTO,JANITOR,JUNIOR, MANAGER, SENIOR,VICE_PRECIDENT, BACHELORS, DOCTORAL, HIGHSCHOOL,MASTERS, NONE, BIOLOGY, BUSINESS, CHEMISTRY, COMPSCI, ENGINEERING, LITARATURE, MATH, NONE, PHYSICS, AUTO, EDUCATION, FINANCE, HEALTH, OIL, SERVICE, WEB, miles, experience




file_path = r'C:\Users\Siva Reddy\Desktop\projects\Employe_salary_prediction\GBR_model.pkl' 

with open(file_path , 'rb') as f:
    loaded_model = pickle.load(f)

# Load and prepare your Saved (GBR) model (same as before)

@app.route('/', methods=['GET', 'POST'])
def predict():

    #return render_template('index.html')
    job_type, degree, major, industry,  distance, experience, business_probelm_result, predicted_salary  =None, None, None, None, None, None, None, None
    if request.method == 'POST':
        try:
            job_type = request.form.get('job_type')
            degree = request.form.get('degree')
            major = request.form.get('major')
            industry = request.form.get('industry')
            distance = request.form.get('distance')
            experience = request.form.get('experience')

            business_probelm_result = business_probelm(job_type, degree, major, industry,  distance, experience)
            #return f"Selected job type: {job_type}"
        
            predicted_salary = loaded_model.predict([business_probelm_result])

            return render_template('index.html', prediction= round(predicted_salary[0],2))
        except Exception as e:
          return render_template('index.html', error=str(e))
    
    else:
      return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
