from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import sys
import os
sys.path.insert(0, 'src')

from farmer_manager import farmer_manager
from alert_manager import alert_manager
from feedback_manager import feedback_manager
from weather_api import weather_api_client
from threshold_evaluator import threshold_evaluator

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'climatovate-sprint1-secret-key-change-in-production')

@app.route('/')
def index():
    """Dashboard home page"""
    try:
        farmers = farmer_manager.get_all_farmers()
        pending_alerts = alert_manager.get_pending_alerts()
        feedbacks = feedback_manager.get_all_feedback()
        cost_saving_count = sum(1 for f in feedbacks if f.cost_saving_indicator)
        
        return render_template('index.html',
                             farmer_count=len(farmers),
                             pending_alert_count=len(pending_alerts),
                             feedback_count=len(feedbacks),
                             cost_saving_count=cost_saving_count)
    except Exception as e:
        flash(f'Error loading dashboard: {str(e)}', 'error')
        return render_template('index.html',
                             farmer_count=0,
                             pending_alert_count=0,
                             feedback_count=0,
                             cost_saving_count=0)

@app.route('/farmers')
def farmers():
    """List all farmers"""
    try:
        farmer_list = farmer_manager.get_all_farmers()
        return render_template('farmers.html', farmers=farmer_list)
    except Exception as e:
        flash(f'Error loading farmers: {str(e)}', 'error')
        return render_template('farmers.html', farmers=[])

@app.route('/farmers/enroll', methods=['GET', 'POST'])
def enroll_farmer():
    """Enroll a new farmer"""
    if request.method == 'POST':
        try:
            phone = request.form['phone']
            lat = float(request.form['lat'])
            lon = float(request.form['lon'])
            
            farmer_id = farmer_manager.enroll_farmer(phone, lat, lon)
            flash(f'Farmer enrolled successfully! ID: {farmer_id}', 'success')
            return redirect(url_for('farmers'))
        except Exception as e:
            flash(f'Error enrolling farmer: {str(e)}', 'error')
    
    return render_template('enroll_farmer.html')

@app.route('/alerts')
def alerts():
    """View all alerts"""
    try:
        pending = alert_manager.get_pending_alerts()
        return render_template('alerts.html', alerts=pending)
    except Exception as e:
        flash(f'Error loading alerts: {str(e)}', 'error')
        return render_template('alerts.html', alerts=[])

@app.route('/alerts/generate', methods=['POST'])
def generate_alerts():
    """Generate alerts for all farmers"""
    try:
        new_alerts = alert_manager.generate_alerts_for_all_farmers()
        flash(f'Generated {len(new_alerts)} alert(s)', 'success')
    except Exception as e:
        flash(f'Error generating alerts: {str(e)}', 'error')
    
    return redirect(url_for('alerts'))

@app.route('/alerts/mark-delivered/<alert_id>', methods=['POST'])
def mark_delivered(alert_id):
    """Mark an alert as delivered"""
    try:
        alert_manager.mark_alert_delivered(alert_id)
        flash('Alert marked as delivered', 'success')
    except Exception as e:
        flash(f'Error: {str(e)}', 'error')
    
    return redirect(url_for('alerts'))

@app.route('/feedback')
def feedback():
    """View all feedback"""
    try:
        feedback_list = feedback_manager.get_all_feedback()
        farmers = {f.farmer_id: f for f in farmer_manager.get_all_farmers()}
        return render_template('feedback.html', feedbacks=feedback_list, farmers=farmers)
    except Exception as e:
        flash(f'Error loading feedback: {str(e)}', 'error')
        return render_template('feedback.html', feedbacks=[], farmers={})

@app.route('/feedback/add', methods=['GET', 'POST'])
def add_feedback():
    """Add farmer feedback"""
    if request.method == 'POST':
        try:
            farmer_id = request.form['farmer_id']
            text = request.form['feedback_text']
            cost_saving = 'cost_saving' in request.form
            
            feedback_id = feedback_manager.record_feedback(farmer_id, text, cost_saving)
            flash(f'Feedback recorded successfully! ID: {feedback_id}', 'success')
            return redirect(url_for('feedback'))
        except Exception as e:
            flash(f'Error recording feedback: {str(e)}', 'error')
    
    try:
        farmers = farmer_manager.get_all_farmers()
        return render_template('add_feedback.html', farmers=farmers)
    except Exception as e:
        flash(f'Error loading farmers: {str(e)}', 'error')
        return render_template('add_feedback.html', farmers=[])

@app.route('/forecast')
def forecast():
    """Weather forecast query page"""
    return render_template('forecast.html')

@app.route('/forecast/query', methods=['POST'])
def query_forecast():
    """Query weather forecast"""
    try:
        lat = float(request.form['lat'])
        lon = float(request.form['lon'])
        
        forecast_data = weather_api_client.get_hyperlocal_forecast(lat, lon)
        conditions = threshold_evaluator.evaluate_forecast(forecast_data)
        
        return render_template('forecast_result.html',
                             lat=lat,
                             lon=lon,
                             forecast=forecast_data['forecast'][:24],  # Show 24 hours
                             conditions=conditions)
    except Exception as e:
        flash(f'Error querying forecast: {str(e)}', 'error')
        return redirect(url_for('forecast'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
