from flask import Flask, request, render_template
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/escalation', methods=['POST'])
def escalation():
    rent = int(request.form['rent'])
    start_date = request.form['start_date']
    
    end_date = request.form['end_date']
    escalation_percentage = int(request.form['escalation_percentage'])

    if is_between_dates(start_date, end_date):
        new_rent = int(rent * (1 + escalation_percentage / 100))
        new_start_date = datetime.strptime(request.form['end_date'], "%Y-%m-%d").date() + timedelta(days=1)
        new_end_date = new_start_date + relativedelta(years=1)
        print(new_rent)
        print("Today is between the specified dates.")
        return render_template('index1.html', rent=rent, start_date = start_date, end_date =end_date,new_rent= new_rent, new_start_date= new_start_date, new_end_date = new_end_date, escalation_percentage = escalation_percentage)

    else:
        print("Today is not between the specified dates.")
        return render_template('index1.html', rent=rent, start_date = start_date, end_date =end_date,new_rent= new_rent)


def is_between_dates(start_date, end_date):
    today = datetime.now().date()

    start = datetime.strptime(start_date, '%Y-%m-%d').date()
    end = datetime.strptime(end_date, '%Y-%m-%d').date()

    return start <= today <= end

if __name__ == '__main__':
    app.run(debug=True)